
from os import kill
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *


from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo

from AoE2ScenarioParser.datasets.other import OtherInfo


from AoE2ScenarioParser.datasets.players import PlayerId


from AoE2ScenarioParser.datasets.trigger_lists import ObjectAttribute
from AoE2ScenarioParser.datasets.trigger_lists import Operation


from util_add_tent_spawn_ability import *


from hero_abstract_class import *

from robin_archer import *
from itertools import chain

from center_sacred_parameters import *
"""
Dynamic Change Enviorment Specification
1. change specific dedicated tiles at the start to unpassable water tile by using invisible object (blocks) that has water foundation
2. after certain wait, the map changes from north to south to winter. trees convert to dead one. water becomes ice (passable). land terrains becomes snow foundation.


Fading changes, trigger should be clustered against their distance to the set POLE

BASIC RULES
- kill building and build new cannot happen in same clock
- place foundation does not work for gaia source player

"""
START_POLE_X = 240
START_POLE_Y = 0

END_POLE_X = 0
END_POLE_Y = 240

#TIME_START_FROZEN = 20
# Configuration
FROZEN_PACE_DELAY = 2 

invisible_storage_with_water_foundation_id = 1081
tentb_id = 1098


OBJECT_TO_CREATE_ICE_FOR_WATER_TERRAIN_ID = tentb_id

TERRAIN_USED_AS_ICEABLE_WATER_TILE_ID = TerrainId.BEACH_NON_NAVIGABLE_WET_ROCK

OBJECT_USED_TO_GENERATE_SNOW_TERRAIN_ID = 1097

OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID = 1101

USED_SOURCE_PLAYER = 8


UNFREEZE_POINT_RIVER_X =153
UNFREEZE_POINT_RIVER_Y = 50


# WINTER CHANGE SPEED CONTROL
TIME_START_FROZEN = 4000
CLUSTER_SIZE = 30
#CLUSTER_SIZE = 500
KILL_EARLY = 1

TREE_REPLACE_OBJECTS = [
            OtherInfo.TREE_SNOW_PINE.ID,
            #OtherInfo.TREE_OAK_AUTUMN_SNOW.ID,
            OtherInfo.TREE_DEAD.ID,
            OtherInfo.TREE_I.ID
        ]

SHALLOW_ID = [4,59,54]

"""
IDEA of creating trigger for winter fading effect

START_POLE ------------xxx----------------xxxxx-------------xxxxxxxxxxxxxxxxxxxxxxx--------------------END_POLE
           ------------trigger1------------trigger2---------trigger3trigger4trigger5 ------------------

trigger1 activates trigger2, trigger2 activates trigger3 and so forth.
but condition timer of trigger2...n. depends on the interval between each trigger on this diagram

the cluster parameter would be density parameter that decides how many trigger we create.
e.g. if cluster is 1, then the first xxx in the line would create 3 triggers.
if cluster is 2, then 2,
if cluster is 3, then 1.


"""



def calculate_distance_to_end_pole(tile):
    return int(((tile.x - END_POLE_X)** 2) + (END_POLE_Y - tile.y) ** 2)
def calculate_distance_to_start_pole(tile):
    return int(((tile.x - START_POLE_X)** 2) + (START_POLE_Y - tile.y) ** 2)
def calculate_unfreeze_point_distance_to_start_pole():
    return int(((UNFREEZE_POINT_RIVER_X - START_POLE_X)** 2) + (START_POLE_Y - UNFREEZE_POINT_RIVER_Y) ** 2)

def calculate_euclean_distance_to_center_sacred(tile):
    return int(math.sqrt(((CENTER_SACRED_X - tile.x)** 2) + (CENTER_SACRED_Y - tile.y) ** 2))

def add_blockage_object_to_target_tiles_that_mimic_water(source_scenario:AoE2DEScenario):

    source_trigger_manager = source_scenario.trigger_manager
    # get all the terrains tiles (compiled in a list) in the map
    originalTerrains = source_scenario.map_manager.terrain



    prepare_object_for_changing_terrain(source_trigger_manager)




    """identify which tiles are to be replaced with water-looking tile"""


    dict_iceable_river = dict()
    dict_water_terrain = dict()
    dict_all_non_water_terrain = dict()


    all_discovered_distance = set()

    for terrain in originalTerrains:
        distance = calculate_distance_to_end_pole(terrain)

        """
        add filter and decides up to where to freeze
        """

        if calculate_distance_to_start_pole(terrain) > calculate_unfreeze_point_distance_to_start_pole():
            continue

        # DO NO TOUCH terrain near sacred center
        if calculate_euclean_distance_to_center_sacred(terrain) < CENTER_WINTER_NO_CHANGE_DISTANCE:
            continue 

        #BRIDGE
        if terrain.terrain_id == TERRAIN_USED_AS_ICEABLE_WATER_TILE_ID:

            all_discovered_distance.add(distance)
            dict_iceable_river.setdefault(distance, []).append(terrain)


        #WATER
        elif terrain.terrain_id in TerrainId.water_terrains() or terrain.terrain_id in TerrainId.beach_terrains() or terrain.terrain_id in SHALLOW_ID:
            #print("found black tile")

            #some just do not freeze,
            #if terrain.terrain_id in TerrainId.water_terrains() or terrain.terrain_id in TerrainId.beach_terrains() and (calculate_distance_to_start_pole(terrain) > calculate_unfreeze_point_distance_to_start_pole()):
            if (terrain.terrain_id in TerrainId.water_terrains() or terrain.terrain_id in TerrainId.beach_terrains()) and (calculate_distance_to_start_pole(terrain) > calculate_unfreeze_point_distance_to_start_pole()):

                #print("skip this water terrain")
                continue
            #print("add this water terrain")
            all_discovered_distance.add(distance)
            dict_water_terrain.setdefault(distance, []).append(terrain)

        #NON WATER
        elif terrain.terrain_id not in TerrainId.water_terrains() and terrain.terrain_id not in TerrainId.beach_terrains() and terrain.terrain_id not in SHALLOW_ID:

            all_discovered_distance.add(distance)
            dict_all_non_water_terrain.setdefault(distance, []).append(terrain)

    gaia_units = source_scenario.unit_manager.get_player_units(PlayerId.GAIA)

    dict_non_winter_tree = dict()

    #non_winter_tree = []
    # get reference id
    for gaia_unit in gaia_units:

        if calculate_distance_to_start_pole(gaia_unit) > calculate_unfreeze_point_distance_to_start_pole():
            continue

        # DO NO TOUCH terrain near sacred center
        if calculate_euclean_distance_to_center_sacred(gaia_unit) < CENTER_WINTER_NO_CHANGE_DISTANCE:
            continue 

        if gaia_unit.unit_const in [x.ID for x in OtherInfo.trees()]:
            distance = calculate_distance_to_end_pole(gaia_unit)
            if gaia_unit.unit_const != OtherInfo.TREE_SNOW_PINE and  gaia_unit.unit_const != OtherInfo.TREE_OAK_AUTUMN_SNOW:
                all_discovered_distance.add(calculate_distance_to_end_pole(gaia_unit))
                dict_non_winter_tree.setdefault(distance, []).append(gaia_unit)


    """
    build dictionary
    
    """


    """
    cluster
    example cluster members
    [337, 338]
    [335, 336]
    [333, 334]
    [331, 332]
    [329, 330]
    [327, 328]
    [325, 326]
    [323, 324]
    [321, 322]
    [319, 320]
    [317, 318]
    [315, 316]
    """



    sorted_distances = sorted(all_discovered_distance)
    # first get maximum in the all_discovered_distance.
    max_distance = max(all_discovered_distance)


    prev_trigger = None
    prev_kill_trigger = None
    # the based on cluster size, we use a for
    for cluster_idx, supposed_cluster in  enumerate(range(max_distance, 0, -CLUSTER_SIZE)):
        #check if this cluster is there but checking if this cluster contains discovered... distance
        cluster_members = set(
            d for d in sorted_distances 
            if supposed_cluster - CLUSTER_SIZE < d <= supposed_cluster
        )
        common_values = all_discovered_distance & cluster_members
        # Check if there are any common values
        if not common_values:
            continue

        #now 
        trigger = source_trigger_manager.add_trigger(
                name=f"freeze_cluster_{cluster_idx}",
                enabled= cluster_idx==0,
                looping=False
            )
        trigger.new_condition.timer(FROZEN_PACE_DELAY)



        """special treatment to kill object, has to happen one second early before place foundation"""
        kill_trigger = source_trigger_manager.add_trigger(
                name=f"kill_cluster_{cluster_idx}",
                enabled= cluster_idx==0,
                looping=False
            )
        kill_trigger.new_condition.timer(FROZEN_PACE_DELAY)


        for distance in cluster_members:
            terrain_list = dict_iceable_river.get(distance)
            if terrain_list is not None:
                for terrain in terrain_list:
                    kill_trigger.new_effect.kill_object(object_list_unit_id=OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID, 
                                                   source_player=0,
                                                   area_x1=terrain.x, area_x2=terrain.x, area_y1=terrain.y, area_y2=terrain.y)
                    

        for distance in cluster_members:
            terrain_list = dict_iceable_river.get(distance)
            if terrain_list is not None:
                for terrain in terrain_list:
                    trigger.new_effect.kill_object(object_list_unit_id=OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID, 
                                                   source_player=0,
                                                   area_x1=terrain.x, area_x2=terrain.x, area_y1=terrain.y, area_y2=terrain.y)
                    trigger.new_effect.place_foundation(
                        object_list_unit_id=OBJECT_TO_CREATE_ICE_FOR_WATER_TERRAIN_ID,
                        source_player=USED_SOURCE_PLAYER,
                        location_x=terrain.x,
                        location_y=terrain.y
                    )


            terrain_list = dict_water_terrain.get(distance)
            if terrain_list is not None:
                for terrain in terrain_list:
                    trigger.new_effect.place_foundation(
                        object_list_unit_id=OBJECT_TO_CREATE_ICE_FOR_WATER_TERRAIN_ID,
                        source_player=USED_SOURCE_PLAYER,
                        location_x=terrain.x,
                        location_y=terrain.y
                    )

            terrain_list = dict_all_non_water_terrain.get(distance)
            if terrain_list is not None:
                for terrain in terrain_list:    
                    trigger.new_effect.place_foundation(
                    object_list_unit_id=OBJECT_USED_TO_GENERATE_SNOW_TERRAIN_ID,
                    source_player=USED_SOURCE_PLAYER,
                    location_x=terrain.x,
                    location_y=terrain.y
                )
            # change object
            tree_list = dict_non_winter_tree.get(distance)
            if tree_list is not None:
                for tree in tree_list:    
                    import random
                    trigger.new_effect.replace_object(
                        source_player=0,
                        target_player=0,
                        selected_object_ids=tree.reference_id,
                        object_list_unit_id_2=random.choice(TREE_REPLACE_OBJECTS)
                    )


        if prev_trigger is not None:
            prev_trigger.new_effect.activate_trigger(trigger.trigger_id)
        else:
            trigger.new_condition.timer(TIME_START_FROZEN)
        prev_trigger = trigger


        if prev_kill_trigger is not None:
            prev_kill_trigger.new_effect.activate_trigger(kill_trigger.trigger_id)
        else:
            kill_trigger.new_condition.timer(TIME_START_FROZEN - KILL_EARLY)

        prev_kill_trigger = kill_trigger

    instruction_trigger = source_trigger_manager.add_trigger("display winter comming", enabled=True, looping=False)
    instruction_trigger.new_condition.timer(TIME_START_FROZEN)
    instruction_trigger.new_effect.display_instructions(object_list_unit_id=HeroInfo.GENGHIS_KHAN.ID,
                                                        source_player=0,
                                                        display_time=20,
                                                        message = "Winter is Coming! Be careful of attack from the frozen river!")


    merged_terrain_list = list(chain(*dict_iceable_river.values()))


    transform_first_to_water = source_trigger_manager.add_trigger("transform_first_to_water", enabled=True,looping=False)

    for terrain in merged_terrain_list:
        
        transform_first_to_water.new_effect.place_foundation(object_list_unit_id=invisible_storage_with_water_foundation_id,source_player=USED_SOURCE_PLAYER,location_x=terrain.x,location_y=terrain.y)
        #transform_first_to_water.new_effect.create_object(object_list_unit_id=invisible_storage_id, source_player=1, location_x=x, location_y=y)

    
    """
    turns out we cannot use change ownership or replace objects to process the building generated by "place foundation"
    """


    transform_building_to_gaia = source_trigger_manager.add_trigger("transform_building_to_gaia", enabled=True,looping=False)
    transform_building_to_gaia.new_condition.timer(3)

    for terrain in merged_terrain_list:
        #transform_first_to_water.new_effect.place_foundation(object_list_unit_id=invisible_storage_with_water_foundation_id,source_player=USED_SOURCE_PLAYER,location_x=x,location_y=y)
        transform_building_to_gaia.new_effect.create_object(object_list_unit_id=OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID, source_player=USED_SOURCE_PLAYER, location_x= terrain.x, location_y=terrain.y)


    # MAKE blocking objects unattackable.
    transform_building_to_gaia.new_effect.disable_object_deletion(source_player=USED_SOURCE_PLAYER, object_list_unit_id=OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID)

    transform_building_to_gaia.new_effect.disable_object_selection(source_player=USED_SOURCE_PLAYER, object_list_unit_id=OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID)
    transform_building_to_gaia.new_effect.disable_unit_targeting(source_player=USED_SOURCE_PLAYER, object_list_unit_id=OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID)

    transform_building_to_gaia.new_effect.change_object_hp(source_player=USED_SOURCE_PLAYER, quantity=0, operation=Operation.SET, object_list_unit_id=OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID)
    transform_building_to_gaia.new_effect.change_object_hp(source_player=USED_SOURCE_PLAYER, quantity=0, operation=Operation.SET, object_list_unit_id=OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID)



    transform_building_to_gaia.new_effect.change_ownership(object_list_unit_id=OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID, source_player=USED_SOURCE_PLAYER, target_player=0)




    """
    this one does not work strange..
    both did not work. to change the used player to gaia ownership
    """
    #transform_building_to_gaia.new_effect.change_ownership(object_list_unit_id=invisible_storage_with_water_foundation_id, source_player=USED_SOURCE_PLAYER, target_player=0)
    # transform_building_to_gaia.new_effect.replace_object(object_list_unit_id=invisible_storage_with_water_foundation_id, 
    #                                                      area_x1=0, area_x2=239, area_y1=0, area_y2=239, 
    #                                                      source_player=USED_SOURCE_PLAYER, 
    #                                                      target_player=0, 
    #                                                      object_list_unit_id_2=invisible_storage_with_water_foundation_id)




    #clear_blockage_building = source_trigger_manager.add_trigger("clear_blockage_building", enabled=True,looping=False)
    #clear_blockage_building.new_condition.timer(timer=TIME_START_FROZEN - 1)
    #clear_blockage_building.new_effect.kill_object(object_list_unit_id=OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID, source_player=0)

    """
    add take turns 
    """







def prepare_object_for_changing_terrain(source_trigger_manager):

    


    inst_intermedite_object_building = Hero(hero_id=OBJECT_TO_CREATE_ICE_FOR_WATER_TERRAIN_ID, 
                                            terrain_restriction_id = 0, 
                                            foundation_terrain = TerrainId.BEACH_ICE, 
                                            health_point = 0, 
                                            train_time=0, 
                                            dying_graphic = 0, 
                                            can_be_built_on = 1,
                                            standing_graphic = 0,
                                            dead_unit_id = 0,
                                            unit_size_x = 1,
                                           unit_size_y = 1,
                                            )
    boost_hero(source_trigger_manager, inst_intermedite_object_building, PlayerId.all()[1:])




    inst_tenta_id_building = Hero(hero_id=OBJECT_USED_TO_GENERATE_SNOW_TERRAIN_ID, 
                                  terrain_restriction_id = 0, 
                                  foundation_terrain = TerrainId.SNOW_FOUNDATION, 
                                  health_point = 0, 
                                  train_time=0, 
                                  dying_graphic = 0, 
                                  can_be_built_on = 1,
                                  standing_graphic = 0,
                                  dead_unit_id = 0,
                                   unit_size_x = 1,
                                unit_size_y = 1,
                                  )
    boost_hero(source_trigger_manager, inst_tenta_id_building, PlayerId.all()[1:])



    """
    TMP
    """
    inst_try_object = Hero(hero_id=OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID, 
                            terrain_restriction_id = 0, 
                            dead_unit_id = 0, 
                            can_be_built_on = 1,
                            standing_graphic = 0, 
                            dying_graphic = 0,
                            unit_size_x = 1,
                            unit_size_y = 1,
                            # health_point = 0, 
                            # train_time=0, 
                            )

    boost_hero(source_trigger_manager, inst_try_object, PlayerId.all()[1:])


    """
    This storage object is to change tile look first to water.
    have to use place foundation to create the terrain. create object does not bring terrain

    """

    inst_invisible_storage_with_water_foundation = Hero(hero_id=invisible_storage_with_water_foundation_id, 
                                                        terrain_restriction_id = 0, 
                                                        foundation_terrain = TerrainId.WATER_SHALLOW, 
                                                        dead_unit_id = 0, 
                                                        health_point = 0, 
                                                        train_time=0, 
                                                        can_be_built_on = 1,
                                                        standing_graphic = 0, 
                                                        dying_graphic = 0,
                                                        unit_size_x = 1,
                                                        unit_size_y = 1,
                                                        )

    boost_hero(source_trigger_manager, inst_invisible_storage_with_water_foundation, PlayerId.all()[1:])
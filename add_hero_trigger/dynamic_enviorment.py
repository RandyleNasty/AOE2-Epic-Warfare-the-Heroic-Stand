
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


"""
Dynamic Change Enviorment Specification
1. change specific dedicated tiles at the start to unpassable water tile by using invisible object (blocks) that has water foundation
2. after certain wait, the map changes from north to south to winter. trees convert to dead one. water becomes ice (passable). land terrains becomes snow foundation.

"""
POLE_X = 0
POLE_Y = 240
TIME_START_FROZEN = 20
# Configuration
FROZEN_PACE_DELAY = 2  # Milliseconds between each freezing wave
FROZEN_BATCH_SIZE = 2  # Number of distance groups per trigger batch




invisible_storage_with_water_foundation_id = 1081

tentb_id = 1098


OBJECT_TO_CREATE_ICE_FOR_WATER_TERRAIN_ID = tentb_id

TERRAIN_USED_AS_ICEABLE_WATER_TILE_ID = TerrainId.BEACH_NON_NAVIGABLE_WET_ROCK

OBJECT_USED_TO_GENERATE_SNOW_TERRAIN_ID = 1097
#tenta_id = 1097

OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID = 1101

def add_blockage_object_to_target_tiles_that_mimic_water(source_scenario:AoE2DEScenario):

    source_trigger_manager = source_scenario.trigger_manager
    # get all the terrains tiles (compiled in a list) in the map
    originalTerrains = source_scenario.map_manager.terrain


    """identify which tiles are to be replaced with water-looking tile"""

    targeted_terrains_detected = []

    for terrain in originalTerrains:
        if terrain.terrain_id == TERRAIN_USED_AS_ICEABLE_WATER_TILE_ID:
            #print("found black tile")
            targeted_terrains_detected.append((terrain.x, terrain.y))

    all_water_terrain = []



    #print(len(all_non_water_terrain))

    USED_SOURCE_PLAYER = 8


    print(targeted_terrains_detected)


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
                                                        foundation_terrain = TerrainId.WATER_MEDIUM, 
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


    transform_first_to_water = source_trigger_manager.add_trigger("transform_first_to_water", enabled=True,looping=False)

    for black_tile in targeted_terrains_detected:
        x,y = black_tile
        transform_first_to_water.new_effect.place_foundation(object_list_unit_id=invisible_storage_with_water_foundation_id,source_player=USED_SOURCE_PLAYER,location_x=x,location_y=y)
        #transform_first_to_water.new_effect.create_object(object_list_unit_id=invisible_storage_id, source_player=1, location_x=x, location_y=y)

    
    """
    turns out we cannot use change ownership or replace objects to process the building generated by "place foundation"
    """


    transform_building_to_gaia = source_trigger_manager.add_trigger("transform_building_to_gaia", enabled=True,looping=False)
    transform_building_to_gaia.new_condition.timer(1)

    for black_tile in targeted_terrains_detected:
        x,y = black_tile
        #transform_first_to_water.new_effect.place_foundation(object_list_unit_id=invisible_storage_with_water_foundation_id,source_player=USED_SOURCE_PLAYER,location_x=x,location_y=y)
        transform_building_to_gaia.new_effect.create_object(object_list_unit_id=OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID, source_player=USED_SOURCE_PLAYER, location_x= x, location_y=y)

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




    clear_blockage_building = source_trigger_manager.add_trigger("clear_blockage_building", enabled=True,looping=False)
    clear_blockage_building.new_condition.timer(timer=TIME_START_FROZEN - 1)
    clear_blockage_building.new_effect.kill_object(object_list_unit_id=OBJECT_USED_TO_BLOCK_CROSSING_FAKE_WATER_ID, source_player=0)










    for terrain in originalTerrains:
        if terrain.terrain_id in TerrainId.water_terrains() and terrain.terrain_id != TERRAIN_USED_AS_ICEABLE_WATER_TILE_ID:
            #print("found black tile")
            all_water_terrain.append((terrain.x, terrain.y))

    all_non_water_terrain = []
    for terrain in originalTerrains:
        if terrain.terrain_id not in TerrainId.water_terrains() and terrain.terrain_id != TERRAIN_USED_AS_ICEABLE_WATER_TILE_ID:
            all_non_water_terrain.append((terrain.x, terrain.y))



    #Start Freezes


    # turn_water_into_ice = source_trigger_manager.add_trigger("turn_water_into_ice", enabled=True,looping=False)
    # turn_water_into_ice.new_condition.timer(timer=TIME_START_FROZEN)

    # for black_tile in targeted_terrains_detected:
    #     x,y = black_tile
    #     turn_water_into_ice.new_effect.place_foundation(object_list_unit_id=intermedite_object_id,source_player=1,location_x=x,location_y=y)

    def process_tile_groups(tile_sets):
        """Process grouped tiles with batched distance groups"""
        # Combine and group tiles as before
        all_tiles = [(x, y, t) for t, tiles in tile_sets.items() for x, y in tiles]
        distance_map = {}
        
        for x, y, t in all_tiles:
            d = (x - POLE_X)**2 + (POLE_Y - y)**2
            if d not in distance_map:
                distance_map[d] = {'water': [], 'non_water': [], 'other': []}
            bucket = 'water' if t == 'water' else 'non_water' if t == 'non_water' else 'other'
            distance_map[d][bucket].append((x, y))

        # Split sorted distances into batches
        sorted_distances = sorted(distance_map.keys(), reverse=True)
        distance_batches = [sorted_distances[i:i+FROZEN_BATCH_SIZE * 3] 
                        for i in range(0, len(sorted_distances), FROZEN_BATCH_SIZE * 3)]

        # Create triggers per distance batch
        for batch_idx, batch_distances in enumerate(distance_batches):
            trigger = source_trigger_manager.add_trigger(
                name=f"freeze_batch_{batch_idx}",
                enabled=True,
                looping=False
            )

            trigger.new_condition.timer(
                timer=TIME_START_FROZEN + (FROZEN_PACE_DELAY * batch_idx)
            )

            # Process all distances in current batch
            for distance in batch_distances:
                # Water tiles
                for x, y in distance_map[distance]['water']:
                    trigger.new_effect.place_foundation(
                        object_list_unit_id=OBJECT_TO_CREATE_ICE_FOR_WATER_TERRAIN_ID,
                        source_player=USED_SOURCE_PLAYER,
                        location_x=x,
                        location_y=y
                    )
                
                # Non-water tiles
                for x, y in distance_map[distance]['non_water']:
                    trigger.new_effect.place_foundation(
                        object_list_unit_id=OBJECT_USED_TO_GENERATE_SNOW_TERRAIN_ID,
                        source_player=USED_SOURCE_PLAYER,
                        location_x=x,
                        location_y=y
                    )
                
                # change 2nd.... to ice
                for x, y in distance_map[distance]['other']:
                    trigger.new_effect.kill_object(object_list_unit_id=invisible_storage_with_water_foundation_id, source_player=0,area_x1=x, area_x2=x, area_y1=y, area_y2=y)
                    trigger.new_effect.place_foundation(
                        object_list_unit_id=OBJECT_TO_CREATE_ICE_FOR_WATER_TERRAIN_ID,
                        source_player=USED_SOURCE_PLAYER,
                        location_x=x,
                        location_y=y
                    )
                

    # Usage
    tile_sets = {
        'water': all_water_terrain,
        'non_water': all_non_water_terrain,
        'other': targeted_terrains_detected  # Add your third category if needed
    }

    process_tile_groups(tile_sets)
    # #

    print(source_scenario.map_manager.map_height)
    print(source_scenario.map_manager.map_width)
    #					0: Unknown (2262) [P1, X103.0, Y39.0] (317958)
    # 317958 worked! but how the hell is this decoding working?




    gaia_units = source_scenario.unit_manager.get_player_units(PlayerId.GAIA)


    # Unit(player=0, x=43.5, y=141.5, z=3.0, reference_id=17330, unit_const=65, status=2, rotation=2.356194496154785, initial_animation_frame=2)

    non_winter_tree = []
    # get reference id
    for gaia_unit in gaia_units:
        if gaia_unit.unit_const in [x.ID for x in OtherInfo.trees()]:
            if gaia_unit.unit_const != OtherInfo.TREE_SNOW_PINE and  gaia_unit.unit_const != OtherInfo.TREE_OAK_AUTUMN_SNOW:
                non_winter_tree.append(gaia_unit)

    def process_winter_trees():
        """Process tree replacement with distance-based batching"""
        # Configuration
        TREE_REPLACE_OBJECTS = [
            OtherInfo.TREE_SNOW_PINE.ID,
            #OtherInfo.TREE_OAK_AUTUMN_SNOW.ID,
            OtherInfo.TREE_DEAD.ID,
            OtherInfo.TREE_I.ID
        ]

        # Group trees by distance
        distance_groups = {}
        for tree in non_winter_tree:
            # Calculate squared distance from northern point
            distance = ((tree.x - POLE_X)** 2) + (POLE_Y - tree.y) ** 2
            # Initialize list if needed
            if distance not in distance_groups:
                distance_groups[distance] = []
                
            distance_groups[distance].append(tree)

        # Create batched triggers
        sorted_distances = sorted(distance_groups.keys(), reverse=True)
        distance_batches = [sorted_distances[i:i+FROZEN_BATCH_SIZE] 
                        for i in range(0, len(sorted_distances), FROZEN_BATCH_SIZE)]

        for batch_idx, batch_distances in enumerate(distance_batches):
            trigger = source_trigger_manager.add_trigger(
                name=f"winter_tree_batch_{batch_idx}",
                enabled=True,
                looping=False
            )

            # Timer condition with progressive delay
            trigger.new_condition.timer(
                timer=TIME_START_FROZEN + (FROZEN_PACE_DELAY * batch_idx)
            )

            # Add replacement effects
            for distance in batch_distances:
                for tree in distance_groups[distance]:
                    import random
                    trigger.new_effect.replace_object(
                        source_player=0,
                        target_player=0,
                        selected_object_ids=tree.reference_id,
                        object_list_unit_id_2=random.choice(TREE_REPLACE_OBJECTS)
                    )

    instruction_trigger = source_trigger_manager.add_trigger("display winter comming", enabled=True, looping=False)
    instruction_trigger.new_condition.timer(TIME_START_FROZEN)
    instruction_trigger.new_effect.display_instructions(object_list_unit_id=HeroInfo.GENGHIS_KHAN.ID,
                                                        source_player=0,
                                                        display_time=20,
                                                        message = "Winter is Coming! Be careful of attack from the frozen river!")


    # Usage
    process_winter_trees()

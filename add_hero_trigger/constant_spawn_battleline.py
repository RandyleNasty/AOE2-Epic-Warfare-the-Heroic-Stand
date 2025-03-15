from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.other import OtherInfo


from AoE2ScenarioParser.datasets.players import PlayerId


from AoE2ScenarioParser.datasets.trigger_lists import ObjectAttribute
from AoE2ScenarioParser.datasets.trigger_lists import Operation


from util_add_tent_spawn_ability import *


from hero_abstract_class import *

from robin_archer import *

from dynamic_enviorment import *

from center_sacred_parameters import *
from hero_exploding_elephant import *

def give_building_ability_to_constantly_spawn_battle_line_unit(source_trigger_manager, 
                                                               building_referece_id, 
                                                               building_unit_id,
                                                               moving_location_x, 
                                                               moving_location_y, 
                                                               source_player):


    
    """
    Trigger that constantly spawn battle line troops from castle


    disabl
    """
    INTERVAL_TO_SPAWN_BATTLE_LINE = 120
    INTERVAL_ATTACK_ORDER = 20
    BATTLELINE_FOOTMAN_0 = 168
    BATTLELINE_ARCHER_0 = 686
    BATTLELINE_FOOTMAN_1 = 164

    BATTLELINE_UNIT_LIST = [BATTLELINE_FOOTMAN_0, BATTLELINE_FOOTMAN_1, BATTLELINE_ARCHER_0]
    BATTLELINE_UNIT_LIST2 = [BATTLELINE_FOOTMAN_0, 
                             BATTLELINE_FOOTMAN_0,
                             BATTLELINE_FOOTMAN_0,
                             BATTLELINE_FOOTMAN_0,
                             BATTLELINE_FOOTMAN_0,
                             BATTLELINE_FOOTMAN_0,
                             BATTLELINE_FOOTMAN_1,
                             BATTLELINE_FOOTMAN_1, 
                             BATTLELINE_FOOTMAN_1,
                             BATTLELINE_FOOTMAN_1,
                             BATTLELINE_FOOTMAN_1, 
                             BATTLELINE_FOOTMAN_1, 

                             #BATTLELINE_ARCHER_0,
                             #BATTLELINE_ARCHER_0,
                             #BATTLELINE_ARCHER_0
                             ]
    

    #modify garrision unit limit
    change_castle_garrison_limit =  source_trigger_manager.add_trigger("change_castle_garrison_limit", enabled=True, looping=False)
    change_castle_garrison_limit.new_effect.modify_attribute(source_player=source_player, 
                                                            #quantity=len(list_hero_ids), 
                                                            quantity=20, 
                                                            operation=Operation.SET, 
                                                            object_attributes=ObjectAttribute.GARRISON_CAPACITY,
                                                            object_list_unit_id=building_unit_id)

    #disable selection
    #battleline_disable_selection = source_trigger_manager.add_trigger("battleline_disable_selection", enabled=True, looping=False)
    #battleline_attack_move_trigger = source_trigger_manager.add_trigger("battleline_attack_move_trigger", enabled=True, looping=True)

    for unit_id in BATTLELINE_UNIT_LIST:
        inst_unit_to_be_boosted = Hero(
        hero_id= unit_id,  # You'll need to provide the correct hero_id
        population = 0,
        hero_status = 0,
        search_radius = 21,
        line_of_sight = 12,
        health_point = 45,
        )
        boost_object(source_trigger_manager, inst_unit_to_be_boosted, [source_player])
        #battleline_disable_selection.new_effect.disable_object_selection(
        #    source_player=source_player,
        #    object_list_unit_id = unit_id
        #)
        #battleline_attack_move_trigger.new_condition.timer(INTERVAL_TO_SPAWN_BATTLE_LINE)
        #battleline_attack_move_trigger.
    

    

    spawn_all_battleline_unit_from_castle = source_trigger_manager.add_trigger("spawn_all_battleline_unit_from_castle", enabled=True, looping=True)


    spawn_all_battleline_unit_from_castle.new_condition.timer(INTERVAL_TO_SPAWN_BATTLE_LINE)

    for unit_id in BATTLELINE_UNIT_LIST2:
        spawn_all_battleline_unit_from_castle.new_effect.create_garrisoned_object(source_player=source_player, 
                                                                    object_list_unit_id_2=unit_id,
                                                                    selected_object_ids = building_referece_id)

    spawn_all_battleline_unit_from_castle.new_effect.unload(source_player=source_player, location_x=moving_location_x, location_y= moving_location_y, selected_object_ids=building_referece_id)
    for unit_id in BATTLELINE_UNIT_LIST:
        spawn_all_battleline_unit_from_castle.new_effect.attack_move(object_list_unit_id = unit_id, location_x=moving_location_x, location_y= moving_location_y, source_player=source_player)
        
        spawn_all_battleline_unit_from_castle.new_effect.disable_object_selection(
            source_player=source_player,
            object_list_unit_id = unit_id
        )


    #add trigger that keep give attack order
    keep_giving_attack_order = source_trigger_manager.add_trigger("keep_giving_attack_order", enabled=True, looping=True)
    keep_giving_attack_order.new_condition.timer(INTERVAL_ATTACK_ORDER)
    for unit_id in BATTLELINE_UNIT_LIST:
        keep_giving_attack_order.new_effect.attack_move(object_list_unit_id = unit_id, location_x=moving_location_x, location_y= moving_location_y, source_player=source_player)

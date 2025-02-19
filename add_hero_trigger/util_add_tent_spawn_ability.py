from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *


from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo

from AoE2ScenarioParser.datasets.players import PlayerId


from AoE2ScenarioParser.datasets.trigger_lists import ObjectAttribute
from AoE2ScenarioParser.datasets.trigger_lists import Operation



def process_heros_for_every_player(trigger_manager, list_hero_ids, playerid):
    trigger_hero_add_tent_spawn_ability = trigger_manager.add_trigger(
                                "hero_add_tent_spawn_ability_globally_" + str(playerid), 
                                enabled=True,
                                looping=False)
    for index, hero_id in enumerate(list_hero_ids):
        process_single_hero(trigger_manager, hero_id, index + 1, trigger_hero_add_tent_spawn_ability, playerid)



def process_single_hero(trigger_manager, hero_id, num_train_button, trigger_hero_add_tent_spawn_ability, playerid):
    #train location, train button, enable the hero. train time, train cost    
    GREEK_COMMANDER_TENT_ID = 2262

    #TRAIN_TIME_HERO = 5 causing bug with condition own object
    TRAIN_TIME_HERO = 0
    trigger_hero_add_tent_spawn_ability.new_effect.modify_attribute(quantity = GREEK_COMMANDER_TENT_ID, 
                                                                    object_attributes = ObjectAttribute.TRAIN_LOCATION, 
                                                                    object_list_unit_id = hero_id, 
                                                                    source_player = playerid, 
                                                                    operation = Operation.SET)

    trigger_hero_add_tent_spawn_ability.new_effect.enable_disable_object(source_player = playerid, 
                                                                        object_list_unit_id = hero_id,
                                                                        enabled = True)
    
    trigger_hero_add_tent_spawn_ability.new_effect.modify_attribute(object_attributes = ObjectAttribute.TRAIN_BUTTON,
                                                                    quantity = num_train_button,
                                                                    source_player = playerid, 
                                                                    object_list_unit_id = hero_id,
                                                                    operation = Operation.SET
                                                                    )

    trigger_hero_add_tent_spawn_ability.new_effect.modify_attribute(object_attributes = ObjectAttribute.TRAIN_TIME,
                                                                    quantity = TRAIN_TIME_HERO,
                                                                    source_player = playerid, 
                                                                    object_list_unit_id = hero_id,
                                                                    operation = Operation.SET
                                                                    )

""" 
    change_object_cost [Index: 5, Display: 5]:
        object_list_unit_id: Frankish Paladin (632)
        source_player: Player One (1)
        resource_1: Unused Resource 008 (8)
        resource_1_quantity: 1
        resource_2: Food Storage (0)
        resource_2_quantity: 0
        resource_3: Food Storage (0)
        resource_3_quantity: 0 """




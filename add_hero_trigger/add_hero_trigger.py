


from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *


from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo

from AoE2ScenarioParser.datasets.players import PlayerId


from AoE2ScenarioParser.datasets.trigger_lists import ObjectAttribute
from AoE2ScenarioParser.datasets.trigger_lists import Operation


from util_add_tent_spawn_ability import *

# File & Folder setup - Declare your scenario directory path
#scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

scenario_folder = "C:/Users/Randy/Games/Age of Empires 2 DE/76561198060805641/resources/_common/scenario/"

# Source scenario to work with

#input_path = scenario_folder + "hero test.aoe2scenario"
#output_path = scenario_folder + "hero test Parsed.aoe2scenario"
input_path = scenario_folder + "Epic_Warfare Remastered v2_0.aoe2scenario"

#input_path = scenario_folder + "Epic_Warfare Remastered v2_0 Parsed.aoe2scenario"

output_path = scenario_folder + "Epic_Warfare Remastered v2_0 Parsed.aoe2scenario"

# declare scenario class

source_scenario:AoE2DEScenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# Start writing your code here:
#print(source_trigger_manager.get_summary_as_string())

content = source_trigger_manager.get_content_as_string()

# Save to a text file
with open("trigger_info.txt", "w", encoding="utf-8") as file:
    file.write(content)



list_hero_ids = [HeroInfo.FRANKISH_PALADIN.ID, HeroInfo.ROBIN_HOOD.ID]

# conduct trigger wisely
for playid in PlayerId.all()[1:]:
    process_heros_for_every_player(source_trigger_manager, list_hero_ids, playid)

#add random spawn after 2 minutes

# detect hero own, if not random spawn one.




"""
strategy though is to bind each custom unit with an unique unused resource
unused resource is between 102 to 117
No No No, use own hero to activate which hero selected by player or random


"""


trigger_delay_hero_auto_spawn = source_trigger_manager.add_trigger(
                                "trigger_delay_hero_auto_spawn", 
                                enabled=True,
                                looping=False)
trigger_delay_hero_auto_spawn.new_condition.timer(timer = 60)
trigger_delay_hero_auto_spawn.new_effect.activate_trigger(trigger_id=len(source_trigger_manager.triggers)) #activate the next added trigger


trigger_detect_hero_die_activate_count_down = source_trigger_manager.add_trigger(
                                "detect_hero_own_and_random_spawn_one", 
                                enabled=False,
                                looping=False)


trigger_detect_hero_die_activate_count_down.new_condition.own_fewer_objects(source_player=1,
                                                                            object_list = HeroInfo.FRANKISH_PALADIN.ID,
                                                                            quantity = 0)
trigger_detect_hero_die_activate_count_down.new_condition.and_()
trigger_detect_hero_die_activate_count_down.new_condition.own_fewer_objects(source_player=1,
                                                                            object_list = HeroInfo.ROBIN_HOOD.ID,
                                                                            quantity = 0)

trigger_detect_hero_die_activate_count_down.new_effect.display_timer(display_time = 1, time_unit=1, timer = 5, reset_timer = 1, message= 'Player1 Hero Spawns in ')
trigger_detect_hero_die_activate_count_down.new_effect.activate_trigger(trigger_id=len(source_trigger_manager.triggers)) #activate the next added trigger



trigger_start_timer_and_spawn_hero = source_trigger_manager.add_trigger("start_timer_and_spawn_hero", enabled=False, looping=False)
trigger_start_timer_and_spawn_hero.new_condition.timer(timer = 30)



trigger_start_timer_and_spawn_hero.new_effect.tribute(quantity=1, tribute_list=8, source_player=0, target_player=1)
trigger_start_timer_and_spawn_hero.new_effect.train_unit(object_list_unit_id=HeroInfo.FRANKISH_PALADIN.ID, quantity=1, selected_object_ids= 317958, source_player=1)
trigger_start_timer_and_spawn_hero.new_effect.activate_trigger(trigger_id = len(source_trigger_manager.triggers) - 2) #activate the last added trigger



# equal chance to spawn the hero
trigger_give_start_resource_8 = source_trigger_manager.add_trigger(
                                "trigger_give_start_resource_8", 
                                enabled=True,
                                looping=False)
trigger_give_start_resource_8.new_effect.tribute(quantity=1,
                                                                tribute_list=8,
                                                                source_player=0,
                                                                target_player=1)


"""
This One is for Equal Chance to spawn Hero, Worked!
add delay to give the user to select hero!
"""
trigger_delay_hero_random_spawn = source_trigger_manager.add_trigger(
                                "trigger_delay_hero_auto_spawn", 
                                enabled=True,
                                looping=False)
trigger_delay_hero_random_spawn.new_condition.timer(timer = 30)
trigger_delay_hero_random_spawn.new_effect.activate_trigger(trigger_id=len(source_trigger_manager.triggers)) #activate the next added trigger

# equal chance to spawn the hero
trigger_may_choose_first_hero = source_trigger_manager.add_trigger(
                                "trigger_may_choose_first_hero", 
                                enabled=False,
                                looping=False)

trigger_may_choose_first_hero.new_condition.chance(quantity=50)
trigger_may_choose_first_hero.new_effect.train_unit(object_list_unit_id=HeroInfo.FRANKISH_PALADIN.ID, 
                                                                   quantity=1, 
                                                                   selected_object_ids= 317958,
                                                                   source_player=1)

trigger_delay_hero_random_spawn = source_trigger_manager.add_trigger(
                                "trigger_delay_hero_random_spawn", 
                                enabled=True,
                                looping=False)
trigger_delay_hero_random_spawn.new_condition.timer(timer = 30)
trigger_delay_hero_random_spawn.new_effect.activate_trigger(trigger_id=len(source_trigger_manager.triggers)) #activate the next added trigger


# equal chance to spawn the hero
trigger_may_choose_second_hero = source_trigger_manager.add_trigger(
                                "trigger_delay_hero_random_spawn", 
                                enabled=False,
                                looping=False)

trigger_may_choose_second_hero.new_condition.chance(quantity=50)
trigger_may_choose_second_hero.new_effect.train_unit(object_list_unit_id=HeroInfo.ROBIN_HOOD.ID, 
                                                                   quantity=1, 
                                                                   selected_object_ids= 317958,
                                                                   source_player=1)




#					0: Unknown (2262) [P1, X103.0, Y39.0] (317958)
# 317958 worked! but how the hell is this decoding working?

# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)




""" #player1 			
                location_x: 103
            #  location_y: 41

				source_player: Player Two (2)
				location_x: 53
				location_y: 114

				source_player: Player Three (3)
				location_x: 27
				location_y: 187
				item_id: 650
				source_player: Player Four (4)
				location_x: 22
				location_y: 102
    
    				source_player: Player Five (5)
				location_x: 180
				location_y: 174
    
    				source_player: Player Six (6)
				location_x: 205
				location_y: 84
    
    				source_player: Player Seven (7)
				location_x: 130
				location_y: 210
    
    				source_player: Player Eight (8)
				location_x: 233
				location_y: 147 """

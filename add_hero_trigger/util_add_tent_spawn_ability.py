from email import message
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *


from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo

from AoE2ScenarioParser.datasets.players import PlayerId


from AoE2ScenarioParser.datasets.trigger_lists import ObjectAttribute
from AoE2ScenarioParser.datasets.trigger_lists import Operation

from general_hero_stats import *

def process_heros_for_every_player(trigger_manager, list_hero_ids, playerid, list_description):
    trigger_hero_add_tent_spawn_ability = trigger_manager.add_trigger(
                                "hero_add_tent_spawn_ability_globally_" + str(playerid), 
                                enabled=True,
                                looping=False)
    for index, hero_id in enumerate(list_hero_ids):
        process_single_hero(trigger_manager, hero_id, index + 1, trigger_hero_add_tent_spawn_ability, playerid, list_description[index])



def process_single_hero(trigger_manager, hero_id, num_train_button, trigger_hero_add_tent_spawn_ability, playerid, description):
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

    # trigger_hero_add_tent_spawn_ability.new_effect.modify_attribute(object_attributes = ObjectAttribute.SHORT_DESCRIPTION_ID,
    #                                                                 quantity = 0,
    #                                                                 source_player = playerid, 
    #                                                                 object_list_unit_id = hero_id,
    #                                                                 operation = Operation.SET,
    #                                                                 message = "test introduction"
    #                                                                 )


    trigger_hero_add_tent_spawn_ability.new_effect.change_object_description(source_player = playerid, object_list_unit_id = hero_id, message = description)

    trigger_hero_add_tent_spawn_ability.new_effect.change_object_cost(object_list_unit_id = hero_id,
                                                    resource_1 = 8,
                                                    resource_1_quantity = 1,
                                                    resource_2 = 0,
                                                    resource_2_quantity = 0,
                                                    resource_3 = 0,
                                                    resource_3_quantity = 0,
                                                    source_player = playerid)

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







""" # For specific player subset
create_hero_respawn_system(
    source_trigger_manager,
    [HeroInfo.VIKING_KING.ID],
    [1, 3, 5]  # Specific player IDs
)

# For all players except GAIA (player 0)
create_hero_respawn_system(
    source_trigger_manager,
    list_hero_ids,
    PlayerId.all()[1:]
)

"""

def create_hero_respawn_system(trigger_manager, hero_ids, players, triggers_that_randomly_chooses_hero_for_players, CONST_MAP_SIZE):
    """Encapsulated hero respawn system for multiple players and heroes"""
    for index, player_id in enumerate(players):
        for hero_id in hero_ids:
            _create_single_hero_triggers(trigger_manager, player_id, hero_id, triggers_that_randomly_chooses_hero_for_players[index], CONST_MAP_SIZE)


    #modify commander tent garrision limit
    # for player_id in players:
    #     change_tent_garrison_limit =  trigger_manager.add_trigger("change_tent_garrison_limit", enabled=True, looping=False)
    #     change_tent_garrison_limit.new_effect.modify_attribute(source_player=player_id, 
    #                                                             #quantity=len(list_hero_ids), 
    #                                                             quantity=1, 
    #                                                             operation=Operation.SET, 
    #                                                             object_attributes=ObjectAttribute.GARRISON_CAPACITY,
    #                                                             object_list_unit_id=2262)        

    """
    to solve conflict between user pick and auto respawn system
    1. if detect hero then deactivate all triggers_that_randomly_chooses_hero_for_players
    2. if detect hero dies then re activate this monitor trigger...
    
    """
    for player_id in players:
        monitor_hero_if_detected_deactivate_auto_spawn = trigger_manager.add_trigger(
        f"monitor_hero_if_detected_deactivate_auto_spawn",
        enabled=True,
        looping=False
        )

        # detect hero dies reactivate this
        detect_hero_die_and_reactivate_the_monitor_trigger = trigger_manager.add_trigger(
        f"detect_hero_die_and_reactivate_the_monitor_trigger",
        enabled=False,
        looping=False
        )


        for idx, hero_id in enumerate(LIST_HERO_IDS):
            monitor_hero_if_detected_deactivate_auto_spawn.new_condition.objects_in_area(
                source_player=player_id,
                object_list=hero_id,
                area_x1=0,
                area_x2=CONST_MAP_SIZE - 1,
                area_y1=0,
                area_y2=CONST_MAP_SIZE - 1,
                object_state=ObjectState.ALIVE, 
                quantity=1,
            )

            if idx < len(LIST_HERO_IDS) - 1:
                monitor_hero_if_detected_deactivate_auto_spawn.new_condition.or_()

        monitor_hero_if_detected_deactivate_auto_spawn.new_effect.deactivate_trigger(triggers_that_randomly_chooses_hero_for_players[player_id-1].trigger_id)
        monitor_hero_if_detected_deactivate_auto_spawn.new_effect.activate_trigger(detect_hero_die_and_reactivate_the_monitor_trigger.trigger_id)

 
        for idx, hero_id in enumerate(LIST_HERO_IDS):
            detect_hero_die_and_reactivate_the_monitor_trigger.new_condition.objects_in_area(
                source_player=player_id,
                object_list=hero_id,
                area_x1=0,
                area_x2=CONST_MAP_SIZE - 1,
                area_y1=0,
                area_y2=CONST_MAP_SIZE - 1,
                object_state=ObjectState.DYING, 
                quantity=1,
            )

            if idx < len(LIST_HERO_IDS) - 1:
                detect_hero_die_and_reactivate_the_monitor_trigger.new_condition.or_()

        detect_hero_die_and_reactivate_the_monitor_trigger.new_effect.activate_trigger(monitor_hero_if_detected_deactivate_auto_spawn.trigger_id)



def _create_single_hero_triggers(manager, player_id, hero_id, trigger_that_randomly_chooses_hero, CONST_MAP_SIZE ):
    """Create trigger chain for one player-hero combination"""
    # Detection trigger
    # detect_trigger = manager.add_trigger(
    #     f"detect_hero_{player_id}_{hero_id}",
    #     enabled=True,
    #     looping=False
    # )
    # detect_trigger.new_condition.own_objects(
    #     source_player=player_id,
    #     object_list=hero_id,
    #     quantity=1
    # )



    # Death detection trigger
    death_trigger = manager.add_trigger(
        f"death_detect_{player_id}_{hero_id}",
        enabled=True,
        looping=False
    )
    # death_trigger.new_condition.own_fewer_objects(
    #     source_player=player_id,
    #     object_list=hero_id,
    #     quantity=0
    # )

    death_trigger.new_condition.objects_in_area(
        source_player = player_id,
        object_list = hero_id,
        area_x1 = 0,
        area_x2 = CONST_MAP_SIZE - 1,
        area_y1 = 0,
        area_y2 = CONST_MAP_SIZE - 1,
        object_state = ObjectState.DYING, 
        quantity = 1,
    )
    #death_trigger.new_condition.or_()

    if hero_id == HeroInfo.GODS_OWN_SLING_PACKED.ID:
        death_trigger.new_condition.and_()        
        death_trigger.new_condition.own_fewer_objects(
            source_player=player_id,
            object_list=HeroInfo.GODS_OWN_SLING.ID,
            quantity=0
        )   

    # Respawn trigger
    respawn_trigger = manager.add_trigger(
        f"respawn_{player_id}_{hero_id}",
        enabled=False,
        looping=False
    )

    """
    Give player 20 seconds more to choose hero again after the old dead
    """

    if player_id in [5, 6, 7, 8]:
        respawn_trigger.new_condition.timer(timer=int(TIME_HERO_RESPAWN/2) - 20)
        death_trigger.new_effect.display_timer(
        display_time=int(TIME_HERO_RESPAWN/2) - 20,
        time_unit=TimeUnit.SECONDS,
        timer=player_id,
        reset_timer=1,
        message=f'Player {player_id} can repick Hero in ' + r"%d"
        )
    else:
        respawn_trigger.new_condition.timer(timer=TIME_HERO_RESPAWN - 20)
        death_trigger.new_effect.display_timer(
        display_time=TIME_HERO_RESPAWN - 20,
        time_unit=TimeUnit.SECONDS,
        timer=player_id,
        reset_timer=1,
        message=f'Player {player_id} can repick Hero in ' + r"%d"
        )
    
    # Setup trigger relationships
    #detect_trigger.new_effect.activate_trigger(death_trigger.trigger_id)



    death_trigger.new_effect.activate_trigger(respawn_trigger.trigger_id)
    death_trigger.new_effect.activate_trigger(trigger_that_randomly_chooses_hero.trigger_id)


    respawn_trigger.new_effect.tribute(
        quantity=1,
        tribute_list=8,
        source_player=0,
        target_player=player_id
    )

    respawn_trigger.new_effect.activate_trigger(death_trigger.trigger_id)


    """
    This One is for Equal Chance to spawn Hero, Worked!
    add delay to give the user to select hero!
    """


def create_equal_chance_system(trigger_manager, players, hero_ids, tents_list, NUM_HERO_ALLOWED):
    """Create equal chance hero selection system with:
    - Auto-calculated percentages
    - Integer rounding compensation
    - Player-specific spawn points
    """
    num_heroes = len(hero_ids)
    if num_heroes == 0:
        raise ValueError("At least one hero must be provided")
        
    # Calculate base chance and adjust for rounding errors
    base_chance = round(100 / num_heroes)
    chances = [base_chance] * num_heroes
    total = sum(chances)
    

    triggers_that_randomly_chooses_hero_for_players = []

    # Adjust last chance if needed
    if total != 100:
        chances[-1] += 100 - total
    
    for player_id in players:
        spawn_id = tents_list[player_id - 1]
        
        # Create delay trigger
        delay_trigger = trigger_manager.add_trigger(
            f"p{player_id}_hero_delay",
            enabled=True,
            looping=False
        )

        if player_id in [5, 6, 7, 8]:
            delay_trigger.new_condition.timer(timer=int(TIME_WINDOW_PLAYER_CHOOSE_HERO/2))
        else:
            delay_trigger.new_condition.timer(timer=TIME_WINDOW_PLAYER_CHOOSE_HERO)

        # if player_id == 3:
        #     delay_trigger.new_effect.display_instructions(object_list_unit_id=HeroInfo.GENGHIS_KHAN.ID,
        #                                                 source_player=3,
        #                                                 display_time=20,
        #                                                 message = "Random Dice begins!")
        
        chance_triggers = []

        # Create chance triggers
        for idx, (hero_id, chance) in enumerate(zip(hero_ids, chances), 1):
            trigger = trigger_manager.add_trigger(
                f"p{player_id}_hero{idx}_chance",
                enabled=False,
                looping=False
            )
            

            #trigger.new_condition.timer(idx * 2)

            trigger.new_condition.chance(quantity=chance)

            x, y = tent_training_location_tuple[player_id-1]

            # trigger.new_effect.train_unit(
            #     object_list_unit_id=hero_id,
            #     quantity=1,
            #     selected_object_ids=spawn_id,
            #     source_player=player_id,
            #     area_x1 = tent_area_data[player_id-1]['area_x1'],
            #     area_x2 = tent_area_data[player_id-1]['area_x2'],
            #     area_y1 = tent_area_data[player_id-1]['area_y1'],
            #     area_y2 = tent_area_data[player_id-1]['area_y2'],                
            # )

            
            trigger.new_effect.create_garrisoned_object(source_player=player_id, 
                                                                    object_list_unit_id_2=hero_id,
                                                                    selected_object_ids = TENTS_SELECTED_OBJECT_IDS[player_id-1])
            trigger.new_effect.unload(source_player=player_id, location_x=x, location_y= y, selected_object_ids=TENTS_SELECTED_OBJECT_IDS[player_id-1])



            chance_triggers.append(trigger)
            delay_trigger.new_effect.activate_trigger(trigger.trigger_id)
        import random
        #once one chance trigger activate disable other generated chance trigger
        for trigger in chance_triggers:
            #get other chance trigger except for itself
            other_triggers = [t for t in chance_triggers if t != trigger][NUM_HERO_ALLOWED - 1:]
            num_to_remove = len(other_triggers) - (NUM_HERO_ALLOWED - 1)

            #so that second selected hero not always chariot hero
            #if num_to_remove > 0:
                #other_triggers = random.sample(other_triggers, len(other_triggers) - num_to_remove)

            for other in other_triggers:
                trigger.new_effect.deactivate_trigger(other.trigger_id)

        triggers_that_randomly_chooses_hero_for_players.append(delay_trigger)
    
    return triggers_that_randomly_chooses_hero_for_players
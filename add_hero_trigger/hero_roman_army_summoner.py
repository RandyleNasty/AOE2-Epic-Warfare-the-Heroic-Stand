from hero_abstract_class import *
from AoE2ScenarioParser.datasets.heroes import HeroInfo

from AoE2ScenarioParser.datasets.players import PlayerId

from AoE2ScenarioParser.datasets.trigger_lists import ObjectAttribute
from AoE2ScenarioParser.datasets.trigger_lists import Operation
from AoE2ScenarioParser.datasets.trigger_lists import ActionType
from general_hero_stats import *

def create_roman_army_summoner(source_trigger_manager):

    """
    ROMAN ARMY SUMMON HERO
    """
    projectile_LBT_id = 512


    footman_summoned_id = 2318
    archerman_summoned_id = HeroInfo.GUGLIELMO_EMBRIACO.ID

    num_summon_roman_army = 13
    num_summon_hp_drop_per_second_roman_army = 10
    CONST_TIME_INTERVAL_TRIGGER = 17

    reload_time = 18

    CONST_SUMMON_NUM_DETECT_THRESHOLD = 3

    HERO_ID_ROMAN_ARMY_SUMMONER = HeroInfo.BELISARIUS.ID

    inst_projectile_LBT = Hero(hero_id = projectile_LBT_id, 
                                    #standing_graphic = 1721, 
                                    standing_graphic = 4258, 
                                    #walking_graphic = 3822,
                                    #dying_graphic = 1744,
                                    dead_unit_id = footman_summoned_id,
                                    projectile_arc = 1,
                                    projectile_arc_divide = 3,
                                    projectile_arc_multiply = 2,
                                    #blood_unit = sabo_man_id,

                                    #blood_unit = HeroInfo.HENRY_II.ID,
                                    movement_speed_divide = 2
                                    )


    inst_roman_army_summon_hero = Hero(
        hero_id=HERO_ID_ROMAN_ARMY_SUMMONER,  # You'll need to provide the correct hero_id
        projectile_unit=projectile_LBT_id,
        secondary_projectile_unit = HeroInfo.GUGLIELMO_EMBRIACO.ID,
        max_range=7,
        min_range=1,
        search_radius = 10,
        line_of_sight = 10,


        melee_attack=1,
        #blast_width=1,
        #blast_attack_level=2,
        pierce_armor=general_cav_pierce_armour,
        melee_armour=general_cav_melee_armour,
        attack_reload_set=reload_time,  
        accuracy_percent=1,
        attack_dispersion = 3,
        total_missile = num_summon_roman_army,
        #attack_dispersion = 1,
        #attack_dispersion_multiply=3,
        combat_ability= 1 + 16 + 8,
        # #walking_graphic = 654,
        # movement_speed=1,
        # #frame_delay=4,
        health_point=350,
        #projectile_smart_mode = 3,
        population = 0,
        garrison_capacity = 25,
        charge_event = 1,
        charge_type = 4,
        recharge_rate = 1,
        max_charge = 5,

    )

    boost_object(source_trigger_manager, inst_projectile_LBT, PlayerId.all()[1:])
    boost_object(source_trigger_manager, inst_roman_army_summon_hero, PlayerId.all()[1:])

    """
    following code does not work, because UNLOAD does not work
    """

    # detect_attack_and_spawn_list = []
   
    # add_delays_to_detection_list = []
    # for player in range(1, 9):
    #     add_delay_trigger = source_trigger_manager.add_trigger("add_delay_trigger", enabled=False, looping=False)
    #     add_delays_to_detection_list.append(add_delay_trigger)

    # for player in range(1, 9):
    #     detect_attack_action_army_hero = source_trigger_manager.add_trigger("detect_attack_action_army_hero", enabled=True, looping=False)
    #     detect_attack_action_army_hero.new_condition.own_objects(quantity=num_summon_roman_army-1, object_list=projectile_LBT_id, source_player=player)
    #     detect_attack_action_army_hero.new_condition.timer(1)
    #     for unit in range(1, 4):
    #         detect_attack_action_army_hero.new_effect.create_garrisoned_object(source_player=player, 
    #                                                                     object_list_unit_id = HERO_ID_ROMAN_ARMY_SUMMONER,
    #                                                                     object_list_unit_id_2=footman_summoned_id)
    #     for unit in range(1, 4):
    #         detect_attack_action_army_hero.new_effect.create_garrisoned_object(source_player=player, 
    #                                                                 object_list_unit_id = HERO_ID_ROMAN_ARMY_SUMMONER,
    #                                                                 object_list_unit_id_2=archerman_summoned_id)
    #     #detect_attack_action_army_hero.new_effect.unload(source_player=player, object_list_unit_id=HERO_ID_ROMAN_ARMY_SUMMONER, area_x1 = 0, area_x2 = 200, area_y1 = 0, area_y2 = 200, location_x = WEST_TARGET_LOCATION_X,  location_y = WEST_TARGET_LOCATION_Y)
    #     detect_attack_action_army_hero.new_effect.task_object(source_player=player,object_list_unit_id=HERO_ID_ROMAN_ARMY_SUMMONER, action_type=ActionType.UNLOAD)

    #     detect_attack_action_army_hero.new_effect.task_object(source_player=player,object_list_unit_id=footman_summoned_id, action_type=ActionType.STAGGERED_FORMATION)
    #     detect_attack_action_army_hero.new_effect.task_object(source_player=player,object_list_unit_id=archerman_summoned_id, action_type=ActionType.STAGGERED_FORMATION)

    #     detect_attack_action_army_hero.new_effect.activate_trigger(add_delays_to_detection_list[player-1].trigger_id)

    #     detect_attack_and_spawn_list.append(detect_attack_action_army_hero)

    # #detect_attack_action_army_hero
    # for player in range(1, 9):
    #     add_delays_to_detection_list[player-1].new_condition.timer(reload_time - 1)
    #     add_delays_to_detection_list[player-1].new_effect.activate_trigger(detect_attack_and_spawn_list[player-1].trigger_id)
        #add_delays_to_detection_list[player-1].new_effect.task_object(source_player=player,object_list_unit_id=HERO_ID_ROMAN_ARMY_SUMMONER, action_type=ActionType.UNGARRISON)

    

    # add lifetime of summoned footman
    list_footman_detection = []
    list_footman_minus_hp = []

    for player in range(1, 9):
        minus_trigger = source_trigger_manager.add_trigger("global_footman_minus_hp", enabled=False, looping=False)
        list_footman_minus_hp.append(minus_trigger)

    for player in range(1, 9):
        detection_trigger = source_trigger_manager.add_trigger("global_footman_detection", enabled=True, looping=False)
        detection_trigger.new_condition.own_objects(quantity=3*num_summon_roman_army+1, object_list=footman_summoned_id, source_player=player)
        detection_trigger.new_effect.activate_trigger(list_footman_minus_hp[player-1].trigger_id)
        list_footman_detection.append(detection_trigger)

    for index, trigger in enumerate(list_footman_minus_hp):
        trigger.new_condition.timer(CONST_TIME_INTERVAL_TRIGGER)
        # trigger.new_effect.change_object_hp(
        #     object_list_unit_id=footman_summoned_id, operation=3, quantity=num_summon_hp_drop_per_second_roman_army, source_player=index+1
        # )
        trigger.new_effect.kill_object(source_player = index+1, object_list_unit_id = footman_summoned_id)
        trigger.new_effect.change_object_stance(
            object_list_unit_id=footman_summoned_id, source_player=index+1, attack_stance=0
        )
        trigger.new_effect.activate_trigger(list_footman_detection[index].trigger_id)


    # add lifetime of summoned archer
    list_archer_detection = []
    list_archer_minus_hp = []

    for player in range(1, 9):
        minus_trigger = source_trigger_manager.add_trigger("global_archer_minus_hp", enabled=False, looping=False)
        list_archer_minus_hp.append(minus_trigger)

    for player in range(1, 9):
        detection_trigger = source_trigger_manager.add_trigger("global_archer_detection", enabled=True, looping=False)
        detection_trigger.new_condition.own_objects(quantity=CONST_SUMMON_NUM_DETECT_THRESHOLD, object_list=archerman_summoned_id, source_player=player)
        detection_trigger.new_effect.activate_trigger(list_archer_minus_hp[player-1].trigger_id)
        list_archer_detection.append(detection_trigger)

    for index, trigger in enumerate(list_archer_minus_hp):
        trigger.new_condition.timer(CONST_TIME_INTERVAL_TRIGGER)
        # trigger.new_effect.change_object_hp(
        #     object_list_unit_id=archerman_summoned_id, operation=3, quantity=num_summon_hp_drop_per_second_roman_army, source_player=index+1
        # )
        trigger.new_effect.kill_object(source_player = index+1, object_list_unit_id = archerman_summoned_id)
        trigger.new_effect.change_object_stance(
            object_list_unit_id=archerman_summoned_id, source_player=index+1, attack_stance=0
        )
        trigger.new_effect.activate_trigger(list_archer_detection[index].trigger_id)




    """
    TO-DO garrisoned unit and unload to create units
    """ 












    inst_footman_summoned = Hero(
        hero_id=footman_summoned_id,  # You'll need to provide the correct hero_id
        dying_graphic = 5462,
        health_point=20,
        dead_unit_id = 0,
        population = 0,
        search_radius = 10,
        line_of_sight = 10,
        # projectile_smart_mode = 2,

    )

    inst_archerman_summoned = Hero(
        hero_id=archerman_summoned_id,  # You'll need to provide the correct hero_id
        dying_graphic = 5462,
        health_point=45,
        dead_unit_id = footman_summoned_id,
        population = 0,
        search_radius = 10,
        line_of_sight = 10,
        # projectile_smart_mode = 2,


    )

    boost_object(source_trigger_manager, inst_footman_summoned, PlayerId.all()[1:])
    boost_object(source_trigger_manager, inst_archerman_summoned, PlayerId.all()[1:])








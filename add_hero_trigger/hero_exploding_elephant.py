from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *


from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.other import OtherInfo


from AoE2ScenarioParser.datasets.players import PlayerId


from AoE2ScenarioParser.datasets.trigger_lists import ObjectAttribute
from AoE2ScenarioParser.datasets.trigger_lists import Operation



from hero_abstract_class import *

HERO_FAKE_AS_EXPLODING_ELEPHANT_ID = 1071
sabo_man_id = 706

def create_hero_exploding_elephant(source_trigger_manager):
    """
    Ranged Unit to enable Friendly Fire
    With Projectile Range > 1, blast width > 0. 

    """

    """
    EXPLODING ELEPHANT 
    implementation idea:
    have a low attack, high health elephant,
    which when dead, spawns a heavily boost second type elephant that fires explosive while summon exploding man.

    """

    LAST_EXPLODING_ELEPHANT_ID = 1162
    NUM_TOTAL_MISSILE = 45

    inst_weak_elephant = Hero(hero_id=HERO_FAKE_AS_EXPLODING_ELEPHANT_ID, 
                            dead_unit_id = HeroInfo.BAYINNAUNG.ID,
                            blood_unit = HeroInfo.BAYINNAUNG.ID,
                            health_point = 500,
                            melee_attack=1,
                            dying_graphic = 0,
                            search_radius = 7,
                            line_of_sight = 7,
                                population = 0,
                            )

    # forbidden auto delete
    disable_selection_trigger = source_trigger_manager.add_trigger("disable_selection_trigger",enabled=True, looping=False)
    for player in PlayerId.all()[1:]:
        disable_selection_trigger.new_effect.disable_object_deletion(object_list_unit_id=HERO_FAKE_AS_EXPLODING_ELEPHANT_ID, source_player=player)

    boost_object(source_trigger_manager, inst_weak_elephant, PlayerId.all()[1:])

    attack_dispersion_for_exploding_elephant = 2
    blast_width_for_exploding_elephant = 3

    inst_exploding_elephant = Hero(
        hero_id=HeroInfo.BAYINNAUNG.ID,  # You'll need to provide the correct hero_id
        secondary_projectile_unit = sabo_man_id,
        projectile_unit=1595,
        blast_attack_level=4,
        blast_width = blast_width_for_exploding_elephant,
        melee_attack=150,
        max_range=2,
        min_range=0,
        total_missile = NUM_TOTAL_MISSILE,
        combat_ability= 1 + 8 + 16,
        attack_dispersion = attack_dispersion_for_exploding_elephant,
        accuracy_percent = 20,

        health_point=100,
        standing_graphic = 2863,
        dying_graphic = 2860,
        walking_graphic = 2864,
        attack_reload_set = 60,

        dead_unit_id = LAST_EXPLODING_ELEPHANT_ID,
        blood_unit = LAST_EXPLODING_ELEPHANT_ID,
        search_radius = 10,
        #movement_speed = 2,
        line_of_sight = 10,
        population = 0,

        melee_attack_for_building = 100,
        melee_attack_for_wall_and_gate = 100,
    )

    boost_object(source_trigger_manager, inst_exploding_elephant, PlayerId.all()[1:])



    inst_last_exploding_elephant = Hero(
        hero_id=LAST_EXPLODING_ELEPHANT_ID,  # You'll need to provide the correct hero_id
        secondary_projectile_unit = sabo_man_id,
        projectile_unit=1595,
        blast_attack_level=4,
        blast_width = blast_width_for_exploding_elephant,
        melee_attack=150,
        max_range=2,
        min_range=0,
        total_missile = NUM_TOTAL_MISSILE,
        combat_ability= 1 + 8 + 16,
        attack_dispersion = attack_dispersion_for_exploding_elephant,
        accuracy_percent = 20,

        health_point=100,
        standing_graphic = 2863,
        dying_graphic = 2860,
        walking_graphic = 2864,
        attack_reload_set = 60,
        search_radius = 10,
        #movement_speed = 2,
        line_of_sight = 10,
            population = 0,
        dead_unit_id = 706,
        blood_unit  = 706,
        melee_attack_for_building = 100,
        melee_attack_for_wall_and_gate = 100,

    )

    boost_object(source_trigger_manager, inst_last_exploding_elephant, PlayerId.all()[1:])


    const_time_trigger_interval = 5
    num_hp_drop = 40

    list_exploding_elephant_detection = []
    list_exploding_elephant_minus_hp = []

    list_last_exploding_elephant_detection = []
    list_last_exploding_elephant_minus_hp = []

        # Exploding Elephant
    for player in range(1, 9):
        minus_trigger = source_trigger_manager.add_trigger("global_exploding_elephant_minus_hp", enabled=False, looping=False)
        list_exploding_elephant_minus_hp.append(minus_trigger)

    for player in range(1, 9):
        detection_trigger = source_trigger_manager.add_trigger("global_exploding_elephant_detection", enabled=True, looping=False)
        detection_trigger.new_condition.own_objects(quantity=NUM_TOTAL_MISSILE - 1, object_list=inst_exploding_elephant.hero_id, source_player=player)
        detection_trigger.new_effect.activate_trigger(list_exploding_elephant_minus_hp[player-1].trigger_id)
        list_exploding_elephant_detection.append(detection_trigger)

    for index, trigger in enumerate(list_exploding_elephant_minus_hp):
        trigger.new_condition.timer(const_time_trigger_interval)
        trigger.new_effect.change_object_hp(
            object_list_unit_id=inst_exploding_elephant.hero_id, operation=3, quantity=num_hp_drop, source_player=index+1
        )
        trigger.new_effect.change_object_stance(
            object_list_unit_id=inst_exploding_elephant.hero_id, source_player=index+1, attack_stance=0
        )
        trigger.new_effect.activate_trigger(list_exploding_elephant_detection[index].trigger_id)

    # Last Exploding Elephant
    for player in range(1, 9):
        minus_trigger = source_trigger_manager.add_trigger("global_last_exploding_elephant_minus_hp", enabled=False, looping=False)
        list_last_exploding_elephant_minus_hp.append(minus_trigger)

    for player in range(1, 9):
        detection_trigger = source_trigger_manager.add_trigger("global_last_exploding_elephant_detection", enabled=True, looping=False)
        detection_trigger.new_condition.own_objects(quantity=NUM_TOTAL_MISSILE - 1, object_list=inst_last_exploding_elephant.hero_id, source_player=player)
        detection_trigger.new_effect.activate_trigger(list_last_exploding_elephant_minus_hp[player-1].trigger_id)
        list_last_exploding_elephant_detection.append(detection_trigger)

    for index, trigger in enumerate(list_last_exploding_elephant_minus_hp):
        trigger.new_condition.timer(const_time_trigger_interval)
        trigger.new_effect.change_object_hp(
            object_list_unit_id=inst_last_exploding_elephant.hero_id, operation=3, quantity=num_hp_drop, source_player=index+1
        )
        trigger.new_effect.change_object_stance(
            object_list_unit_id=inst_last_exploding_elephant.hero_id, source_player=index+1, attack_stance=0
        )
        trigger.new_effect.activate_trigger(list_last_exploding_elephant_detection[index].trigger_id)

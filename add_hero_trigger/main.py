


import glob
from multiprocessing import spawn
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


from util_add_tent_spawn_ability import *
from constant_spawn_battleline import *

from hero_abstract_class import *

from robin_archer import *

from dynamic_enviorment import *

from center_sacred_parameters import *
from hero_exploding_elephant import *
from hero_roman_army_summoner import *

# File & Folder setup - Declare your scenario directory path
#scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

from general_hero_stats import *
# Source scenario to work with

#input_path = scenario_folder + "hero test.aoe2scenario"
#output_path = scenario_folder + "hero test Parsed.aoe2scenario"
#input_path = scenario_folder + "Epic_Warfare Remastered v2_1.aoe2scenario"


#output_path = "C:/Users/Randy/Games/Age of Empires 2 DE/76561198060805641/mods/local/Epic Warfare the Heroic Stand Remasterd 2_0/resources/_common/scenario/Epic Warfare the Heroic Stand Remasterd 2_0.aoe2scenario"


# declare scenario class


def parse_scenario_with_epic_warfare_logic(input_path, output_path, num_hero_allowed):


    source_scenario:AoE2DEScenario = AoE2DEScenario.from_file(input_path)

    # declare trigger manager to work with variables and triggers
    source_trigger_manager = source_scenario.trigger_manager

    # Start writing your code here:
    #print(source_trigger_manager.get_summary_as_string())

    content = source_trigger_manager.get_content_as_string()

    print("print to trigger_info")
    # Save to a text file
    with open("trigger_info.txt", "w", encoding="utf-8") as file:
        file.write(content)

    cleon_ID = 2346
    Darius_ID = 2347
    Jean_De_Lorrain_ID = 644  
    Dagnajan_Elephant_ID = 1106

    sabo_man_id = 706
    hero_test_id = 1072



    #BRASIDAS suspicious of having bug
    #HERO_BRASIDAS_ID = 2162
    HERO_BRASIDAS_ID = 2317
    #HeroInfo.ROBIN_HOOD.ID
    list_hero_ids = [
                    #Darius_ID, 
                    HeroInfo.ROBIN_HOOD.ID,
                    HeroInfo.JEAN_BUREAU.ID,
                    cleon_ID,
                    HeroInfo.KOTYAN_KHAN.ID,
                    HeroInfo.ULRICH_VON_JUNGINGEN.ID,
                    HeroInfo.TSAR_KONSTANTIN.ID,
                    Dagnajan_Elephant_ID,
                    HeroInfo.GENGHIS_KHAN.ID,
                    # HeroInfo.GODS_OWN_SLING_PACKED.ID,
                    HERO_FAKE_AS_EXPLODING_ELEPHANT_ID,
                    HERO_BRASIDAS_ID,
                    #HeroInfo.FRANCISCO_DE_ORELLANA.ID,
                    HeroInfo.BELISARIUS.ID
                    ]





    list_description = [
        #"Javelin Splashing duo-horse Chariot", 
                        "Vaelor, the Stormbow, a feared master of the battlefield, wields the legendary Stormbow, capable of unleashing a relentless downpour of arrows upon his enemies. His volleys blot out the sun, leaving no escape for those caught beneath his deadly rain. Tales of his wrath spread across kingdoms, as entire armies have fallen under his sky-darkening assault.",
                        "The Cataclysm Ordinance: Skyfall Cluster Bomb Cannon, a doomsday weapon of unparalleled destruction, reshapes the battlefield with every thunderous volley. Upon activation, it unleashes a cascade of incendiary canisters, each fragmenting into countless explosive shards that rain devastation from the heavens. No stronghold is impenetrable, no army beyond its reach—its fury engulfs all who dare stand beneath its cataclysmic downpour. Legends speak in hushed whispers of its wrath, a harbinger of ruin whose echoes linger long after the battlefield is reduced to ash.",
                        "The Invincible Footman, known as the Warlord's Juggernaut, marches fearlessly into battle, an unstoppable force clad in impenetrable armor. Armed with devastating explosives, he turns the tide of war with calculated detonations, blasting through enemy ranks and fortifications alike. Blades shatter against him, arrows break upon his shield—no force can halt his advance. Stories of his wrath spread like wildfire, a living legend of destruction that leaves only ruin in his wake.", 
                        "The Explosive Arrow Mounter Archer, known as the Blazing Harbinger, strikes fear into the hearts of his foes with every fiery shot. Armed with a deadly arsenal of explosive-tipped arrows, he turns the sky into a battlefield, each projectile igniting upon impact in a storm of fire and shrapnel. No wall is safe, no formation unbroken—his volleys tear through ranks and fortifications alike. Whispers of his devastation spread far and wide, a bringer of ruin whose arrows spell the end for those caught in their blazing wake.",
                        "The Flaming Throw Knight, known as the Infernal Vanguard, charges into battle wreathed in fire, his weapon a conduit of relentless devastation. With every swing, he hurls searing flames, engulfing enemies in a blazing storm that leaves only ashes in its wake. His presence alone turns the battlefield into an inferno, where armor melts and courage falters. Tales of his fiery wrath spread like wildfire, a harbinger of ruin whose advance none can withstand.", 
                        "The Gatling Ballista Tri-Horse Chariot, known as the Stormstride Reaper, thunders across the battlefield like a force of nature. Drawn by three war-hardened steeds, its rotating ballista unleashes an unrelenting hail of bolts, shredding ranks and fortifications with mechanical precision. No warrior can outrun its charge, no shield can withstand its storm—those caught in its path are left in ruin. Legends of its devastation echo through war-torn lands, a relentless harbinger of annihilation.", 
                        "The Flaming Thunder War Elephant, known as the Pyrostorm Behemoth, is a living engine of destruction, towering over the battlefield as fire and fury erupt in its wake. Adorned with armor wreathed in flame, it charges with unstoppable force, trampling ranks beneath its colossal might while hurling searing blasts of fire and lightning. Walls crumble, armies scatter, and the earth trembles beneath its relentless advance. Whispers of its devastation spread like wildfire—when the Pyrostorm Behemoth marches, only ashes remain.", 
                        "The Exploding Wolf Summoner, known as the Ravager of the Wilds, calls forth a pack of fiery, explosive wolves that tear through the battlefield with savage fury. Each summoned beast is a ticking time bomb, charging at enemies with a howl that heralds their doom, detonating in violent bursts of fire and shrapnel upon impact. No enemy is safe, as the explosive wolves hunt in relentless packs, turning the battlefield into a chaotic inferno. Tales of the Ravager’s fury spread across the lands, a terrifying force that leaves only destruction in its wake.",
                        #"God Swing",
                        "The Self-Exploding Elephant, known as the Doombringer, is a massive, unstoppable force of nature, bound for annihilation. With every step, it charges relentlessly toward its target, its body rigged with volatile explosives. Upon impact, it detonates in a cataclysmic explosion, obliterating everything in its path—fortifications, armies, and the earth itself. No structure stands, no army survives its wrath. Whispers of the Doombringer's devastation spread far and wide, a terrifying omen of unstoppable destruction, where only ruin remains in its wake.",
                        "The AOE Greek Hero Footman, known as the Spartan Vanguard, stands as a symbol of unmatched strength and courage. Clad in heavy armor and armed with a legendary shield, he leads the charge with the might of a warrior born from the gods. With every swing of his weapon, he creates shockwaves that ripple across the battlefield, striking down foes in all directions. His presence inspires his allies, while his devastating attacks leave nothing but destruction in his wake. The stories of his valor and wrath echo throughout the lands, a living legend whose fury no enemy can withstand.",
                        #"Mounted Gunpower Knight",
                        "The Roman Army Summon General, known as the Imperial Warlord, commands the might of a disciplined and unyielding legion. With a single call, he summons the full force of the Roman army, their ironclad ranks forming an impenetrable wall of power and precision. His strategic brilliance leads them into battle, with every legionnaire moving in perfect harmony to crush enemies under the weight of Roman might. No force can rival his command, no army can break his ranks. Legends speak of the Imperial Warlord’s ability to turn the tide of war, leaving only the echoes of victory in his wake."
                        ]



    TIME_WINDOW_PLAYER_CHOOSE_HERO = 120
    TIME_HERO_RESPAWN = 120
    NUM_HERO_ALLOWED = num_hero_allowed




    instruction_trigger = source_trigger_manager.add_trigger(
                                    "display hero instruction", 
                                    enabled=True,
                                    looping=False)
    instruction_trigger.new_effect.display_instructions(object_list_unit_id=HeroInfo.GENGHIS_KHAN.ID,
                                                        source_player=0,
                                                        display_time=20,
                                                        message = "Welcome to Epic Warfare - The Heroic Stand! Feel free to select a hero from the Holy Commander Tent. Your choice will be your main hero, who will respawn throughout the game.")

    instruction_trigger.new_effect.display_timer(
        display_time=TIME_WINDOW_PLAYER_CHOOSE_HERO,
        time_unit=TimeUnit.SECONDS,
        timer=0,
        reset_timer=1,
        message=r"Time out selecting heroes in %d"
    )



    """
    TO-DO find better solution for thumb ring technolgy affects hero...
    """
    # conduct trigger wisely by encapusaltion
    # disable_thumb_ring_tech_for_all = source_trigger_manager.add_trigger("disable_thumb_ring_tech_for_all", enabled=True, looping=False)

    # for playid in PlayerId.all()[1:]:
    #     disable_thumb_ring_tech_for_all.new_effect.enable_disable_technology(playid, enabled=False, technology=TechInfo.THUMB_RING.ID)












    # conduct trigger wisely by encapusaltion
    for playid in PlayerId.all()[1:]:
        process_heros_for_every_player(source_trigger_manager, list_hero_ids, playid, list_description)

    # very fragile value! if in map the commander tent changes, could cause crash!
    tents_selected_object_ids = [317958, 317979, 322879, 319227, 328305, 328275, 328335, 328365]

        # attack_graphic = 1786,
        # standing_graphic = 1788,
        # dying_graphic = 1787,
        # walking_graphic = 1789,


    create_roman_army_summoner(source_trigger_manager)

    create_hero_exploding_elephant(source_trigger_manager)




    """

    Projectile spawns unit

    512 Projectile LBT used by longboat 250
    """




    inst_mounted_gunpower_hero = Hero(
        hero_id=HeroInfo.FRANCISCO_DE_ORELLANA.ID,  # You'll need to provide the correct hero_id
        #projectile_unit=projectile_LBT_id,
        #secondary_projectile_unit = 676,
        # max_range=10,
        # min_range=4,
        # melee_attack=5,
        blast_width=1,
        blast_attack_level=4,
        # pierce_armor=10,
        # melee_armour=10,
        # attack_reload_set=4,  
        accuracy_percent=75,
        total_missile = 10,
        attack_dispersion = 1,
        #attack_dispersion_multiply=3,
        combat_ability= 1 + 16 + 8,
        # #walking_graphic = 654,
        # movement_speed=1,
        # #frame_delay=4,
        # health_point=200,
        # projectile_smart_mode = 2,
        population = 0,
    )





    boost_object(source_trigger_manager, inst_mounted_gunpower_hero, PlayerId.all()[1:])





    """
    BRASIDAS FOOTMAN HERO

    """
    projectile_BRASIDAS_used = 1057


    inst_war_galley_projectile = Hero(hero_id = projectile_BRASIDAS_used, 
                                    #standing_graphic = 1743, 
                                    #walking_graphic = 1743,
                                    #dying_graphic = 1743,
                                    dead_unit_id = 1334,
                                    #blood_unit = 1334,
                                    movement_speed_divide = 3,
                                    movement_speed_multiply = 2)

    boost_object(source_trigger_manager, inst_war_galley_projectile, PlayerId.all()[1:])



    inst_BRASIDAS_footman_hero = Hero(
        hero_id=HERO_BRASIDAS_ID,  # You'll need to provide the correct hero_id
        #projectile_unit=war_galley_projectile_id,
        projectile_unit = projectile_BRASIDAS_used,
        #secondary_projectile_unit = 676,
        max_range=3,
        min_range=0,
        melee_attack=15,
        blast_width=1,
        blast_attack_level=4,
        pierce_armor=general_footman_pierce_armour,
        melee_armour=general_footman_melee_armour,
        attack_reload_set=2,  
        accuracy_percent=45,
        total_missile = 25,
        attack_dispersion = 1,
        attack_dispersion_multiply=3,
        attack_dispersion_divide = 2,
        combat_ability= 1 + 16,
        #walking_graphic = 654,
        #movement_speed=1,
        #frame_delay=4,
        health_point=500,
        projectile_smart_mode = 2,

        charge_event = 1,
        charge_type = 4,
        recharge_rate = 1,
        max_charge = 5,
        #charge_event = 1,
        #charge_type = 3,
        #recharge_rate = 1,
        #max_charge = 10,
        population = 0,
    )


    boost_object(source_trigger_manager, inst_BRASIDAS_footman_hero, PlayerId.all()[1:])



    inst_projectile_unit_laser = Hero(
        hero_id= 1595,  # You'll need to provide the correct hero_id
        movement_speed_divide = 2,
        #blast_attack_level = 2,
        blast_width = 2,
        standing_graphic = 3403,
    )

    boost_object(source_trigger_manager, inst_projectile_unit_laser, PlayerId.all()[1:])


    # fire arrows 787
   


    #for playerid in PlayerId.all()[1:]:
    #    detect_exploding_elephant_trigger = source_trigger_manager.add_trigger("detect_exploding_elephant_trigger",)


    # global_elephant_detection= source_trigger_manager.add_trigger("global_elephant_detection", enabled=True, looping=False)
    # global_elephant_attack_stance_change = source_trigger_manager.add_trigger("global_elephant_attack_stance_change",enabled=False,looping=False)
    # for player in range(1,9):
    #     global_elephant_detection.new_condition.own_objects(quantity=1, object_list=LAST_EXPLODING_ELEPHANT_ID, source_player=player)
    #     global_elephant_detection.new_condition.or_()
    #     global_elephant_detection.new_condition.own_objects(quantity=1, object_list=HeroInfo.BAYINNAUNG.ID, source_player=player)
    #     global_elephant_detection.new_effect.activate_trigger(global_elephant_attack_stance_change.trigger_id)



    # for player in range(1, 9):  # Loop from player 1 to 9
    #     global_elephant_attack_stance_change.new_condition.timer(2)
    #     global_elephant_attack_stance_change.new_effect.change_object_stance(
    #         object_list_unit_id=LAST_EXPLODING_ELEPHANT_ID, source_player=player, attack_stance=0
    #     )
    #     global_elephant_attack_stance_change.new_effect.change_object_stance(
    #         object_list_unit_id=HeroInfo.BAYINNAUNG.ID, source_player=player, attack_stance=0
    #     )
    #     global_elephant_attack_stance_change.new_effect.activate_trigger(global_elephant_detection.trigger_id)



    # for player in PlayerId.all()[1:]:
    #     trigger_that_kills_exploding_elephant = source_trigger_manager.add_trigger("trigger_that_kills_exploding_elephant", enabled=True, looping=True)
    #     trigger_that_kills_exploding_elephant.new_condition.own_objects(quantity=5, object_list=1595, source_player=player)
    #     trigger_that_kills_exploding_elephant.new_effect.kill_object(object_list_unit_id=HeroInfo.BAYINNAUNG.ID, source_player=player)




    leviathan_projectile_id = 2226
    inst_leviathan_projectile = Hero(hero_id=leviathan_projectile_id, 
                                    dead_unit_id = 1334, 
                                    #movement_speed_divide = 2
                                    dying_graphic = 15534,

                                    )
    boost_object(source_trigger_manager, inst_leviathan_projectile, PlayerId.all()[1:])



    inst_dagnajan_hero = Hero(
        hero_id= Dagnajan_Elephant_ID,  # You'll need to provide the correct hero_id
        projectile_unit=leviathan_projectile_id,
        #secondary_projectile_unit = 
        max_range=7,
        min_range=0,
        blast_width = 1,
        blast_attack_level=4,
        attack_dispersion_multiply=5,
        accuracy_percent=50,
        pierce_armor=general_cav_pierce_armour,
        melee_armour=general_cav_melee_armour,
        melee_attack = 20,
        attack_reload_set=3,  
        total_missile = 30,
        combat_ability= 1 + 8 + 16,
        #walking_graphic = 654,
        movement_speed=1,
        #projectile_vanish_mode = 1
        #unit_trait = 8,
        #trait_piece = 2151,
        health_point = 500,
        line_of_sight = 7,
        search_radius = 7,
            population = 0,

        charge_event = 1,
        charge_type = 4,
        recharge_rate = 1,
        max_charge = 10,
    )
    boost_object(source_trigger_manager, inst_dagnajan_hero, PlayerId.all()[1:])





    """GOD SWING BOOST"""

    inst_god_swing_packed_hero = Hero(
        hero_id=HeroInfo.GODS_OWN_SLING_PACKED.ID,  # You'll need to provide the correct hero_id
        projectile_unit=469,
        max_range=20,
        line_of_sight = 20,
        search_radius = 20,
        min_range=13,
        blast_width=1,
        blast_attack_level=2, 
        accuracy_percent=45,
        total_missile = 30,
        attack_dispersion=1,
        movement_speed=1,
        health_point = 300,
            population = 0,
    )
    boost_object(source_trigger_manager, inst_god_swing_packed_hero, PlayerId.all()[1:])



    # original projectile 469
    projectile_from_war_galley_antiquity = 506

    inst_god_swing_projectile = Hero(hero_id = projectile_from_war_galley_antiquity, 
                                    standing_graphic = 3393, 
                                    walking_graphic = 3378,
                                    dying_graphic = 12206,
                                    dead_unit_id = 1334,
                                    #blood_unit = 1334,
                                #movement_speed_divide = 2
                                )
    boost_object(source_trigger_manager, inst_god_swing_projectile, PlayerId.all()[1:])




    inst_god_swing_hero = Hero(
        hero_id=HeroInfo.GODS_OWN_SLING.ID,  # You'll need to provide the correct hero_id
        projectile_unit=projectile_from_war_galley_antiquity,
        max_range=20,
        line_of_sight = 20,
        search_radius = 20,
        min_range=2,
        blast_width=2,
        blast_attack_level=2, 
        accuracy_percent=45,
        total_missile = 30,
        attack_dispersion=1,
        health_point = 300,

        combat_ability= 1 + 16 + 8,
            population = 0,
            
    )

    boost_object(source_trigger_manager, inst_god_swing_hero, PlayerId.all()[1:])






    inst_frank_paladin_hero = Hero(
        hero_id=HeroInfo.FRANKISH_PALADIN.ID,  # You'll need to provide the correct hero_id
        projectile_unit=1780,
        max_range=1,
        min_range=0,
        melee_attack=12,
        blast_width=1,
        blast_attack_level=2,
        pierce_armor=10,
        melee_armour=10,
        attack_reload_divide=2,  
        accuracy_percent=15,
        total_missile = 30,
        attack_dispersion=1,
        combat_ability= 16 + 8,
        #walking_graphic = 654,
        movement_speed=2,
        #dead_unit_id = 942,
        health_point = 300,
            population = 0,

    )

    boost_object(source_trigger_manager, inst_frank_paladin_hero, PlayerId.all()[1:])




    # Instantiate Jean Bureau
    inst_jean_bureau = Hero(
        hero_id=HeroInfo.JEAN_BUREAU.ID,  # You'll need to provide the correct hero_id
        max_range=11,  #
        line_of_sight = 11,
        search_radius = 11,
        min_range=7,  # Not modified in the original function
        total_missile=60,
        projectile_unit=658,
        accuracy_percent=35,
        attack_dispersion = 1,
        attack_dispersion_divide=2,
        #melee_armour=0,  # Not modified in the original function
        #pierce_armor=0,  # Not modified in the original function
        melee_attack=10,
        melee_attack_for_building = 5,
        melee_attack_for_wall_and_gate = 5,
        movement_speed=1,
        health_point=300,
        blast_width=1,
        blast_attack_level=2,
        combat_ability = 1 + 8 + 16,
            population = 0,

    )


    """
    TO-DO extend projectile unit with standing grpahic 1722

    war_galley_projectile_id = 373
    projectile_polycritus_id = 2342

    """
    flame_id_spawned_after_explosion = 1334
    inst_fire_projectile_for_ulrich = Hero(

        hero_id=676,
        standing_graphic = 1722,
        dead_unit_id = flame_id_spawned_after_explosion
        
    )

    boost_object(source_trigger_manager, inst_fire_projectile_for_ulrich, PlayerId.all()[1:])




    inst_hero_ulrich = Hero(
        hero_id=HeroInfo.ULRICH_VON_JUNGINGEN.ID,  # You'll need to provide the correct hero_id
        melee_attack=15,
        #movement_speed=2,
        blast_width=1,
        melee_armour=general_cav_melee_armour,
        pierce_armor=general_cav_pierce_armour,
        blast_attack_level=4,
        max_range=2,
        total_missile=30,
        projectile_unit=676,
        accuracy_percent=50,
        combat_ability= 1 + 8 + 16,
        attack_dispersion = 3,
        health_point = 450,
        population = 0,
        movement_speed = 2,
    )




    javaline_with_fire_id = 1780

    inst_hero_darius = Hero(
        max_range=4,
        min_range = 0,
        line_of_sight = 4,
        search_radius = 4,
        hero_id=Darius_ID,  # You'll need to provide the correct hero_id
        blast_width=1,
        blast_attack_level=4,
        melee_attack=15,
        total_missile=40,  # This covers both Max Total Missiles and Total Missiles
        projectile_unit=leviathan_projectile_id, 
        pierce_armor=15 ,
        melee_armour=15,
        movement_speed=2,
        combat_ability= 1 + 16 + 8,
        accuracy_percent = 20,
        attack_dispersion=1,
        attack_reload_set = 2,
        population = 0,
    )


    inst_hero_mounted_archer = Hero(
        hero_id=HeroInfo.KOTYAN_KHAN.ID,  # You'll need to provide the correct hero_id
        max_range=9,
        min_range = 0,
        line_of_sight = 9,
        search_radius = 9,
        melee_attack=15,
        blast_width=1,
        blast_attack_level=4,
        accuracy_percent=70,
        #attack_dispersion=1,
        total_missile=4,
        pierce_armor=general_cav_pierce_armour,
        melee_armour=general_cav_melee_armour,
        attack_reload_set=2, 
        projectile_unit = 1595,
        combat_ability= 1 + 16 + 8,
            population = 0,
    )

    inst_hero_tsar_constantin = Hero(
        hero_id=HeroInfo.TSAR_KONSTANTIN.ID,  # You'll need to provide the correct hero_id
        projectile_unit=627,
        max_range=10,
        line_of_sight = 10,
        search_radius = 10,
        melee_attack=15,
        blast_width=1,
        blast_attack_level=4,
        pierce_armor=general_cav_pierce_armour,
        melee_armour=general_cav_melee_armour,
        attack_reload_divide=12,  # This will be divided, not added
        accuracy_percent=50,
        attack_dispersion=1,
        #combat_ability= 8, # has bug that attack ground no projectile shown
        projectile_vanish_mode = 1,
        projectile_hit_mode = 1,
        combat_ability= 1,
            population = 0,
    )













    wolf_id = 700

    num_summon = 6
    summon_cooldown = 7
    summon_hp_drop_per_second = 35
    flame_id_spawned_after_explosion = 1334
    num_max_flame = num_summon * 4

    inst_tamar_summon_hero = Hero(
        hero_id= HeroInfo.GENGHIS_KHAN.ID,  # You'll need to provide the correct hero_id
        #blast_defense_level = 1,
        projectile_unit=676,
        secondary_projectile_unit=wolf_id,
        max_range=6,
        line_of_sight = 7,
        search_radius = 7,
        attack_dispersion=5,
        accuracy_percent=20,
        pierce_armor=general_cav_pierce_armour,
        melee_armour=general_cav_melee_armour,
        melee_attack = 1,
        attack_reload_set=summon_cooldown,  
        total_missile = num_summon,
        combat_ability= 8 + 16,
        #walking_graphic = 654,
        #movement_speed=2,
        #dead_unit_id = 942,
        attack_graphic = 12660,
        standing_graphic = 12663,
        #standing_graphic_2 = 12662,
        dying_graphic = 12661,
        walking_graphic = 12665,
        icon_id = 414,
        charge_event = 1,
        charge_type = 3,
        recharge_rate = 1,
        max_charge = summon_cooldown-3,
        health_point = 200,
        #projectile_vanish_mode = 1
        #unit_trait = 8,
        #trait_piece = 2151,
            population = 0,
    )
    inst_summon_unit = Hero(
        hero_id= wolf_id,  # You'll need to provide the correct hero_id
        search_radius = 7,
        movement_speed = 1,
        line_of_sight = 7,
        hero_status = 64,
        dead_unit_id = sabo_man_id,
            population = 0,
    )
    # not actually doing damage to friendly unit
    inst_sabo_man_unit = Hero(
        hero_id= sabo_man_id,  # You'll need to provide the correct hero_id
        melee_attack = 20,
        melee_attack_for_building = 10,
        melee_attack_for_wall_and_gate = 5,
        blast_attack_level=4,
        health_point = 0,
        max_range=2,
        min_range=0,
        blast_width = 1,
        blood_unit = flame_id_spawned_after_explosion,
        standing_graphic = 7253,
        attack_graphic = 7251,
        #dying_graphic = 7252,
        walking_graphic = 7256,
        #undead_graphic = 7252
            population = 0,
    )

    # remove flames regularly
    for player_num in range(1, 9):
        # Create triggers for each player
        detect_trigger = source_trigger_manager.add_trigger(
            f"remove_flame_p{player_num}_trigger",
            enabled=True,
            looping=False
        )
        
        remove_trigger = source_trigger_manager.add_trigger(
            f"remove_flame_p{player_num}_cleanup",
            enabled=False,
            looping=False
        )

        # Set up detection conditions/effects
        detect_trigger.new_condition.own_objects(
            quantity=num_max_flame,
            source_player=player_num,
            object_list=flame_id_spawned_after_explosion
        )
        detect_trigger.new_effect.activate_trigger(remove_trigger.trigger_id)

        # Set up removal effects
        remove_trigger.new_effect.kill_object(
            object_list_unit_id=flame_id_spawned_after_explosion,
            source_player=player_num
        )
        remove_trigger.new_effect.activate_trigger(detect_trigger.trigger_id)



    #need trigger to remove flames for performance reason

    # add lifetime of summoned wolf
    list_wolf_detection = []
    list_wolf_minus_hp = []

    for player in range(1, 9):
        minus_trigger = source_trigger_manager.add_trigger("global_wolf_minus_hp",enabled=False,looping=False)
        list_wolf_minus_hp.append(minus_trigger)

    for player in range(1, 9):
        detection_trigger = source_trigger_manager.add_trigger("global_wolf_detection", enabled=True, looping= False)
        detection_trigger.new_condition.own_objects(quantity=num_summon-1, object_list=wolf_id, source_player=player)
        detection_trigger.new_effect.activate_trigger(list_wolf_minus_hp[player-1].trigger_id)
        list_wolf_detection.append(detection_trigger)

    for index, trigger in enumerate(list_wolf_minus_hp):
        trigger.new_condition.timer(5)
        trigger.new_effect.change_object_hp(
            object_list_unit_id=wolf_id, operation=3, quantity=summon_hp_drop_per_second, source_player=index+1
        )
        trigger.new_effect.change_object_stance(
            object_list_unit_id=wolf_id, source_player=index+1, attack_stance=0
        )
        trigger.new_effect.activate_trigger(list_wolf_detection[index].trigger_id)




    boost_object(source_trigger_manager, inst_tamar_summon_hero, PlayerId.all()[1:])
    boost_object(source_trigger_manager, inst_summon_unit, PlayerId.all()[1:])
    boost_object(source_trigger_manager, inst_sabo_man_unit, PlayerId.all()[1:])
    # elephant, where invisible project, but with flame impact

    #change projectile to unit. spawn hero


    #inst_projectile_vol_fire = Hero(hero_id = 511, standing_graphic = 1743)

    boost_object(source_trigger_manager, inst_robin_archer_hero, PlayerId.all()[1:])
    # add fire effect to arrows





    boost_object(source_trigger_manager, inst_projectile_vol_fire, PlayerId.all()[1:])


    boost_object(source_trigger_manager, inst_jean_bureau, PlayerId.all()[1:])
    boost_object(source_trigger_manager, inst_hero_ulrich, PlayerId.all()[1:])
    boost_object(source_trigger_manager, inst_hero_darius, PlayerId.all()[1:])
    boost_object(source_trigger_manager, inst_hero_mounted_archer, PlayerId.all()[1:])

    boost_object(source_trigger_manager, inst_hero_tsar_constantin, PlayerId.all()[1:])

    #boost_hero(source_trigger_manager, inst_projectile_vol_fire, PlayerId.all()[1:])



    #cleon_ID
    inst_cleon_hero = Hero(
        hero_id= cleon_ID,  # You'll need to provide the correct hero_id
        #projectile_unit=1798,
        secondary_projectile_unit = sabo_man_id,
        projectile_unit=1595,
        blast_attack_level=4 + 64 + 128,
        #blast_defense_level = 1,
        melee_attack=15,
        max_range=2,
        min_range=0,
        pierce_armor=general_footman_pierce_armour,
        melee_armour=general_footman_melee_armour,
        attack_reload_set=3,  
        total_missile = 7,
        combat_ability= 8 + 16,
        #attack_dispersion = 1,
        #accuracy_percent = 10,
        blast_width = 2,
        health_point=350,
        movement_speed_divide=3,
        movement_speed_multiply=3,
        #walking_graphic = 654,
        projectile_smart_mode = 2,
        #dead_unit_id = 942,
        projectile_vanish_mode = 0,
        #unit_trait = 8,
        #trait_piece = 2151,

        charge_event = 1,
        charge_type = 4,
        recharge_rate = 1,
        max_charge = 5,

            population = 0,
    )


    # inst_summon_hawk_unit = Hero(
    #     hero_id= 96,  # You'll need to provide the correct hero_id
    #     dead_unit_id = sabo_man_id,
    # )

    # boost_hero(source_trigger_manager, inst_summon_hawk_unit, PlayerId.all()[1:])
    boost_object(source_trigger_manager, inst_cleon_hero, PlayerId.all()[1:])

    #put change object cost to last, not before modify attribute.

    # for player_id in PlayerId.all()[1:]:
    #     for hero_id in list_hero_ids:
    #         trigger = source_trigger_manager.add_trigger(
    #                                     "change_hero_cost_" + str(player_id) + "_" + str(hero_id), 
    #                                     enabled=True,
    #                                     looping=False)
    #         trigger.new_effect.change_object_cost(object_list_unit_id = hero_id,
    #                                                 resource_1 = 8,
    #                                                 resource_1_quantity = 1,
    #                                                 resource_2 = 0,
    #                                                 resource_2_quantity = 0,
    #                                                 resource_3 = 0,
    #                                                 resource_3_quantity = 0,
    #                                                 source_player = player_id)



    # Give Player just 1 resource id 8. so hero limited to 1
    def give_start_resource_to_players(trigger_manager, resource_id, quantity, players):
        """Give initial resources to multiple players using encapsulated triggers"""
        for player_id in players:
            trigger = trigger_manager.add_trigger(
                f"give_resource_{resource_id}_to_p{player_id}", 
                enabled=True,
                looping=False
            )
            trigger.new_effect.tribute(
                quantity=quantity,
                tribute_list=resource_id,
                source_player=0,
                target_player=player_id
            )




    # Usage for all human players (assuming 8 players total)
    give_start_resource_to_players(
        source_trigger_manager,
        resource_id=8,
        quantity=NUM_HERO_ALLOWED,
        players=[1, 2, 3, 4, 5, 6, 7, 8]  # Or use PlayerId.humans() if available
    )



    create_variable = source_trigger_manager.add_trigger("create_variable", enabled=True, looping=False)
    create_variable.new_effect.change_variable(quantity=1, operation=Operation.SET, variable=0)



    """
    This One is for Equal Chance to spawn Hero, Worked!
    add delay to give the user to select hero!
    """


    def create_equal_chance_system(trigger_manager, players, hero_ids, tents_list):
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
                

                trigger.new_condition.timer(idx * 2)

                trigger.new_condition.chance(quantity=chance)
                trigger.new_effect.train_unit(
                    object_list_unit_id=hero_id,
                    quantity=1,
                    selected_object_ids=spawn_id,
                    source_player=player_id
                )
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

    # Usage examples:
    # 2 heroes (50/50)
    triggers_that_randomly_chooses_hero_for_players = create_equal_chance_system(
        source_trigger_manager,
        PlayerId.all()[1:],
        list_hero_ids,
        tents_list=tents_selected_object_ids
    )











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

    def create_hero_respawn_system(trigger_manager, hero_ids, players, triggers_that_randomly_chooses_hero_for_players):
        """Encapsulated hero respawn system for multiple players and heroes"""
        for index, player_id in enumerate(players):
            for hero_id in hero_ids:
                _create_single_hero_triggers(trigger_manager, player_id, hero_id, triggers_that_randomly_chooses_hero_for_players[index])

    def _create_single_hero_triggers(manager, player_id, hero_id, trigger_that_randomly_chooses_hero):
        """Create trigger chain for one player-hero combination"""
        # Detection trigger
        detect_trigger = manager.add_trigger(
            f"detect_hero_{player_id}_{hero_id}",
            enabled=True,
            looping=False
        )
        detect_trigger.new_condition.own_objects(
            source_player=player_id,
            object_list=hero_id,
            quantity=1
        )
        



        # Death detection trigger
        death_trigger = manager.add_trigger(
            f"death_detect_{player_id}_{hero_id}",
            enabled=False,
            looping=False
        )
        death_trigger.new_condition.own_fewer_objects(
            source_player=player_id,
            object_list=hero_id,
            quantity=0
        )

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

        respawn_trigger.new_condition.timer(timer=TIME_HERO_RESPAWN - 20)
        
        # Setup trigger relationships
        detect_trigger.new_effect.activate_trigger(death_trigger.trigger_id)
        death_trigger.new_effect.display_timer(
            display_time=100,
            time_unit=TimeUnit.SECONDS,
            timer=player_id,
            reset_timer=1,
            message=f'Player {player_id} can repick Hero in ' + r"%d"
        )
        death_trigger.new_effect.activate_trigger(respawn_trigger.trigger_id)
        death_trigger.new_effect.activate_trigger(trigger_that_randomly_chooses_hero.trigger_id)


        respawn_trigger.new_effect.tribute(
            quantity=1,
            tribute_list=8,
            source_player=0,
            target_player=player_id
        )

        # respawn_trigger.new_effect.display_timer(
        #     display_time=20,
        #     time_unit=TimeUnit.SECONDS,
        #     timer=player_id,
        #     reset_timer=1,
        #     message=f'Player {player_id} can repick Hero in' + r"%d"
        # )
        

        # respawn_trigger.new_effect.train_unit(
        #     object_list_unit_id=hero_id,
        #     quantity=1,
        #     selected_object_ids=tents_ids[player_id-1],
        #     source_player=player_id
        # )
        respawn_trigger.new_effect.activate_trigger(detect_trigger.trigger_id)





    # For all players except GAIA (player 0)
    create_hero_respawn_system(
        source_trigger_manager,
        list_hero_ids,
        PlayerId.all()[1:],
        triggers_that_randomly_chooses_hero_for_players
    )





    add_blockage_object_to_target_tiles_that_mimic_water(source_scenario)



    """
    CENTER SACRED SPA CONTROL TRANSFER MECHANISM

    https://www.bilibili.com/video/BV1oM43enEhw?spm_id_from=333.788.recommend_more_video.8&vd_source=b55afea14026a74cb6f67fd8241ebb69

    MAKING MOVEMENT SPEED = 0, would disable Monk healing ability

    """
    MONK_HERO_ID = 177
    PAGAN_SHRINE_ID = 1712
    ### GIVE SPECIAL ABILITY TO CENTER SPA
    CENTER_MONK_HERO_ID = 1822
    #movement speed = 0 make unit cannot heal
    inst_spa_monk = Hero(
        hero_id= CENTER_MONK_HERO_ID,  # You'll need to provide the correct hero_id
        max_range=12,
        #accuracy_percent=0,
        #combat_ability= 16,
        attack_graphic = 1516,
        standing_graphic = 0,
        standing_graphic_2 = 0,
        walking_graphic = 1519,
        population = 0,
        #selection_effect = 2,
        search_radius = 12,
        line_of_sight = 12,
        occlusion_mode = 0,
        #movement_speed_divide = 4,
        #movement_speed=0,

    )
    boost_object(source_trigger_manager, inst_spa_monk, PlayerId.all())

    inst_shrine = Hero(hero_id = PAGAN_SHRINE_ID, combat_ability = 32, hero_status = 64)

    boost_object(source_trigger_manager, inst_shrine, PlayerId.all())


    #area_x1: 111
    #area_y1: 117
    #area_x2: 125
    #area_y2: 130

    UNIT_DETECT_AREA_X1 = 109
    UNIT_DETECT_AREA_X2 = 127
    UNIT_DETECT_AREA_Y1 = 115
    UNIT_DETECT_AREA_Y2 = 132

    BUILDING_AREA_X1 = 113
    BUILDING_AREA_X2 = 123
    BUILDING_AREA_Y1 = 118  
    BUILDING_AREA_Y2 = 128

    INITIAL_OWNER = 1

    initialize_trigger = source_trigger_manager.add_trigger("initialization", enabled=True, looping=False)
    #initialize_trigger.new_effect.disable_object_deletion(source_player=INITIAL_OWNER, area_x1=BUILDING_AREA_X1, area_x2=BUILDING_AREA_X2, area_y1=BUILDING_AREA_Y1, area_y2=BUILDING_AREA_Y2)

    #initialize_trigger.new_effect.disable_object_selection(source_player=INITIAL_OWNER, area_x1=BUILDING_AREA_X1, area_x2=BUILDING_AREA_X2, area_y1=BUILDING_AREA_Y1, area_y2=BUILDING_AREA_Y2)


    # for player in PlayerId.all():  # Players 1 to 8
    initialize_trigger.new_effect.disable_object_deletion(
        source_player=INITIAL_OWNER,
        area_x1=BUILDING_AREA_X1, area_x2=BUILDING_AREA_X2,
        area_y1=BUILDING_AREA_Y1, area_y2=BUILDING_AREA_Y2
    )

    initialize_trigger.new_effect.disable_object_selection(
        source_player=INITIAL_OWNER,
        area_x1=BUILDING_AREA_X1, area_x2=BUILDING_AREA_X2,
        area_y1=BUILDING_AREA_Y1, area_y2=BUILDING_AREA_Y2
    )


    initialize_trigger.new_effect.disable_unit_targeting(
            source_player=INITIAL_OWNER,
            area_x1=BUILDING_AREA_X1, area_x2=BUILDING_AREA_X2,
            area_y1=BUILDING_AREA_Y1, area_y2=BUILDING_AREA_Y2
    )

    initialize_trigger.new_effect.change_object_hp(source_player=INITIAL_OWNER, area_x1=BUILDING_AREA_X1, area_x2=BUILDING_AREA_X2, area_y1=BUILDING_AREA_Y1, area_y2=BUILDING_AREA_Y2, quantity=0, operation=Operation.SET)
    initialize_trigger.new_effect.change_object_hp(source_player=INITIAL_OWNER, area_x1=BUILDING_AREA_X1, area_x2=BUILDING_AREA_X2, area_y1=BUILDING_AREA_Y1, area_y2=BUILDING_AREA_Y2, quantity=0, operation=Operation.SET)





    NUM_CONVERTABLE_BUILDING = 5

    # MONK also considerable as military
    NUM_PLAYER_UNIT_REQUIRED_TO_CONVERT = 1


    list_give_it_to_player_triggers = []
    for player in PlayerId.all()[1:]:
        trigger = source_trigger_manager.add_trigger(f"p{player}_give", enabled=True, looping=False)
        list_give_it_to_player_triggers.append(trigger)
    # Construct Give to Gaia

    #FROM PLAYER GIVE BACK TO GAIA
    list_give_to_gaia_triggers = []
    for index, player in enumerate(PlayerId.all()[1:]):
        trigger = source_trigger_manager.add_trigger(f"p{player}_give_to_gaia", enabled=True, looping=False)
        list_give_to_gaia_triggers.append(trigger)
        trigger.new_condition.timer(5)
        trigger.new_condition.objects_in_area(quantity=1, 
                                            inverted=True,
                                            area_x1 = UNIT_DETECT_AREA_X1,
                                            area_x2 = UNIT_DETECT_AREA_X2,
                                            area_y1 = UNIT_DETECT_AREA_Y1,
                                            area_y2 =UNIT_DETECT_AREA_Y2,
                                            source_player=player, 
                                            object_state=ObjectState.ALIVE, 
                                            object_type=ObjectType.MILITARY)    
        trigger.new_effect.change_ownership(source_player=player, 
                                            target_player=0, 
                                            area_x1=BUILDING_AREA_X1, 
                                            area_x2=BUILDING_AREA_X2,
                                            area_y1=BUILDING_AREA_Y1, 
                                            area_y2=BUILDING_AREA_Y2,
                                            #object_type=ObjectType.BUILDING
                                            )
        # trigger.new_effect.deactivate_trigger(list_looping_trigger_that_continue_assert_stand_ground[index].trigger_id)
        for give_to_player_trigger in list_give_it_to_player_triggers:
            trigger.new_effect.activate_trigger(give_to_player_trigger.trigger_id)
    
    # After all triggers are added, deactivate all other triggers except the current one
    for index, trigger in enumerate(list_give_to_gaia_triggers):
        for other_index, other_trigger in enumerate(list_give_to_gaia_triggers):
            if other_index != index:
                trigger.new_effect.deactivate_trigger(other_trigger.trigger_id)



    # FROM GAIA TO PLAYER

    for index, trigger in enumerate(list_give_it_to_player_triggers):
        trigger.new_condition.timer(5)
        trigger.new_condition.objects_in_area(quantity=NUM_PLAYER_UNIT_REQUIRED_TO_CONVERT, 
                                            area_x1 = UNIT_DETECT_AREA_X1,
                                            area_x2 = UNIT_DETECT_AREA_X2,
                                            area_y1 = UNIT_DETECT_AREA_Y1,
                                            area_y2 = UNIT_DETECT_AREA_Y2,
                                            source_player=index+1, 
                                            object_state=ObjectState.ALIVE,
                                            #object_type=ObjectType.MILITARY
                                            )
        trigger.new_condition.and_()

        #detect gaia unit
        trigger.new_condition.objects_in_area(
                                            quantity=NUM_CONVERTABLE_BUILDING, 
                                            area_x1=BUILDING_AREA_X1, 
                                            area_x2=BUILDING_AREA_X2, 
                                            area_y1=BUILDING_AREA_Y1, 
                                            area_y2=BUILDING_AREA_Y2,
                                            source_player=0, 
                                            object_state=ObjectState.ALIVE,
                                            object_type=ObjectType.BUILDING
                                            )
        trigger.new_effect.change_ownership(source_player = 0, 
                                            target_player = index + 1,
                                            area_x1=BUILDING_AREA_X1, 
                                            area_x2=BUILDING_AREA_X2, 
                                            area_y1=BUILDING_AREA_Y1, 
                                            area_y2=BUILDING_AREA_Y2,
                                            #object_type=ObjectType.BUILDING
                                            )


        # trigger.new_effect.activate_trigger(list_looping_trigger_that_continue_assert_stand_ground[index].trigger_id)
        trigger.new_effect.activate_trigger(list_give_to_gaia_triggers[index].trigger_id)


    # After all triggers are added, deactivate all other triggers except the current one
    for index, trigger in enumerate(list_give_it_to_player_triggers):
        for other_index, other_trigger in enumerate(list_give_it_to_player_triggers):
            if other_index != index:
                trigger.new_effect.deactivate_trigger(other_trigger.trigger_id)



    print(len(list_give_it_to_player_triggers))
    print(len(list_give_to_gaia_triggers))



    """
    ADD FINAL EAST ALL  STAR HERO PUSH


                    area_x1: 210
                    area_y1: 182
                    area_x2: 238
                    area_y2: 239
    """
    BATTLELINE_CASTLE_SPAWN_REFERENCE_ID = 224976
    change_castle_garrison_limit =  source_trigger_manager.add_trigger("change_castle_garrison_limit", enabled=True, looping=False)
    change_castle_garrison_limit.new_effect.modify_attribute(source_player=8, 
                                                            #quantity=len(list_hero_ids), 
                                                            quantity=20, 
                                                            operation=Operation.SET, 
                                                            object_attributes=ObjectAttribute.GARRISON_CAPACITY,
                                                            object_list_unit_id=445)


    spawn_all_hero_from_castle = source_trigger_manager.add_trigger("spawn_all_hero_from_castle", enabled=False, looping=False)
    looping_keep_spawning_trash_unit =  source_trigger_manager.add_trigger("looping_keep_spawning_trash_unit", enabled=False, looping=True)


    detect_area_x1 = 210
    detect_area_x2 = 238
    detect_area_y1 = 182
    detect_area_y2 = 239
    detection_east_castle_under_threat = source_trigger_manager.add_trigger("detection_east_castle_under_threat", enabled=True, looping=False)
    for player in range(1, 5):  # Loop from player 1 to player 8
        detection_east_castle_under_threat.new_condition.objects_in_area(
            quantity=3,
            source_player=player,
            area_x1=detect_area_x1,
            area_x2=detect_area_x2,
            area_y1=detect_area_y1,
            area_y2=detect_area_y2,
            object_state=ObjectState.ALIVE,
            object_type=ObjectType.MILITARY
        )
        if player < 4:
            detection_east_castle_under_threat.new_condition.or_()
    detection_east_castle_under_threat.new_effect.activate_trigger(spawn_all_hero_from_castle.trigger_id)
    detection_east_castle_under_threat.new_effect.activate_trigger(looping_keep_spawning_trash_unit.trigger_id)
    detection_east_castle_under_threat.new_effect.display_instructions(object_list_unit_id=HeroInfo.GENGHIS_KHAN.ID,
                                                        source_player=0,
                                                        display_time=20,
                                                        message = "Enemy has summoned all heros for final push!")


    spawn_all_hero_from_castle.new_condition.timer(5)

    for hero_id in list_hero_ids:
        spawn_all_hero_from_castle.new_effect.create_garrisoned_object(source_player=8, 
                                                                    object_list_unit_id_2=hero_id,
                                                                    selected_object_ids = BATTLELINE_CASTLE_SPAWN_REFERENCE_ID)

    spawn_all_hero_from_castle.new_effect.unload(source_player=8, location_x=39, location_y= 52, selected_object_ids=BATTLELINE_CASTLE_SPAWN_REFERENCE_ID)


    looping_keep_spawning_trash_unit.new_condition.timer(10)
    looping_keep_spawning_trash_unit.new_effect.create_garrisoned_object(source_player=8, 
                                                                    object_list_unit_id_2=359,
                                                                    selected_object_ids = BATTLELINE_CASTLE_SPAWN_REFERENCE_ID)
    looping_keep_spawning_trash_unit.new_effect.create_garrisoned_object(source_player=8, 
                                                                    object_list_unit_id_2=6,
                                                                    selected_object_ids = BATTLELINE_CASTLE_SPAWN_REFERENCE_ID)
    looping_keep_spawning_trash_unit.new_effect.create_garrisoned_object(source_player=8, 
                                                                    object_list_unit_id_2=359,
                                                                    selected_object_ids = BATTLELINE_CASTLE_SPAWN_REFERENCE_ID)
    looping_keep_spawning_trash_unit.new_effect.create_garrisoned_object(source_player=8, 
                                                                    object_list_unit_id_2=6,
                                                                    selected_object_ids = BATTLELINE_CASTLE_SPAWN_REFERENCE_ID)
    looping_keep_spawning_trash_unit.new_effect.unload(source_player=8, location_x=39, location_y= 52, selected_object_ids=BATTLELINE_CASTLE_SPAWN_REFERENCE_ID)







    for east_player in [5, 6, 7, 8]:
        give_building_ability_to_constantly_spawn_battle_line_unit(source_trigger_manager, 
                                                                tents_selected_object_ids[east_player-1], 
                                                                ID_COMMANDER_TENT,
                                                                EAST_TARGET_LOCATION_X,
                                                                EAST_TARGET_LOCATION_Y,
                                                                east_player)
    


    for west_player in [1, 2, 3, 4]:
        give_building_ability_to_constantly_spawn_battle_line_unit(source_trigger_manager, 
                                                                tents_selected_object_ids[west_player-1], 
                                                                ID_COMMANDER_TENT,
                                                                WEST_TARGET_LOCATION_X,
                                                                WEST_TARGET_LOCATION_Y,
                                                                west_player)








    # Final step: write a modified scenario class to a new scenario file
    source_scenario.write_to_file(output_path)







scenario_folder = "C:/Users/Randy/Games/Age of Empires 2 DE/76561198060805641/resources/_common/scenario/"

input_path1 = scenario_folder + "Epic_Warfare 2_0 Raw.aoe2scenario"
#input_path2 = scenario_folder + "Epic_Warfare 2_0 Hero PK Test.aoe2scenario"

output_path1 = scenario_folder + "Epic Warfare 2_0 ONE HERO the Heroic Stand Remastered Generated.aoe2scenario"

output_path3 = scenario_folder + "Epic Warfare 2_0 ALL STAR the Heroic Stand Remastered.aoe2scenario"

output_path2 = scenario_folder + "Epic Warfare 2_0 Hero PK Test Generated.aoe2scenario"

parse_scenario_with_epic_warfare_logic(input_path1, output_path1, num_hero_allowed = 1)
parse_scenario_with_epic_warfare_logic(input_path1, output_path3, num_hero_allowed=11)
#parse_scenario_with_epic_warfare_logic(input_path2, output_path2, num_hero_allowed=11)

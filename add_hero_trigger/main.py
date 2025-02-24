


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

# File & Folder setup - Declare your scenario directory path
#scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

scenario_folder = "C:/Users/Randy/Games/Age of Empires 2 DE/76561198060805641/resources/_common/scenario/"

# Source scenario to work with

#input_path = scenario_folder + "hero test.aoe2scenario"
#output_path = scenario_folder + "hero test Parsed.aoe2scenario"
#input_path = scenario_folder + "Epic_Warfare Remastered v2_1.aoe2scenario"

input_path = scenario_folder + "Epic_Warfare Remastered v2_3 test frozen river.aoe2scenario"


#input_path = scenario_folder + "Epic_Warfare Remastered v2_0 Parsed.aoe2scenario"

#output_path = scenario_folder + "Epic_Warfare Remastered v2_1 Parsed.aoe2scenario"
output_path = scenario_folder + "Epic_Warfare Remastered v2_3 test frozen river Parsed.aoe2scenario"
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

Themistocles_ID = 2315
Darius_ID = 2347
Jean_De_Lorrain_ID = 644  
Dagnajan_Elephant_ID = 1106
#HeroInfo.ROBIN_HOOD.ID
list_hero_ids = [Darius_ID, 
                 HeroInfo.ROBIN_HOOD.ID,
                 HeroInfo.JEAN_BUREAU.ID,
                 Themistocles_ID,
                 HeroInfo.KOTYAN_KHAN.ID,
                 HeroInfo.ULRICH_VON_JUNGINGEN.ID,
                 HeroInfo.TSAR_KONSTANTIN.ID,
                 Dagnajan_Elephant_ID,
                 HeroInfo.GENGHIS_KHAN.ID,
                 HeroInfo.GODS_OWN_SLING_PACKED.ID

                 ]




list_description = ["Javelin Splashing duo-horse Chariot", 
                    "Vaelor, the Stormbow, a feared master of the battlefield, wields the legendary Stormbow, capable of unleashing a relentless downpour of arrows upon his enemies. His volleys blot out the sun, leaving no escape for those caught beneath his deadly rain. Tales of his wrath spread across kingdoms, as entire armies have fallen under his sky-darkening assault.",
                    "Skyfall Cluster Bomb Cannon",
                    "Invisible Footman with Explosives", 
                    "Explosive Arrow Mounter Archer",
                    "Flaming Throw knight", 
                    "Gatling Ballista tri-horse Chariot", 
                    "Flaming Thunder War Elephant", 
                    "Knight of the Exploding Wolf Summon",
                    "God Swing",
                    ]



TIME_WINDOW_PLAYER_CHOOSE_HERO = 120
TIME_HERO_RESPAWN = 120
NUM_HERO_ALLOWED = 1

POLE_X = 0
POLE_Y = 240
TIME_START_FROZEN = 3600
# Configuration
FROZEN_PACE_DELAY = 2  # Milliseconds between each freezing wave
FROZEN_BATCH_SIZE = 2  # Number of distance groups per trigger batch



instruction_trigger = source_trigger_manager.add_trigger(
                                "display hero instruction", 
                                enabled=True,
                                looping=False)
instruction_trigger.new_effect.display_instructions(object_list_unit_id=HeroInfo.GENGHIS_KHAN.ID,
                                                    source_player=0,
                                                    display_time=20,
                                                    message = "Welcome to Epic Warfare - The Heroic Stand! Feel free to select a hero from the Holy Commander Tent. Your first choice will be your main hero, who will respawn throughout the game. The second hero, however, has only one life for your attempt.")

instruction_trigger.new_effect.display_timer(
    display_time=2,
    time_unit=1,
    timer=0,
    reset_timer=1,
    message=r"Time out selecting heroes in %d"
)


# conduct trigger wisely by encapusaltion
for playid in PlayerId.all()[1:]:
    process_heros_for_every_player(source_trigger_manager, list_hero_ids, playid, list_description)

# very fragile value! if in map the commander tent changes, could cause crash!
tents_selected_object_ids = [317958, 317979, 322879, 319227, 328305, 328275, 328335, 328365]

    # attack_graphic = 1786,
    # standing_graphic = 1788,
    # dying_graphic = 1787,
    # walking_graphic = 1789,


inst_dagnajan_hero = Hero(
    hero_id= Dagnajan_Elephant_ID,  # You'll need to provide the correct hero_id
    projectile_unit=469,
    max_range=5,
    min_range=1,
    attack_dispersion=1,
    accuracy_percent=30,
    pierce_armor=10,
    melee_armour=8,
    melee_attack = 17,
    attack_reload_set=2,  
    total_missile = 30,
    combat_ability= 8 + 16,
    #walking_graphic = 654,
    movement_speed=1,
    #projectile_vanish_mode = 1
    #unit_trait = 8,
    #trait_piece = 2151,
    health_point = 500
)
boost_hero(source_trigger_manager, inst_dagnajan_hero, PlayerId.all()[1:])





"""GOD SWING BOOST"""

inst_god_swing_packed_hero = Hero(
    hero_id=HeroInfo.GODS_OWN_SLING_PACKED.ID,  # You'll need to provide the correct hero_id
    projectile_unit=469,
    max_range=14,
    min_range=13,
    blast_width=1,
    blast_attack_level=2, 
    accuracy_percent=15,
    total_missile = 30,
    attack_dispersion=1,
    movement_speed=1,
    health_point = 300,
    line_of_sight = 15,
)
boost_hero(source_trigger_manager, inst_god_swing_packed_hero, PlayerId.all()[1:])


inst_god_swing_hero = Hero(
    hero_id=HeroInfo.GODS_OWN_SLING.ID,  # You'll need to provide the correct hero_id
    projectile_unit=469,
    max_range=14,
    min_range=4,
    blast_width=1,
    blast_attack_level=2, 
    accuracy_percent=15,
    total_missile = 30,
    attack_dispersion=1,
    health_point = 300,
    line_of_sight = 15,
    combat_ability= 16 + 8,
)

boost_hero(source_trigger_manager, inst_god_swing_hero, PlayerId.all()[1:])






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

)

boost_hero(source_trigger_manager, inst_frank_paladin_hero, PlayerId.all()[1:])

inst_mounted_elephant_hero = Hero(
    hero_id=HeroInfo.BAYINNAUNG.ID,  # You'll need to provide the correct hero_id
    projectile_unit=1168,
    max_range=2,
    min_range=1,
    melee_attack=12,
    blast_width=1,
    blast_attack_level=2,
    pierce_armor=5,
    melee_armour=5,
    attack_reload_set=2,  
    accuracy_percent=15,
    total_missile = 30,
    attack_dispersion=1,
    combat_ability= 16 + 8,
    #walking_graphic = 654,
    movement_speed=1,
    #dead_unit_id = 942,
    health_point = 300,

)

boost_hero(source_trigger_manager, inst_mounted_elephant_hero, PlayerId.all()[1:])


# Instantiate Jean Bureau
inst_jean_bureau = Hero(
    hero_id=HeroInfo.JEAN_BUREAU.ID,  # You'll need to provide the correct hero_id
    max_range=15,  #
    min_range=5,  # Not modified in the original function
    total_missile=75,
    projectile_unit=658,
    accuracy_percent=35,
    attack_dispersion = 1,
    attack_dispersion_divide=2,
    #melee_armour=0,  # Not modified in the original function
    #pierce_armor=0,  # Not modified in the original function
    melee_attack=15,
    movement_speed=1,
    health_point=150,
    blast_width=1,
    blast_attack_level=2
)
            
inst_hero_ulrich = Hero(
    hero_id=HeroInfo.ULRICH_VON_JUNGINGEN.ID,  # You'll need to provide the correct hero_id
    melee_attack=25,
    #movement_speed=2,
    blast_width=1,
    melee_armour=25,
    pierce_armor=25,
    blast_attack_level=4,
    max_range=2,
    total_missile=20,
    projectile_unit=676,
    accuracy_percent=30,
    combat_ability= 8 + 16,
    attack_dispersion = 3,
)

inst_hero_darius = Hero(
    max_range=4,
    min_range = 2,
    hero_id=Darius_ID,  # You'll need to provide the correct hero_id
    blast_width=1,
    blast_attack_level=2,
    melee_attack=25,
    total_missile=40,  # This covers both Max Total Missiles and Total Missiles
    projectile_unit=1780, 
    pierce_armor=15,
    melee_armour=8,
    movement_speed=2,
    combat_ability= 16 + 8,
    accuracy_percent = 20,
    attack_dispersion=1,
    attack_reload_set = 2,

)


inst_hero_mounted_archer = Hero(
    hero_id=HeroInfo.KOTYAN_KHAN.ID,  # You'll need to provide the correct hero_id
    max_range=9,
    min_range = 3,
    melee_attack=25,
    blast_width=1,
    blast_attack_level=4,
    accuracy_percent=70,
    #attack_dispersion=1,
    total_missile=4,
    pierce_armor=15,
    melee_armour=8,
    attack_reload_set=1,  # This will be divided, not added
    projectile_unit = 1595,
    combat_ability= 16 + 8,
)

inst_hero_tsar_constantin = Hero(
    hero_id=HeroInfo.TSAR_KONSTANTIN.ID,  # You'll need to provide the correct hero_id
    projectile_unit=627,
    max_range=10,
    melee_attack=25,
    blast_width=1,
    blast_attack_level=4,
    pierce_armor=13,
    melee_armour=5,
    attack_reload_divide=12,  # This will be divided, not added
    accuracy_percent=50,
    attack_dispersion=1,
    #combat_ability= 8, # has bug that attack ground no projectile shown
    projectile_vanish_mode = 1,
    projectile_hit_mode = 1,
)













wolf_id = 700
sabo_man_id = 706
num_summon = 7
summon_cooldown = 7
summon_hp_drop_per_second = 10
flame_id_spawned_after_explosion = 1334
num_max_flame = num_summon * 4

inst_tamar_summon_hero = Hero(
    hero_id= HeroInfo.GENGHIS_KHAN.ID,  # You'll need to provide the correct hero_id
    projectile_unit=676,
    secondary_projectile_unit=wolf_id,
    line_of_sight = 7,
    max_range=7,
    attack_dispersion=5,
    accuracy_percent=20,
    pierce_armor=10,
    melee_armour=10,
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
    #projectile_vanish_mode = 1
    #unit_trait = 8,
    #trait_piece = 2151,
)
inst_summon_unit = Hero(
    hero_id= wolf_id,  # You'll need to provide the correct hero_id
    search_radius = 7,
    movement_speed = 1,
    line_of_sight = 7,
    hero_status = 64,
    dead_unit_id = sabo_man_id,
)
# not actually doing damage to friendly unit
inst_sabo_man_unit = Hero(
    hero_id= sabo_man_id,  # You'll need to provide the correct hero_id
    melee_attack = 50,
    blast_attack_level=2,
    health_point = 0,
    blast_width = 2,
    blood_unit = 1334,
    standing_graphic = 7253,
    attack_graphic = 7251,
    #dying_graphic = 7252,
    walking_graphic = 7256,
    #undead_graphic = 7252
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
global_wolf_minus_hp = source_trigger_manager.add_trigger("global_wolf_minus_hp",enabled=True,looping=True)
for player in range(1, 9):  # Loop from player 1 to 9
    global_wolf_minus_hp.new_effect.change_object_hp(
        object_list_unit_id=wolf_id, operation=3, quantity=summon_hp_drop_per_second, source_player=player
    )
    global_wolf_minus_hp.new_effect.change_object_stance(
        object_list_unit_id=wolf_id, source_player=player, attack_stance=0
    )



boost_hero(source_trigger_manager, inst_tamar_summon_hero, PlayerId.all()[1:])
boost_hero(source_trigger_manager, inst_summon_unit, PlayerId.all()[1:])
boost_hero(source_trigger_manager, inst_sabo_man_unit, PlayerId.all()[1:])
# elephant, where invisible project, but with flame impact

#change projectile to unit. spawn hero


#inst_projectile_vol_fire = Hero(hero_id = 511, standing_graphic = 1743)

boost_hero(source_trigger_manager, inst_robin_archer_hero, PlayerId.all()[1:])
# add fire effect to arrows





boost_hero(source_trigger_manager, inst_projectile_vol_fire, PlayerId.all()[1:])


boost_hero(source_trigger_manager, inst_jean_bureau, PlayerId.all()[1:])
boost_hero(source_trigger_manager, inst_hero_ulrich, PlayerId.all()[1:])
boost_hero(source_trigger_manager, inst_hero_darius, PlayerId.all()[1:])
boost_hero(source_trigger_manager, inst_hero_mounted_archer, PlayerId.all()[1:])

boost_hero(source_trigger_manager, inst_hero_tsar_constantin, PlayerId.all()[1:])

#boost_hero(source_trigger_manager, inst_projectile_vol_fire, PlayerId.all()[1:])



Themistocles_ID
inst_themistocles_hero = Hero(
    hero_id= Themistocles_ID,  # You'll need to provide the correct hero_id
    #projectile_unit=1798,
    secondary_projectile_unit = sabo_man_id,
    projectile_unit=1595,
    blast_attack_level=2,
    melee_attack=20,
    max_range=1,
    min_range=0,
    pierce_armor=20,
    melee_armour=20,
    attack_reload_set=3,  
    total_missile = 30,
    combat_ability= 8 + 16,
    attack_dispersion = 2,
    accuracy_percent = 10,
    blast_width = 2,
    health_point=500,
    #walking_graphic = 654,
    movement_speed_divide=3,
    movement_speed_multiply=2,
    #projectile_smart_mode = 2,
    #dead_unit_id = 942,
    #projectile_vanish_mode = 1
    #unit_trait = 8,
    #trait_piece = 2151,
)

inst_projectile_unit_laser = Hero(
    hero_id= 1595,  # You'll need to provide the correct hero_id
    movement_speed_divide = 2,
)

boost_hero(source_trigger_manager, inst_projectile_unit_laser, PlayerId.all()[1:])
# inst_summon_hawk_unit = Hero(
#     hero_id= 96,  # You'll need to provide the correct hero_id
#     dead_unit_id = sabo_man_id,
# )

# boost_hero(source_trigger_manager, inst_summon_hawk_unit, PlayerId.all()[1:])
boost_hero(source_trigger_manager, inst_themistocles_hero, PlayerId.all()[1:])

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

def create_hero_respawn_system(trigger_manager, hero_ids, players, tents_ids):
    """Encapsulated hero respawn system for multiple players and heroes"""
    for player_id in players:
        for hero_id in hero_ids:
            _create_single_hero_triggers(trigger_manager, player_id, hero_id, tents_ids)

def _create_single_hero_triggers(manager, player_id, hero_id, tents_ids):
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
    respawn_trigger.new_condition.timer(timer=TIME_HERO_RESPAWN)
    
    # Setup trigger relationships
    detect_trigger.new_effect.activate_trigger(death_trigger.trigger_id)
    death_trigger.new_effect.display_timer(
        display_time=2,
        time_unit=1,
        timer=player_id,
        reset_timer=1,
        message=f'Player {player_id} Hero Spawns in ' + r"%d"
    )
    death_trigger.new_effect.activate_trigger(respawn_trigger.trigger_id)
    
    respawn_trigger.new_effect.tribute(
        quantity=1,
        tribute_list=8,
        source_player=0,
        target_player=player_id
    )
    respawn_trigger.new_effect.train_unit(
        object_list_unit_id=hero_id,
        quantity=1,
        selected_object_ids=tents_ids[player_id-1],
        source_player=player_id
    )
    respawn_trigger.new_effect.activate_trigger(detect_trigger.trigger_id)





# For all players except GAIA (player 0)
create_hero_respawn_system(
    source_trigger_manager,
    list_hero_ids,
    PlayerId.all()[1:],
    tents_selected_object_ids
)




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
        
        chance_triggers = []

        # Create chance triggers
        for idx, (hero_id, chance) in enumerate(zip(hero_ids, chances), 1):
            trigger = trigger_manager.add_trigger(
                f"p{player_id}_hero{idx}_chance",
                enabled=False,
                looping=False
            )
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
            other_triggers = [t for t in chance_triggers if t != trigger][NUM_HERO_ALLOWED - 1:]
            num_to_remove = len(other_triggers) - (NUM_HERO_ALLOWED - 1)

            #so that second selected hero not always chariot hero
            if num_to_remove > 0:
                other_triggers = random.sample(other_triggers, len(other_triggers) - num_to_remove)

            for other in other_triggers:
                trigger.new_effect.deactivate_trigger(other.trigger_id)


# Usage examples:
# 2 heroes (50/50)
create_equal_chance_system(
    source_trigger_manager,
    PlayerId.all()[1:],
    list_hero_ids,
    tents_list=tents_selected_object_ids
)








invisible_storage_id = 1081
tent_id = 1197


tentb_id = 1098


intermedite_object_id = tentb_id
ice_id = 728



inst_intermedite_object_building = Hero(hero_id=intermedite_object_id, terrain_restriction_id = 0, foundation_terrain = TerrainId.BEACH_ICE, dead_unit_id = ice_id, health_point = 0, train_time=0, dying_graphic = 0, can_be_built_on = 1,
                                        standing_graphic = 0,)
boost_hero(source_trigger_manager, inst_intermedite_object_building, PlayerId.all()[1:])

tenta_id = 1097
inst_tenta_id_building = Hero(hero_id=tenta_id, terrain_restriction_id = 0, foundation_terrain = TerrainId.SNOW_FOUNDATION, dead_unit_id = ice_id, health_point = 0, train_time=0, dying_graphic = 0, can_be_built_on = 1,
                                        standing_graphic = 0,)
boost_hero(source_trigger_manager, inst_tenta_id_building, PlayerId.all()[1:])

# inst_invisible_object = Hero(hero_id=invisible_storage_id, blockage_class=1, 
#                              terrain_restriction_id = 0, 
#                              #standing_graphic = 0, 
#                              dying_graphic = 0, 
#                              dead_unit_id = ice_id, 
#                              can_be_built_on = 1)
# boost_hero(source_trigger_manager, inst_invisible_object, PlayerId.all()[1:])


# get all the terrains tiles (compiled in a list) in the map
originalTerrains = source_scenario.map_manager.terrain

targeted_terrains_detected = []

for terrain in originalTerrains:
    if terrain.terrain_id == TerrainId.BEACH_NON_NAVIGABLE_WET_ROCK:
        #print("found black tile")
        targeted_terrains_detected.append((terrain.x, terrain.y))

all_water_terrain = []

for terrain in originalTerrains:
    if terrain.terrain_id in TerrainId.water_terrains() or terrain.terrain_id == TerrainId.BEACH_NON_NAVIGABLE_WET_ROCK:
        #print("found black tile")
        all_water_terrain.append((terrain.x, terrain.y))

all_non_water_terrain = []
for terrain in originalTerrains:
    if terrain.terrain_id not in TerrainId.water_terrains() and terrain.terrain_id != TerrainId.BEACH_NON_NAVIGABLE_WET_ROCK:
        all_non_water_terrain.append((terrain.x, terrain.y))


print(len(all_non_water_terrain))

USED_SOURCE_PLAYER = 8


print(targeted_terrains_detected)
print("targeted_terrains_detected")

middle_bridge_piece_id = 1842
inst_middle_bridge_piece_building = Hero(hero_id=invisible_storage_id, terrain_restriction_id = 0, foundation_terrain = TerrainId.WATER_MEDIUM, dead_unit_id = 0, health_point = 500, train_time=0, can_be_built_on = 1,
                                        standing_graphic = 0, dying_graphic = 0)
boost_hero(source_trigger_manager, inst_middle_bridge_piece_building, PlayerId.all()[1:])

transform_first_to_water = source_trigger_manager.add_trigger("transform_first_to_water", enabled=True,looping=False)

for black_tile in targeted_terrains_detected:
    x,y = black_tile
    transform_first_to_water.new_effect.place_foundation(object_list_unit_id=invisible_storage_id,source_player=USED_SOURCE_PLAYER,location_x=x,location_y=y)
    #transform_first_to_water.new_effect.create_object(object_list_unit_id=invisible_storage_id, source_player=1, location_x=x, location_y=y)


clear_blockage_building = source_trigger_manager.add_trigger("clear_blockage_building", enabled=True,looping=False)
clear_blockage_building.new_condition.timer(timer=TIME_START_FROZEN - 1)
clear_blockage_building.new_effect.kill_object(object_list_unit_id=invisible_storage_id, source_player=USED_SOURCE_PLAYER)

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
    distance_batches = [sorted_distances[i:i+FROZEN_BATCH_SIZE] 
                      for i in range(0, len(sorted_distances), FROZEN_BATCH_SIZE)]

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
                    object_list_unit_id=intermedite_object_id,
                    source_player=USED_SOURCE_PLAYER,
                    location_x=x,
                    location_y=y
                )
            
            # Non-water tiles
            for x, y in distance_map[distance]['non_water']:
                trigger.new_effect.place_foundation(
                    object_list_unit_id=tenta_id,
                    source_player=USED_SOURCE_PLAYER,
                    location_x=x,
                    location_y=y
                )
            
            # Other tiles
            for x, y in distance_map[distance]['other']:
                trigger.new_effect.place_foundation(
                    object_list_unit_id=intermedite_object_id,
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

# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)




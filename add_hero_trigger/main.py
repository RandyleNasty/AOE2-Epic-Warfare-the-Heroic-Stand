


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


from hero_abstract_class import *
# File & Folder setup - Declare your scenario directory path
#scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

scenario_folder = "C:/Users/Randy/Games/Age of Empires 2 DE/76561198060805641/resources/_common/scenario/"

# Source scenario to work with

#input_path = scenario_folder + "hero test.aoe2scenario"
#output_path = scenario_folder + "hero test Parsed.aoe2scenario"
input_path = scenario_folder + "Epic_Warfare Remastered v2_1.aoe2scenario"

#input_path = scenario_folder + "Epic_Warfare Remastered v2_0 Parsed.aoe2scenario"

output_path = scenario_folder + "Epic_Warfare Remastered v2_1 Parsed.aoe2scenario"

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
#HeroInfo.ROBIN_HOOD.ID
list_hero_ids = [HeroInfo.FRANKISH_PALADIN.ID, 
                 HeroInfo.ROBIN_HOOD.ID,
                 HeroInfo.JEAN_BUREAU.ID,
                 Themistocles_ID,
                 HeroInfo.KOTYAN_KHAN.ID,
                 HeroInfo.ULRICH_VON_JUNGINGEN.ID,
                 HeroInfo.TSAR_KONSTANTIN.ID,
                 HeroInfo.BAYINNAUNG.ID,
                 HeroInfo.GENGHIS_KHAN.ID,
                 HeroInfo.GODS_OWN_SLING_PACKED.ID
                 ]




list_description = ["knight", 
                    "Vaelor, the Stormbow, a feared master of the battlefield, wields the legendary Stormbow, capable of unleashing a relentless downpour of arrows upon his enemies. His volleys blot out the sun, leaving no escape for those caught beneath his deadly rain. Tales of his wrath spread across kingdoms, as entire armies have fallen under his sky-darkening assault.",
                    "super cannon", 
                    "Invicible footman",
                    "laser mounter archer", 
                    "fire knight", 
                    "Ballista Chariot", 
                    "Mounted Gun Powder",
                    "Elephant",
                    "Projectile Summon Rider",
                    "GOD SWING"
                    ]



TIME_WINDOW_PLAYER_CHOOSE_HERO = 120
TIME_HERO_RESPAWN = 120
NUM_HERO_ALLOWED = 15

# conduct trigger wisely by encapusaltion
for playid in PlayerId.all()[1:]:
    process_heros_for_every_player(source_trigger_manager, list_hero_ids, playid, list_description)

# very fragile value! if in map the commander tent changes, could cause crash!
tents_selected_object_ids = [317958, 317979, 322879, 319227, 328305, 328275, 328335, 328365]

    # attack_graphic = 1786,
    # standing_graphic = 1788,
    # dying_graphic = 1787,
    # walking_graphic = 1789,


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
    min_range=13,
    blast_width=1,
    blast_attack_level=2, 
    accuracy_percent=15,
    total_missile = 30,
    attack_dispersion=1,
    movement_speed=1,
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
    pierce_attack=12,
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
    dead_unit_id = 942,
    health_point = 300,

)

boost_hero(source_trigger_manager, inst_frank_paladin_hero, PlayerId.all()[1:])

inst_mounted_elephant_hero = Hero(
    hero_id=HeroInfo.BAYINNAUNG.ID,  # You'll need to provide the correct hero_id
    projectile_unit=1168,
    max_range=2,
    min_range=1,
    pierce_attack=12,
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
    dead_unit_id = 942,
    health_point = 300,

)

boost_hero(source_trigger_manager, inst_mounted_elephant_hero, PlayerId.all()[1:])


# Instantiate Jean Bureau
inst_jean_bureau = Hero(
    hero_id=HeroInfo.JEAN_BUREAU.ID,  # You'll need to provide the correct hero_id
    max_range=15,  #
    min_range=2,  # Not modified in the original function
    total_missile=75,
    projectile_unit=658,
    accuracy_percent=35,
    attack_dispersion=1,
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
    movement_speed=2,
    blast_width=3,
    melee_armour=25,
    pierce_armor=25,
    blast_attack_level=4,
    max_range=2,
    total_missile=20,
    projectile_unit=676,
    accuracy_percent=30
)

inst_hero_darius = Hero(
    hero_id=Darius_ID,  # You'll need to provide the correct hero_id
    blast_width=1,
    blast_attack_level=4,
    melee_attack=25,
    total_missile=7,  # This covers both Max Total Missiles and Total Missiles
    projectile_unit=328, 
    pierce_armor=25,
    melee_armour=25,
    movement_speed=2
)


inst_hero_mounted_archer = Hero(
    hero_id=HeroInfo.KOTYAN_KHAN.ID,  # You'll need to provide the correct hero_id
    max_range=11,
    pierce_attack=40,
    base_armor=20,
    blast_width=2,
    blast_attack_level=4,
    accuracy_percent=70,
    attack_dispersion=1,
    total_missile=3,
    pierce_armor=20,
    melee_armour=20,
    attack_reload_divide=2,  # This will be divided, not added
    projectile_unit = 1595
)

inst_hero_tsar_constantin = Hero(
    hero_id=HeroInfo.TSAR_KONSTANTIN.ID,  # You'll need to provide the correct hero_id
    projectile_unit=627,
    max_range=9,
    pierce_attack=25,
    blast_width=1,
    blast_attack_level=4,
    pierce_armor=13,
    melee_armour=5,
    attack_reload_divide=10,  # This will be divided, not added
    accuracy_percent=50,
    attack_dispersion=1
)










inst_robin_archer_hero = Hero(
    hero_id=HeroInfo.ROBIN_HOOD.ID,  # You'll need to provide the correct hero_id
    projectile_unit=511,
    max_range=9,
    pierce_attack=12,
    blast_width=1,
    blast_attack_level=4,
    pierce_armor=13,
    melee_armour=5,
    attack_reload_set=2,  
    accuracy_percent=15,
    total_missile = 80,
    attack_dispersion=1,
    combat_ability= 16 + 8,
    #walking_graphic = 654,
    movement_speed=1

)


wolf_id = 700
inst_tamar_summon_hero = Hero(
    hero_id= HeroInfo.GENGHIS_KHAN.ID,  # You'll need to provide the correct hero_id
    projectile_unit=wolf_id,
    secondary_projectile_unit=wolf_id,
    max_range=9,
    attack_dispersion=1,
    accuracy_percent=15,
    pierce_armor=13,
    melee_armour=5,
    attack_reload_set=20,  
    total_missile = 6,
    combat_ability= 8 + 16 + 32,
    #walking_graphic = 654,
    movement_speed=1,
    dead_unit_id = 942,
    attack_graphic = 12660,
    standing_graphic = 12663,
    #standing_graphic_2 = 12662,
    dying_graphic = 12661,
    walking_graphic = 12665,
    icon_id = 414,
    #projectile_vanish_mode = 1
    #unit_trait = 8,
    #trait_piece = 2151,
)
inst_summon_unit = Hero(
    hero_id= wolf_id,  # You'll need to provide the correct hero_id
    search_radius = 10,
    movement_speed = 2,
    line_of_sight = 10,
    hero_status = 64,
)

# add lifetime of summoned wolf
global_wolf_minus_hp = source_trigger_manager.add_trigger("global_wolf_minus_hp",enabled=True,looping=True)
for player in range(1, 9):  # Loop from player 1 to 9
    global_wolf_minus_hp.new_effect.change_object_hp(
        object_list_unit_id=wolf_id, operation=3, quantity=2, source_player=player
    )
    global_wolf_minus_hp.new_effect.change_object_stance(
        object_list_unit_id=wolf_id, source_player=player, attack_stance=0
    )



boost_hero(source_trigger_manager, inst_tamar_summon_hero, PlayerId.all()[1:])
boost_hero(source_trigger_manager, inst_summon_unit, PlayerId.all()[1:])
# elephant, where invisible project, but with flame impact

#change projectile to unit. spawn hero


#inst_projectile_vol_fire = Hero(hero_id = 511, standing_graphic = 1743)

boost_hero(source_trigger_manager, inst_robin_archer_hero, PlayerId.all()[1:])
inst_projectile_vol_fire = Hero(hero_id = 511, standing_graphic = 1743)
boost_hero(source_trigger_manager, inst_projectile_vol_fire, PlayerId.all()[1:])


boost_hero(source_trigger_manager, inst_jean_bureau, PlayerId.all()[1:])
boost_hero(source_trigger_manager, inst_hero_ulrich, PlayerId.all()[1:])
boost_hero(source_trigger_manager, inst_hero_darius, PlayerId.all()[1:])
boost_hero(source_trigger_manager, inst_hero_mounted_archer, PlayerId.all()[1:])

boost_hero(source_trigger_manager, inst_hero_tsar_constantin, PlayerId.all()[1:])

#boost_hero(source_trigger_manager, inst_projectile_vol_fire, PlayerId.all()[1:])


"""
TO DO
"""
#boost_ulrich(source_trigger_manager, HeroInfo.FRANKISH_PALADIN.ID, PlayerId.all()[1:])
#boost_ulrich(source_trigger_manager, HeroInfo.BAYINNAUNG.ID, PlayerId.all()[1:])




Themistocles_ID
inst_themistocles_hero = Hero(
    hero_id= Themistocles_ID,  # You'll need to provide the correct hero_id
    projectile_unit=469,
    melee_attack=15,
    pierce_attack=15,
    max_range=1,
    min_range=0,
    pierce_armor=12,
    melee_armour=12,
    attack_reload_divide=20,  
    total_missile = 5,
    combat_ability= 8 + 16,
    attack_dispersion = 5,
    accuracy_percent = 15,
    blast_width = 2,
    health_point=500,
    #walking_graphic = 654,
    movement_speed=1,
    dead_unit_id = 942,
    #projectile_vanish_mode = 1
    #unit_trait = 8,
    #trait_piece = 2151,
)



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
        message=f'Player {player_id} Hero Spawns in '
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

        #once one chance trigger activate disable other generated chance trigger
        for trigger in chance_triggers:
            other_triggers = [t for t in chance_triggers if t != trigger]
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





#					0: Unknown (2262) [P1, X103.0, Y39.0] (317958)
# 317958 worked! but how the hell is this decoding working?

# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)




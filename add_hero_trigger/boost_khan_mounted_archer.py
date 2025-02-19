

from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *


from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo

from AoE2ScenarioParser.datasets.players import PlayerId


from AoE2ScenarioParser.datasets.trigger_lists import ObjectAttribute
from AoE2ScenarioParser.datasets.trigger_lists import Operation

#calling this applies to all players
def boost_ranged_hero(trigger_manager, hero_id, players_applied, hero_configuration_matrix = None):
    for player_id in players_applied:
        # Create trigger
        trigger = trigger_manager.add_trigger(
            f"hero_{hero_id}_p{player_id}",
            enabled=True,
            looping=False
        )
        trigger.new_effect.modify_attribute(quantity=1595, object_attributes=16,operation=1,source_player=player_id, object_list_unit_id = hero_id)
        # Index 4: Max Range
        trigger.new_effect.modify_attribute(
            quantity=11,
            object_attributes=12,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 5: Attack (Pierce)
        trigger.new_effect.modify_attribute(
            armour_attack_quantity=40,
            armour_attack_class=3,
            object_attributes=9,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 6: Base Armor
        trigger.new_effect.modify_attribute(
            quantity=20,
            object_attributes=15,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 7: Blast Width
        trigger.new_effect.modify_attribute(
            quantity=2,
            object_attributes=22,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 8: Blast Attack Level
        trigger.new_effect.modify_attribute(
            quantity=4,
            object_attributes=44,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 9: Accuracy Percent
        trigger.new_effect.modify_attribute(
            quantity=70,
            object_attributes=11,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 10: Attack Dispersion
        trigger.new_effect.modify_attribute(
            quantity=1,
            object_attributes=64,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 11: Total Missiles
        trigger.new_effect.modify_attribute(
            quantity=3,
            object_attributes=102,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 12: Max Total Missiles
        trigger.new_effect.modify_attribute(
            quantity=3,
            object_attributes=107,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 13: Armor (Pierce)
        trigger.new_effect.modify_attribute(
            armour_attack_quantity=20,
            armour_attack_class=3,
            object_attributes=8,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 14: Armor (Melee)
        trigger.new_effect.modify_attribute(
            armour_attack_quantity=20,
            armour_attack_class=4,
            object_attributes=8,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 15: Attack Reload Time (Divide operation)
        trigger.new_effect.modify_attribute(
            quantity=2,
            object_attributes=10,
            operation=5,
            source_player=player_id,
            object_list_unit_id=hero_id
        )
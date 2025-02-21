from abc import ABC, abstractmethod
from typing import Dict, List, Any

""" def modify_attribute(...) ¶
The parameters 'armour_attack_quantity' and 'armour_attack_class' are only used when object_attributes is Armor or Attack (8 or 9). Use, 'quantity' otherwise.

Parameters:

Name	Type	Description	Default
quantity	int | None	-	None
armour_attack_quantity	int | None	-	None
armour_attack_class	int | None	-	None
object_list_unit_id	int | None	-	None
source_player	int | None	-	None
operation	int | None	-	None
object_attributes	int | None	-	None
message	str | None	-	None """


"""        # Index 4: Max Range
        trigger.new_effect.modify_attribute(
            quantity=11,
            object_attributes=12,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )
 """
class Hero(ABC):
    """Abstract base class for hero units"""
    def __init__(self, hero_id=None, **attributes):
        self.hero_id = hero_id
        self.attributes = attributes

class HeroChangesGraphics(ABC):
    pass

def boost_hero(trigger_manager, hero, players_applied):
    # Define a dictionary mapping attribute names to their corresponding object_attributes values
    attribute_mapping = {
        'max_range': 12,
        'min_range': 20,
        'total_missile': [107, 102],
        'projectile_unit': 16,
        'accuracy_percent': 11,
        'attack_dispersion': 64,
        'attack_reload_divide': 10,
        'attack_reload_set': 10,
        'melee_armour': (8, 4),
        'pierce_armor': (8, 3),
        'melee_attack': (9, 4),
        'movement_speed': 5,
        'health_point': 0,
        'blast_width': 22,
        'blast_attack_level': 44,
        'projectile_arc': 69,
        'attack_graphic': 70,
        'standing_graphic': 71,
        'standing_graphic_2': 72,
        'dying_graphic': 73,
        'undead_graphic': 74,
        'walking_graphic': 75,
        'running_graphic': 76,
        'dead_unit_id': 57,
        'projectile_arc': 69,
        'combat_ability': 63,
        'icon_id': 25,
        'secondary_projectile_unit': 65,
        'projectile_vanish_mode': 68,
        'unit_trait': 54,
        'trait_piece': 56,
        'search_radius': 23,
        'line_of_sight': 1,
        'hero_status':40,
        'charge_type': 62,
        'recharge_rate': 60,
        'charge_event': 61,
        'max_charge':59,
    }



    for player_id in players_applied:
        trigger = trigger_manager.add_trigger(
            f"hero_{hero.hero_id}_p{player_id}",
            enabled=True,
            looping=False
        )

        for attr, value in hero.attributes.items():
            if value is not None and attr in attribute_mapping:
                obj_attr = attribute_mapping[attr]
                
                if isinstance(obj_attr, list):
                    # Handle attributes that need multiple applications
                    for oa in obj_attr:
                        trigger.new_effect.modify_attribute(
                            quantity=value,
                            object_attributes=oa,
                            operation=1,
                            source_player=player_id,
                            object_list_unit_id=hero.hero_id
                        )
                elif isinstance(obj_attr, tuple):
                    # Handle armor/attack attributes
                    trigger.new_effect.modify_attribute(
                        armour_attack_quantity=value,
                        armour_attack_class=obj_attr[1],
                        object_attributes=obj_attr[0],
                        operation=1,
                        source_player=player_id,
                        object_list_unit_id=hero.hero_id
                    )
                elif attr == "attack_reload_divide":
                        trigger.new_effect.modify_attribute(
                        quantity=value,
                        object_attributes=obj_attr,
                        operation=5,
                        source_player=player_id,
                        object_list_unit_id=hero.hero_id
                    )          
                else:
                    # Handle standard attributes
                    trigger.new_effect.modify_attribute(
                        quantity=value,
                        object_attributes=obj_attr,
                        operation=1,
                        source_player=player_id,
                        object_list_unit_id=hero.hero_id
                    )
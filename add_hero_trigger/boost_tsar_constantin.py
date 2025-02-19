
#calling this applies to all players
def boost_tsar_constantin(trigger_manager, hero_id, players_applied, hero_configuration_matrix = None):
    for player_id in players_applied:
        # Create trigger
        trigger = trigger_manager.add_trigger(
            f"hero_{hero_id}_p{player_id}",
            enabled=True,
            looping=False
        )

        # Index 2: Projectile Unit
        trigger.new_effect.modify_attribute(
            quantity=627,
            object_attributes=16,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 3: Max Range
        trigger.new_effect.modify_attribute(
            quantity=9,
            object_attributes=12,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 4: Attack (Pierce)
        trigger.new_effect.modify_attribute(
            armour_attack_quantity=25,
            armour_attack_class=3,
            object_attributes=9,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 5: Blast Width
        trigger.new_effect.modify_attribute(
            quantity=1,
            object_attributes=22,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 6: Blast Attack Level
        trigger.new_effect.modify_attribute(
            quantity=4,
            object_attributes=44,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 7: Armor (Pierce)
        trigger.new_effect.modify_attribute(
            armour_attack_quantity=13,
            armour_attack_class=3,
            object_attributes=8,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 8: Armor (Melee)
        trigger.new_effect.modify_attribute(
            armour_attack_quantity=5,
            armour_attack_class=4,
            object_attributes=8,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 9: Attack Reload Time (Divide)
        trigger.new_effect.modify_attribute(
            quantity=10,
            object_attributes=10,
            operation=5,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 10: Accuracy Percent
        trigger.new_effect.modify_attribute(
            quantity=50,
            object_attributes=11,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 11: Attack Dispersion
        trigger.new_effect.modify_attribute(
            quantity=1,
            object_attributes=64,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

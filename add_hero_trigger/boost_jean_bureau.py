def boost_jean_bureau(trigger_manager, hero_id, players_applied, hero_configuration_matrix=None):
    for player_id in players_applied:
        trigger = trigger_manager.add_trigger(
            f"hero_{hero_id}_p{player_id}",
            enabled=True,
            looping=False
        )

        # Index 2: Max Total Missiles
        trigger.new_effect.modify_attribute(
            quantity=75,
            object_attributes=107,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 3: Total Missiles
        trigger.new_effect.modify_attribute(
            quantity=75,
            object_attributes=102,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 4: Projectile Unit
        trigger.new_effect.modify_attribute(
            quantity=658,
            object_attributes=16,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 5: Attack Dispersion
        trigger.new_effect.modify_attribute(
            quantity=1,
            object_attributes=64,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 6: Accuracy Percent
        trigger.new_effect.modify_attribute(
            quantity=35,
            object_attributes=11,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 7: Max Range (First instance)
        trigger.new_effect.modify_attribute(
            quantity=13,
            object_attributes=12,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 8: Melee Attack
        trigger.new_effect.modify_attribute(
            armour_attack_quantity=15,
            armour_attack_class=4,
            object_attributes=9,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 9: Blast Attack Level
        trigger.new_effect.modify_attribute(
            quantity=2,
            object_attributes=44,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 10: Blast Width
        trigger.new_effect.modify_attribute(
            quantity=1,
            object_attributes=22,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 11: Hit Points
        trigger.new_effect.modify_attribute(
            quantity=150,
            object_attributes=0,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 12: Max Range (Second instance)
        trigger.new_effect.modify_attribute(
            quantity=15,
            object_attributes=12,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 13: Movement Speed
        trigger.new_effect.modify_attribute(
            quantity=1,
            object_attributes=5,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

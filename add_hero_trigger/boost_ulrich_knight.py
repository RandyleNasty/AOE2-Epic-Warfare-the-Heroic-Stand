def boost_ulrich(trigger_manager, hero_id, players_applied, hero_configuration_matrix=None):
    for player_id in players_applied:
        trigger = trigger_manager.add_trigger(
            f"hero_{hero_id}_p{player_id}",
            enabled=True,
            looping=False
        )

        # Index 2: Melee Attack
        trigger.new_effect.modify_attribute(
            armour_attack_quantity=25,
            armour_attack_class=4,
            object_attributes=9,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 3: Movement Speed
        trigger.new_effect.modify_attribute(
            quantity=2,
            object_attributes=5,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 4: Blast Width
        trigger.new_effect.modify_attribute(
            quantity=3,
            object_attributes=22,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 5: Melee Armor
        trigger.new_effect.modify_attribute(
            armour_attack_quantity=25,
            armour_attack_class=4,
            object_attributes=8,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 6: Pierce Armor
        trigger.new_effect.modify_attribute(
            armour_attack_quantity=25,
            armour_attack_class=3,
            object_attributes=8,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 7: Blast Attack Level
        trigger.new_effect.modify_attribute(
            quantity=4,
            object_attributes=44,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 8: Max Range
        trigger.new_effect.modify_attribute(
            quantity=2,
            object_attributes=12,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 9: Total Missiles
        trigger.new_effect.modify_attribute(
            quantity=20,
            object_attributes=102,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 10: Max Total Missiles
        trigger.new_effect.modify_attribute(
            quantity=20,
            object_attributes=107,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 11: Projectile Unit
        trigger.new_effect.modify_attribute(
            quantity=676,
            object_attributes=16,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # Index 12: Accuracy Percent
        trigger.new_effect.modify_attribute(
            quantity=30,
            object_attributes=11,
            operation=1,
            source_player=player_id,
            object_list_unit_id=hero_id
        )

        # I

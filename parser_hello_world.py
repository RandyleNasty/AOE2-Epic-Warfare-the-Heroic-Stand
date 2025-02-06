from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.units import UnitInfo


#input_path = "Epic_Warfare Remastered v1_4 Hero PvE.aoe2scenario"
input_path = "hero test.aoe2scenario"
output_path = "../Output.aoe2scenario"


scenario = AoE2DEScenario.from_file(input_path)

trigger_manager = scenario.trigger_manager


# Save the created trigger
hello_world_trigger = trigger_manager.add_trigger("Hello World Trigger")
# Add display_instructions effect to the new trigger
hello_world_trigger.new_effect.display_instructions(
    display_time=11,
    message="Hello World"
)


unit_manager = scenario.unit_manager
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.MILITIA.ID,              x=15, y=12)
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.MAN_AT_ARMS.ID,          x=15, y=13)
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.LONG_SWORDSMAN.ID,       x=15, y=14)
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.TWO_HANDED_SWORDSMAN.ID, x=15, y=15)
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.CHAMPION.ID,             x=15, y=16)



map_manager = scenario.map_manager
map_manager.set_elevation(elevation=3, x1=10, y1=10, x2=20, y2=20)



scenario.write_to_file(output_path)
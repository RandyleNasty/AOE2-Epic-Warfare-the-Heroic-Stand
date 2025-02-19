from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.units import UnitInfo
import random

#input_path = ""
input_path = "hero test.aoe2scenario"
output_path = "../Output.aoe2scenario"


epic_warfare_path = "Epic_Warfare Remastered v1_4 Hero PvE.aoe2scenario"
# Define Scenario files
epic_warfare_scenario = AoE2DEScenario.from_file(epic_warfare_path)

# Define Trigger Managers
epic_warfare__trigger_manager = epic_warfare_scenario.trigger_manager


# Print all triggers with their details
print(f"\nTotal triggers: {len(epic_warfare__trigger_manager.triggers)}")
for index, trigger in enumerate(epic_warfare__trigger_manager.triggers):
    print(f"""
    Trigger {index + 1}:
    Name: {trigger.name}
    Description: {trigger.description}
    Enabled: {trigger.enabled}
    """)




scenario = AoE2DEScenario.from_file(input_path)


trigger_manager = scenario.trigger_manager


# Save the created trigger
hello_world_trigger = trigger_manager.add_trigger("Hello World Trigger")
# Add display_instructions effect to the new trigger
hello_world_trigger.new_effect.display_instructions(
    display_time=11,
    message="Hello World"
)


#originalTerrains = scenario.map_manager.terrain

map_manager = scenario.map_manager


# Configuration
RIVER_WIDTH = 5
TRANSITION_ZONE = 8  # Tiles for blending between biomes
SNOW_TERRAINS = [32, 73, 74]  # Snow textures
SPRING_TERRAINS = [12, 5, 71]  # Grass, leaves, jungle underbrush
WATER_TYPES = [4, 58, 59]  # Shallows, azure water variations
DECORATIVE_TERRAINS = [90, 91, 92, 107]  # Reeds, wet beaches

for terrain in map_manager.terrain:
    x, y = terrain.x, terrain.y
    
    # Create winding river using Perlin-like pattern
    river_center = int((map_manager.map_size / 2) + 15 * 
                      (0.5 * (1 + (x/15 % 1)) + 0.3 * (1 + (y/10 % 1))))
    
    distance_to_river = abs(y - river_center)
    
    # River biome
    if distance_to_river < RIVER_WIDTH:
        terrain.terrain_id = random.choice(WATER_TYPES)
        terrain.elevation = 0  # Ensure flat water surface
        # Add riverbank details
        if distance_to_river == RIVER_WIDTH - 1:
            terrain.layer = random.choice([107, 108])  # Wet beaches
            if random.random() < 0.3:
                terrain.terrain_id = random.choice(DECORATIVE_TERRAINS)

    # Snow biome (north side)
    elif y < river_center - TRANSITION_ZONE:
        base_terrain = random.choices([0, 9, 32], weights=[5, 3, 2])[0]  # Grass/snow
        terrain.terrain_id = base_terrain
        # Layer snow textures
        terrain.layer = random.choices(SNOW_TERRAINS + [-1], 
                                     weights=[4,3,2,1], k=1)[0]  # 60% chance of snow layer
        # Add elevation variation
        terrain.elevation = 1 + int((river_center - y)/10) % 2
        
    # Spring biome (south side)    
    elif y > river_center + TRANSITION_ZONE:
        terrain.terrain_id = random.choices([12, 10, 17], weights=[6, 3, 1])[0]  # Grass/forests
        terrain.layer = random.choices([5, 71, 77] + [-1], 
                                     weights=[4,2,1,3], k=1)[0]  # 60% vegetation
        terrain.elevation = 1 + int((y - river_center)/12) % 2

    # Transition zone
    else:
        blend = (y - (river_center - TRANSITION_ZONE)) / (2*TRANSITION_ZONE)
        # Snow fading elements
        if random.random() > blend**2:
            terrain.layer = random.choice(SNOW_TERRAINS)
            terrain.terrain_id = random.choice([0, 9, 32, 6])  # Mix snow/earth
        else:
            terrain.layer = random.choice([5, 71, 44])  # Underbrush/mud
            terrain.terrain_id = random.choice([12, 11, 42])  # Spring grasses
        
        # Elevation smoothing
        terrain.elevation = 1 + int(2 * abs(blend - 0.5))

# Final touches
#map_manager.add_elevation_ramps()  # Smooth terrain transitions

# Manual elevation blending for smooth transitions
# 

# TRANSITION_WIDTH = 8  # Tiles for gradual blending
# for terrain in scenario.map_manager.terrain:
#     if terrain.y < map_center_y - TRANSITION_WIDTH:
#         # Snow biome: Base terrain 32 (Snow) with layers 73/74
#         terrain.terrain_id = 32
#         terrain.layer = random.choice([73, 74, -1])
#     elif terrain.y > map_center_y + TRANSITION_WIDTH:
#         # Spring biome: Base 12 (Grass 2) with layers 71/77
#         terrain.terrain_id = 12
#         terrain.layer = random.choice([71, 77, -1])
#     else:  # Transition zone
#         blend = (terrain.y - (map_center_y - TRANSITION_WIDTH)) / (2*TRANSITION_WIDTH)
#         terrain.terrain_id = 32 if random.random() > blend else 12
#         terrain.layer = 74 if blend < 0.3 else 77 if blend > 0.7 else -1

unit_manager = scenario.unit_manager
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.MILITIA.ID,              x=0, y=12)
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.MAN_AT_ARMS.ID,          x=0, y=13)
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.LONG_SWORDSMAN.ID,       x=0, y=14)
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.TWO_HANDED_SWORDSMAN.ID, x=0, y=15)
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.CHAMPION.ID,             x=0, y=16)



map_manager = scenario.map_manager
map_manager.set_elevation(elevation=3, x1=10, y1=10, x2=20, y2=20)



scenario.write_to_file(output_path)
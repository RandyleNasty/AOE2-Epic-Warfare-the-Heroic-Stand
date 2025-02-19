


from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.terrains import TerrainId
import random

# Initialize scenario
# Initialize scenario
scenario =  AoE2DEScenario.from_file("empty.aoe2scenario")
#scenario.map_manager.map_size = (100, 100)
# Set base terrain
for x in range(100):
    for y in range(100):
        tile = scenario.map_manager.get_tile(x, y)
        tile.terrain_id = TerrainId.GRASS_1  # ID 0
        tile.elevation = 0

# Create river
river_path = []
for y in range(30, 70):
    x = 50 + int(10 * random.gauss(0, 1))
    x = max(20, min(x, 80))
    river_path.append((x, y))
    
    for dx in range(-3, 4):
        for dy in range(-1, 2):
            if 0 <= x+dx < 100 and 0 <= y+dy < 100:
                tile = scenario.map_manager.get_tile(x+dx, y+dy)
                tile.terrain_id = 1  # WATER_SHALLOW
                tile.layer = random.choice([59, 1])  # SHALLOWS_AZURE/WATER_SHALLOW

# Add river banks
for (x,y) in river_path:
    for dx in range(-5, 6):
        for dy in range(-3, 4):
            if 0 <= x+dx < 100 and 0 <= y+dy < 100:
                tile = scenario.map_manager.get_tile(x+dx, y+dy)
                if tile.terrain_id == 0:  # GRASS_1
                    tile.terrain_id = 2  # BEACH

# Create castle area
castle_x, castle_y = 50, 20
for dx in range(-15, 16):
    for dy in range(-10, 11):
        x = castle_x + dx
        y = castle_y + dy
        if 0 <= x < 100 and 0 <= y < 100:
            dist = (dx**2 + dy**2)**0.5
            scenario.map_manager.get_tile(x, y).elevation = max(0, int(3 * (1 - dist/20)))

# Place Castle (ID 82)
scenario.unit_manager.add_unit(
    player=1,
    unit_const=82,
    x=castle_x,
    y=castle_y,
)

# Building IDs from your dataset
BUILDINGS = [
    (70, 30),   # HOUSE
    (104, 2),   # MONASTERY
    (84, 1),    # MARKET
    (103, 1),   # BLACKSMITH
    (109, 1)    # TOWN_CENTER
]

for building_id, count in BUILDINGS:
    for _ in range(count):
        angle = random.uniform(0, 6.28)
        radius = random.randint(15, 25)
        x = castle_x + int(radius * 1.5 * random.uniform(0.8, 1.2))
        y = castle_y + int(radius * random.uniform(0.8, 1.2))
        
        scenario.unit_manager.add_unit(
            player=1,
            unit_const=building_id,
            x=x,
            y=y,
        )

# Add roads
road_path = [
    (castle_x, castle_y, 50, 50),
    (50, 50, 50, 70)
]

for path in road_path:
    for x, y in zip(range(path[0], path[2]+1), range(path[1], path[3]+1)):
        for dx in range(-2, 3):
            for dy in range(-1, 2):
                tile = scenario.map_manager.get_tile(x+dx, y+dy)
                if tile.terrain_id in [0, 2]:  # GRASS_1/BEACH
                    tile.terrain_id = random.choice([24, 25])  # ROAD/ROAD_BROKEN

# Decorations from your dataset
DECORATIONS = [
    (399, 40),  # TREE_A
    (349, 30),  # TREE_OAK
    (350, 20),  # TREE_PINE
    (334, 100), # FLOWERS_1
    (623, 20)   # ROCK_1
]

for decor_id, count in DECORATIONS:
    for _ in range(count):
        x = random.randint(0, 99)
        y = random.randint(0, 99)
        scenario.unit_manager.add_unit(
            player=0,
            unit_const=decor_id,
            x=x,
            y=y,
        )

# Save scenario
scenario.write_to_file("salzburg_city.aoe2scenario")
print("Salzburg city generated successfully!")

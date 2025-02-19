from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.terrains import TerrainId

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.players import PlayerId
#from AoE2ScenarioParser.datasets.


import random
import math

# Initialize scenario
scenario =  AoE2DEScenario.from_file("empty.aoe2scenario")

# Set base snowy terrain
for x in range(120):
    for y in range(120):
        tile = scenario.map_manager.get_tile(x, y)
        tile.terrain_id = TerrainId.SNOW  # ID 32
        tile.layer = random.choice([TerrainId.SNOW, TerrainId.FOREST_PINE])  # IDs 31,32
        tile.elevation = random.choice([0, 0, 1])  # Uneven snowy ground

# Create mountain backdrop
for _ in range(15):  # Create 15 mountain peaks
    peak_x = random.randint(0, 119)
    peak_y = random.randint(0, 119)
    for dx in range(-30, 31):
        for dy in range(-30, 31):
            x = peak_x + dx
            y = peak_y + dy
            if 0 <= x < 120 and 0 <= y < 120:
                dist = (dx**2 + dy**2)**0.5
                elev = max(0, int(8 * (1 - dist/30)))
                scenario.map_manager.get_tile(x, y).elevation += elev

# Create frozen river
river_path = []
for x in range(20, 100):
    y = 60 + int(15 * random.gauss(0, 1))
    y = max(30, min(y, 90))
    river_path.append((x, y))
    
    for dx in range(-4, 5):
        for dy in range(-2, 3):
            if 0 <= x+dx < 120 and 0 <= y+dy < 120:
                tile = scenario.map_manager.get_tile(x+dx, y+dy)
                tile.terrain_id = TerrainId.ICE  # ID 26
                if random.random() > 0.7:
                    tile.layer = TerrainId.SHALLOWS_AZURE  # ID 59

# Create docks area
dock_center = (70, 65)
for dx in range(-15, 16):
    for dy in range(-5, 6):
        x = dock_center[0] + dx
        y = dock_center[1] + dy
        if 0 <= x < 120 and 0 <= y < 120:
            # Flatten dock area
            scenario.map_manager.get_tile(x, y).elevation = 0
            if abs(dx) < 12 and abs(dy) < 4:
                tile.terrain_id = TerrainId.WATER_SHALLOW  # ID 1
            elif abs(dx) < 15:
                tile.terrain_id = TerrainId.BEACH  # ID 2

# Add city structures
city_center = (60, 60)
structures = [
    # Format: (unit_id, count, min_dist, max_dist)
    (70, 40, 10, 30),   # Houses
    (84, 3, 15, 25),    # Markets
    (104, 2, 20, 30),   # Monasteries
    (79, 4, 5, 40),     # Watchtowers (ID 79)
    (45, 5, -15, -5),   # Docks (ID 45) placed near water
    (117, 8, 0, 50),    # Stone walls (ID 117)
    (1338, 10, 10, 35), # Carts (ID 1338)
    (814, 15, 20, 50)   # Horses (ID 814)
]

for unit_id, count, min_d, max_d in structures:
    for _ in range(count):
        angle = random.uniform(0, 6.28)
        distance = random.randint(min_d, max_d)
        x = city_center[0] + int(distance * math.cos(angle))
        y = city_center[1] + int(distance * math.sin(angle))
        
        if 0 <= x < 120 and 0 <= y < 120:
            # Add snow caps to buildings
            if unit_id in [70, 84, 104]:
                scenario.map_manager.get_tile(x, y).layer = TerrainId.SNOW  # ID 31
            
            scenario.unit_manager.add_unit(
                player=1,
                unit_const=unit_id,
                x=x,
                y=y
            )

# Add boats
for _ in range(8):
    x = random.randint(55, 85)
    y = random.randint(60, 70)
    scenario.unit_manager.add_unit(
        player=1,
        unit_const=random.choice([13, 17, 527]),  # Fishing Ship, Trade Cog, DemoShip
        x=x,
        y=y
    )

# Add pine forest
for _ in range(300):
    x = random.randint(0, 119)
    y = random.randint(0, 119)
    if 40 < x < 100 and 40 < y < 100: continue  # Avoid city center
    scenario.unit_manager.add_unit(
        player=0,
        unit_const=350,  # TREE_PINE
        x=x,
        y=y
    )

# Add decorative flags and rocks
for _ in range(50):
    x = random.randint(40, 80)
    y = random.randint(40, 80)
    scenario.unit_manager.add_unit(
        player=0,
        unit_const=random.choice([623, 334, 349]),  # Rock1, Flowers1, Oak
        x=x,
        y=y
    )

# Create paths
for _ in range(20):
    start_x = random.randint(40, 80)
    start_y = random.randint(40, 80)
    for step in range(30):
        x = start_x + int(step * random.gauss(0, 1))
        y = start_y + int(step * random.gauss(0, 1))
        if 0 <= x < 120 and 0 <= y < 120:
            tile = scenario.map_manager.get_tile(x, y)
            tile.terrain_id = random.choice([24, 25])  # Road types

scenario.write_to_file("snowy_mountain_city.aoe2scenario")
print("Winter city generated successfully!")

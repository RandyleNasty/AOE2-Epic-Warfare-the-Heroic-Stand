from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.players import PlayerId
import random
import math
# Initialize scenario
scenario = AoE2DEScenario.from_file("empty.aoe2scenario")

## ====== ENHANCED TERRAIN SYSTEM ======
def create_terrain():
    for x in range(100):
        for y in range(100):
            tile = scenario.map_manager.get_tile(x, y)
            # Base terrain with gradual transitions
            if y > 80:  # Far North (Beyond the Wall)
                tile.terrain_id = random.choice([TerrainId.ICE, TerrainId.SNOW_STRONG])
            elif 60 < y <= 80:  # Haunted Forest
                tile.terrain_id = TerrainId.GRASS_3 if random.random() > 0.3 else TerrainId.ICE
            elif 40 < y <= 60:  # The Riverlands
                tile.terrain_id = TerrainId.GRASS_2 if x < 40 else TerrainId.DIRT_MUD
            else:  # Southern Kingdoms
                tile.terrain_id = TerrainId.GRASS_DRY

            # Strategic elevation (mountains and cliffs only)
            if (45 < x < 55 and y > 85) or (20 < x < 30 and 20 < y < 40):
                tile.elevation = min(4, int((abs(x-50) + abs(y-85))/4))
            else:
                tile.elevation = 0 if random.random() > 0.95 else 1

create_terrain()

## ====== KING'S LANDING COMPLEX ======
def build_kings_landing():
    # Red Keep Complex
    scenario.unit_manager.add_unit(PlayerId.THREE, BuildingInfo.CASTLE.ID, 75, 25)
    for dx, dy in [(0,5), (5,0), (-5,0), (0,-5)]:
        scenario.unit_manager.add_unit(PlayerId.THREE, BuildingInfo.GUARD_TOWER.ID, 75+dx, 25+dy)
    
    # Throne Room Complex
    scenario.unit_manager.add_unit(PlayerId.THREE, BuildingInfo.WONDER.ID, 75, 30)
    scenario.unit_manager.add_unit(PlayerId.GAIA, BuildingInfo.CATHEDRAL.ID, 75, 35)
    for x in range(70,80,2):
        scenario.unit_manager.add_unit(PlayerId.THREE, UnitInfo.PALADIN.ID, x, 40)
    
    # Flea Market
    for i in range(5):
        scenario.unit_manager.add_unit(PlayerId.GAIA, BuildingInfo.MARKET.ID, 85+i*3, 30)
        scenario.unit_manager.add_unit(PlayerId.GAIA, UnitInfo.VILLAGER_MALE.ID, 85+i*3, 31)

build_kings_landing()

## ====== WINTERFELL EXPANDED ======
def build_winterfell():
    # Main Castle Complex
    scenario.unit_manager.add_unit(PlayerId.TWO, BuildingInfo.CASTLE.ID, 25, 25)
    for angle in range(0, 360, 45):
        dx = int(8 * math.cos(math.radians(angle)))
        dy = int(8 * math.sin(math.radians(angle)))
        scenario.unit_manager.add_unit(PlayerId.TWO, BuildingInfo.WATCH_TOWER.ID, 25+dx, 25+dy)
    
    # Stark Army Garrison
    units = [UnitInfo.KNIGHT, UnitInfo.CHAMPION, UnitInfo.SPEARMAN]
    for i in range(20):
        unit = random.choice(units)
        scenario.unit_manager.add_unit(PlayerId.TWO, unit.ID, 25+random.randint(-10,10), 25+random.randint(-10,10))
    
    # Godswood with Weirwood Tree
    # for x in range(15,35):
    #     for y in range(30,40):
    #         if random.random() > 0.7:
    #             scenario.unit_manager.add_unit(PlayerId.GAIA, UnitInfo.TREE_ACACIA.ID, x, y)
    # scenario.unit_manager.add_unit(PlayerId.GAIA, BuildingInfo.MONUMENT.ID, 20, 35)

build_winterfell()

## ====== THE WALL DEFENSES ======
def build_the_wall():
    # Enhanced Wall System
    for y in range(85, 90):
        scenario.unit_manager.add_unit(PlayerId.ONE, BuildingInfo.FORTIFIED_WALL.ID, 40, y)
        scenario.unit_manager.add_unit(PlayerId.ONE, BuildingInfo.FORTIFIED_WALL.ID, 60, y)
    
    # Castle Black Complex
    scenario.unit_manager.add_unit(PlayerId.ONE, BuildingInfo.CASTLE.ID, 50, 83)
    for x in range(45,55,2):
        scenario.unit_manager.add_unit(PlayerId.ONE, BuildingInfo.BARRACKS.ID, x, 80)
        scenario.unit_manager.add_unit(PlayerId.ONE, UnitInfo.PIKEMAN.ID, x, 81)
    
    # Eastwatch Harbor
    for x in range(55,65):
        scenario.unit_manager.add_unit(PlayerId.ONE, BuildingInfo.DOCK.ID, x, 95)
        scenario.unit_manager.add_unit(PlayerId.ONE, UnitInfo.WAR_GALLEY.ID, x+1, 96)

build_the_wall()

## ====== DRAGONSTONE & ESSOS ======
def build_dragonstone():
    # Targaryen Stronghold
    scenario.unit_manager.add_unit(PlayerId.FOUR, BuildingInfo.CASTLE.ID, 90, 15)
    for i in range(3):  # Dragons
        scenario.unit_manager.add_unit(PlayerId.FOUR, UnitInfo.FALCON.ID, 85+i*5, 10)
    
    # Unsullied Formation
    for x in range(85,95,2):
        scenario.unit_manager.add_unit(PlayerId.FOUR, UnitInfo.HALBERDIER.ID, x, 20)
        scenario.unit_manager.add_unit(PlayerId.FOUR, UnitInfo.CAVALRY_ARCHER.ID, x, 21)

build_dragonstone()

## ====== DYNAMIC ENVIRONMENT ======
# Wildling Camps
for _ in range(5):
    x, y = random.randint(35,65), random.randint(90,95)
    scenario.unit_manager.add_unit(PlayerId.GAIA, BuildingInfo.TENT_A.ID, x, y)
    scenario.unit_manager.add_unit(PlayerId.GAIA, UnitInfo.IRON_BOAR.ID, x+1, y)

# River System
for x in range(30,70):
    scenario.map_manager.get_tile(x,50).terrain_id = TerrainId.WATER_SHALLOW
    if x % 5 == 0:
        scenario.unit_manager.add_unit(PlayerId.GAIA, BuildingInfo.BRIDGE_A_MIDDLE.ID, x, 50)

# Tourney Grounds
for x in range(40,60,4):
    scenario.unit_manager.add_unit(PlayerId.GAIA, BuildingInfo.STABLE.ID, x, 35)
    scenario.unit_manager.add_unit(PlayerId.GAIA, UnitInfo.KNIGHT.ID, x+1, 35)

# Save scenario
scenario.write_to_file("throne_of_winter_v2.aoe2scenario")
print("Valar Morghulis! Enhanced scenario generated!")

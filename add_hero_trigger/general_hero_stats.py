from AoE2ScenarioParser.datasets.heroes import HeroInfo

"""define general hero armour"""
general_footman_melee_armour = 9
general_footman_pierce_armour = 9
general_cav_melee_armour = 7
general_cav_pierce_armour = 7

general_ranged_melee_armour = 5
general_ranged_pierce_armour = 5

EAST_TARGET_LOCATION_X = 42
EAST_TARGET_LOCATION_Y = 46
ID_COMMANDER_TENT = 2262
WEST_TARGET_LOCATION_X = 225
WEST_TARGET_LOCATION_Y = 214




TIME_WINDOW_PLAYER_CHOOSE_HERO = 120
TIME_HERO_RESPAWN = 120

tent_training_location_tuple = [
    (103, 41),
    (54, 114),
    (27, 187),
    (22, 101),
    (180, 174),
    (205, 84),
    (130, 210),
    (233, 148)
]

tent_area_data = [
    {'area_x1': 102, 'area_y1': 38, 'area_x2': 103, 'area_y2': 39},
    {'area_x1': 53,  'area_y1': 112, 'area_x2': 54,  'area_y2': 113},
    {'area_x1': 26,  'area_y1': 184, 'area_x2': 27,  'area_y2': 185},
    {'area_x1': 21,  'area_y1': 99,  'area_x2': 22,  'area_y2': 100},
    {'area_x1': 179, 'area_y1': 171, 'area_x2': 180, 'area_y2': 172},
    {'area_x1': 204, 'area_y1': 81,  'area_x2': 205, 'area_y2': 82},
    {'area_x1': 129, 'area_y1': 207, 'area_x2': 130, 'area_y2': 208},
    {'area_x1': 232, 'area_y1': 144, 'area_x2': 233, 'area_y2': 145}
]


cleon_ID = 2346
Darius_ID = 2347
Jean_De_Lorrain_ID = 644  
Dagnajan_Elephant_ID = 1106

sabo_man_id = 706
hero_test_id = 1072



#NUM_HERO_ALLOWED = None

HERO_FAKE_AS_EXPLODING_ELEPHANT_ID = 1071
sabo_man_id = 706


#BRASIDAS suspicious of having bug
#HERO_BRASIDAS_ID = 2162
HERO_BRASIDAS_ID = 2317
#HeroInfo.ROBIN_HOOD.ID
LIST_HERO_IDS = [
                #Darius_ID, 
                HeroInfo.ROBIN_HOOD.ID,
                HeroInfo.JEAN_BUREAU.ID,
                cleon_ID,
                HeroInfo.KOTYAN_KHAN.ID,
                HeroInfo.ULRICH_VON_JUNGINGEN.ID,
                HeroInfo.TSAR_KONSTANTIN.ID,
                Dagnajan_Elephant_ID,
                HeroInfo.GENGHIS_KHAN.ID,
                # HeroInfo.GODS_OWN_SLING_PACKED.ID,
                HERO_FAKE_AS_EXPLODING_ELEPHANT_ID,
                HERO_BRASIDAS_ID,
                
                HeroInfo.BELISARIUS.ID,
                #HeroInfo.FRANCISCO_DE_ORELLANA.ID,
                ]


#HERO DEAD BODY IDs 
"""
serve to help trigger detect hero has died

"""
LIST_HERO_DEAD_IDS = [
                #Darius_ID, 
                115,
                HeroInfo.JEAN_BUREAU.ID,
                cleon_ID,
                HeroInfo.KOTYAN_KHAN.ID,
                HeroInfo.ULRICH_VON_JUNGINGEN.ID,
                HeroInfo.TSAR_KONSTANTIN.ID,
                Dagnajan_Elephant_ID,
                HeroInfo.GENGHIS_KHAN.ID,
                # HeroInfo.GODS_OWN_SLING_PACKED.ID,
                HERO_FAKE_AS_EXPLODING_ELEPHANT_ID,
                HERO_BRASIDAS_ID,
                #HeroInfo.FRANCISCO_DE_ORELLANA.ID,
                HeroInfo.BELISARIUS.ID
                ]

LIST_DESCRIPTION = [
    #"Javelin Splashing duo-horse Chariot", 
                    "wields the legendary Stormbow",
                    "Skyfall Cluster Bomb Cannon",
                    "The Invincible Footman", 
                    "The Explosive Arrow Mounter Archer",
                    "The Flaming Throw Knight", 
                    "The Gatling Ballista Tri-Horse Chariot,", 
                    "The Flaming Thunder War Elephant", 
                    "The Exploding Wolf Summoner",
                    #"God Swing",
                    "The Self-Exploding Elephant",
                    "The AOE Greek Hero Footman",
                    #"Mounted Gunpower Knight",
                    "The Roman Army Summon General",
                    #"Mounted Hero Test"
                    ]

# very fragile value! if in map the commander tent changes, could cause crash!
TENTS_SELECTED_OBJECT_IDS = [317958, 317979, 322879, 319227, 328305, 328275, 328335, 328365]

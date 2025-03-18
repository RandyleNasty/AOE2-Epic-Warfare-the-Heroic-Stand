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

cleon_ID = 2346
Darius_ID = 2347
Jean_De_Lorrain_ID = 644  
Dagnajan_Elephant_ID = 1106

sabo_man_id = 706
hero_test_id = 1072


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
                #HeroInfo.FRANCISCO_DE_ORELLANA.ID,
                HeroInfo.BELISARIUS.ID
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

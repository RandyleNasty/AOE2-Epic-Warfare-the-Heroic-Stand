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

LIST_DESCRIPTION = [
    #"Javelin Splashing duo-horse Chariot", 
                    "Vaelor, the Stormbow, a feared master of the battlefield, wields the legendary Stormbow, capable of unleashing a relentless downpour of arrows upon his enemies. His volleys blot out the sun, leaving no escape for those caught beneath his deadly rain. Tales of his wrath spread across kingdoms, as entire armies have fallen under his sky-darkening assault.",
                    "The Cataclysm Ordinance: Skyfall Cluster Bomb Cannon, a doomsday weapon of unparalleled destruction, reshapes the battlefield with every thunderous volley. Upon activation, it unleashes a cascade of incendiary canisters, each fragmenting into countless explosive shards that rain devastation from the heavens. No stronghold is impenetrable, no army beyond its reach—its fury engulfs all who dare stand beneath its cataclysmic downpour. Legends speak in hushed whispers of its wrath, a harbinger of ruin whose echoes linger long after the battlefield is reduced to ash.",
                    "The Invincible Footman, known as the Warlord's Juggernaut, marches fearlessly into battle, an unstoppable force clad in impenetrable armor. Armed with devastating explosives, he turns the tide of war with calculated detonations, blasting through enemy ranks and fortifications alike. Blades shatter against him, arrows break upon his shield—no force can halt his advance. Stories of his wrath spread like wildfire, a living legend of destruction that leaves only ruin in his wake.", 
                    "The Explosive Arrow Mounter Archer, known as the Blazing Harbinger, strikes fear into the hearts of his foes with every fiery shot. Armed with a deadly arsenal of explosive-tipped arrows, he turns the sky into a battlefield, each projectile igniting upon impact in a storm of fire and shrapnel. No wall is safe, no formation unbroken—his volleys tear through ranks and fortifications alike. Whispers of his devastation spread far and wide, a bringer of ruin whose arrows spell the end for those caught in their blazing wake.",
                    "The Flaming Throw Knight, known as the Infernal Vanguard, charges into battle wreathed in fire, his weapon a conduit of relentless devastation. With every swing, he hurls searing flames, engulfing enemies in a blazing storm that leaves only ashes in its wake. His presence alone turns the battlefield into an inferno, where armor melts and courage falters. Tales of his fiery wrath spread like wildfire, a harbinger of ruin whose advance none can withstand.", 
                    "The Gatling Ballista Tri-Horse Chariot, known as the Stormstride Reaper, thunders across the battlefield like a force of nature. Drawn by three war-hardened steeds, its rotating ballista unleashes an unrelenting hail of bolts, shredding ranks and fortifications with mechanical precision. No warrior can outrun its charge, no shield can withstand its storm—those caught in its path are left in ruin. Legends of its devastation echo through war-torn lands, a relentless harbinger of annihilation.", 
                    "The Flaming Thunder War Elephant, known as the Pyrostorm Behemoth, is a living engine of destruction, towering over the battlefield as fire and fury erupt in its wake. Adorned with armor wreathed in flame, it charges with unstoppable force, trampling ranks beneath its colossal might while hurling searing blasts of fire and lightning. Walls crumble, armies scatter, and the earth trembles beneath its relentless advance. Whispers of its devastation spread like wildfire—when the Pyrostorm Behemoth marches, only ashes remain.", 
                    "The Exploding Wolf Summoner, known as the Ravager of the Wilds, calls forth a pack of fiery, explosive wolves that tear through the battlefield with savage fury. Each summoned beast is a ticking time bomb, charging at enemies with a howl that heralds their doom, detonating in violent bursts of fire and shrapnel upon impact. No enemy is safe, as the explosive wolves hunt in relentless packs, turning the battlefield into a chaotic inferno. Tales of the Ravager’s fury spread across the lands, a terrifying force that leaves only destruction in its wake.",
                    #"God Swing",
                    "The Self-Exploding Elephant, known as the Doombringer, is a massive, unstoppable force of nature, bound for annihilation. With every step, it charges relentlessly toward its target, its body rigged with volatile explosives. Upon impact, it detonates in a cataclysmic explosion, obliterating everything in its path—fortifications, armies, and the earth itself. No structure stands, no army survives its wrath. Whispers of the Doombringer's devastation spread far and wide, a terrifying omen of unstoppable destruction, where only ruin remains in its wake.",
                    "The AOE Greek Hero Footman, known as the Spartan Vanguard, stands as a symbol of unmatched strength and courage. Clad in heavy armor and armed with a legendary shield, he leads the charge with the might of a warrior born from the gods. With every swing of his weapon, he creates shockwaves that ripple across the battlefield, striking down foes in all directions. His presence inspires his allies, while his devastating attacks leave nothing but destruction in his wake. The stories of his valor and wrath echo throughout the lands, a living legend whose fury no enemy can withstand.",
                    #"Mounted Gunpower Knight",
                    "The Roman Army Summon General, known as the Imperial Warlord, commands the might of a disciplined and unyielding legion. With a single call, he summons the full force of the Roman army, their ironclad ranks forming an impenetrable wall of power and precision. His strategic brilliance leads them into battle, with every legionnaire moving in perfect harmony to crush enemies under the weight of Roman might. No force can rival his command, no army can break his ranks. Legends speak of the Imperial Warlord’s ability to turn the tide of war, leaving only the echoes of victory in his wake."
                    ]

# very fragile value! if in map the commander tent changes, could cause crash!
TENTS_SELECTED_OBJECT_IDS = [317958, 317979, 322879, 319227, 328305, 328275, 328335, 328365]

from hero_abstract_class import *
from AoE2ScenarioParser.datasets.heroes import HeroInfo

from AoE2ScenarioParser.datasets.players import PlayerId

longbow_projectile_id = 511


projectile_from_war_galley_antiquity = 540

used_projectile = projectile_from_war_galley_antiquity

inst_robin_archer_hero = Hero(
    hero_id=HeroInfo.ROBIN_HOOD.ID,  # You'll need to provide the correct hero_id
    projectile_unit=used_projectile,
    #secondary_projectile_unit = 676,
    max_range=10,
    min_range=1,
    melee_attack=5,
    blast_width=1,
    blast_attack_level=4,
    pierce_armor=10,
    melee_armour=10,
    attack_reload_set=4,  
    accuracy_percent=25,
    total_missile = 100,
    attack_dispersion_multiply=2,
    combat_ability= 1 + 16 + 8,
    #walking_graphic = 654,
    movement_speed=1,
    #frame_delay=4,
    health_point=200,
    projectile_smart_mode = 2,
    population = 0,

)

#longbow project arc -0.06
inst_projectile_vol_fire = Hero(hero_id = used_projectile, 
                                #standing_graphic = 1743, 
                                #walking_graphic = 1743,
                                #dying_graphic = 1743,
                                dead_unit_id = 1334,
                                #blood_unit = 1334,
                                movement_speed_divide = 2
                                )


# inst_projectile_vol_fire = Hero(hero_id = used_projectile, 
#                                 standing_graphic = 3378, 
#                                 walking_graphic = 3378,
#                                 #dying_graphic = 1743,
#                                 dead_unit_id = 1334,
#                                 #blood_unit = 1334,
#                                #movement_speed_divide = 2
#                                )
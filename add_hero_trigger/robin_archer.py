from hero_abstract_class import *
from AoE2ScenarioParser.datasets.heroes import HeroInfo

from AoE2ScenarioParser.datasets.players import PlayerId


inst_robin_archer_hero = Hero(
    hero_id=HeroInfo.ROBIN_HOOD.ID,  # You'll need to provide the correct hero_id
    projectile_unit=511,
    max_range=10,
    min_range=4,
    melee_attack=5,
    blast_width=1,
    blast_attack_level=2 + 64,
    pierce_armor=10,
    melee_armour=10,
    attack_reload_set=3,  
    accuracy_percent=15,
    total_missile = 80,
    attack_dispersion_multiply=2,
    combat_ability= 1 + 16 + 8,
    #walking_graphic = 654,
    movement_speed=1,
    frame_delay=4,
    health_point=200,

)
# This page will create the functions to handle the combat system
import random
import time

# function that handles chase attack
def chase_attack(hero, h_name, move_n, e_hero):
    hero_name = hero.get_name()
    hero_str = hero.get_strength()
    hero_int = hero.get_intellect()
    hero_ch_atk_dmg = hero.move["chase_attack"]["damage"]
    hero_ch_atk_name = hero.move["chase_attack"]["name"]
    e_h_def = e_hero.get_defense()
    chase_dmg = hero_ch_atk_dmg + (hero_str * 3) - (e_h_def * 2)
    print(
        f"{hero_name} follows {h_name}'s {move_n} with {hero_ch_atk_name}. {chase_dmg} damage...")
    return chase_dmg



def fight_boss(t1h1,a_move, t1h2, t1h3, t1h4, t2h1, t2h2, t2h3, t2h4):
    # defining all variables that can we used in combat for utilization



    t1h1_m_attack = t1h1.move[a_move]
    #t1s1_chase = t1h2.move["chase_attack"]
    t1h1_name = t1h1.get_name()
    chase_dmg = 0
    print("BATTLE BEGINS")
    h1atk = t1h1.get_strength()
    h2def = t2h1.get_defense()
    main_atk = t1h1.move[a_move]["damage"]
    damage = int(main_atk) + (int(h1atk) * 3 - int(h2def) * 2)
    h2hp = t2h1.get_health()
    print(f"{t1h1_name} uses {t1h1.move[a_move]['name']}. {damage} damage...")
    #time.sleep(2)
    h2hp -= damage
    support= [t1h2, t1h3, t1h4]
    for x in support:
        if t1h1_m_attack["cause"] == x.move["chase_attack"]["chase"]:
            cause_atk_name= t1h2.get_name()
            #calling chase function to get chase damage
            chase_dmg = chase_attack(x, cause_atk_name, t1h1_name, t2h1)
            #time.sleep(2)
            h2hp -= chase_dmg
            
    print(f"{t2h1.get_name()} now has {h2hp} hit points!")
    return h2hp


def fight_hero(t2h1, a_move, t2h2, t2h3, t2h4, t1h1, t1h2, t1h3, t1h4,):
    # defining all variables that can we used in combat for utilization

    t1h1_m_attack = t1h1.move["kinto_attack"]
    t1s1_chase = t1h2.move["chase_attack"]
    chase_dmg = 0
    print("BATTLE BEGINS")
    h1atk = t1h1.get_strength()
    h2def = t2h1.get_defense()
    main_atk = t1h1.move[a_move]["damage"]
    damage = int(main_atk) + (int(h1atk) * 3 - int(h2def) * 2)
    print(f"{t1h1.get_name()} uses {t1h1.move[a_move]['name']}. {damage} damage...")
    time.sleep(2)
    if t1h1_m_attack["cause"] == t1s1_chase["chase"]:
        chase_dmg = int(t1s1_chase["damage"]) + (int(t1h2.get_strength()) * 3) - (int(h2def) * 2)
        print(
            f"{t1h2.get_name()} follows {t1h1.get_name()}'s {t1h1.move[a_move]['name']} with {t1s1_chase['name']}. {chase_dmg} damage...")
        time.sleep(2)
        h2hp = t2h1.get_health()

        h2hp = int(h2hp) - damage - chase_dmg
        print(f"{t2h1.get_name()} now has {h2hp} hit points!")
        return h2hp

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
import random
character_choices = [
    {'name':'Human',
    'health': 10,
    'power': 5,
    'super_power': 'double_strike',
    'bounty': 12
    },
    {'name':'Wizard',
    'health': 10,
    'power': 5,
    'super_power': 'black_magick',
    'bounty': 18
    }, 
    {'name':'Goblin',
    'health': 6,
    'power': 4,
    'super_power': 'quick',
    'bounty': 8
    }, 
    {'name':'Drow',
    'health': 6,
    'power': 7,
    'super_power': 'stealth',
    'bounty': 15
    }, 
    {'name':'Shadow',
    'health': 5,
    'power': 5,
    'super_power': 'phasing',
    'bounty': 10
    }, 
    {'name':'Cleric',
    'health': 8,
    'power': 4,
    'super_power': 'healing',
    'bounty': 10
    }, 
    {'name':'Zombie',
    'health': 6,
    'power': 1,
    'super_power': 'relentless',
    'bounty': 5
    }, 
    {'name':'Gunslinger',
    'health': 10,
    'power': 5,
    'super_power': 'headshot',
    'bounty': 20
    }
]


class Character:
    def __init__(self, name, health, power, super_power):
        self.name = name
        self.health = health
        self.power = power
        self.super_power = super_power
        # self.bounty

    def print_status(self, enemy):
        print('You are %s, prepare to fight!' % (self.name))
        print("You have %d health and %d power." % (self.health, self.power))
        print("%s has %d health and %d power." % (enemy.name, enemy.health, enemy.power))
        print()
        print("What do you want to do?")
        print("1. Fight %s" % (enemy.name))
        print("2. do nothing")
        print("3. flee")
        print("> ",)
    
    def alive(self):
        return self.health > 0
#establish super power mechanic and what abilities do what.
    def activate_super_power(self, enemy):
        if enemy.super_power == 'healing':
            health_regen = random.random() * 100
            if health_regen <= 20:
                enemy.health += 2
                print('***%s cast healing for 2 points?!?~~***' % (enemy.name))
        if self.super_power == 'double_strike':
            attack_percentage = random.random() * 100
            if attack_percentage <= 20:
                enemy.health -= self.power
                print('Double Strike! %s deals %d extra damage' % (self.name, self.power))
        if self.super_power == 'black_magick':
            magicka_percentage = random.random() * 100
            if magicka_percentage <= 5:
                enemy.health -= (enemy.health / 2)
                print('%s opens up a dark portal extracting half %s\'s lifepoints' % (self.name, enemy.name))
        if self.super_power == 'relentless':
            if self.health <= 0:
                self.health = 1
                print('The Zombie stands back up! What will %s do???' % enemy.name)



class Human(Character):
    def attack(self, enemy):
        enemy.health -= self.power
        print('%s deals %d to %s with his falchion' % (self.name, self.power, enemy.name))

class Wizard(Character):
    super_power = 'regeneration'
    def attack(self, enemy):
        enemy.health -= self.power
        print('> The wizard shoots a lightning bolt at %s, dealing %d damage to them' % (enemy.name, self.power))
                   
class Goblin(Character):
    def attack(self, enemy):
        enemy.health -= main_char.power
        print("> %s does %d damage to %s." % (self.name, self.power, enemy.name))
    
class Zombie(Character):
    def attack(self, enemy):
        enemy.health -= self.power
        print('> %s slowly lurches forwards and bites %s for %d damage' % (self.name, enemy.name, self.power))

class Cleric(Character):
    def attack(self, enemy):
        enemy.health -= self.power
        print('%s swings with their mace for %d damage to %s' % (self.name, self.power, enemy.name))

def main():
    while main_char.alive() and enemy_char.alive():
        #print out status from main characters perspective
        main_char.print_status(enemy_char)
        user_input = input()
        #take inputs from user
        if user_input == "1":
            # Hero attacks goblin
            main_char.attack(enemy_char)
            if enemy_char.alive() == False:
                print('You have claimed the bounty on %s' % enemy_char.name)
                print("%s is dead." % (enemy_char.name))
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        main_char.activate_super_power(enemy_char)
        enemy_char.activate_super_power(main_char)
        #if the enemy is alive he attacks back
        if enemy_char.alive():
        #     # enemy attacks hero
            enemy_char.attack(main_char)
            #if character is still alive run again
            if main_char.alive():
                pass
            else: 
                print('You have died...')   

def who_will_you_be(character_class_name):
    main_char = character_class_name()


main_char = Wizard('Sven the Wizard', 200, 4, 'black_magick')
enemy_char = Cleric('Güt the Cleric', 100, 5, 'healing')

main()

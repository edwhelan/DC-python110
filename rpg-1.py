"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
import random
character_choices = ['Wizard', 'Goblin', 'Drow', 'Shadow', 'Medic', 'Zombie', 'Gunslinger']


class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
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


class Human(Character):
    def attack(self, enemy):
        attack_percentage = random.random() * 100
        temp_power = self.power * 2
        if attack_percentage <= 20:
            enemy.health -= temp_power
            print("%s does %d damage to the %s." % (self.name, temp_power, enemy.name))
        else:
            enemy.health -= self.power
            print("> %s does %d damage to %s." % (self.name, self.power, enemy.name))

class Wizard(Character):
    def attack(self, enemy):
        enemy.health -= self.power
        print('> The wizard shoots a lightning bolt at %s, dealing %d damage to them' % (enemy.name, self.power))
                
        
class Goblin(Character):
    def attack(self, enemy):
        # Goblin attacks usable character
        enemy.health -= main_char.power
        print("> %s does %d damage to %s." % (self.name, self.power, enemy.name))
    
class Zombie(Character):
    def attack(self, enemy):
        enemy.health -= self.power
        print('> %s slowly lurches forwards and bites %s for %d damage' % (self.name, enemy.name, self.power))

def main():
    while main_char.alive() and enemy_char.alive():
        main_char.print_status(enemy_char)
        user_input = input()
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

        if enemy_char.alive():
        #     # Goblin attacks hero
            enemy_char.attack(main_char)
            #if character is still alive run again
            if main_char.alive():
                pass
            else: 
                print('You have died...')   



main_char = Goblin('Sven the Goblin', 20, 4)
enemy_char = Human('Wilson the Human', 10,5)

main()

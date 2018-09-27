"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
from random import *


class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("You do %d damage to the goblin." % self.power)
    
    def alive(self):
        return self.health > 0 


class Hero(Character):
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))
        print("The goblin has %d health and %d power." % (goblin_char.health, goblin_char.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
                
        
class Goblin(Character):
    def attack(self, enemy):
        if enemy.health > 0:
        # Goblin attacks hero
            enemy.health -= goblin_char.power
            print("The goblin does %d damage to you." % goblin_char.power)
            if enemy.health <= 0:
                print("You are dead.")
            

goblin_char = Goblin(6, 2)
hero_char = Hero(10,5)

def main():
    while goblin_char.alive() and hero_char.alive():
        hero_char.print_status()
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero_char.attack(goblin_char)
            if goblin_char.alive() == False:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin_char.alive():
        #     # Goblin attacks hero
            goblin_char.attack(hero_char)
            #if character is still alive run again
            hero_char.alive()   
goblin_char = Goblin(6, 2)
hero_char = Hero(10,5)

main()

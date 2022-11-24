#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Adventure game for Udacity/Cognizant Train to Hire Scholarship
    Adventure game is based on the fates from Greek mythology.
    Player wanders around an island and is turned into one of
    several monsters for each iteration of the game. Game ends
    when player either dies or completes his/her adventure.
    __author__ = "Albert Bustamante"
    __email__ = "albertbustamante@hotmail.com"
    __version__ = "1.0.1"
"""

import time
import random


def print_pause(dialog, seconds=2):
    print(dialog)
    time.sleep(seconds)


def apology(one: str, two: str):
    print_pause("I am sorry.  I do not understand, please type "
                f"{one} or {two}.")


def intro():
    print_pause("You find yourself on a beautiful greek island.")
    print_pause("You are unable to remember how you came to this paradise.", 3)
    print_pause("You encounter a forked path in the woods ahead of you.", 3)
    crossroads()


def fall():
    print_pause("You come around a corner and step over a cliff.")
    print_pause("You fall 500 feet into the sea and drown.", 3)
    print_pause("Atropos has choose to cut your thread of life early!"
                " GAME OVER!", 3)
    play_again()


def crossroads():
    print_pause("You can choose to go LEFT or RIGHT.")
    path = input("Please type either LEFT or RIGHT.\n").lower()
    # while True:
    if "right" == path:
        walk_around()
    elif "left" == path:
        print_pause("You travel down a scenic forest path and meet"
                    " a beautiful young girl.", 3)
        print_pause("She tells you her name is Clotho.")
        clotho()
    else:
        apology("LEFT", "RIGHT")
        crossroads()


def walk_around():
    print_pause("You take a long and beautiful walk around the perimeter of"
                " the island with many beautiful views.", 4)
    print_pause("You find yourself back at the same crossroad where you "
                "began this journey.")
    crossroads()


def rocky_pass():
    print_pause("Would you like to approach her or continue on on the "
                "other path?", 3)
    rocky_fork = input("Please type YES to approach Clotho or NO to continue "
                       "down the rocky path.").lower()
    if "1yes" == rocky_fork:
        clotho()
    elif "no" == rocky_fork:
        walk_around()
    else:
        apology("YES", "NO")
        rocky_pass()


def play_again():
    print_pause("Would you like to play again?")
    again = input("Please type YES to play again or NO to end game.\n").lower()
    if "yes" in again:
        intro()
    elif "no" in again:
        exit()
    else:
        apology("YES", "NO")
        play_again()


def clotho():
    print_pause("Would you like to speak with her or continue down the "
                "path?")
    clotho_response = input("Please type YES to speak with her or NO "
                            "to continue.\n").lower()
    if "yes" in clotho_response:
        print_pause("You speak with Clotho and as she looks into your "
                    "eyes.", 3)
        print_pause("You feel a strange sensation.", 3)
        print_pause("You have been transformed!", 3)
        print_pause("In your shock you move away from Clotho and back "
                    "into the forest.", 3)
        print_pause("Up ahead you see a clearing in the forest.", 3)
        lachesis()
    elif "no" in clotho_response:
        print_pause("You find yourself at a different forked path in "
                    "the forest.", 3)
        print_pause("Would you like to go LEFT or RIGHT?")
        cliff_fork = input("Please type LEFT or RIGHT.\n").lower()
        if "right" in cliff_fork:
            fall()
        elif "left" in cliff_fork:
            print_pause("You walk through a rocky pass and onto a "
                        "forest trail.")
            print_pause("At a fork in the trail, you can see the young girl "
                        "you just left.", 3)
            rocky_pass()
        else:
            apology("LEFT", "RIGHT")
            clotho()
    else:
        apology("YES", "NO")
        clotho()


def lachesis():
    print_pause("In the clearing you see a beautiful young woman dressed in "
                "a white gown behind her is a mirror.", 3)
    print_pause("She tells you her name is Lachesis.")
    print_pause("Lachesis bows deeply and says:")

    monsters = ["Typhos", "Echidna", "Gorgon Stheno", "Gorgon Euryal",
                "Gorgon Medusa", "Harpy", "Siren", "Cerebus"]
    you = random.choice(monsters)

    print_pause(f"Welcome,  Mighty {you}.")

    if "Typhos" == you:
        print_pause("Father and most powerful of all monsters!")
        print_pause("You will be destined to rule over all monsters and "
                    "father some of the most powerful beings alive.", 3)
        print_pause("You look into the mirror and see that you have been "
                    "transformed.", 3)
        print_pause("To a giant winged beast, that is half man and half "
                    "serpent.", 3)
        print_pause("A crown of fire and a hundred snakes cover your "
                    "shoulders.", 3)
    elif "Echidna" == you:
        print_pause("Mother of all monsters, destined to live forever!")
        print_pause("You will be forever young .")
        print_pause("You will consume the flesh from any foe.")
        print_pause("You look into the mirror and see that you have been "
                    "transformed into a giant beautiful maiden.", 3)
        print_pause("You have long flowing hair and a snakes body.", 3)
    elif "Gorgon" in you:
        if "Gorgon Medusa" == you:
            print_pause("Queen of the Gorgons and holder of divine eyes.")
            print_pause("You are the only of your siblings who will perish. "
                        "Your sisters will live forever.", 4)
        else:
            print_pause("Holder of divine eyes.  You will live forever.")
        print_pause("You will be end of a many a mortal.", 3)
    elif "Siren" == you:
        print_pause("Singer of divine song and daughters of earth.")
        print_pause("You will be captive to the sea.")
        print_pause("You can choose to lure sailors to their deaths "
                    "or help them find their way home.", 4)
        print_pause("You look into the mirror and see a beautiful winged "
                    "woman.", 3)
    elif "Harpy" == you:
        print_pause("Queen of the wind and guardian of souls.")
        print_pause("You will be carry the souls of the departed to Hades.", 3)
        print_pause("Or take evil doers to the Furies for the their just "
                    "punishments.", 3)
        print_pause("You look into the mirror and see the face of a beautiful "
                    "woman with the body of raptor.", 4)
        print_pause("You have long talons on your feet and claws for "
                    "hands.", 3)
    else:
        print_pause("King of all Hounds and guardian of Hades.")
        print_pause("You will guard the gates of Hades to prevent the dead "
                    "from leaving and \n"
                    "stop any human from entering.", 4)
        print_pause("You look into the mirror and see a giant hound with "
                    "three heads and a serpent for a tail.", 3)
    print_pause("In your new form, you feel immensely strong and powerful!")
    momentous()


def momentous():
    print_pause("You must choose how to use your new powers. Do you choose "
                "to be a good monster or a bad monster.")
    alignment = input("Please type GOOD or BAD!\n").lower()
    if alignment == "good":
        good()
    elif alignment == "bad":
        bad()
    else:
        apology("GOOD", "BAD")
        momentous()


def good():
    print_pause("You help the people of Greece and become a benevolent "
                "legend.", 3)
    print_pause("You live out your fate for what seems like a long but "
                "indeterminate amount of time.", 3)
    atrapos()


def bad():
    print_pause("You live to rain destruction and torment upon the "
                "Greek people.", 3)
    print_pause("You live out your fate and become a myth of caution and "
                "fear for all time.", 3)
    atrapos()


def atrapos():
    print_pause("One day a beautiful woman is standing in front of you.", 3)
    print_pause("She says her name is Atrapos.")
    print_pause("She smiles at you and tells you the time has come to return "
                "to the island.", 3)
    print_pause("Atropos has cut your thread of life. Your ADVENTURE is at "
                "an end.", 3)
    print_pause("GAME OVER!", 1)
    play_again()


def main():
    intro()


if __name__ == '__main__':
    main()

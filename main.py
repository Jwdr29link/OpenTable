#This is a simple program for use to find the atomic number and mass number + other useful information
# Created for use in the Skinner's school as it directly uses the information from the issued planner and also https://www.rsc.org/periodic-table

# Imports -

import random
import time
import os

# OBI -

import config1

# Sub routines -


def Logo():
    print(
        "░█████╗░██████╗░███████╗███╗░░██╗  ████████╗░█████╗░██████╗░██╗░░░░░███████╗"
    )
    print(
        "██╔══██╗██╔══██╗██╔════╝████╗░██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝"
    )
    print(
        "██║░░██║██████╔╝█████╗░░██╔██╗██║  ░░░██║░░░███████║██████╦╝██║░░░░░█████╗░░"
    )
    print(
        "██║░░██║██╔═══╝░██╔══╝░░██║╚████║  ░░░██║░░░██╔══██║██╔══██╗██║░░░░░██╔══╝░░"
    )
    print(
        "╚█████╔╝██║░░░░░███████╗██║░╚███║  ░░░██║░░░██║░░██║██████╦╝███████╗███████╗"
    )
    print(
        "░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚══╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝"
    )
    # Random Subtext
    RandList = [
        "The name's Bond, ionic Bond!",
        "Lose an electron? Gotta keep an ion it!",
        "I use chemistry puns, but only periodically...",
        "Is this a bonding exercise?",
        "Don’t trust atoms, they make up everything!",
        "Keep your ion the prize",
        "I’d tell you another chemistry pun. Unfortunately, all the good ones argon.",
    ]
    RanIt = random.choice(RandList)
    print(RanIt)


def Help():
    print(
        "Open table is intended to be used as a database containing all of the information which you would need to work out simple chemical equations."
    )
    print("")
    print(
        "To find an element you can input 3 different things, the symbol, the name or the element number -"
    )
    print("e.g. 'H' 'Hydrogen' '1'")
    print("")
    time.sleep(1)
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def License():
    try:
        print(
            "Copyright 2022 Jake Reddy, Oliver Wye, Federico Sonino, Milo Macmillan-Bashir, Monty Lyons, Timi Harte and Alexander Gallagher"
        )
        print("OBI - Copyright Jake Reddy 2022 ")
        print("")
        print("Licensed under the MIT License (the 'License')")
        print(
            "you may not use this file except in compliance with the License.")
        print(
            "You can obtain a copy of the License at - https://opensource.org/licenses/MIT and in the license.md file"
        )
        print("")
        print("By pressing enter you agree to the license")
        print("")
        print(
            "Extra information taken from - https://www.rsc.org/periodic-table"
        )
        print("")
        time.sleep(0.09)
        input("Press enter to start ->")
        os.system('clear')
        MainMenu()
    except:
        os.system('clear')
        Error()


def MainMenu():
    os.system('clear')
    Logo()
    print("")
    try:
        MainMenuInstructions = "Input the name or symbol of your selected element (type 'help' for assistance) - \n\
   \n>"

        UserChoice = input(MainMenuInstructions)
        #Elements Doe
        if UserChoice == "0":
            os.system('clear')
            MainMenu()
        # OBI
        elif UserChoice.lower() == "obi":
            os.system("clear")
            OBI()
        elif UserChoice.lower() == "obiconf1":
            exec(config1.py)
        elif UserChoice.lower() == "end":
            os.system('clear')
            quit()
        elif UserChoice.lower() == "help":
            os.system('clear')
            Help()
        #Hydrogen
        elif UserChoice.lower() == "hydrogen":
            os.system('clear')
            Hydrogen()
        elif UserChoice.lower() == "h":
            os.system('clear')
            Hydrogen()
        elif UserChoice == "1":
            os.system('clear')
            Hydrogen()
        #Helium
        elif UserChoice.lower() == "helium":
            os.system('clear')
            Helium()
        elif UserChoice.lower() == "he":
            os.system('clear')
            Helium()
        elif UserChoice == "2":
            os.system('clear')
        #Lithium
        elif UserChoice.lower() == "lithium":
            os.system('clear')
            Lithium()
        elif UserChoice.lower() == "li":
            os.system('clear')
            Lithium()
        elif UserChoice == "3":
            os.system('clear')
            Lithium()
        #Beryllium
        elif UserChoice == "beryllium":
            os.system('clear')
            Beryllium()
        elif UserChoice.lower() == "be":
            os.system('clear')
            Beryllium()
        elif UserChoice == "4":
            os.system('clear')
            Beryllium()
        #Boron
        elif UserChoice.lower() == "boron":
            os.system('clear')
            Boron()
        elif UserChoice.lower() == "b":
            os.system('clear')
            Boron()
        elif UserChoice == "5":
            os.system('clear')
            Boron()
        #Carbon
        elif UserChoice.lower() == "carbon":
            os.system('clear')
            Carbon()
        elif UserChoice.lower() == "c":
            os.system('clear')
            Carbon()
        elif UserChoice == "6":
            os.system('clear')
            Carbon()
        #Nitrogen
        elif UserChoice.lower() == "nitrogen":
            os.system('clear')
            Nitrogen()
        elif UserChoice.lower() == "n":
            os.system('clear')
            Nitrogen()
        elif UserChoice.lower() == "7":
            os.system('clear')
            Nitrogen()
        #Oxygen
        elif UserChoice.lower() == "oxygen":
            os.system('clear')
            Oxygen()
        elif UserChoice.lower() == "o":
            os.system('clear')
            Oxygen()
        elif UserChoice.lower() == "8":
            os.system('clear')
            Oxygen()
        #Fluorine
        elif UserChoice.lower() == "fluorine":
            os.system('clear')
            Fluorine()
        elif UserChoice.lower() == "f":
            os.system('clear')
            Fluorine()
        elif UserChoice.lower() == "9":
            os.system('clear')
            Fluorine()
        #Neon
        elif UserChoice.lower() == "neon":
            os.system('clear')
            Neon()
        elif UserChoice.lower() == "ne":
            os.system('clear')
            Neon()
        elif UserChoice.lower() == "10":
            os.system('clear')
            Neon()
        #Sodium
        elif UserChoice.lower() == "sodium":
            os.system('clear')
            Sodium()
        elif UserChoice.lower() == "na":
            os.system('clear')
            Sodium()
        elif UserChoice.lower() == "11":
            os.system('clear')
            Sodium()
        #Magnesium
        elif UserChoice.lower() == "magnesium":
            os.system('clear')
            Magnesium()
        elif UserChoice.lower() == "mg":
            os.system('clear')
            Magnesium()
        elif UserChoice.lower() == "12":
            os.system('clear')
            Magnesium()
        #Aluminium
        elif UserChoice.lower() == "aluminium":
            os.system('clear')
            Aluminium()
        elif UserChoice.lower() == "al":
            os.system('clear')
            Aluminium()
        elif UserChoice.lower() == "13":
            os.system('clear')
            Aluminium()
        #Silicon
        elif UserChoice.lower() == "silicon":
            os.system('clear')
            Silicon()
        elif UserChoice.lower() == "si":
            os.system('clear')
            Silicon()
        elif UserChoice.lower() == "14":
            os.system('clear')
            Silicon()
        #Phosphorus
        elif UserChoice.lower() == "phosphorus":
            os.system('clear')
            Phosphorus()
        elif UserChoice.lower() == "p":
            os.system('clear')
            Phosphorus()
        elif UserChoice.lower() == "15":
            os.system('clear')
            Phosphorus()
        #Sulfur
        elif UserChoice.lower() == "sulfur":
            os.system('clear')
            Sulfur()
        elif UserChoice.lower() == "s":
            os.system('clear')
            Sulfur()
        elif UserChoice.lower() == "16":
            os.system('clear')
            Sulfur()
        #Chlorine
        elif UserChoice.lower() == "chlorine":
            os.system('clear')
            Chlorine()
        elif UserChoice.lower() == "cl":
            os.system('clear')
            Chlorine()
        elif UserChoice.lower() == "17":
            os.system('clear')
            Chlorine()
        #Argon
        elif UserChoice.lower() == "argon":
            os.system('clear')
            Argon()
        elif UserChoice.lower() == "ar":
            os.system('clear')
            Argon()
        elif UserChoice.lower() == "18":
            os.system('clear')
            Argon()
        #Potassium
        elif UserChoice.lower() == "potassium":
            os.system('clear')
            Potassium()
        elif UserChoice.lower() == "k":
            os.system('clear')
            Potassium()
        elif UserChoice.lower() == "19":
            os.system('clear')
            Potassium()
        #Calcium
        elif UserChoice.lower() == "calcium":
            os.system('clear')
            Calcium()
        elif UserChoice.lower() == "ca":
            os.system('clear')
            Calcium()
        elif UserChoice.lower() == "20":
            os.system('clear')
            Calcium()
        #Scandium
        elif UserChoice.lower() == "scandium":
            os.system('clear')
            Scandium()
        elif UserChoice.lower() == "sc":
            os.system('clear')
            Scandium()
        elif UserChoice.lower() == "21":
            os.system('clear')
            Scandium()
        #Titanium
        elif UserChoice.lower() == "titanium":
            os.system('clear')
            Titanium()
        elif UserChoice.lower() == "ti":
            os.system('clear')
            Titanium()
        elif UserChoice.lower() == "22":
            os.system('clear')
            Titanium()
        #Vanadium
        elif UserChoice.lower() == "vanadium":
            os.system('clear')
            Vanadium()
        elif UserChoice.lower() == "v":
            os.system('clear')
            Vanadium()
        elif UserChoice.lower() == "23":
            os.system('clear')
            Vanadium()
        #Chromium
        elif UserChoice.lower() == "chromium":
            os.system('clear')
            Chromium()
        elif UserChoice.lower() == "cr":
            os.system('clear')
            Chromium()
        elif UserChoice.lower() == "24":
            os.system('clear')
            Chromium()
        #Manganese
        elif UserChoice.lower() == "manganese":
            os.system('clear')
            Manganese()
        elif UserChoice.lower() == "mn":
            os.system('clear')
            Manganese()
        elif UserChoice.lower() == "25":
            os.system('clear')
            Manganese()
        #Iron
        elif UserChoice.lower() == "iron":
            os.system('clear')
            Manganese()
        elif UserChoice.lower() == "mn":
            os.system('clear')
            Manganese()
        elif UserChoice.lower() == "25":
            os.system('clear')
            Manganese()
        #Cobalt
        elif UserChoice.lower() == "cobalt":
            os.system('clear')
            Cobalt()
        elif UserChoice.lower() == "co":
            os.system('clear')
            Cobalt()
        elif UserChoice.lower() == "27":
            os.system('clear')
            Cobalt()
        #Nickel
        elif UserChoice.lower() == "nickel":
            os.system('clear')
            Nickel()
        elif UserChoice.lower() == "ni":
            os.system('clear')
            Nickel()
        elif UserChoice.lower() == "28":
            os.system('clear')
            Nickel()
        #Copper
        elif UserChoice.lower() == "copper":
            os.system('clear')
            Copper()
        elif UserChoice.lower() == "cu":
            os.system('clear')
            Copper()
        elif UserChoice.lower() == "29":
            os.system('clear')
            Copper()
        #Zinc
        elif UserChoice.lower() == "zinc":
            os.system('clear')
            Zinc()
        elif UserChoice.lower() == "zn":
            os.system('clear')
            Zinc()
        elif UserChoice.lower() == "30":
            os.system('clear')
            Zinc()
        #Gallium
        elif UserChoice.lower() == "gallium":
            os.system('clear')
            Gallium()
        elif UserChoice.lower() == "ga":
            os.system('clear')
            Gallium()
        elif UserChoice.lower() == "31":
            os.system('clear')
            Gallium()
        #Germanium
        elif UserChoice.lower() == "germanium":
            os.system('clear')
            Germanium()
        elif UserChoice.lower() == "ga":
            os.system('clear')
            Germanium()
        elif UserChoice.lower() == "32":
            os.system('clear')
            Germanium()
        elif UserChoice.lower() == "arsenic":
            os.system('clear')
            Arsenic()
        elif UserChoice.lower() == "as":
            os.system('clear')
            Arsenic()
        elif UserChoice.lower() == "33":
            os.system('clear')
            Arsenic()
        elif UserChoice.lower() == "selenium":
            os.system('clear')
            Selenium()
        elif UserChoice.lower() == "se":
            os.system('clear')
            Selenium()
        elif UserChoice.lower() == "34":
            os.system('clear')
            Selenium()
        elif UserChoice.lower() == "bromine":
            os.system('clear')
            Bromine()
        elif UserChoice.lower() == "br":
            os.system('clear')
            Bromine()
        elif UserChoice.lower() == "35":
            os.system('clear')
            Bromine()
        elif UserChoice.lower() == "krypton":
            os.system('clear')
            Krypton()
        elif UserChoice.lower() == "kr":
            os.system('clear')
            Krypton()
        elif UserChoice.lower() == "36":
            os.system('clear')
            Krypton()
        elif UserChoice.lower() == "rubidium":
            os.system('clear')
            Rubidium()
        elif UserChoice.lower() == "Rb":
            os.system('clear')
            Rubidium()
        elif UserChoice.lower() == "37":
            os.system('clear')
            Rubidium()
        elif UserChoice.lower() == "strontium":
            os.system('clear')
            Strontium()
        elif UserChoice.lower() == "sr":
            os.system('clear')
            Strontium()
        elif UserChoice.lower() == "38":
            os.system('clear')
            Strontium()
        elif UserChoice.lower() == "yttrium":
            os.system('clear')
            Yttrium()
        elif UserChoice.lower() == "y":
            os.system('clear')
            Yttrium()
        elif UserChoice.lower() == "39":
            os.system('clear')
            Yttrium()
        elif UserChoice.lower() == "zirconium":
            os.system('clear')
            Zirconium()
        elif UserChoice.lower() == "zr":
            os.system('clear')
            Zirconium()
        elif UserChoice.lower() == "40":
            os.system('clear')
            Zirconium()
        elif UserChoice.lower() == "niobium":
            os.system('clear')
            Niobium()
        elif UserChoice.lower() == "nb":
            os.system('clear')
            Niobium()
        elif UserChoice.lower() == "41":
            os.system('clear')
            Niobium()
        elif UserChoice.lower() == "molybdenum":
            os.system('clear')
            Molybdenum()
        elif UserChoice.lower() == "mo":
            os.system('clear')
            Molybdenum()
        elif UserChoice.lower() == "42":
            os.system('clear')
            Molybdenum()
        elif UserChoice.lower() == "technetium":
            os.system('clear')
            Technetium()
        elif UserChoice.lower() == "te":
            os.system('clear')
            Technetium()
        elif UserChoice.lower() == "43":
            os.system('clear')
            Technetium()
        else:
            os.system('clear')
            Error()
    except:
        os.system('clear')
        Error()


def Error():
    print(
        "The inputed text has incorrect syntax (your input has not been recoginsied by the script )"
    )
    time.sleep(1)
    print("")
    input("Press enter to return to the main menu ->")
    MainMenu()


# Elements -


def Hydrogen():
    os.system('clear')
    print("H - Hydrogen - Element Number 1")
    print("Relative atomic mass - 1")
    print("Atomic (proton) number - 1")
    print("Discovered in 1766")
    print("Gas at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Helium():
    os.system('clear')
    print("He - Helium - Element number 2 ")
    print("Relative atomic mass - 4 (4.003) ")
    print("Atomic (proton) number - 2 ")
    print("Discovered in 1868")
    print("Gas at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Lithium():
    os.system('clear')
    print("Li - Lithium - Element Number 3 ")
    print("Relative atomic mass - 7 ")
    print("Atomic (proton) number - 3")
    print("Discovered in 1817")
    print("Solid at room temp")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Beryllium():
    os.system('clear')
    print("Be - Beryllium - Element number 4 ")
    print("Relative atomic mass - 9 ")
    print("Atomic (proton) number - 4 ")
    print("Discovered in 1798")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Boron():
    os.system('clear')
    print("B - Boron - Element number 5 ")
    print("Relative atomic mass - 11 ")
    print("Atomic (proton) number - 4 ")
    print("Discovered in 1808")
    print("solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Carbon():
    os.system('clear')
    print("C - Carbon - Element number 6 ")
    print("Relative atomic mass - 12 ")
    print("Atomic (proton) number - 6 ")
    print("Discovered in 3750 BCE")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Nitrogen():
    os.system('clear')
    print("N - Nitrogen - Element number 7 ")
    print("Relative atomic mass - 14 ")
    print("Atomic (proton) number - 7 ")
    print("Discovered in 1772")
    print("Gas at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Oxygen():
    os.system('clear')
    print("O - Oxygen - Element number 8 ")
    print("Relative atomic mass - 16 ")
    print("Atomic (proton) number - 8 ")
    print("Discovered in 1771")
    print("Gas at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Fluorine():
    os.system('clear')
    print("F - Fluorine - Element number 9 ")
    print("Relative atomic mass - 19 ")
    print("Atomic (proton) number - 9 ")
    print("Discovered in 1810")
    print("Gas at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Neon():
    os.system('clear')
    print("Ne - Neon - Element number 10 ")
    print("Relative atomic mass - 20 ")
    print("Atomic (proton) number - 10 ")
    print("Discovered in 1897")
    print("Gas at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Sodium():
    os.system('clear')
    print("Na - Sodium - Element number 11 ")
    print("Relative atomic mass - 23 ")
    print("Atomic (proton) number - 11 ")
    print("Discovered in 1807")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Magnesium():
    os.system('clear')
    print("Mg - Magnesium - Element number 12 ")
    print("Relative atomic mass - 24 ")
    print("Atomic (proton) number - 12 ")
    print("Discovered in 1755")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Aluminium():
    os.system('clear')
    print("Al - Aluminium - Element number 13 ")
    print("Relative atomic mass - 27 ")
    print("Atomic (proton) number - 13 ")
    print("Discovered in 1824")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Silicon():
    os.system('clear')
    print("Si - Silicon - Element number 14 ")
    print("Relative atomic mass - 28 ")
    print("Atomic (proton) number - 14 ")
    print("Discovered in 1824")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Phosphorus():
    os.system('clear')
    print("P - Phosphorus - Element number 2 ")
    print("Relative atomic mass - 31 ")
    print("Atomic (proton) number - 15 ")
    print("Discovered in 1669")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Sulfur():
    os.system('clear')
    print("S - Sulfur - Element number 16 ")
    print("Relative atomic mass - 32 ")
    print("Atomic (proton) number - 16 ")
    print("Discovered before 2000 BCE")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Chlorine():
    os.system('clear')
    print("Cl - Chlorine - Element number 17 ")
    print("Relative atomic mass - 35.5 ")
    print("Atomic (proton) number - 17 ")
    print("Discovered in 1774")
    print("Gas at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Argon():
    os.system('clear')
    print("Ar - Argon - Element number 18 ")
    print("Relative atomic mass - 40 ")
    print("Atomic (proton) number - 18 ")
    print("Discovered in 1894")
    print("Gas at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Potassium():
    os.system('clear')
    print("K - Potassium - Element number 19 ")
    print("Relative atomic mass - 39 ")
    print("Atomic (proton) number - 19 ")
    print("Discovered in 1807")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Calcium():
    os.system('clear')
    print("Ca - Calcium - Element number 20 ")
    print("Relative atomic mass - 40 ")
    print("Atomic (proton) number - 20 ")
    print("Discovered in 1808")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Scandium():
    os.system('clear')
    print("Sc - Scandium - Element number 21 ")
    print("Relative atomic mass - 45 ")
    print("Atomic (proton) number - 21 ")
    print("Discovered in 1879")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Titanium():
    os.system('clear')
    print("Ti - Titanium - Element number 22 ")
    print("Relative atomic mass - 48 ")
    print("Atomic (proton) number - 22 ")
    print("Discovered in 1791")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Vanadium():
    os.system('clear')
    print("V - Vanadium - Element number 23 ")
    print("Relative atomic mass - 51 ")
    print("Atomic (proton) number - 23 ")
    print("Discovered in 1801")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Chromium():
    os.system('clear')
    print("Cr - Chromium - Element number 24 ")
    print("Relative atomic mass - 52 ")
    print("Atomic (proton) number - 24 ")
    print("Discovered in 1798")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Manganese():
    os.system('clear')
    print("Mn - Manganese - Element number 25 ")
    print("Relative atomic mass - 55 ")
    print("Atomic (proton) number - 25 ")
    print("Discovered in 1774")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Iron():
    os.system('clear')
    print("Fe - Iron - Element number 26 ")
    print("Relative atomic mass - 56 ")
    print("Atomic (proton) number - 26 ")
    print("Discovered approximately in 3500BC")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Cobalt():
    os.system('clear')
    print("Co - Cobalt - Element number 27 ")
    print("Relative atomic mass - 59 ")
    print("Atomic (proton) number - 27 ")
    print("Discovered in 1739")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Nickel():
    os.system('clear')
    print("Ni - Nickel - Element number 28 ")
    print("Relative atomic mass - 59 ")
    print("Atomic (proton) number - 28 ")
    print("Discovered in 1739")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Copper():
    os.system('clear')
    print("Cu - Copper - Element number 29 ")
    print("Relative atomic mass - 63.5 ")
    print("Atomic (proton) number - 29 ")
    print("Discovered in 9000 BC")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Zinc():
    os.system('clear')
    print("Zn - Zinc - Element number 30 ")
    print("Relative atomic mass - 65 ")
    print("Atomic (proton) number - 30 ")
    print("Discovered in 1746")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Gallium():
    os.system('clear')
    print("Ga - Gallium - Element number 31 ")
    print("Relative atomic mass - 70 ")
    print("Atomic (proton) number - 31 ")
    print("Discovered in 1875")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Germanium():
    os.system('clear')
    print("Ge - Germanium - Element number 32 ")
    print("Relative atomic mass - 73 ")
    print("Atomic (proton) number - 32 ")
    print("Discovered in 1886")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Arsenic():
    os.system('clear')
    print("As - Arsenic - Element number 33 ")
    print("Relative atomic mass - 75 ")
    print("Atomic (proton) number - 33 ")
    print("Discovered approximately 1250")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Selenium():
    os.system('clear')
    print("Se - Selenium - Element number 34 ")
    print("Relative atomic mass - 79 ")
    print("Atomic (proton) number - 34 ")
    print("Discovered in 1817")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Bromine():
    os.system('clear')
    print("Br - Bromine - Element number 35 ")
    print("Relative atomic mass - 80 ")
    print("Atomic (proton) number - 35 ")
    print("Discovered in 1826")
    print("Liquid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Krypton():
    os.system('clear')
    print("Kr - Krypton - Element number 36 ")
    print("Relative atomic mass - 84 ")
    print("Atomic (proton) number - 36 ")
    print("Discovered in 1898")
    print("Gas at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Rubidium():
    os.system('clear')
    print("Rb - Rubidium - Element number 37 ")
    print("Relative atomic mass - 85 ")
    print("Atomic (proton) number - 37 ")
    print("Discovered in 1861")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Strontium():
    os.system('clear')
    print("Sr - Strontium - Element number 38 ")
    print("Relative atomic mass - 88 ")
    print("Atomic (proton) number - 38 ")
    print("Discovered in 1790")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Yttrium():
    os.system('clear')
    print("Y - Yttrium - Element number 39 ")
    print("Relative atomic mass - 89 ")
    print("Atomic (proton) number - 39 ")
    print("Discovered in 1794")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Zirconium():
    os.system('clear')
    print("Zr - Zirconium - Element number 40 ")
    print("Relative atomic mass - 91 ")
    print("Atomic (proton) number - 40 ")
    print("Discovered in 1789")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Niobium():
    os.system('clear')
    print("Nb - Niobium - Element number 41 ")
    print("Relative atomic mass - 93 ")
    print("Atomic (proton) number - 41 ")
    print("Discovered in 1801")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Molybdenum():
    os.system('clear')
    print("Mo - Molybdenum - Element number 42 ")
    print("Relative atomic mass - 96 ")
    print("Atomic (proton) number - 42 ")
    print("Discovered in 1778")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Technetium():
    os.system('clear')
    print("Tc - Technetium - Element number 43 ")
    print("Relative atomic mass - 98 ")
    print("Atomic (proton) number - 43 ")
    print("Discovered in 1937")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Ruthenium():
    os.system('clear')
    print("Ru - Ruthenium - Element number 44 ")
    print("Relative atomic mass - 101 ")
    print("Atomic (proton) number - 44 ")
    print("Discovered in 1844")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Rhodium():
    os.system('clear')
    print("Rh - Rhodium - Element number 45 ")
    print("Relative atomic mass - 103 ")
    print("Atomic (proton) number - 45 ")
    print("Discovered in 1803")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Palladium():
    os.system('clear')
    print("Pd - Palladium - Element number 46 ")
    print("Relative atomic mass - 106 ")
    print("Atomic (proton) number - 46 ")
    print("Discovered in 1803")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Silver():
    os.system('clear')
    print("Ag - Silver - Element number 47 ")
    print("Relative atomic mass - 108 ")
    print("Atomic (proton) number - 47 ")
    print("Discovered around 3000 BC")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Cadmium():
    os.system('clear')
    print("Cd - Cadmium - Element number 48 ")
    print("Relative atomic mass - 112 ")
    print("Atomic (proton) number - 48 ")
    print("Discovered in 1817")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Indium():
    os.system('clear')
    print("In - Indium - Element number 49 ")
    print("Relative atomic mass - 115 ")
    print("Atomic (proton) number - 49 ")
    print("Discovered in 1863")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Tin():
    os.system('clear')
    print("Sn - Tin - Element number 50 ")
    print("Relative atomic mass - 119 ")
    print("Atomic (proton) number - 50 ")
    print("Discovered in 1810")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Antimony():
    os.system('clear')
    print("Sb - Antimony - Element number 51 ")
    print("Relative atomic mass - 122 ")
    print("Atomic (proton) number - 51 ")
    print("Discovered around 3000 BC")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Tellurium():
    os.system('clear')
    print("Te - Tellurium - Element number 52 ")
    print("Relative atomic mass - 128 ")
    print("Atomic (proton) number - 52 ")
    print("Discovered in 1782")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Iodine():
    os.system('clear')
    print("I - Iodine - Element number 53 ")
    print("Relative atomic mass - 127 ")
    print("Atomic (proton) number - 53 ")
    print("Discovered in 1811")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Xenon():
    os.system('clear')
    print("Xe - Xenon - Element number 54 ")
    print("Relative atomic mass - 131 ")
    print("Atomic (proton) number - 54 ")
    print("Discovered in 1898")
    print("Gas at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Caesium():
    os.system('clear')
    print("Cs - Caesium - Element number 55 ")
    print("Relative atomic mass - 133 ")
    print("Atomic (proton) number - 55 ")
    print("Discovered in 1860")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Barium():
    os.system('clear')
    print("Ba - Barium - Element number 56 ")
    print("Relative atomic mass - 137 ")
    print("Atomic (proton) number - 56 ")
    print("Discovered in 1808")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Lanthanum():
    os.system('clear')
    print("La - Lanthanum - Element number 57 ")
    print("Relative atomic mass - 139 ")
    print("Atomic (proton) number - 57 ")
    print("Discovered in 1839")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Cerium():
    os.system('clear')
    print("Ce - Cerium - Element number 58 ")
    print("Relative atomic mass - 140 ")
    print("Atomic (proton) number - 58 ")
    print("Discovered in 1803")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Praseodymium():
    os.system('clear')
    print("Pr - Praseodymium - Element number 59 ")
    print("Relative atomic mass - 141 ")
    print("Atomic (proton) number - 59 ")
    print("Discovered in 1885")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Neodymium():
    os.system('clear')
    print("Nd - Neodymium - Element number 60 ")
    print("Relative atomic mass - 144 ")
    print("Atomic (proton) number - 60 ")
    print("Discovered in 1885")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Promethium():
    os.system('clear')
    print("Pm - Promethium - Element number 61 ")
    print("Relative atomic mass - 145 ")
    print("Atomic (proton) number - 61 ")
    print("Discovered in 1945")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Samarium():
    os.system('clear')
    print("Sm - Samarium - Element number 62 ")
    print("Relative atomic mass - 150 ")
    print("Atomic (proton) number - 62 ")
    print("Discovered in 1879")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Europium():
    os.system('clear')
    print("Eu - Europium - Element number 63 ")
    print("Relative atomic mass - 152 ")
    print("Atomic (proton) number - 63 ")
    print("Discovered in 1901")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Gadolinium():
    os.system('clear')
    print("Gd - gadolinium - Element number 64 ")
    print("Relative atomic mass - 157 ")
    print("Atomic (proton) number - 64 ")
    print("Discovered in 1880")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Terbium():
    os.system('clear')
    print("Tb - Terbium - Element number 65 ")
    print("Relative atomic mass - 159 ")
    print("Atomic (proton) number - 65 ")
    print("Discovered in 1843")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Dysprosium():
    os.system('clear')
    print("Dy - Dysprosium - Element number 66 ")
    print("Relative atomic mass - 163 ")
    print("Atomic (proton) number - 66 ")
    print("Discovered in 1886")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Holmium():
    os.system('clear')
    print("Ho - Dysprosium - Element number 67 ")
    print("Relative atomic mass - 165 ")
    print("Atomic (proton) number - 67 ")
    print("Discovered in 1878")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Erbium():
    os.system('clear')
    print("Er - Erbium - Element number 68 ")
    print("Relative atomic mass - 167 ")
    print("Atomic (proton) number - 68 ")
    print("Discovered in 1843")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Thulium():
    os.system('clear')
    print("Tm - Dysprosium - Element number 69 ")
    print("Relative atomic mass - 169 ")
    print("Atomic (proton) number - 69 ")
    print("Discovered in 1879")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Ytterbium():
    os.system('clear')
    print("Yb - Dysprosium - Element number 70 ")
    print("Relative atomic mass - 173 ")
    print("Atomic (proton) number - 70 ")
    print("Discovered in 1878")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Lutetium():
    os.system('clear')
    print("Lu - Dysprosium - Element number 71 ")
    print("Relative atomic mass - 175 ")
    print("Atomic (proton) number - 71 ")
    print("Discovered in 1907")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Hafnium():
    os.system('clear')
    print("Hf - Dysprosium - Element number 72 ")
    print("Relative atomic mass - 178 ")
    print("Atomic (proton) number - 72 ")
    print("Discovered in 1923")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Tantalum():
    os.system('clear')
    print("Ta - Tantalum - Element number 73 ")
    print("Relative atomic mass - 181 ")
    print("Atomic (proton) number - 73 ")
    print("Discovered in 1802")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Tungsten():
    os.system('clear')
    print("W - Tungsten - Element number 74 ")
    print("Relative atomic mass - 184 ")
    print("Atomic (proton) number - 74 ")
    print("Discovered in 1783")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Rhenium():
    os.system('clear')
    print("Re - Rhenium - Element number 75 ")
    print("Relative atomic mass - 186 ")
    print("Atomic (proton) number - 75 ")
    print("Discovered in 1925")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Osmium():
    os.system('clear')
    print("Os - Rhenium - Element number 76 ")
    print("Relative atomic mass - 190 ")
    print("Atomic (proton) number - 76 ")
    print("Discovered in 1803")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Iridium():
    os.system('clear')
    print("Ir - Rhenium - Element number 77 ")
    print("Relative atomic mass - 192 ")
    print("Atomic (proton) number - 77 ")
    print("Discovered in 1803")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Platinum():
    os.system('clear')
    print("Pt - Rhenium - Element number 78 ")
    print("Relative atomic mass - 195 ")
    print("Atomic (proton) number - 78 ")
    print("Discovered in 1742")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Gold():
    os.system('clear')
    print("Au - Gold - Element number 79 ")
    print("Relative atomic mass - 197 ")
    print("Atomic (proton) number - 79 ")
    print("Discovered around 3000 BC")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Mercury():
    os.system('clear')
    print("Hg - Mercury - Element number 80 ")
    print("Relative atomic mass - 201 ")
    print("Atomic (proton) number - 80 ")
    print("Discovered around 1500 BC")
    print("Liquid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Thallium():
    os.system('clear')
    print("Tl - Thallium - Element number 81 ")
    print("Relative atomic mass - 204 ")
    print("Atomic (proton) number - 81 ")
    print("Discovered in 1861")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Lead():
    os.system('clear')
    print("Pb - Lead - Element number 82 ")
    print("Relative atomic mass - 207 ")
    print("Atomic (proton) number - 82 ")
    print("Discovered around 7000 BC")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Bismuth():
    os.system('clear')
    print("Bi - Bismuth - Element number 83 ")
    print("Relative atomic mass - 209 ")
    print("Atomic (proton) number - 83 ")
    print("Discovered in 1753")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Polonium():
    os.system('clear')
    print("Po - Polonium - Element number 84 ")
    print("Relative atomic mass - 209 ")
    print("Atomic (proton) number - 84 ")
    print("Discovered in 1898")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Astatine():
    os.system('clear')
    print("At - Astatine - Element number 85 ")
    print("Relative atomic mass - 210 ")
    print("Atomic (proton) number - 85 ")
    print("Discovered in 1940")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Radon():
    os.system('clear')
    print("Rn - Radon - Element number 86 ")
    print("Relative atomic mass - 222 ")
    print("Atomic (proton) number - 86 ")
    print("Discovered in 1900")
    print("Gas at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Francium():
    os.system('clear')
    print("Fr - Francium - Element number 87 ")
    print("Relative atomic mass - 223 ")
    print("Atomic (proton) number - 87 ")
    print("Discovered in 1939")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Radium():
    os.system('clear')
    print("Ra - Radium - Element number 88 ")
    print("Relative atomic mass - 226 ")
    print("Atomic (proton) number - 88 ")
    print("Discovered in 1898")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Actinium():
    os.system('clear')
    print("Ac - Actinium - Element number 89 ")
    print("Relative atomic mass - 227 ")
    print("Atomic (proton) number - 89 ")
    print("Discovered in 1899")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Thorium():
    os.system('clear')
    print("Th - Thorium - Element number 90 ")
    print("Relative atomic mass - 232 ")
    print("Atomic (proton) number - 90 ")
    print("Discovered in 1829")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Protactinium():
    os.system('clear')
    print("Pa - Protactinium - Element number 91 ")
    print("Relative atomic mass - 231 ")
    print("Atomic (proton) number - 91 ")
    print("Discovered in 1913")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Uranium():
    os.system('clear')
    print("U - Uranium - Element number 92 ")
    print("Relative atomic mass - 238 ")
    print("Atomic (proton) number - 92 ")
    print("Discovered in 1789")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Neptunium():
    os.system('clear')
    print("Np - Neptunium - Element number 93 ")
    print("Relative atomic mass - 237 ")
    print("Atomic (proton) number - 93 ")
    print("Discovered in 1940")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Plutonium():
    os.system('clear')
    print("Pu - Plutonium - Element number 94 ")
    print("Relative atomic mass - 244 ")
    print("Atomic (proton) number - 94 ")
    print("Discovered in 1940")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Americium():
    os.system('clear')
    print("Am - Americium - Element number 95 ")
    print("Relative atomic mass - 243 ")
    print("Atomic (proton) number - 95 ")
    print("Discovered in 1944")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Curium():
    os.system('clear')
    print("Cm - Curium - Element number 96 ")
    print("Relative atomic mass - 247 ")
    print("Atomic (proton) number - 96 ")
    print("Discovered in 1944")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Berkelium():
    os.system('clear')
    print("Bk - Berkelium - Element number 97 ")
    print("Relative atomic mass - 247 ")
    print("Atomic (proton) number - 97 ")
    print("Discovered in 1949")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Californium():
    os.system('clear')
    print("Cf - Californium - Element number 98 ")
    print("Relative atomic mass - 251 ")
    print("Atomic (proton) number - 98 ")
    print("Discovered in 1950")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Einsteinium():
    os.system('clear')
    print("Es - Americium - Element number 99 ")
    print("Relative atomic mass - 252 ")
    print("Atomic (proton) number - 99 ")
    print("Discovered in 1952")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Fermium():
    os.system('clear')
    print("Fm - Fermium - Element number 100 ")
    print("Relative atomic mass - 257 ")
    print("Atomic (proton) number - 100 ")
    print("Discovered in 1953")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Mendelevium():
    os.system('clear')
    print("Md - Mendelevium - Element number 101 ")
    print("Relative atomic mass - 258 ")
    print("Atomic (proton) number - 101 ")
    print("Discovered in 1955")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Nobelium():
    os.system('clear')
    print("No - Nobelium - Element number 102 ")
    print("Relative atomic mass - 257 ")
    print("Atomic (proton) number - 102 ")
    print("Discovered in 1963")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Lawrencium():
    os.system('clear')
    print("Lr - Lawrencium - Element number 103 ")
    print("Relative atomic mass - 262 ")
    print("Atomic (proton) number - 103 ")
    print("Discovered in 1965")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Rutherfordium():
    os.system('clear')
    print("Rf - Rutherfordium - Element number 104 ")
    print("Relative atomic mass - 267 ")
    print("Atomic (proton) number - 104 ")
    print("Discovered in 1964")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Dubnium():
    os.system('clear')
    print("Db - Dubnium - Element number 105 ")
    print("Relative atomic mass - 268 ")
    print("Atomic (proton) number - 105 ")
    print("Discovered from 1968-1970")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Seaborgium():
    os.system('clear')
    print("Sg - Seaborgium - Element number 106 ")
    print("Relative atomic mass - 269 ")
    print("Atomic (proton) number - 106 ")
    print("Discovered in 1974")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Bohrium():
    os.system('clear')
    print("Bh - Bohrium - Element number 107 ")
    print("Relative atomic mass - 270 ")
    print("Atomic (proton) number - 107 ")
    print("Discovered in 1981")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Hassium():
    os.system('clear')
    print("Hs - Hassium - Element number 108 ")
    print("Relative atomic mass - 269 ")
    print("Atomic (proton) number - 108 ")
    print("Discovered in 1984")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Meitnerium():
    os.system('clear')
    print("Mt - Meitnerium - Element number 109 ")
    print("Relative atomic mass - 278 ")
    print("Atomic (proton) number - 109 ")
    print("Discovered in 1982")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Darmstadtium():
    os.system('clear')
    print("Ds - Darmstadtium - Element number 110 ")
    print("Relative atomic mass - 281 ")
    print("Atomic (proton) number - 110 ")
    print("Discovered in 1994")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Roentgenium():
    os.system('clear')
    print("Rg - Roentgenium - Element number 111 ")
    print("Relative atomic mass - 280 ")
    print("Atomic (proton) number - 111 ")
    print("Discovered in 1994")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Copenicium():
    os.system('clear')
    print("Cn - Copernicium - Element number 112 ")
    print("Relative atomic mass - 285 ")
    print("Atomic (proton) number - 112 ")
    print("Discovered in 1996")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Nihonium():
    os.system('clear')
    print("Nh - Nihonium - Element number 113 ")
    print("Relative atomic mass - 286 ")
    print("Atomic (proton) number - 113 ")
    print("Discovered in 2004")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Flerovium():
    os.system('clear')
    print("Fl - Flerovium - Element number 114 ")
    print("Relative atomic mass - 289 ")
    print("Atomic (proton) number - 114 ")
    print("Discovered in 1999")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Moscovium():
    os.system('clear')
    print("Mc - Moscovium - Element number 115 ")
    print("Relative atomic mass - 289 ")
    print("Atomic (proton) number - 115 ")
    print("Discovered in 2010")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Livermorium():
    os.system('clear')
    print("Lv - Livermorium - Element number 116 ")
    print("Relative atomic mass - 293 ")
    print("Atomic (proton) number - 116 ")
    print("Discovered in 2000")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Tennessine():
    os.system('clear')
    print("Ts - Tennessine - Element number 117 ")
    print("Relative atomic mass - 294 ")
    print("Atomic (proton) number - 117 ")
    print("Discovered in 2010")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Oganesson():
    os.system('clear')
    print("Og - Oganesson - Element number 118 ")
    print("Relative atomic mass - 294 ")
    print("Atomic (proton) number - 118 ")
    print("Discovered in 2006")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


def Obamium():
    os.system('clear')
    print("Ob - Obamium - Element number 312 ")
    print("Relative atomic mass - 926 ")
    print("Atomic (proton) number - 312 ")
    print("Discovered in 2019")
    print("Solid at room temperature")
    print("")
    input("Press enter to return to the main menu ->")
    os.system('clear')
    MainMenu()


# OBI -

# OBSIDIAN (or OBI) is the native Third party module system for
# OBI v0.0.2


def OBI():
    UserChoice = input(MenuOneInstructions)
    if UserChoice == "1":
        os.system('clear')
        print("Creating a config file!")
        f = open("config1.py", "w+")
        f.close
        OBI()
    elif UserChoice == "2":
        os.system('clear')
        print("Creating a config file!")
        f = open("config3.py", "w+")
        f.close
        OBI()
    elif UserChoice == "3":
        os.system('clear')
        print("Creating a config file!")
        f = open("config4.py", "w+")
        f.close
        OBI()
    elif UserChoice == "4":
        os.system('clear')
        print("Creating a config file!")
        f = open("config2.py", "w+")
        f.close
        OBI()
    elif UserChoice == "5":
        os.system('clear')
        print("Creating a config file!")
        f = open("config5.py", "w+")
        f.close
        OBI()
    elif UserChoice == "6":
        os.system('clear')
        MainMenu()
    else:
        ErrorOBI()


MenuOneInstructions = "Select one of the following Obsidian options (1-6)\n\
1 - Create config file num 1\n\
2 - Create config file num 2\n\
3 - Create config file num 3\n\
4 - Create config file num 4\n\
5 - Create config file num 5\n\
6 - Return to Main Menu\n\
\n"


def ErrorOBI():
    os.system('clear')
    print(
        "The inputed text has incorrect syntax (your input has not been recoginsied by the Obsidian ) or a conifuration file has been created"
    )
    time.sleep(1)
    print("")
    input("Press enter to return to OBI ->")
    os.system('clear')
    OBI()


# Sequence -

try:
 os.system('clear')
 License()
except:
 os.system('clear')
 Error()

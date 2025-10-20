import sys
from formula import *





def main():
    weapon = {}
    target = {}
    print("Welcome to Mathhammer! Please input weapon and target statistics as requested.")
    weapon["to_hit"] = input("Enter weapon hit value: ")
    weapon["to_wound"] = input("Enter weapon wound value: ")
    weapon["pierce"] = input("Enter weapon ap value: ")
    target["save"] = input("Enter target save value: ")
    target["invuln"] = input("Enter target invulnerable save value (0 if no invuln): ")
    target["feel_no_pain"] = input("Enter target feel no pain value (0 if no fnp): ")
    weapon["attacks"] = input("Enter weapon attacks value: ")
    weapon["damage"] = input("Enter weapon damage value: ")
    weapon["keywords"] = input("Enter weapon keywords.  If multiple keywords seperate by comma: ")
    if "Sustained Hits" in weapon["keywords"]:
        weapon["sustained_hits"] = input("Enter sustained hits value: ")
    rerolls = input("Enter any rerolls (None, Reroll Hits 1, Reroll Hits, Reroll Hits Reroll Wounds): ")
    print("Calculating average wounds dealt...")
    result = math(weapon, target, rerolls)
    print(f"{result} wounds dealt")

if __name__ == "__main__":
        main()
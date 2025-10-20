from constants import *

weapon = {}
target = {}

def math(weapon, target, rerolls):
    h = int(weapon["to_hit"])
    w = int(weapon["to_wound"])
    ap = int(weapon["pierce"])
    s = int(target["save"])
    invln = int(target["invuln"])
    if invln != 0:
        if s + ap >= invln:
            s = invln
            ap = 0 
    fnp = int(target["feel_no_pain"])
    a = int(weapon["attacks"])
    d = int(weapon["damage"])
    sh = 0
    lh = 1
    dw = 1
    if "Sustained Hits" in weapon["keywords"]:
        sh = int(weapon["sustained_hits"])
        a = a * sht[sh]
    if "Lethal Hits" in weapon["keywords"]:
        match w:
            case 2:
            case 3:
            case 4:
            case 5:
            case 6:
    if "Devastating Wounds" in weapon["keywords"]:
        match s:
            case 2:
            case 3:
            case 4:
            case 5:
            case 6:
        
    match rerolls:
        case "None":
            print(f"{(hw[h - 2][w - 2]) * (a * lh * ((sht[sh] - 1) / 2) + 1)} * {((aps[ap][s - 2]) * (a * dw))}  * {d} {rerolls}")
            return (hw[h - 2][w - 2]) * (a * lh * ((sht[sh] - 1) / 2) + 1) * ((aps[ap][s - 2]) * (dw * a))  * d * fnpt[fnp]
        case "Reroll Hits 1":
            print(f"{(hwr1[h - 2][w - 2]) * (a * lh * ((sht[sh] - 1) / 2) + 1)} * {((aps[ap][s - 2]) * (a * dw))}  * {d} {rerolls}")
            return (hwr1[h - 2][w - 2]) * (a * lh * ((sht[sh] - 1) / 2) + 1) * ((aps[ap][s - 2]) * (dw * a))  * d * fnpt[fnp]
        case "Reroll Hits":
            print(f"{(hwrh[h - 2][w - 2]) * (a * lh * ((sht[sh] - 1) / 2) + 1)} * {((aps[ap][s - 2]) * (a * dw))}  * {d} {rerolls}")
            return (hwrh[h - 2][w - 2]) * (a * lh * ((sht[sh] - 1) / 2) + 1) * ((aps[ap][s - 2]) * (dw * a))  * d * fnpt[fnp]
        case "Reroll Hits Reroll Wounds":
            print(f"{(hwrhrw[h - 2][w - 2]) * (a * lh * ((sht[sh] - 1) / 2) + 1)} * {((aps[ap][s - 2]) * (a * dw))}  * {d} {rerolls}")
            return (hwrhrw[h - 2][w - 2]) * (a * lh * ((sht[sh] - 1) / 2) + 1) * ((aps[ap][s - 2]) * (dw * a))  * d * fnpt[fnp]
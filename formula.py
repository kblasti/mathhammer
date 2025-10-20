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
    if "Lethal Hits" in weapon["keywords"]:
        match w:
            case 2:
                lh = 1.2
            case 3:
                lh = 1.4
            case 4:
                lh = 1.6
            case 5:
                lh = 1.8
            case 6:
                lh = 2
    if "Devastating Wounds" in weapon["keywords"]:
        match s:
            case 2:
                dw = 2
            case 3:
                dw = 1.8
            case 4:
                dw = 1.6
            case 5:
                dw = 1.4
            case 6:
                dw = 1.2
        
    match rerolls:
        case "None":
            print(f"{((hw[h - 2][w - 2]) * lh) * (a * ((sht[sh] - 1) / 2) + 1)} * {((aps[ap][s - 2]) * (a * dw))}  * {d} {rerolls}")
            return ((hw[h - 2][w - 2]) * lh) * (a * ((sht[sh] - 1) / 2) + 1) * ((aps[ap][s - 2]) * (dw * a))  * d * fnpt[fnp]
        case "Reroll Hits 1":
            print(f"{((hwr1[h - 2][w - 2]) * lh) * (a * ((sht[sh] - 1) / 2) + 1)} * {((aps[ap][s - 2]) * (a * dw))}  * {d} {rerolls}")
            return ((hwr1[h - 2][w - 2]) * lh) * (a * ((sht[sh] - 1) / 2) + 1) * ((aps[ap][s - 2]) * (dw * a))  * d * fnpt[fnp]
        case "Reroll Hits":
            print(f"{((hwrh[h - 2][w - 2]) * lh) * (a * ((sht[sh] - 1) / 2) + 1)} * {((aps[ap][s - 2]) * (a * dw))}  * {d} {rerolls}")
            return ((hwrh[h - 2][w - 2]) * lh) * (a * ((sht[sh] - 1) / 2) + 1) * ((aps[ap][s - 2]) * (dw * a))  * d * fnpt[fnp]
        case "Reroll Hits Reroll Wounds":
            print(f"{((hwrhrw[h - 2][w - 2]) * lh) * (a * ((sht[sh] - 1) / 2) + 1)} * {((aps[ap][s - 2]) * (a * dw))}  * {d} {rerolls}")
            return ((hwrhrw[h - 2][w - 2]) * lh) * (a * ((sht[sh] - 1) / 2) + 1) * ((aps[ap][s - 2]) * (dw * a))  * d * fnpt[fnp]
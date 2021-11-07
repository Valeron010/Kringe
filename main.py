import sqlite3
import numpy as np
conn = sqlite3.connect(r'D:\BD1.db')
cur = conn.cursor()

def Formul(CharATK, WeapATK, BonusATKper, FlatATK, BonusDMGper, CritDMGper, SkillDMGper):
    return ((CharATK + WeapATK) * ((100 + BonusATKper)/100) + FlatATK) * ((100 + BonusDMGper)/100) * ((100 + CritDMGper)/100) * SkillDMGper/100


CharATK = 0
WeapATK = 0
BonusATKper = 0
FlatATK = 0
BonusDMGper = 0
CritDMGper = 0
SkillDMGper = 100
#Modificator = 0
#ReactionDMG = 0
RESe = 0
RESr = 0
LEVELcr = 90
LEVELe = 1
DEFr = 0
weapassactive = 0

sql = 'SELECT Value FROM ChiChi_stat WHERE Stat_ID = 3'
cur.execute(sql)
result = cur.fetchone()

CharATK = float(result[0])

sql = 'SELECT * FROM Weapons'
cur.execute(sql)
result = cur.fetchall()
Weapon_list = result

sql = 'SELECT perATK FROM Build'
cur.execute(sql)
result = cur.fetchone()
BonusATKper = float(result[0])

sql = 'SELECT Crit_D FROM Build'
cur.execute(sql)
result = cur.fetchone()
CritDMGper = float(result[0])

sql = 'SELECT ATK FROM Build'
cur.execute(sql)
result = cur.fetchone()
FlatATK = float(result[0])

sql = 'SELECT PhysDMG FROM Build'
cur.execute(sql)
result = cur.fetchone()
BonusDMGper = float(result[0])
attack = np.zeros(24)
attack1 = np.zeros(24)

print(len(Weapon_list))
for i in range(len(Weapon_list)):
    WeapATK = Weapon_list[i][1]
    BonusATKper1 = BonusATKper
    BonusDMGper1 = BonusDMGper
    CritDMGper1 = CritDMGper
    if Weapon_list[i][2] == 4:
        BonusATKper1 = BonusATKper1 + Weapon_list[i][3]
    if Weapon_list[i][2] == 9:
        CritDMGper1 = CritDMGper1 + Weapon_list[i][3]
    if Weapon_list[i][2] == 10:
        BonusDMGper1 = BonusDMGper1 + Weapon_list[i][3]
    now_attack = Formul(CharATK, WeapATK, BonusATKper1, FlatATK, BonusDMGper1, CritDMGper1, SkillDMGper)
    print('now attack = ',now_attack)
    if i == 0:
        attack[i] = i
        attack1[i] = now_attack
    else:
        for j in range(len(attack)):
            if now_attack > attack1[j]:
                attack1 = np.insert(attack1, j, now_attack)
                attack = np.insert(attack, j, i)
                break


for i in range(len(Weapon_list)):
    index = int(attack[i])
    print(Weapon_list [index][0], attack1[i])






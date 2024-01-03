from os import system as sys
from datetime import datetime
import colorama
import json

sys('cls')

# Stylesheet
colorama.init(autoreset=True)
c = colorama.Fore
b = colorama.Back
s = colorama.Style

# Datetime
time = datetime.now().strftime("%d.%m.%Y")

# Data
title = 'Killer Croc'
description = 'Arkham prisioner, wanted in Gotham City'
title, description = title.upper(), description.upper()

name = 'Waillon Jones'
sex = 'M'
age = 28
height = 2.1
weight = 300
ethnicity = 'UNKNOWN'
occupation = 'UNKNOWN'
skills = 'TRAKING; FAST UNDER WATHER'

profile = {
    "FULL NAME:": name.upper(),
    "SEX:": sex.upper(),
    "AGE:": age,
    "HEIGHT:": height,
    "FULL NAME:": name.upper(),
    "SEX:": sex.upper(),
    "AGE:": age,
    "HEIGHT:": height,
    "WEIGHT:": weight,
    "ETHNICITY:": ethnicity.upper(),
    "OCCUPATION:": occupation.upper(),
    "SKILLS:": skills.upper()
}

# Convertendo para formato JSON
profile_JSON = json.dumps(profile, indent=2, ensure_ascii=False)

# Viewer Profile
# Calcula o comprimento total do banner
banner_width = len(title) + 20  # 14 é o comprimento fixo das bordas e espaçamento

# Imprime o banner adaptativo
print(f'{c.RED}{s.BRIGHT}┌{"─" * banner_width}┐')
print(f'{c.RED}{s.BRIGHT}│{title.center(banner_width)}│')
print(f'{c.RED}{s.BRIGHT}└{"─" * banner_width}┘')

print(f'{c.RED}{s.BRIGHT}\n‣ {s.NORMAL}{description}\n')
print(b.CYAN + s.BRIGHT + ' INFO                                     \n')
for key, value in profile.items():
    print(f"{c.CYAN}{key.ljust(15)} {value}")

print(' ')
print(f'{c.RED}{s.BRIGHT}/ BIOGRAPHY {s.DIM}/ WAILLON JONES / KILLER CROC\n')
print(c.CYAN + '''Born with a rare skin disease that only worsened over time, Waylon Jones was put under 
the guardianship of his incredibly abusive and alcoholic aunt after his mother died 
giving birth to him and his father had abandoned him. Brutally abused in his 
home and relentlessly bullied at school, Waylon accepted his place in society 
as always being seen as a monster.

As the years went on, Jones's condition made him more and more into a monster. 
That ultimately eradicated any traces of humanity that might have been left as 
he became a monster in both body and spirit. Always seeking his next meal, Croc 
never forgot the scent of Batman and lusted to kill and devour the hero in 
retribution for his capture at his hands.
''')

print(b.CYAN + s.BRIGHT + ' REGISTERS                                     ')

print(f'{c.RED}{s.BRIGHT}\n/ LOCALES\n')
print(f'{c.RED}{s.BRIGHT}‣ {s.DIM}{time} {s.NORMAL}› Visited Arkham Asylum')
print(f'{c.RED}{s.BRIGHT}‣ {s.DIM}{time} {s.NORMAL}› Had been seen before underground')

print(f'{c.RED}{s.BRIGHT}\n/ SOCIAL NETWORKS\n')
print(f'{c.RED}{s.BRIGHT}‣ {s.DIM}{time} {s.NORMAL}› https://instagram.com/@killercroc')
print(f'{c.RED}{s.BRIGHT}‣ {s.DIM}{time} {s.NORMAL}› https://www.youtube.com/@BatmanArkhamVideos')

action = input(f'\n{s.BRIGHT}{c.CYAN}(krs@TUX-BOOK) [PROFILES/DEMO/KILLER CROC] >>> {s.NORMAL}{c.RED}')

from os import system as sys
import colorama
import json

sys('cls')

# Stylesheet
colorama.init(autoreset=True)
c = colorama.Fore
b = colorama.Back
s = colorama.Style

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
print(' ')
print(f'{c.RED}{s.BRIGHT}┌────────────────────────────────────────┐')
print(f'{c.RED}{s.BRIGHT}│              {title}               │')
print(f'{c.RED}{s.BRIGHT}└────────────────────────────────────────┘')
print(f'{c.RED}{s.DIM}\n‣ {description}\n')
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
import sqlite3
import os

# Obtém o diretório atual do script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para o arquivo do banco de dados
db_path = os.path.join(current_directory, 'profiler.db')

# Conecta com o banco de dados

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Teste de banco de dados

fullname = 'Waillon Jones'
sex = 'M'
age = 28

profileInfo = {
    "FULL NAME:": fullname.upper(),
    "SEX:": sex.upper(),
    "AGE:": age,
}

# Add a new profile
def addProfile(title, description):
    cur.execute("INSERT INTO Profiles (title, description) VALUES (?, ?)", (title, description))
    conn.commit()

# Add a new information to the profile
def addInfo(profileTitle, item, value):
    cur.execute("SELECT * FROM Profiles WHERE title = ?", (profileTitle,))
    profile = cur.fetchone()
    profile_id = profile[0]

    cur.execute("INSERT INTO Info (profile_id, item, value) VALUES (?, ?, ?)", (profile_id, item, value))
    conn.commit()

# Add a Biography to the profile
def addBiography(profileTitle, biography):
    cur.execute("SELECT * FROM Profiles WHERE title =?", (profileTitle,))
    profile = cur.fetchone()
    profile_id = profile[0]

    cur.execute("INSERT INTO Biography (profile_id, biography) VALUES (?, ?)", (profile_id, biography))
    conn.commit()

# Showing data from the profile
def showProfile(profileTitle):
    # Searching profile
    cur.execute("SELECT * FROM Profiles WHERE title = ?", (profileTitle,))
    profile = cur.fetchone()
    profile_id = profile[0]
    # Getting info
    cur.execute("SELECT * FROM Info WHERE profile_id = ?", (profile_id,))
    conn.commit()
    profileInfo = cur.fetchall()
    # Getting biography
    cur.execute("SELECT * FROM Biography WHERE profile_id = ?", (profile_id,))
    conn.commit()
    profileBio = cur.fetchone()
    print(profile)
    print(profileInfo)
    print(profileBio)


title = 'Hera venenosa'
description = 'Hera venenosa é perigosa, mantenha distancia'
bio = 'Hera venenosa é uma vilã inteligente de Gotham city que criou a capacidade de manipular plantas e venenos'

title, description = title.upper(), description.upper()

addProfile(title=title, description=description)
addInfo(profileTitle=title, item='SEX', value='F')
addInfo(profileTitle=title, item='HABILIDADE', value='UTILIZAR VENENOS')
addBiography(profileTitle=title, biography=bio)
showProfile(title)

conn.close()
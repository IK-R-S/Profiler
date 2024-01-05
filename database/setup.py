import sqlite3
import os

# Obtém o diretório atual do script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para o arquivo do banco de dados
db_path = os.path.join(current_directory, 'profiler.db')

# Conecta ao banco de dados
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Profiles
cur.execute('''
    CREATE TABLE IF NOT EXISTS Profiles (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT
    );
''')

# Info
cur.execute('''
    CREATE TABLE IF NOT EXISTS Info (
        id INTEGER PRIMARY KEY,
        profile_id INTEGER,
        item TEXT,
        value TEXT,
        FOREIGN KEY (profile_id) REFERENCES Profiles(id)
    );
''')

# Biography
cur.execute('''
    CREATE TABLE IF NOT EXISTS Biography (
        id INTEGER PRIMARY KEY,
        profile_id INTEGER,
        biography TEXT,
        FOREIGN KEY (profile_id) REFERENCES Profiles(id)
    );
''')

# Records
cur.execute('''
    CREATE TABLE IF NOT EXISTS Records (
        id INTEGER PRIMARY KEY,
        profile_id INTEGER,
        title TEXT,
        datetime TEXT,
        FOREIGN KEY (profile_id) REFERENCES Profiles(id)
    );
''')

# Records_contents
cur.execute('''
    CREATE TABLE IF NOT EXISTS Records_contents (
        id INTEGER PRIMARY KEY,
        record_id INTEGER,
        content TEXT,
        datetime TEXT,
        FOREIGN KEY (record_id) REFERENCES Records(id)
    );
''')

conn.commit()
conn.close()

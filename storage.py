import json

USERS_FILE = 'users.json'

def load_users():
    try:
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    except:
        return {}
    
def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

MOODS_FILE = 'moods.json'

def load_moods():
    try:
        with open(MOODS_FILE, 'r') as file:
            return json.load(file)
    except:
        return {}
    
def save_moods(moods):
    with open(MOODS_FILE, 'w') as file:
        json.dump(moods, file, indent=4)
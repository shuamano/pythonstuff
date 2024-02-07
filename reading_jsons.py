from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username 
    else:
        return None 

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}.")
    else:
        username = get_new_user_name(path)

def get_new_user_name(path):
     username = input("What is your name?")
     contents = json.dumps(username)
     path.write_text(contents)
     return username

greet_user()


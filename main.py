import json

def load_data():
    try:
        with open("languages.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"English": "Hello", "Spanish": "Hola"}
    
def save_data(data):
    with open("languages.json", "w") as file:
        json.dump(data, file, indent=4)

languages = load_data()

def greetings(lang_name):
    if lang_name in languages:
        print(f"\n{languages[lang_name]}!")
        return False
    else:
        print(f"\nSorry! I don't know {lang_name} yet.")
        return True

user_lang = input("What language do you speak?").strip().capitalize()
if greetings(user_lang):
    new_greeting = input(f"What is 'Hello' in {user_lang}? ")

    languages[user_lang] = new_greeting
    save_data(languages)
    print("Memory updated! I'll remember that next time.")
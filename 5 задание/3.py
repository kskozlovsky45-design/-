import random
import json
import string


def generate_user_data():
    first_names = ["Michael", "David", "John", "Mary", "Helen", "Tonny"]
    last_names = ["Jackson", "Williams", "Smith", "Miller", "Martinez", "Lopez"]
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = random.randint(18, 80)

    email_name = name.lower().replace(" ", ".")
    domains = ["example.com", "mail.ru", "gmail.com", "yandex.ru"]
    email = f"{email_name}@{random.choice(domains)}"

    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_chars) for _ in range(12))

    user = {
        "name": name,
        "age": age,
        "email": email,
        "password": password
    }

    with open("user.json", "w", encoding="utf-8") as f:
        json.dump(user, f, indent=4, ensure_ascii=False)

    with open("user.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print(json.dumps(data, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    print("\nЗадание 3:")
    generate_user_data()
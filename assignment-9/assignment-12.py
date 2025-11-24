# 1. დაწერეთ პითონის ფუნქცია, რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის საქაღალდის მისამართს, ფაილის სახელს და შექმნის მას.

import os

def create_file(directory, filename):
    try:
        # ვამოწმებთ, არსებობს თუ არა საქაღალდე, თუ არ არსებობს, ვქმნით
        os.makedirs(directory, exist_ok=True)

        # ფაილის შექმნა კონტექსტის მენეჯერის გამოყენებით
        file_path = os.path.join(directory, filename)
        with open(file_path, "w") as f:
            f.write("Hello")

        return f"File created successfully: {file_path}"

    except Exception as e:
        return f"Error: {e}"

# მაგალითი
print(create_file("data_folder", "example.txt"))



# 2. დაწერეთ პითონის ფუნქცია, რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს.

def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# მაგალითი
read_file("data_folder/example.txt")



# 3. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და ჩაწერს/გაანახლებს ფაილის კონტენტს.

# [
#   {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
#   {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# ]

# ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია.

import json
import os

def update_chess_players(new_data, file_path):
    try:
        existing_data = []

        # არსებული მონაცემების წაკითხვა, თუ ფაილი არსებობს
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                existing_data = json.load(f)

        # არსებული და ახალი მონაცემების გაერთიანება
        updated_data = existing_data + new_data

        # JSON ფორმატით ჩაწერა
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(updated_data, f, ensure_ascii=False, indent=2)

        print(f"Data successfully written to {file_path}")

    except json.JSONDecodeError:
        print("Error: The JSON file is corrupted or empty.")
    except Exception as e:
        print(f"Error: {e}")


# მაგალითი
chess_players = [
    {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
    {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
    {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
    {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
    {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
    {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
    {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
    {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
    {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

update_chess_players(chess_players, "data_folder/chess_players.json")

new_players = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

update_chess_players(new_players, "data_folder/chess_players.json")



# 4. დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს.

def overwrite_file(file_path, new_content):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"File '{file_path}' updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

# მაგალითი
overwrite_file("data_folder/example.txt", "გამარჯობა")

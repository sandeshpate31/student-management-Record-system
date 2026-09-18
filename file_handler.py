import json
import os

FILE_NAME = "data/records.json"


def load_records():
    try:
        if not os.path.exists(FILE_NAME):
            return []

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("File reading error:", e)
        return []


def save_records(records):
    try:
        os.makedirs("data", exist_ok=True)

        with open(FILE_NAME, "w") as file:
            json.dump(records, file, indent=4)

    except IOError as e:
        print("File writing error:", e)
import json
import os

def count_mods_in_json_files(directory):
    mod_count = 0
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                mod_count += len(data)
    return mod_count

if __name__ == "__main__":
    directory = './'  # Adjust to the path where your JSON files are located
    total_mods = count_mods_in_json_files(directory)
    with open('mod_count_badge.json', 'w') as f:
        json.dump({"schemaVersion": 1, "label": "mods", "message": str(total_mods), "color": "brightgreen"}, f)

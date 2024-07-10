import json
import os

def count_mods_in_specific_files(files):
    mod_count = 0
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            mod_count += len(data.get("Mods", []))
    return mod_count

if __name__ == "__main__":
    files = [
        './PS3/game-cheats.json',
        './PS3/game-mods.json',
        './PS3/homebrew.json',
        './PS3/resources.json',
        './XBOX360/plugins.json'
    ]
    total_mods = count_mods_in_specific_files(files)
    badge_data = {
        "schemaVersion": 1,
        "label": "mods",
        "message": str(total_mods),
        "color": "brightgreen"
    }
    with open('mod_count_badge.json', 'w') as f:
        json.dump(badge_data, f)

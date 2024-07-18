import json
import os

def count_mods_in_specific_files(files):
    mod_count = 0
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            mod_count += len(data.get("Mods", []))
    return mod_count

def count_saves_in_specific_files(files):
    save_count = 0
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            save_count += len(data.get("GameSaves", []))
    return save_count

if __name__ == "__main__":
    files = [
        './PS3/game-cheats.json',
        './PS3/game-mods.json',
        './PS3/homebrew.json',
        './PS3/resources.json',
        './XBOX360/plugins.json'
    ]
    
    saves = [
        './game-saves.json'
    ]
    
    total_mods = count_mods_in_specific_files(files)
    total_saves = count_saves_in_specific_files(saves)
    
    total_count = total_mods + total_saves
    
    badge_data = {
        "schemaVersion": 1,
        "label": "mods",
        "message": str(total_count),
        "color": "brightgreen"
    }
    
    with open('mod_count_badge.json', 'w') as f:
        json.dump(badge_data, f)

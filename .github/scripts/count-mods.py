import json
import os
import requests

def fetch_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch JSON from {url}. Status code: {response.status_code}")
        return None

def count_mods_in_specific_files(urls):
    mod_count = 0
    for url in urls:
        data = fetch_json(url)
        if data:
            mod_count += len(data.get("Mods", []))
        else:
            print(f"Failed to load JSON from {url}")
    return mod_count

def count_saves_in_specific_files(urls):
    save_count = 0
    for url in urls:
        data = fetch_json(url)
        if data:
            save_count += len(data.get("GameSaves", []))
        else:
            print(f"Failed to load JSON from {url}")
    return save_count

if __name__ == "__main__":
    mod_urls = [
        "https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/PS3/game-mods.json",
        "https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/PS3/homebrew.json",
        "https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/PS3/resources.json",
        "https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/XBOX360/plugins.json"
    ]
    
    save_urls = [
        "https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/game-saves.json"
    ]
    
    total_mods = count_mods_in_specific_files(mod_urls)
    total_saves = count_saves_in_specific_files(save_urls)
    
    total_count = total_mods + total_saves
    
    badge_data = {
        "schemaVersion": 1,
        "label": "mods",
        "message": str(total_count),
        "color": "brightgreen"
    }
    
    os.makedirs('.github/badges', exist_ok=True)
    badge_path = '.github/badges/mod-count-badge.json'
    with open(badge_path, 'w') as f:
        json.dump(badge_data, f)
    
    print(f"Badge data written to {badge_path}")

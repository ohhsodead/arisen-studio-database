import requests
import json
import os

# URLs of the JSON files
urls = [
    "https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/PS3/packages/avatars.json",
    "https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/PS3/packages/demos.json",
    "https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/PS3/packages/dlcs.json",
    "https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/PS3/packages/games.json",
    "https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/PS3/packages/themes.json"
]

total_packages = 0

# Count the packages
for url in urls:
    response = requests.get(url)
    data = response.json()
    total_packages += len(data["Packages"])

# Generate the badge
badge_url = f"https://img.shields.io/badge/Total%20Packages-{total_packages}-brightgreen"
response = requests.get(badge_url)

# Save the badge to a file
badge_path = "badge.svg"
with open(badge_path, "wb") as file:
    file.write(response.content)

print(f"Total packages: {total_packages}")
print(f"Badge saved to {badge_path}")

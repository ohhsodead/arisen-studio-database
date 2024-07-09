name: Update Mod Count Badge

on:
  push:
    paths:
      - 'PS3/game-cheats.json'
      - 'PS3/game-mods.json'
      - 'PS3/homebrew.json'
      - 'PS3/resources.json'
      - 'XBOX360/plugins.json'
  workflow_dispatch:  # Allows manual triggering

jobs:
  update-badge:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip

      - name: Count mods and update badge
        run: |
          python count_mods.py
          mkdir -p badge
          mv mod_count_badge.json badge/mod_count_badge.json

      - name: Commit and push changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add badge/mod_count_badge.json
          git commit -m "Update mod count badge"
          git push
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

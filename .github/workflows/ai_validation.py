name: Validation IA des commits

on:
  push:
    branches:
      - main

jobs:
  ai-validation:
    runs-on: ubuntu-latest
    steps:
      - name: 📥 Récupération du code
        uses: actions/checkout@v4

      - name: 🐍 Installation de Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: 🚀 Exécution de l'analyse IA
        run: python ai_validation.py

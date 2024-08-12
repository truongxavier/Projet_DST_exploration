Structure du projet 
________________________________________________________________________________________________________
project_name: Jul24_bds_extraction_info
│
├── data/                 # Contient les fichiers de données brutes et traitées
│   ├── raw/              # Données brutes (non modifiées)
│   ├── processed/        # Données prétraitées
│
├── notebooks/            # Jupyter Notebooks pour l'exploration et les analyses
│
├── scripts/              # Scripts Python pour le traitement des données et les modèles
│   ├── data_preprocessing.py  # Prétraitement des données
│   ├── feature_engineering.py  # Ingénierie des caractéristiques
│   ├── train_model.py         # Entraînement des modèles
│   ├── evaluate_model.py      # Évaluation des modèles
│
├── models/               # Modèles entraînés et sauvegardés
│
├── results/              # Résultats des analyses et visualisations
│
├── logs/                 # Fichiers journaux (logs) pour le suivi des exécutions
│
├── tests/                # Tests unitaires et d'intégration
│
├── .gitignore            # Fichiers à ignorer par Git
├── README.md             # Documentation du projet
├── requirements.txt      # Liste des dépendances Python du projet
└── .env                  # Variables d'environnement sensibles
__________________________________________________________________________________________________________



pour installer le projet :
python3 -m venv mon_env

source mon_env/bin/activate

pip install -r requirements.txt

les images sont à importer sur exploration/data


![exploration](https://github.com/user-attachments/assets/987cda39-5a44-4352-b2e7-96985eac64bf)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from spellchecker import SpellChecker
import re

#lecture de fichier CSV
df = pd.read_csv("..\data\processed\Raw_data_OCR.csv")
df.head(10)


# le nombre de différentes images '.tif' dans la colonne 'image_filename' :408
print(f"nombre de documents : {df['image_filename'].nunique()}")

# Fréquence des mots
print(f"Fréquence des mots : {df['Word Text'].value_counts()}")

# Nettoyage des données
valeurs_a_supprimer = ['-','•','*']
df = df[~df['Word Text'].isin(valeurs_a_supprimer)]
print(f"Fréquence des mots : {df['Word Text'].value_counts()}")

# le type'Word Text' 
print(f"le type de la variable Word Text est : {df['Word Text'].dtype}")

# Calcul du score moyen/median de confiance par image
mean_Confidence = np.mean(df.Confidence)
median_Confidence = np.median(df.Confidence)
print(f"confiance moyenne de l'OCR par image  : {df.groupby('image_filename')['Confidence'].mean()}")

# Statistiques pour la variable 'Confidence'
print(f"les statistiques pour la variable 'Confidence': {df['Confidence'].describe()}")

#______________________________________________________________________Normalisation des mots

def normalize_text(text):
    # Convertir l'entrée en chaîne de caractères
    converted_text = str(text) if text is not None else ''
    if isinstance(text, (int, float)):  # Gérer les cas de nombres
        return str(text)  # Convertir directement les nombres en chaînes de caractères
    if not isinstance(converted_text, str):
        raise ValueError(f"Conversion échouée, le type est {type(converted_text)} au lieu de str.")
    if  isinstance(converted_text, str):
        converted_text = ''.join(char.lower() if char.isalpha() else char for char in text)
        #print(f"la chaine convertie  est:  {converted_text}")
    return converted_text

# Appliquer la fonction à chaque élément de la colonne 'Word Text'
df['Word Text'] = df['Word Text'].apply(normalize_text)
print(f" Word Text est : {df['Word Text'].head(20)}")

# Trier le dataframe  par ordre croissant de Colonne Confidence
df_trie = df.sort_values(by='Confidence',ascending=False)
# Réinitialiser les index
df_trie = df_trie.reset_index(drop=True)
print(df_trie.head(100))
# Tracé pour la confiance globale sur les mots de l'OCR

plt.figure(figsize=(18,6))
plt.plot(df_trie.Confidence,color='#4d3c39', linestyle='-', label='Confidence')
plt.axhline(y=mean_Confidence, color='#c4ca0d', linestyle='-', label='Mean Confidence')
plt.axhline(y=median_Confidence, color='#3276f4', linestyle='-', label='Median Confidence')
plt.text(x=400, y=mean_Confidence+0.03, s=f"Mean Value = {mean_Confidence:.2f}", fontsize=12,color='#c4ca0d')
plt.text(x=400, y=median_Confidence-0.03, s=f"Median Value = {median_Confidence:.2f}", fontsize=12,color='#3276f4')
plt.xlabel('Text_Index')
plt.ylabel('OCR_Confidence')
plt.title('OCR_Confidence ')
plt.ylim(bottom=0.0)
plt.xlim(left=min(df_trie.Confidence))
plt.legend(loc='upper right')
# plt.grid()
plt.show()



from PIL import Image
import numpy as np
import pandas as pd
import os

# Chemin du dossier contenant les images TIFF
dossier_images = '/home/xavier/code/truongxavier/Projet_DST_exploration/exploration/data'

# Liste pour stocker les données des images
data_list = []

# Parcourir tous les fichiers du dossier
for fichier in os.listdir(dossier_images):
    if fichier.endswith('.tif'):
        # Charger l'image TIFF
        image = Image.open(os.path.join(dossier_images, fichier))

        # Convertir l'image en tableau numpy
        image_array = np.array(image)

        # Ajouter une dimension pour identifier l'image
        image_id = os.path.splitext(fichier)[0]
        image_data = pd.DataFrame(image_array)
        image_data['image_id'] = image_id

        # Ajouter les données de l'image à la liste
        data_list.append(image_data)

# Combiner toutes les données dans un seul DataFrame
df_combined = pd.concat(data_list, ignore_index=True)

print(df_combined['image_id'].head())
df_combined.info()
df_combined.head(1)

import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
import os 
# Espace de noms du fichier XML (à partir de l'attribut xmlns)
namespace = {'ns': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15'}
dossier_xml = 'C:/Users/HP/OneDrive/Bureau/FormationDataScient/Projet/ImageAndXML_Data-20240808T145037Z-001/ImageAndXML_Data'
data = []
# Charger le fichier XML
for fichier in os.listdir(dossier_xml):
    if fichier.endswith('ocr.xml'):
        chemin_fichier = os.path.join(dossier_xml, fichier)
        tree = ET.parse(chemin_fichier)
        root = tree.getroot()

# Accéder aux métadonnées
        metadata = root.find('ns:Metadata', namespace)
        creator = metadata.find('ns:Creator', namespace).text
        created = metadata.find('ns:Created', namespace).text
        last_change = metadata.find('ns:LastChange', namespace).text

        # print(f"Créateur : {creator}")
        # print(f"Créé le : {created}")
        # print(f"Dernière modification : {last_change}")

        # Accéder à la page
        page = root.find('ns:Page', namespace)
        image_filename = page.get('imageFilename')
        image_height = page.get('imageHeight')
        image_width = page.get('imageWidth')

        # print(f"Nom du fichier image : {image_filename}")
        # print(f"Hauteur de l'image : {image_height}")
        # print(f"Largeur de l'image : {image_width}")

        # Accéder aux régions de texte et autres informations
        for text_region in page.findall('ns:TextRegion', namespace):
            region_id = text_region.get('id')
            region_type = text_region.find('./ns:Property', namespace).get('key')
            region_value = text_region.find('./ns:Property', namespace).get('value')
            coords = text_region.find('ns:Coords', namespace).get('points')
            properties = {prop.get('key'): prop.get('value') for prop in text_region.findall('ns:Property', namespace)}
            
            # print(f"Région de texte ID : {region_id}")
            # print(f"Coordonnées : {coords}")
            # print(f"Propriétés : {properties}")
            
            # Accéder aux lignes de texte dans chaque région
            for text_line in text_region.findall('ns:TextLine', namespace):
                line_id = text_line.get('id')
                line_coords = text_line.find('ns:Coords', namespace).get('points')
                
                # print(f"  Ligne de texte ID : {line_id}")
                # print(f"  Coordonnées de la ligne : {line_coords}")
                
                # Accéder aux mots dans chaque ligne
                for word in text_line.findall('ns:Word', namespace):
                    word_id = word.get('id')
                    word_coords = word.find('ns:Coords', namespace).get('points')
                    word_text = word.find('ns:TextEquiv/ns:Unicode', namespace).text
                    word_conf = word.find('./ns:TextEquiv', namespace).get('conf')
                    confidence = word.find('ns:TextEquiv', namespace).get('conf')
                    
                    # print(f"    Mot ID : {word_id}")
                    # print(f"    Coordonnées du mot : {word_coords}")
                    # print(f"    Texte : {word_text}")
                    print(f"    Confiance : {confidence}")
                    for page_elem in root.findall('.//Page'):
    # Extraire les attributs de la balise <Page>
                        image_filename = page_elem.get('imageFilename')
                        image_height = page_elem.get('imageHeight')
                        image_width = page_elem.get('imageWidth')
                            
                    data.append({
                'image_filename': image_filename,  
                'image_height': image_height, 
                'image_width': image_width,     
                'Region ID': region_id,
                'Region Type': region_type,
                'Region Value': region_value,
                'Region Coords': coords,
                'Line ID': line_id,
                'Line Coords': line_coords,
                'Word ID': word_id,
                'Word Coords': word_coords,
                'Word Text': word_text,
                'Confidence': word_conf
            })
df = pd.DataFrame(data)
df.to_csv('Info_OCR.csv', index=False, encoding='utf-8')
data_OCR_CSV=pd.read_csv('Info_OCR.csv')
print(data_OCR_CSV.head(40))
print(f"    data_CSV shape is  : {data_OCR_CSV.shape}")
count_purchase = data_OCR_CSV['Word Text'].str.contains('purchase', case=False, na=False).sum()
print(f" le nombre de fois le mot purchase est repeter dans le data_OCR_CSV: {count_purchase}")
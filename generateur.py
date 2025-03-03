from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# 1. Lire le fichier Excel
file_path = 'parfum.xlsx'  # Chemin vers votre fichier Excel
data = pd.read_excel(file_path)

# 2. Charger le template
template_path = 'asset/template.jpg'  # Chemin vers le template
output_folder = 'etiquettes'  # Dossier de sortie pour les étiquettes

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Charger le template
template = Image.open(template_path)

image_width, image_height = template.size

# 3. Charger une police (vérifiez le chemin vers une police existante sur votre système)

main_font = 'asset/font.ttf'
second_font = 'asset/dior.otf'

# Fonction pour ajuster dynamiquement la taille de la police
def get_dynamic_font(text, max_width, font_path, base_size=40):
    font_size = base_size  # Taille de départ
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculer la largeur du texte
    text_bbox = font.getbbox(text)  # Récupérer les dimensions du texte
    text_width = text_bbox[2] - text_bbox[0]  # Largeur du texte
    text_height = text_bbox[3] - text_bbox[1]  # Hauteur du texte
    
    # Réduire la taille de la police jusqu'à ce que le texte rentre
    while text_width > max_width:
        font_size -= 1  # Réduire la taille de la police
        font = ImageFont.truetype(font_path, font_size)
        text_bbox = font.getbbox(text)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
    
    return font

# 4. Générer les étiquettes
for index, row in data.iterrows():
    image = template.copy()
    draw = ImageDraw.Draw(image)
    
    # Ajouter les informations sur l'étiquette
    nom_parfum = str(row['Name'])  # Conversion explicite en chaîne
    maison = str(row['House'])  # Conversion explicite en chaîne
    genre = str(row['Gender'])  # Conversion explicite en chaîne
    types = str(row['Type'])  # Conversion explicite en chaîne

    if types == 'nan':
        types = ''
    
    # Définir une largeur maximale pour le texte
    max_width = image_width - 100  # Un peu d'espace autour

    # Ajuster dynamiquement la taille de la police pour la maison
    font_maison = get_dynamic_font(maison, max_width, second_font, base_size=60)
    # Ajuster dynamiquement la taille de la police pour le nom du parfum
    font_nom = get_dynamic_font(nom_parfum, max_width, main_font, base_size=50)

    font_type = get_dynamic_font(types, max_width, main_font, base_size=50)
    
    # Calculer les dimensions du texte pour le nom du parfum
    text_bbox_nom = font_nom.getbbox(nom_parfum)
    text_bbox_maison = font_maison.getbbox(maison)
    text_bbox_type = font_type.getbbox(types)
    
    #(left, upper, right, lower)
    text_width_nom = text_bbox_nom[2] - text_bbox_nom[0]
    text_height_nom = text_bbox_nom[3] - text_bbox_nom[1]
    
    text_width_maison = text_bbox_maison[2] - text_bbox_maison[0]
    text_height_maison = text_bbox_maison[3] - text_bbox_maison[1]

    text_width_type = text_bbox_type[2] - text_bbox_type[0]
    text_height_type = text_bbox_type[2] - text_bbox_type[0]

    # Calculer les positions pour centrer le texte
    x_maison = (image_width - text_width_maison) // 2
    y_maison = (image_height - image_height * 0.75 - text_height_maison)

    x_nom = (image_width - text_width_nom) // 2
    y_nom = (image_height - text_height_nom) // 2
    
    
    x_type = (image_width - text_width_type) // 2
    y_type = (image_height - image_height * 0.2 - text_height_type) 

    # Positionner le texte sur l'image
    draw.text((x_maison, y_maison), maison, font=font_maison, fill="black")
    draw.text((x_nom, y_nom), nom_parfum, font=font_nom, fill="black")

    draw.text((x_type,y_type), types, font=font_type , fill="black")


    # Enregistrer l'image
    output_path = os.path.join(output_folder, f"etiquette_{index + 1}.jpg")
    image.save(output_path)

print("Les étiquettes ont été générées avec succès dans le dossier :", output_folder)

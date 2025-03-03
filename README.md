# Générateur d'Étiquettes de Parfum

Ce script Python génère des étiquettes de parfum à partir d'un fichier Excel contenant les noms des parfums, leur maison, leur genre et leur type. Il utilise un template d'image et ajuste dynamiquement la taille du texte pour une meilleure lisibilité.

## 📌 Fonctionnalités
- Lecture des données depuis un fichier Excel (`parfum.xlsx`)
- Génération d'étiquettes en utilisant une image modèle (`template.jpg`)
- Ajustement automatique de la taille du texte pour correspondre à l'espace disponible
- Enregistrement des étiquettes générées dans un dossier spécifique (`etiquettes/`)

## 🛠️ Prérequis
### 📂 Fichiers nécessaires
Assurez-vous d'avoir les fichiers suivants dans les bons répertoires :
- `parfum.xlsx` : fichier Excel contenant les données des parfums
- `asset/template.jpg` : image servant de modèle pour les étiquettes
- `asset/font.ttf` : police principale pour le texte
- `asset/dior.otf` : police secondaire pour les noms de maison

### 🖥️ Installation des dépendances
Ce script utilise les bibliothèques suivantes :
```bash
pip install pillow pandas openpyxl
```

## 🚀 Utilisation
1. Placez votre fichier `parfum.xlsx` dans le dossier du script.
2. Assurez-vous que le template et les polices sont bien placés dans le dossier `asset/`.
3. Exécutez le script :
```bash
python script.py
```
4. Les étiquettes générées seront enregistrées dans le dossier `etiquettes/`.

## 📄 Structure du fichier Excel
Le fichier Excel doit contenir les colonnes suivantes :
| Name | House | Gender | Type |
|------|-------|--------|------|
| Parfum A | Maison X | Homme | Eau de Parfum |
| Parfum B | Maison Y | Femme | Eau de Toilette |

## 📝 Personnalisation
- **Police** : Vous pouvez modifier les fichiers de police en remplaçant `font.ttf` et `dior.otf`.
- **Template** : Changez `template.jpg` pour personnaliser le design des étiquettes.
- **Couleurs et position du texte** : Modifiez les paramètres dans le script (`fill="black"`, positions `x`, `y`).

## 📌 Exemples d'Étiquettes Générées
Les étiquettes générées sont stockées dans le dossier `etiquettes/` sous la forme :
```
etiquettes/
  ├── etiquette_1.jpg
  ├── etiquette_2.jpg
  ├── ...
```

## 📜 Licence
Ce projet est sous licence MIT. Vous pouvez l'utiliser et le modifier librement.



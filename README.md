📚 Mini-Projet Big Data: Analyse de Livres (Web Scraping, HDFS & MapReduce)
📋 Présentation du Projet
Ce projet met en place une chaîne de traitement Big Data complète :

Collecte de données via Web Scraping.

Stockage distribué sur un cluster Hadoop (HDFS).

Traitement parallèle avec MapReduce en Python.

Visualisation des résultats finaux.

🏗️ Architecture du Projet
L'arborescence HDFS a été structurée pour séparer les données brutes des résultats :

/projet/raw/ : Contient le fichier books_raw.csv (Données brutes).

/projet/clean/ : Contient les données nettoyées après premier passage.

/projet/output_result/ : Résultat de l'analyse par Catégorie.

/projet/output_rating/ : Résultat de l'analyse par Note (Rating).

🛠️ Guide d'Exécution (Pipeline Automatisé)
Pour reproduire l'analyse, un script d'automatisation pipeline.bat a été créé. Il exécute les étapes suivantes :

Scraping : python scraper.py (Extraction de Titre, Prix, Note, Dispo, Lien).

Transfert : Chargement du CSV vers le NameNode Docker.

HDFS : Envoi des données vers /projet/raw/.

MapReduce 1 : Comptage des livres par catégorie.

MapReduce 2 : Analyse de la distribution des notes (Ratings).

📊 Analyse & Interprétation des Résultats
1. Analyse par Catégorie
Le scraper a ciblé la section "Mystery", révélant une dominance de cette catégorie (19 livres) par rapport aux autres sections scrapées.

2. Analyse par Note (Ratings)
Grâce au job MapReduce, nj'ai extrait la distribution suivante :

Note Dominante : 4 Étoiles (5 livres).

Observation : La majorité des ouvrages (9/19) possèdent une note de 4 ou 5 étoiles, indiquant une sélection de haute qualité dans cette catégorie.

📈 Visualisation
Graphique généré localement via Matplotlib après extraction des résultats HDFS.

⚠️ Limites et Améliorations
Limites du Scraping : Le script actuel ne traite qu'une seule page. Pour un projet à plus grande échelle, l'implémentation d'une pagination (boucles sur plusieurs URLs) serait nécessaire.

Qualité des Données : j'ai rencontré des anomalies de parsing (virgules dans les titres). Un filtre de validation a été ajouté dans le mapper_rating.py pour garantir la propreté des résultats finaux.

Amélioration possible : Utiliser Apache Spark pour des transformations plus complexes et plus rapides que MapReduce.

📂 Contenu du Dépôt
scraper.py : Script de collecte BeautifulSoup.

mapper.py / reducer.py : Analyse des catégories.

mapper_rating.py / reducer_rating.py : Analyse des notes.

visualisation.py : Script de génération du graphique.

pipeline.bat : Script d'automatisation Windows.

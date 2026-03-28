@echo off
echo ==========================================
echo DEBUT DU PIPELINE BIG DATA
echo ==========================================

:: c'est pour generer le fichier csv
echo [1/5] Scraping des données en cours...
python scraper.py

:: la préparation des scripts pour hadoop
echo [2/5] Envoi des scripts vers le NameNode...
docker cp mapper.py namenode:/tmp/
docker cp reducer.py namenode:/tmp/
docker cp mapper_rating.py namenode:/tmp/
docker cp reducer_rating.py namenode:/tmp/

:: ca pour le nettoyage des caractères windows
docker exec -u 0 namenode sed -i "s/\r$//" /tmp/mapper.py
docker exec -u 0 namenode sed -i "s/\r$//" /tmp/reducer.py
docker exec -u 0 namenode sed -i "s/\r$//" /tmp/mapper_rating.py
docker exec -u 0 namenode sed -i "s/\r$//" /tmp/reducer_rating.py

:: le chargement des données dans HDFS
echo [3/5] Chargement du CSV dans HDFS (/projet/raw)...
docker cp books_raw.csv namenode:/tmp/
docker exec namenode hdfs dfs -mkdir -p /projet/raw
docker exec namenode hdfs dfs -put -f /tmp/books_raw.csv /projet/raw/

:: l'exécution du traitement MapReduce (Analyse 1 Catégories)
echo [4/5] Exécution MapReduce : Analyse des Catégories...
docker exec namenode hdfs dfs -rm -r /projet/output_result
docker exec namenode hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar ^
 -D mapreduce.admin.user.env=HADOOP_MAPRED_HOME=/opt/hadoop-3.2.1 ^
 -D yarn.app.mapreduce.am.env=HADOOP_MAPRED_HOME=/opt/hadoop-3.2.1 ^
 -D mapreduce.map.env=HADOOP_MAPRED_HOME=/opt/hadoop-3.2.1 ^
 -D mapreduce.reduce.env=HADOOP_MAPRED_HOME=/opt/hadoop-3.2.1 ^
 -files /tmp/mapper.py,/tmp/reducer.py ^
 -input /projet/raw/books_raw.csv ^
 -output /projet/output_result ^
 -mapper "python3 mapper.py" ^
 -reducer "python3 reducer.py"

:: l'exécution du traitement MapReduce (Analyse 2 Notes/Ratings)
echo [5/5] Exécution MapReduce : Analyse des Notes...
docker exec namenode hdfs dfs -rm -r /projet/output_rating
docker exec namenode hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar ^
 -D mapreduce.admin.user.env=HADOOP_MAPRED_HOME=/opt/hadoop-3.2.1 ^
 -D yarn.app.mapreduce.am.env=HADOOP_MAPRED_HOME=/opt/hadoop-3.2.1 ^
 -D mapreduce.map.env=HADOOP_MAPRED_HOME=/opt/hadoop-3.2.1 ^
 -D mapreduce.reduce.env=HADOOP_MAPRED_HOME=/opt/hadoop-3.2.1 ^
 -files /tmp/mapper_rating.py,/tmp/reducer_rating.py ^
 -input /projet/raw/books_raw.csv ^
 -output /projet/output_rating ^
 -mapper "python3 mapper_rating.py" ^
 -reducer "python3 reducer_rating.py"

echo ==========================================
echo PIPELINE TERMINE AVEC SUCCES !
echo ==========================================
pause
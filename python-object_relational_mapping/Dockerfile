# Utiliser une image officielle de Python comme image de base
FROM python:3.8

# Mettre à jour le gestionnaire de paquets et installer les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    zlib1g-dev \
    pkg-config \
    default-mysql-client \
    default-mysql-server

# Installer mysqlclient pour Python
RUN pip install mysql-connector-python

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . .

# Définir la commande par défaut à exécuter
CMD ["python3", "hbtn_0e_0_usa", "root", "root"]

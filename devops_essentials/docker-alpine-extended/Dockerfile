# Utilise l'image de base Alpine
FROM alpine

# Installe le package curl
RUN apk add --no-cache curl

# Copie le fichier config.txt dans le conteneur
COPY config.txt /app/config.txt

# Commande pour garder le conteneur en exécution et permettre l'interaction
CMD ["/bin/sh"]

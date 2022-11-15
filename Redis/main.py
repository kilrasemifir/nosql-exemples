import redis

# Création d'une instance de connexion à Redis
client = redis.Redis(host='localhost', port=6379, db=0)

# Ajout d'une clé
client.set('key', 'value')
client.set('cle', 'une super valeur')

# Récupération de la valeur de la clé
print(client.get('key'))


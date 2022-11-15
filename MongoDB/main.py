from pymongo import MongoClient

# Connection à la base de données MongoDB
client = MongoClient('localhost', 27017)

# Création d'une base de données
db = client['test']

# Création d'une collection
collection = db['voiture']

# Ajout d'un document
result = collection.insert_one({'marque': 'Peugeot', 'modele': '308'})

# Récupération de la valeur de la clé
print(result.inserted_id)

# Récupération de la valeur de la clé
print(collection.find_one({'marque': 'Peugeot'}))

# Récupération de la valeur de la clé
print(collection.find_one({'marque': 'Peugeot'})['_id'])

# Exemple avec une donnée plus complexe
result = collection.insert_one({'marque': 'Peugeot', 'modele': '308', 'options': ['climatisation', 'jantes alliage', 'toit ouvrant']})

# Récupération de la valeur de la clé
print(collection.find_one({'marque': 'Peugeot'})['options'])

# Récupération de la valeur de la clé
print(collection.find_one({'marque': 'Peugeot'})['options'][0])
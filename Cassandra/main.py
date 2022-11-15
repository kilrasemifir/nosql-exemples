from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Configuaration de la connexion à la base de données Cassandra
auth = PlainTextAuthProvider(username='cassandra', password='cassandra')
cluster = Cluster(['localhost'], auth_provider=auth)
session = cluster.connect()

# Création d'une base de données (Keyspace en Cassandra)
## En SQL: CREATE DATABASE test;
cql_create_keyspace = """
CREATE KEYSPACE IF NOT EXISTS test WITH REPLICATION = { 
    'class' : 'SimpleStrategy', 
    'replication_factor' : 3 
};
"""
session.execute(cql_create_keyspace)

# Changement de la base de données par défaut
session.execute('USE test;')

# cql_delete_table = """
# DROP TABLE IF EXISTS voitures;
# """
# session.execute(cql_delete_table)

# Création d'une table
cql_create_table = f"""
CREATE TABLE IF NOT EXISTS voitures (
    id uuid,
    marque text,
    modele text,
    options list<text>,
    PRIMARY KEY (id, marque)
);
"""
session.execute(cql_create_table)

# Ajout d'une donnée

voitures = {
    'marque': 'Peugeot',
    'modele': '308',
    'options': ['climatisation', 'jantes alliage', 'toit ouvrant']
}

cql_insert = f"""
INSERT INTO voitures (id, marque, modele, options) VALUES (
    uuid(),
    '{voitures['marque']}',
    '{voitures['modele']}',
    {voitures['options']}
);
"""

result = session.execute(cql_insert)
print(result)

# Récupération de la donnée
result = session.execute('''SELECT COUNT(*) FROM voitures WHERE marque = 'Peugeot' ALLOW FILTERING;''')

for row in result:
    print(row)

cluster.shutdown()
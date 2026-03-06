from neo4j import GraphDatabase
import pandas as pd

# Load triples
df = pd.read_csv("data/processed/structured_triples.csv")

# Remove rows with missing values
df = df.dropna(subset=["Subject", "Predicate", "Object"])

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "Satwik786"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))


def create_relationship(tx, subject, predicate, obj):

    predicate = predicate.replace(" ", "_")

    query = f"""
    MERGE (a:Entity {{name:$subject}})
    MERGE (b:Entity {{name:$object}})
    MERGE (a)-[:{predicate}]->(b)
    """

    tx.run(query, subject=subject, object=obj)


with driver.session() as session:

    for _, row in df.iterrows():

        subject = str(row["Subject"]).strip()
        predicate = str(row["Predicate"]).strip()
        obj = str(row["Object"]).strip()

        # Skip empty values
        if subject == "" or predicate == "" or obj == "":
            continue

        session.execute_write(
            create_relationship,
            subject,
            predicate,
            obj
        )

driver.close()

print("Graph successfully stored in Neo4j")
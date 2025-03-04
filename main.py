import os
from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph

load_dotenv('./.env', override=True)
NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USER = os.getenv('NEO4J_USER')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
NEO4J_DATABASE = os.getenv('NEO4J_DATABASE')

kg = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USER, password=NEO4J_PASSWORD, database=NEO4J_DATABASE)

# Querying single and multiple nodes in the movie knowledge graph
all_nodes_cypher_query = """
MATCH (n)
RETURN  count(n) AS number_of_nodes
"""

all_nodes = kg.query(all_nodes_cypher_query)
# print(f'There are {all_nodes[0]["number_of_nodes"]} nodes in the graph')

movie_nodes_cypher_query = """
MATCH (m:Movie)
RETURN count(m) AS number_of_movies
"""

all_movie_nodes = kg.query(movie_nodes_cypher_query)
# print(f'There are {all_movie_nodes[0]["number_of_movies"]} movies in the graph')

all_person_nodes_cypher_query = """
MATCH (p:Person)
RETURN count(p) AS number_of_people
"""

all_person_nodes = kg.query(all_person_nodes_cypher_query)
# print(f'There are {all_person_nodes[0]["number_of_people"]} people in the graph')

person_nodes_cypher_query = """
MATCH(tom:Person {name:'Tom Hanks'})
RETURN tom
"""
single_person_node = kg.query(person_nodes_cypher_query)
# print(single_person_node) 

movie_nodes_cypher_query = """
MATCH (cloudAtlas:Movie {title: 'Cloud Atlas'})
RETURN cloudAtlas.released AS released_date, cloudAtlas.tagline AS tagline
"""
single_movie_node = kg.query(movie_nodes_cypher_query)
# print(single_movie_node)


# Cypher patterns with conditional matching
movie_realaese_date_cypher_query = """
MATCH (nineties:Movie)
WHERE nineties.released >= 1990 AND nineties.released < 2000
RETURN nineties.title AS title
"""

nineties_movie_nodes = kg.query(movie_realaese_date_cypher_query)
print(nineties_movie_nodes)
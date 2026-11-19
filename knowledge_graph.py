
import networkx as nx
import re

# Create a directed knowledge graph
G = nx.DiGraph()


# Solar System
G.add_edge("Earth", "Sun", relation="orbits")
G.add_edge("Mars", "Sun", relation="orbits")
G.add_edge("Jupiter", "Sun", relation="orbits")
G.add_edge("Saturn", "Sun", relation="orbits")
G.add_edge("Neptune", "Sun", relation="orbits")

# Moons
G.add_edge("Moon", "Earth", relation="orbits")
G.add_edge("Ganymede", "Jupiter", relation="orbits")
G.add_edge("Titan", "Saturn", relation="orbits")

# Planet information
G.add_edge("Mars", "Red Planet", relation="known_as")
G.add_edge("Jupiter", "Largest Planet", relation="known_as")
G.add_edge("Saturn", "Rings", relation="has")

# Galaxies and universe
G.add_edge("Milky Way", "Solar System", relation="contains")
G.add_edge("Milky Way", "Galaxy", relation="is_a")
G.add_edge("Universe", "Milky Way", relation="contains")

# Stars
G.add_edge("Sun", "Star", relation="is_a")
G.add_edge("Sun", "Solar Energy", relation="produces")

# Space exploration
G.add_edge("ISRO", "Chandrayaan-3", relation="launched")
G.add_edge("NASA", "Perseverance Rover", relation="operates")


# Search the knowledge graph
def search_knowledge_graph(question):

    results = []

    question_words = set(re.findall(r"[a-z0-9]+", question.lower()))

    for subject, object, data in G.edges(data=True):

        subject_words = set(re.findall(r"[a-z0-9]+", subject.lower()))
        object_words = set(re.findall(r"[a-z0-9]+", object.lower()))

        if subject_words.intersection(question_words):
            results.append(
                f"{subject} {data['relation']} {object}"
            )

        elif object_words.intersection(question_words):
            results.append(
                f"{subject} {data['relation']} {object}"
            )

    return list(dict.fromkeys(results))

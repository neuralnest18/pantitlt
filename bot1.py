from py2neo import Graph, Node, Relationship
import pytholog as pl
from pyaiml21 import Kernel
from glob import glob
import time

graph = Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))
kb = pl.KnowledgeBase("SocialNetwork")
kb.from_file("Facts_and_Rules.pl")
facts = []
rules = []
def fetch_facts_and_rules(file_path):
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("%") or not line:
                continue
            if ":-" in line:
                rule = line.split(":-")[0].strip()
                rule = rule.strip()
                rules.append(rule)
            else:
                facts.append(line)
    return facts, rules


def create_nodes(facts):
    for f in facts:
        f = str(f)
        predicate, arguments = f.split('(')
        predicate = predicate.strip()
        arguments = arguments[:-2].strip()

        if predicate == 'male' or predicate == 'female':
            person_node = Node("Person", name=arguments, gender=predicate)
            graph.merge(person_node, "Person", "name")

        elif predicate == 'parent':
            arg1, arg2 = arguments.split(',')
            arg1 = arg1.strip()
            arg2 = arg2.strip()

            parent_node = Node("Person", name=arg1)
            graph.merge(parent_node, "Person", "name")

            child_node = Node("Person", name=arg2)
            graph.merge(child_node, "Person", "name")

            relationship = Relationship(parent_node, "PARENT_OF", child_node)
            graph.merge(relationship)


def create_relations(rules):
    for r in rules:
        r = str(r)
        predicate, arguments = r.split('(')
        predicate = predicate.strip()

        cypher_query = "MATCH (n:Person) RETURN n"
        result = graph.run(cypher_query)

        names = [record['n']['name'] for record in result]

        for i in names:
            i = str(i)
            print("i: ", i)

            e = kb.query((pl.Expr("{}(X, {})".format(predicate, i))))
            if e[0] == 'No':
                pass
            else:
                node = e[0]['X']

                node1 = Node("Person", name=node)
                graph.merge(node1, "Person", "name")

                node2 = Node("Person", name=i)
                graph.merge(node2, "Person", "name")

                relationship = Relationship(node1, predicate, node2)
                graph.merge(relationship)


file_path = "Facts_and_Rules.pl"
facts, rules = fetch_facts_and_rules(file_path)

create_nodes(facts)
create_relations(rules)
def learn_aiml_from_directory(directory):
    Bot = Kernel()
    for file in glob(f"{directory}/*.aiml"):
        print("Learning from", file)
        Bot.learn(file)
    return Bot


def main():
    # Load AIML files
    Bot = learn_aiml_from_directory("data")

    # Interaction loop
    print("Bot: Hi there! How can I help you?")

    while True:
        userIn = input("User > ")
        response = Bot.respond(userIn, 'User1')
        print('<Bot>', response)
        print()
        if response.lower() == 'bye see you again':
            break


if __name__ == "__main__":
    main()

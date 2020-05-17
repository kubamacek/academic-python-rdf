from rdflib import Graph
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sparql', nargs=3, 
                        metavar=('subject', 'predicates', 'objects'), required=True, 
                        help='Semantic triple. Subject can be player or team. \
                              To make more advanced query, pass predicates and objects separated by comma.')
    return parser.parse_args()


def split_by_comma(arg):
    """Split argument by comma and return result as a list."""
    splitted = arg.split(',')
    return splitted


def execute_query(g, subject, predicates, objects):
    """Execute SPARQL query with given parameters."""
    query = 'SELECT ?{} WHERE {{ '.format(subject)
    for i in range(len(predicates)):
        query += '?{} {} {} . '.format(subject, predicates[i], objects[i])
    query += '}'
    print("Executing SPARQL query: '{}'".format(query))
    results = g.query(query)
    return results


def main():
    """
    Main program.
    - parse commandline args 
    - load RDF instance in turtle format
    - create and execute SPARQL query
    - print results
    """
    args = parse_args()
    g = Graph()
    g.parse('ontology.ttl', format='turtle')
    subject, predicates, objects = args.sparql
    splitted_predicates = split_by_comma(predicates)
    splitted_objects = split_by_comma(objects)
    if len(splitted_objects) == len(splitted_predicates) and subject in ('player', 'team'):
        results = execute_query(g, subject, splitted_predicates, splitted_objects)
        for result in results:
            print(getattr(result, subject))
    else:
        print("Wrong query. Type `python rdf.py -h` to get help.")
        sys.exit(1)


if __name__ == '__main__':
    main()

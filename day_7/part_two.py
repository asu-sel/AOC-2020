import sys
import networkx as nx
from re import compile

COLOUR_REGEX = compile(r'(?P<colour>[\w ]+) bags contain (?P<bags>.*)\.$')
BAGS_REGEX   = compile(r'(?P<count>\d+) (?P<colour>[\w ]+) bags?')

def graph(data):
    g = nx.DiGraph()
    
    for l in data:
        rm = COLOUR_REGEX.match(l)
        colour = rm.group('colour')
        if not (children := BAGS_REGEX.findall(rm.group('bags'))): continue

        for child in children:
            g.add_edge(colour, child[1], count=int(child[0]))
    
    return g

def count(g, root):
    return sum(e['count'] + e['count'] * count(g, n) for n, e in g[root].items())

def main():
    with open(sys.argv[1]) as f:
        data = f.read().splitlines()
    
    g = graph(data)
    c = count(g, 'shiny gold')
    print(f'Count: {c}')

if __name__ == '__main__':
    main()
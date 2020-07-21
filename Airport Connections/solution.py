# Solves the airport connections problem

# O(v+e) time | O(v) space
def update_cycle_edges(root, adj_list, was_visited, cycle_edges, backward=True):
    stack = [root]
    parent_of = dict()

    while stack:
        node = stack.pop()
        if node not in was_visited:
            was_visited.add(node)
            stack.extend(adj_list.get(node, []))
            for child in adj_list.get(node, []):
                parent_of[child] = node
        else:
            if backward:
                cycle_edges.add((node, parent_of[node]))
            else:
                cycle_edges.add((parent_of[node], node))
        
def get_acylic_edges(nodes, edges):
    fruitful_nodes = set()
    for edge in edges:
        fruitful_nodes.add(edge[0])
    unfruitful_nodes = nodes.difference(fruitful_nodes)

    # Forward cleansing from here
    adj_list = dict()
    for edge in edges:
        adj_list.setdefault(edge[0], []).append(edge[1])
    
    cycle_edges = set()
    for node in get_root_nodes(edges, nodes):
        was_visited = set()
        update_cycle_edges(node, adj_list, was_visited, cycle_edges, backward=False)
    
    new_edges = edges.difference(cycle_edges)
    
    # Backward cleansing from here
    inv_adj_list = dict()
    for edge in new_edges:
        inv_adj_list.setdefault(edge[1], []).append(edge[0])
    
    cycle_edges = set()
    for node in unfruitful_nodes:
        was_visited = set()
        update_cycle_edges(node, inv_adj_list, was_visited, cycle_edges)
    
    return new_edges.difference(cycle_edges)
        

def get_root_nodes(edges, nodes):
    non_root_nodes = set()
    for edge in edges:
        non_root_nodes.add(edge[1])
    root_nodes = nodes.difference(non_root_nodes)
    return root_nodes

def airport_connections(nodes, edges, root):
    acyclic_edges = get_acylic_edges(nodes, edges)
    return len(get_root_nodes(acyclic_edges, nodes))


if __name__ == "__main__":
    res = airport_connections(
        {
            "BGI",
            "CDG",
            "DEL",
            "DOH",
            "DSM",
            "EWR",
            "EYW",
            "HND",
            "ICN",
            "JFK",
            "LGA",
            "LHR",
            "ORD",
            "SAN",
            "SFO",
            "SIN",
            "TLV",
            "BUD",
        },
        {
            ("DSM","ORD"),
            ("ORD","BGI"),
            ("BGI","LGA"),
            ("SIN","CDG"),
            ("CDG","SIN"),
            ("CDG","BUD"),
            ("DEL","DOH"),
            ("DEL","CDG"),
            ("TLV","DEL"),
            ("EWR","HND"),
            ("HND","ICN"),
            ("HND","JFK"),
            ("ICN","JFK"),
            ("JFK","LGA"),
            ("EYW","LHR"),
            ("LHR","SFO"),
            ("SFO","SAN"),
            ("SFO","DSM"),
            ("SAN","EYW"),
        },
        "LGA"
    )

    assert res == 3, res

    print("You're all set!")
from collections import Counter


def label_propagation(G, seed_subgraph):
    # Initialize labels
    labels = {}
    label_counter = 0

    # Assign initial labels based on seed_subgraph
    for subgraph in seed_subgraph:
        label_counter += 1
        for node in subgraph:
            labels[node] = label_counter

    # Function to get the most common label among neighbors
    def most_common_label(node):
        neighbor_labels = [labels[neighbor] for neighbor in G.neighbors(node) if neighbor in labels]
        if neighbor_labels:
            return Counter(neighbor_labels).most_common(1)[0][0]
        else:
            return None

    # Nodes that are not labeled initially
    unlabeled_nodes = [node for node in G.nodes() if node not in labels]

    # Sort unlabeled nodes by the number of labeled neighbors
    unlabeled_nodes.sort(key=lambda x: sum(1 for neighbor in G.neighbors(x) if neighbor in labels), reverse=True)

    # Propagate labels
    for node in unlabeled_nodes:
        labels[node] = most_common_label(node)

    # Organize nodes into communities
    community_dict = {}
    for node, label in labels.items():
        if label not in community_dict:
            community_dict[label] = []
        community_dict[label].append(node)

    detected_communities = list(community_dict.values())
    return detected_communities




# Evaluate NMI between detected communities and ground truth
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics import f1_score
from sklearn.metrics.cluster import adjusted_rand_score
import argparse


# Reading the Ground-Truth Community Data
def load_ground_truth(file_path):
    node_to_community = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                node, community = int(parts[0]), int(parts[1])
                node_to_community[node] = community
    # Convert to list of lists for compatibility with NMI calculation
    community_to_nodes = {}
    for node, community in node_to_community.items():
        if community not in community_to_nodes:
            community_to_nodes[community] = []
        community_to_nodes[community].append(node)
    return list(community_to_nodes.values())


# Calculating NMI Score
def calculate_nmi(true_communities, detected_communities):
    # Flatten the lists and create label vectors
    true_labels = {}
    for i, community in enumerate(true_communities):
        for node in community:
            true_labels[node] = i
    detected_labels = {}
    for i, community in enumerate(detected_communities):
        for node in community:
            detected_labels[node] = i

    # Ensure the labels are in the same order for both true and detected
    nodes = sorted(set(true_labels) | set(detected_labels))
    true_labels_vector = [true_labels[node] for node in nodes]
    detected_labels_vector = [detected_labels.get(node, -1) for node in nodes]

    return normalized_mutual_info_score(true_labels_vector, detected_labels_vector)

def calculate_ari(true_communities, detected_communities):
    # Flatten the lists and create label vectors
    true_labels = {}
    for i, community in enumerate(true_communities):
        for node in community:
            true_labels[node] = i
    detected_labels = {}
    for i, community in enumerate(detected_communities):
        for node in community:
            detected_labels[node] = i

    # Ensure the labels are in the same order for both true and detected
    nodes = sorted(set(true_labels) | set(detected_labels))
    true_labels_vector = [true_labels[node] for node in nodes]
    detected_labels_vector = [detected_labels.get(node, -1) for node in nodes]

    return adjusted_rand_score(true_labels_vector, detected_labels_vector)
def calculate_F1score(true_communities, detected_communities):
    # Flatten the lists and create label vectors
    true_labels = {}
    for i, community in enumerate(true_communities):
        for node in community:
            true_labels[node] = i
    detected_labels = {}
    for i, community in enumerate(detected_communities):
        for node in community:
            detected_labels[node] = i

    # Ensure the labels are in the same order for both true and detected
    nodes = sorted(set(true_labels) | set(detected_labels))
    true_labels_vector = [true_labels[node] for node in nodes]
    detected_labels_vector = [detected_labels.get(node, -1) for node in nodes]

    return f1_score(true_labels_vector, detected_labels_vector, average='weighted')

def eval(network_file_path, approach):
    # Replace or append file extensions as necessary to construct paths
    community_file_path = network_file_path.replace('.dat', f'_{approach}.cmty')
    if 'TC1' in network_file_path:
        ground_truth_file_path = network_file_path.replace('.dat', '-c.dat')
    elif 'network.dat' in network_file_path:
        ground_truth_file_path = network_file_path.replace('network.dat', 'community.dat')
    else:
        return None, None, None

    detected_communities = load_ground_truth(community_file_path)
    true_communities = load_ground_truth(ground_truth_file_path)
    nmi_score = calculate_nmi(true_communities, detected_communities)
    f1_score = calculate_F1score(true_communities, detected_communities)
    ari_score = calculate_ari(true_communities, detected_communities)
    return nmi_score, f1_score, ari_score


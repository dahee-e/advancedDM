import networkx as nx
import community as community_louvain
import random
import csv
import numpy as np
import argparse
import matplotlib.pyplot as plt
import os

random_seed = 42
random.seed(random_seed)
np.random.seed(random_seed)




def save_communities_to_file(communities, file_path):
    # Convert the list of lists into a dictionary with community as key and nodes as values
    community_dict = {}
    for community_id, nodes in enumerate(communities):
        for node in nodes:
            community_dict[node] = community_id

    # Sort the dictionary by community key (which are the node numbers here)
    sorted_community_items = sorted(community_dict.items())

    # Write to file, now ensuring nodes are listed in the sorted order of their community keys
    with open(file_path, 'w') as f:
        for node, community_id in sorted_community_items:
            f.write(f"{node} {community_id}\n")


def dict_to_csv(dict_data, filename):
	with open(filename, 'w', newline='') as file:
		writer = csv.writer(file)
		for key, value in dict_data.items():
			writer.writerow([key, value])
	

def sort_dict(dict_data, idx=1, decreasing=True):
	return dict(sorted(dict_data.items(), key=lambda item: float(item[idx]), reverse=decreasing))


def get_community_num(filepath):
    unique_values = set()
    column_index = 1

    data = []
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.split()
            data.append([int(p) for p in parts])
            if len(parts) > column_index:
                value = parts[column_index]
                unique_values.add(value)
    
    return len(unique_values), data, unique_values


def get_ground_truth_community(filepath):
    node_to_cmty = {}
    cmty_to_node = {}
    with open(filepath, 'r') as file:
        for line in file:
            n_id, c_id = [int(v) for v in line.split()]
            node_to_cmty[n_id] = c_id

            if c_id in cmty_to_node: cmty_to_node[c_id].append(n_id)
            else: cmty_to_node[c_id] = [n_id]
    
    return node_to_cmty, cmty_to_node


def calculate_seed_selection_accuracy(selected_seeds, ground_truth_cmty_filepath):
    test_cmty = {}
    gt_node_to_cmty, gt_cmty_to_node = get_ground_truth_community(ground_truth_cmty_filepath)
    
    for sup_node in selected_seeds:
        cmty_id = gt_node_to_cmty[sup_node]
        if cmty_id in test_cmty: test_cmty[cmty_id].append(sup_node)
        else: test_cmty[cmty_id] = [sup_node]
    
    print(f"\n[*] RESULT selected seeds")
    print("======")
    for key, value in sort_dict(test_cmty, idx=0, decreasing=False).items():
        print(key, sorted(value))
    print("======")
    
    return [len(gt_cmty_to_node), len(test_cmty), (len(test_cmty)-len(gt_cmty_to_node))*100/len(gt_cmty_to_node)]


def verify_selected_seeds(selected_seeds, ground_truth_cmty_filepath):
    len_gt_cmty_to_node, len_test_cmty, relative_error = calculate_seed_selection_accuracy(selected_seeds, ground_truth_cmty_filepath)

    relative_error = (len_test_cmty-len_gt_cmty_to_node)*100/len_gt_cmty_to_node
    assert len_test_cmty == len_gt_cmty_to_node, f"\n \
	[!] FAILED verify_superior_seed_selection\n\
	    ground truth community size: {len_gt_cmty_to_node}, test community size: {len_test_cmty}\n \
        relative error: {round(relative_error, 2)} %"



def parse_community(filepath):
    cmty = {}
    with open(filepath, "r") as file:
        lines = file.readlines()
        for line in lines:
            node_id, cmty_id = [int(e) for e in line.strip().split('\t')]
            if cmty_id in cmty: cmty[cmty_id].append(node_id)
            else: cmty[cmty_id] = [node_id]
	
    cmty = sort_dict(cmty, idx=0, decreasing=False)
    for c, n in cmty.items():
        print(c, len(n))








def plot_community(G, cmty_filepath):
    plt.clf()
    NUM_CMTY, cmty_data, communities = get_community_num(cmty_filepath)
    
    cmty_colors = {}
    for i in communities:
        cmty_colors[int(i)] = "#" + "%06x" % random.randint(0, 0xFFFFFF)
    
    
    node_cmty = {}
    for node in cmty_data:
        node_cmty[node[0]] = node[1]
    pos = nx.spring_layout(G) 
    nx.draw(G, pos, node_color=[cmty_colors[node_cmty[node]] for node in G.nodes()], with_labels=True)
    
    plt.savefig(cmty_filepath+".png")

def get_base(file_path) :
    path = os.path.dirname(file_path)
    return path+"/"

def get_estimated_value(file_path, cmty_estimate):

    for key in cmty_estimate.keys():
        if key in file_path:
            return cmty_estimate[key]
    return None

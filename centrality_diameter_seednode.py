import networkx as nx
import time
from dataclasses import dataclass
import math
import random
from collections import Counter
import csv

import evaluation as EV
import utils 
import sys

@dataclass
class Graph:
  graph: nx.Graph = None
  graph_path: str = '' 

  centrality: dict = None

""" Community diameter approximation """
def approximate_cmty_diameter(G, NUM_CMTY):
  cmty_diameter = 0

  n_c = len(G.graph.nodes()) / NUM_CMTY
  d_avg = sum(dict(G.graph.degree()).values()) * 2 / len(G.graph.nodes())

  cmty_diameter = round(2 * math.log(n_c)/math.log(d_avg))
 
  assert(cmty_diameter > 0)
  return cmty_diameter


""" Seed node selection (centrality, diameter based) """

### Compute centrality for each nodes in graph 
def compute_centrality(G, centrality_type):
  if centrality_type == "degree":
    c = nx.degree_centrality(G.graph)
    centrality_type_abbr = "c_d"
  elif centrality_type == "eigenvector":
    c = nx.eigenvector_centrality(G.graph, max_iter=600)
    centrality_type_abbr = "c_e"
  elif centrality_type == "PageRank":
    c = nx.pagerank(G.graph)
    centrality_type_abbr = "c_p"
  elif centrality_type == "local_clustering_coefficient":
    c = nx.clustering(G.graph)
    centrality_type_abbr = "c_lcc"
  elif centrality_type == "betweenness":
    c = nx.betweenness_centrality(G.graph)
    centrality_type_abbr = "c_b"
  else:
    assert False , f"[!] ERROR unsupported centrality {centrality_type}"

  if centrality_type_abbr == "c_b":
    G.centrality[centrality_type] = utils.sort_dict(c, decreasing=False)
  else:
    G.centrality[centrality_type] = utils.sort_dict(c, decreasing=True)

  utils.dict_to_csv(G.centrality[centrality_type], ('/'.join(G.graph_path.split("/")[:-1]))+"/centrality/centrality_"+centrality_type_abbr+".csv")

### Sort nodes with high sum of normalized centrality in decreasing order 
def sort_nodes_with_centrality(G):
  max_centrality = {centrality: max(list(G.centrality[centrality].values())) for centrality in G.centrality}

  norm = {centrality: {node_id: c/max_centrality[centrality] for node_id, c in G.centrality[centrality].items()} for centrality in G.centrality}
  norm = {centrality: utils.sort_dict(norm[centrality]) for centrality in norm}
  
  sorted_nodes = {}
  for node_id in list(G.centrality.values())[0].keys():
    sorted_nodes[node_id] = sum([norm[c_type][node_id] for c_type in norm])
  sorted_nodes = utils.sort_dict(sorted_nodes)
  assert(len(sorted_nodes) > 0)

  return sorted_nodes

### Select seed nodes with diameter 
def _select_seed_nodes(G, NUM_CMTY, cmty_diameter, sorted_nodes):
  # Variables
  ss = []
  i_ss = []
 
  # Select seed nodes from isolated nodes 
  for node in sorted_nodes:
    try:
      # Check there is path between node and the highest centrality node 
      # If not, it is isolated node
      nx.shortest_path_length(G.graph, source=list(sorted_nodes.keys())[0], target=node)
    except nx.NetworkXNoPath:
      found = True 
      for i_s in i_ss: 
        try: 
          nx.shortest_path_length(G.graph, source=node, target=i_s)
          found = False 
        except nx.NetworkXNoPath: continue 

      if found: i_ss.append(node)
  
   ### Select seed nodes from unisolated nodes
  _cmty_diameter = cmty_diameter
  while _cmty_diameter > 0 and len(ss)+len(i_ss) < NUM_CMTY:
    ss = []
  
    for node in sorted_nodes:
      if len(ss) == 0:
        ss.append(node)
        continue
    
      if node in ss or node in i_ss: continue 
    
      # if node is isolated, skip 
      is_isolated_nonseed = False  
      for i_s in i_ss:
        try:
          nx.shortest_path_length(G.graph, source=node, target=i_s)
          is_isolated_nonseed = True 
          break 
        except  nx.NetworkXNoPath:
          continue 
      if is_isolated_nonseed: continue 
  
      # if minimum distance between node and seed nodes is larger than community diameter, 
      # then it is seed node. 
      is_seed = True 
      for s in ss:
        distance = nx.shortest_path_length(G.graph, source=node, target=s)
      
        if distance < _cmty_diameter: 
          is_seed = False
          break
      if is_seed: ss.append(node)
   
      # Stop finding seed nodes 
      if len(ss)+len(i_ss) == NUM_CMTY: 
        break

    _cmty_diameter -= 1 
  
  num_found_seeds = len(i_ss)+len(ss)
  assert num_found_seeds == NUM_CMTY , f"[!] FAILED finding seed nodes, expected: {NUM_CMTY}, found: {num_found_seeds}"

  seed_nodes = ss+i_ss
  assert seed_nodes is not None and len(seed_nodes) > 0, f"[!] ERROR weird seed_nodes: {seed_nodes}"
 
  return seed_nodes


def select_seed_nodes(G, NUM_CMTY, cmty_diameter):
  seed_nodes = None 
  
  # Compute centrality 
  for centrality_type in G.centrality:
    compute_centrality(G, centrality_type)
  
  # Sort nodes 
  sorted_nodes = sort_nodes_with_centrality(G)

  # Select seed nodes with community diameter 
  seed_nodes = _select_seed_nodes(G, NUM_CMTY, cmty_diameter, sorted_nodes)
 
  return seed_nodes
  
""" Seed node expansion (diameter based, label propagation) """
def label_propagation(G, labels, max_iter=100):
  for _ in range(max_iter):
    nodes = list(G.graph.nodes)
    random.shuffle(nodes)
    for node in nodes:
      if labels[node] == -1:
        neighbor_labels = [labels[neighbor] for neighbor in G.graph.neighbors(node) if labels[neighbor] != -1]
        if neighbor_labels:
          most_common_label = Counter(neighbor_labels).most_common(1)[0][0]
          if most_common_label == -1: assert False
          labels[node] = most_common_label

  if -1 in list(labels.values()):
    assert False, "[!] ERROR label uncompleted"
  
  return labels


def find_community_by_label_propagation(G, communities):
  labels = {node: -1 for node in G.graph.nodes}

  for community_id, nodes in enumerate(communities.values()):
    for node in nodes:
      labels[node] = community_id
  
  final_labels = label_propagation(G, labels, max_iter=100)

  communities = {}
  for node, label in labels.items():
    if label in communities: communities[label].append(node)
    else: communities[label] = [node]
  
  assert len(communities) > 0, f"[!] ERROR found communities: {communities}"
  return communities


def expand_seed_nodes(G, cmty_diameter, seed_nodes):
  communities = None
  cmty_radius = cmty_diameter / 2

  # Find community with community radius
  communities = {seed: [] for seed in seed_nodes}
  for ss in seed_nodes:
    path_lengths = nx.single_source_shortest_path_length(G.graph, ss) # O(V+E)
    for neighbor, length in path_lengths.items():
      if length <= cmty_radius:
        communities[ss].append(neighbor)
  
 
  # Filter out overlapped nodes 
  for node in G.graph.nodes():
    included = []
    for seed, neighbors in communities.items():
      if node in neighbors: 
        included.append(seed)
    
    # When node is overlapped 
    if len(included) > 1: 
      for seed in included:
         communities[seed] = list(filter(lambda x: x!= node, communities[seed]))
  
  
  # Find community with label propagation for nodes beyond community radius 
  communities = find_community_by_label_propagation(G, communities)
  
  assert communities is not None, f"[!] FAILED finding communities: {communities}"
  return communities 


def run(G, NUM_CMTY):

  # Step 1. Approximated community diameter
  cmty_diameter = approximate_cmty_diameter(G, NUM_CMTY)
  
  # Step 2. Select seed nodes 
  seed_nodes = select_seed_nodes(G, NUM_CMTY, cmty_diameter)
 
  # Step 3. Expand seed nodes 
  communities = expand_seed_nodes(G, cmty_diameter, seed_nodes)


  return communities, cmty_diameter


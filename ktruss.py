import networkx as nx
import os
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm


#k-truss decomposition = k-tricontour


def run(G,estimated_communities,output_path):
    subgraph_set = dict()
    community_size = 0
    f = open(output_path+"model/ktruss/ktruss.txt", "w")
    k = 3
    highest_k = 0
    while True:
        nodes = nx.k_truss(G,k)
        if len(nodes.nodes()) == 0:
            highest_k = k-1
            break
        k = k + 1
    k = highest_k
    while True:
        if k == 2:
            break
        nodes = nx.k_truss(G, k)
        if len(nodes.nodes()) != 0:
            result = list(nx.connected_components(nodes))
            if community_size + len(result) > estimated_communities:
                #sort by size of result
                result = sorted(result, key=lambda x: len(x), reverse=True)
                result = result[:estimated_communities-community_size]
                f.write(f"k={k}\tV={len(nodes.nodes())}\tlen={len(result)}\n")
                subgraph_set[k] = result
                community_size += len(result)
                # for i in range(len(result)):
                #     nx.draw(G.subgraph(set(subgraph_set[k][i])), with_labels=True)
                #     plt.savefig(f"{output_path}/model/ktruss/ktruss_{k}-truss_{i}.png")
                #     plt.clf()
                break
            f.write(f"k={k}\tV={len(nodes.nodes())}\tlen={len(result)}\n")
            subgraph_set[k] = result
            community_size += len(result)
            # for i in range(len(result)):
            #     nx.draw(G.subgraph(set(subgraph_set[k][i])), with_labels=True)
            #     plt.savefig(f"{output_path}/model/ktruss/ktruss_{k}-truss_{i}.png")
            #     plt.clf()
            G = G.subgraph(set(G.nodes()) - set(nodes.nodes()))
        k = k - 1
    f.close()

    seed_subgraph = []
    for subgraphs in subgraph_set.values():
        seed_subgraph.extend(subgraphs)

    return seed_subgraph



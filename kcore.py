import networkx as nx
import os
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
#k-core decomposition


def run(G,estimated_communities,output_path):
    community_size = 0
    subgraph_set = dict()
    f = open(output_path+"/kcore.txt", "w")
    while True:
        core_number = nx.core_number(G)
        k = max(core_number.values())
        if k == 0:
            break
        nodes = nx.k_core(G,max(core_number.values()))
        if len(nodes.nodes()) == 0:
            break
        result = list(nx.connected_components(nodes))
        print("k-core", k, "V=", len(nodes.nodes()), "\tlen=", len(result))
        #write the file

        f.write(f"k={k}\tV={len(nodes.nodes())}\tlen={len(result)}\n")


        if community_size + len(result) > estimated_communities:
            break
        subgraph_set[k] = result
        community_size += len(result)
        for i in range(len(result)):
            nx.draw(G.subgraph(set(subgraph_set[k][i])), with_labels=True)
            plt.savefig(f"{output_path}/fig/kcore/kcore_{k}-core_{i}.png")
            plt.clf()
        G = G.subgraph(set(G.nodes()) - set(nodes.nodes()))
    f.close()
    # seed_subgraph is concat the list of  subgraph_set.values()
    seed_subgraph = []
    for subgraphs in subgraph_set.values():
        seed_subgraph.extend(subgraphs)

    return seed_subgraph



# def run(G):
#     k = 2
#     subgraph_set = dict()
#     while True:
#         nodes = nx.k_core(G,k)
#         if len(nodes.nodes()) == 0:
#             break
#         result = list(nx.connected_components(nodes))
#         print("k-core", k, "V=", len(nodes.nodes()), "\tlen=", len(result))
#         subgraph_set[k] = result
#         nx.draw(G.subgraph(set(subgraph_set[k][0])), with_labels=True)
#         plt.savefig(f"kcore_{k}.png")
#         k += 1
#
#     return subgraph_set

# def run(G):
#     core_number = nx.core_number(G)
#
#     nx.draw(G, labels=core_number, with_labels=False, node_color=list(core_number.values()), cmap=cm.rainbow)
#
#     plt.savefig("kcore_allnode_TC1-3.png")
#     plt.show()


# def run(G,estimated_communities):
#     k=17
#     nodes = nx.k_core(G,k)
#
#     nx.draw(G.subgraph(nodes), with_labels=True,  cmap=cm.rainbow)
#
#     plt.savefig("kcore_17_TC1-1.png")
#     plt.show()
import argparse
import time
import sys
import networkx as nx
import kcore
import ktruss
import label_propagation as LP
import evaluation as EV
import centrality_diameter_seednode as CDS
import utils

sys.setrecursionlimit(10000)




#############################################################################
parser = argparse.ArgumentParser(description='Run algorithm on network')

parser.add_argument('--model', default="ktruss",
                    help='specify model name (kcore,ktruss)')
parser.add_argument('--network', default=f"./data/TC1/TC1-1/1-1.dat",help='a network file name')
parser.add_argument('--approach', default="seedsubgraph",help='Specify approach name (seednode, seedgraph)')
parser.add_argument('--num-community', default=2,help='Specify the number of communities on the network')
parser.add_argument("--centrality", type=str, required=False, default="degree,eigenvector,local_clustering_coefficient,PageRank", help="Centrality measures to use (degree, eigenvector, local_clustering_coefficient, PageRank)")


args = parser.parse_args()



# Global Parameter
G = None
detected_communities = None
cmty_diamter = None
#############################################################################




cmty_etimate_result= {
    'TC1-1': 137,
    'TC1-2': 151,
    'TC1-3': 171,
    'TC1-4': 186,
    'TC1-5': 209,
    'TC1-6': 230,
    'TC1-7': 256,
    'TC1-8': 296,
    'TC1-9': 294,
    'TC1-10': 294,
    'karate': 2,
    'dolphin': 3,
    'football': 8,
    'railway': 19,
    'polbooks': 5,
    'strike': 2,
    'mexican': 3
}


G = nx.read_edgelist(args.network)
G.remove_edges_from(nx.selfloop_edges(G))

estimate_communities = utils.get_estimated_value(args.network, cmty_etimate_result)
if estimate_communities is None:
    estimate_communities = args.estimateCmty

print("network:\t", args.network)
print("entire graph V=", G.number_of_nodes(), "\tE=", G.number_of_edges())
print("approach:\t", args.approach)
print("num-community:\t", estimate_communities)
if args.approach == "seednode":
    print("centrality measures to use:\t", args.centrality)
else:
    print("model:\t", args.model)
print("output:\t", args.network.replace('.dat', f'_{args.approach}.cmty'))

#seed node based approach
if args.approach == "seednode":
    G = CDS.Graph(graph=G, graph_path=args.network,
              centrality={centrality_measure: {} for centrality_measure in args.centrality.split(",")})

    start_time = time.time()
    detected_communities,cmty_diameter = CDS.run(G, estimate_communities)
    end_time = time.time()
    detected_communities = list(detected_communities.values())
    G = G.graph

#seed subgraph based approach
elif args.approach == "seedsubgraph":

    subgraph_set = dict()
    seed_subgraph = None
    start_time = time.time()

    if args.model == 'kcore':
        seed_subgraph = kcore.run(G, estimate_communities, utils.get_base(args.network))
    elif args.model == 'ktruss':
        seed_subgraph = ktruss.run(G, estimate_communities, utils.get_base(args.network))

    # label propagation with nodes in G - seed_subgraph
    detected_communities = LP.label_propagation(G, seed_subgraph)

    end_time = time.time()


# save community
output_file_path = args.network.replace('.dat', f'_{args.approach}.cmty')
sorted_community_items = utils.save_communities_to_file(detected_communities,output_file_path)


# save result
with open(utils.get_base(args.network) + args.approach + "_result.txt", 'w') as f:
    f.write("Network:\t" + args.network + "\n")
    f.write("entire graph V=" + str(G.number_of_nodes()) + "\tE=" + str(G.number_of_edges()) + "\n")
    f.write("Time:\t" + str(end_time - start_time) + "\n")
    f.write("estimate community:\t" + str(estimate_communities) + "\n")
    if args.approach == "seednode":
        f.write("approximated diamter:\t" + str(cmty_diamter) + "\n")
    if args.approach == "seedsubgraph":
        f.write("model:\t" + args.model + "\n")
    nmi_score, f1_score, ari_score = EV.eval(args.network, args.approach)
    f.write(f"nmi_score: {nmi_score}\n")
    f.write(f"ari_score: {ari_score}\n")
    f.write(f"f1_score: {f1_score}\n")

#print result
print("------------RESULT------------")
print("Time:\t", end_time - start_time)
print("estimate community:\t", estimate_communities)
if args.approach == "seednode":
    print("approximated diamter:\t", cmty_diamter)
print("nmi_score:\t", nmi_score)
print("ari_score:\t", ari_score)
print("f1_score:\t", f1_score)
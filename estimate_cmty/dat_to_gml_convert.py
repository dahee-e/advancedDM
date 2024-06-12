# Convert .dat file to .gml file

def read_dat_file(file_path):
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            node1, node2 = map(int, line.split())
            edges.append((node1, node2))
    return edges


def write_gml_file(edges, output_path):
    nodes = set()
    for edge in edges:
        nodes.update(edge)

    with open(output_path, 'w') as file:
        file.write("graph\n[\n")

        for node in sorted(nodes):
            file.write(f"  node\n  [\n    id {node}\n    label \"{node}\"\n  ]\n")

        for edge in edges:
            source, target = edge
            file.write(f"  edge\n  [\n    source {source}\n    target {target}\n    value 1\n  ]\n")

        file.write("]\n")


file_name = {'karate',
                'dolphin',
                'football',
                'railway',
                'polbooks',
                'strike',
                'mexican'}
# #synthetic data
# for number in range(1, 11):
#     dat_file_path = f'../data/TC1/TC1-{number}/1-{number}.dat'
#     gml_file_path = dat_file_path.replace('.dat', '.gml')
#
#     edges = read_dat_file(dat_file_path)
#     write_gml_file(edges, gml_file_path)
#
# #real world data
# for file in file_name:
#     dat_file_path = f'../data/real_world/{file}/network.dat'
#     gml_file_path = dat_file_path.replace('.dat', '.gml')
#     #
#     edges = read_dat_file(dat_file_path)
#     write_gml_file(edges, gml_file_path)


dat_file_path = f'../data/scalability/tc15.dat'
gml_file_path = dat_file_path.replace('.dat', '.gml')
edges = read_dat_file(dat_file_path)
write_gml_file(edges, gml_file_path)
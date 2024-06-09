# 

MICA is a clustering tool for single-cell RNA-seq data. MICA takes a preprocessed gene expression matrix as input and
efficiently cluster the cells.
MICA consists of the following main components:
1. Mutual information estimation for cell-cell distance quantification
2. Dimension reduction on the non-linear mutual information-based distance space
3. Consensus clustering on dimension-reduced spaces
4. Clustering visualization and cell type annotation







## Usage
MICA workflow has two built-in dimension reduction methods. The auto mode (```mica``` or ```mica auto```) 
selects a dimension reduction method automatically based on the cell count of the preprocessed matrix. 
Users can select graph embedding method (```mica ge```)  or MDS (```mica mds```) or Louvain (```mica louvain```) method manually using the subcommand 
```ge``` or ```mds``` or ```louvain``` respectively. 
```
$ mica -h
usage: mica [-h] {auto,ge,mds} ...

MICA - Mutual Information-based Clustering Analysis tool.



optional arguments:
  -h, --help     show this help message and exit

subcommands:
  {auto,ge,mds}  versions
    auto         automatic version
    ge           graph embedding version
    mds          MDS version
    louvain      simple louvain version
```
Use ```mica ge -h```, ```mica mds -h```, and ```mica louvain -h``` to check helps with subcommands.

#### Inputs
The main input for MICA is tab-separated cells/samples by genes/proteins (rows are cells/samples) expression 
matrix or an [anndata](https://anndata.readthedocs.io/en/latest/index.html) file after preprocessing.


#### Outputs
After the completion of the pipeline, `mica` will generate the following outputs:
* Clustering results plot with clustering label mapped to each cluster
* Clustering results txt file with visualization coordinates and clustering label


## Examples
#### Running MICA auto mode
MICA auto mode reduces the dimensionality using either the multidimensional scaling method (<= 5,000 cells) or 
the graph embedding method (> 5,000 cells), where the number of cells cutoff was chosen based on performance
evaluation of datasets of various sizes. 

`mica auto -i ./test_data/inputs/10x/PBMC/3k/pre-processed/pbmc3k_preprocessed.h5ad -o ./test_data/outputs -pn pbmc3k -nc 10`

#### Running MICA GE mode
MICA GE mode reduces the dimensionality using the graph embedding method. It sweeps a range of resolutions
of the Louvain clustering algorithm. ```-ar``` parameter sets the upper bound of the range.

`mica ge -i ./test_data/inputs/10x/PBMC/3k/pre-processed/pbmc3k_preprocessed.h5ad -o ./test_data/outputs
-ar 4.0 -ss 1`

The default setting is to build the MI distance-based graph with the K-nearest-neighbors algorithm, and the number of the neighbors can be set with ```-nnm```. Another way to build the graph is to run approximate-nearest-neighbors(ann) based on the Hierarchical Navigable Small World(HNSW) algorithm. Set ```-nnt```(knn or ann) to enable nn type selection.

Here are 2 main hyperparameters in ann, ef(```-annef```) and m(```-annm```). Suggested setting:
* default
* Really fast m = 4, ef = 200
* Accurate m = 16, ef = 800

Optimize these 2 parameters to make them work on your case, to make the ge mode both fast and robust. Please increase ef when ```-nnm``` is increased.

`mica ge -i ./test_data/inputs/10x/PBMC/3k/pre-processed/pbmc3k_preprocessed.h5ad -o ./test_data/outputs
-nnt ann -annm 8 -annef 400 -ar 4.0 -ss 1`

To set the number of neighbors in the graph for Louvain clustering, please set ```-nne```

#### Running seed-node approach
MICA MDS mode reduces the dimensionality using the multidimensional scaling method. It includes both Kmeans clustering and louvain clustering.
To run KMeans mode please set ```-nck```, to run louvain graph clustering, please set ```-nn``` or as default.
```-pn``` parameter sets the
project name; ```-nck``` specifies the numbers of clusters (k in k-mean clustering algorithm); ```-dd``` is the
number of dimensions used in performing k-mean clusterings in the dimension reduced matrix.

`mica mds -i ./test_data/inputs/10x/PBMC/3k/pre-processed/pbmc3k_preprocessed.h5ad -o 
./test_data/outputs -pn PBMC3k -nck 8`


## Some sharing parameters
```--network```: 




## Reference
Estimate the number of communities : https://github.com/nmslib/hnswlib. The author of MICA adds a 'mutual-info-distance' to the space of hnswlib.

To be added

# Community Detection Based on Estimated Number of Communities

This repository contains two primary algorithms for community detection:

1. Centrality-based Community Detection (CCD)
2. Truss-based Community Detection (TCD)



## 1️⃣ Running Estimated Number of Communities

To estimate the number of communities, ensure your input file is in `.gml` format.

##### ✅ Run the Estimation code 
Navigate to the `estimate_cmty` directory and run the following command:
```
cd estimate_cmty 
./communities < input.gml > output.txt
```

##### Example : Estimating the number of communities in TC1 dataset. 
```
./communities < ../data/TC1/TC1-1/1-1.gml > ./estimate_value/TC1.txt
./communities < ../data/TC1/TC1-2/1-2.gml > ./estimate_value/TC2.txt
./communities < ../data/TC1/TC1-3/1-3.gml > ./estimate_value/TC3.txt
./communities < ../data/TC1/TC1-4/1-4.gml > ./estimate_value/TC4.txt
./communities < ../data/TC1/TC1-5/1-5.gml > ./estimate_value/TC5.txt
./communities < ../data/TC1/TC1-6/1-6.gml > ./estimate_value/TC6.txt
./communities < ../data/TC1/TC1-7/1-7.gml > ./estimate_value/TC7.txt
./communities < ../data/TC1/TC1-8/1-8.gml > ./estimate_value/TC8.txt
./communities < ../data/TC1/TC1-9/1-9.gml > ./estimate_value/TC9.txt
./communities < ../data/TC1/TC1-10/1-10.gml > ./estimate_value/TC10.txt
```

##### Example : Estimating the number of communities in Real-World dataset. 
```
./communities < ../data/real_world/karate/karate.gml > ./estimate_value/karate.txt
./communities < ../data/real_world/dolphin/dolphin.gml > ./estimate_value/dolphin.txt
./communities < ../data/real_world/football/football.gml > ./estimate_value/football.txt
./communities < ../data/real_world/polbooks/polbooks.gml > ./estimate_value/polbooks.txt
./communities < ../data/real_world/railway/railway.gml > ./estimate_value/railway.txt
./communities < ../data/real_world/mexican/mexican.gml > ./estimate_value/mexican.txt
./communities < ../data/real_world/strike/strike.gml > ./estimate_value/strike.txt
```
### 📊 Results: Estimated Number of Communities


#### Synthetic Datasets (TC1-1 to TC1-10)

| Dataset | Estimated Communities | Dataset | Estimated Communities |
|:-------:|:----------------------:|:-------:|:----------------------:|
| TC1-1   | 137                    | TC1-6   | 230                    |
| TC1-2   | 151                    | TC1-7   | 256                    |
| TC1-3   | 171                    | TC1-8   | 296                    |
| TC1-4   | 186                    | TC1-9   | 294                    |
| TC1-5   | 209                    | TC1-10  | 294                    |

#### Real-World Datasets 

|  Dataset  | Estimated Communities |
|:---------:|:----------------------:|
|  Karate   | 2                      |
|  Strike   | 2                      |
|  Mexican  | 3                      |
|  Dolphin  | 3                      |
| Polbooks  | 5                      |
| Football  | 8                      |
|  Railway  | 19                     |




## 2️⃣ Running Community Detection Algorithms

### (1) Running Centrality-based Community Detection (CCD)
```
python main.py --network <network_path> --approach seednode --numCommunity <the number of communities>
```

##### Example : Running CCD in TC1 dataset. 
```
python main.py --network ./data/TC1/TC1-1/1-1.dat --approach seednode --numCommunity 137
python main.py --network ./data/TC1/TC1-2/1-2.dat --approach seednode --numCommunity 151
python main.py --network ./data/TC1/TC1-3/1-3.dat --approach seednode --numCommunity 171
python main.py --network ./data/TC1/TC1-4/1-4.dat --approach seednode --numCommunity 186
python main.py --network ./data/TC1/TC1-5/1-5.dat --approach seednode --numCommunity 209
python main.py --network ./data/TC1/TC1-6/1-6.dat --approach seednode --numCommunity 230
python main.py --network ./data/TC1/TC1-7/1-7.dat --approach seednode --numCommunity 256
python main.py --network ./data/TC1/TC1-8/1-8.dat --approach seednode --numCommunity 296
python main.py --network ./data/TC1/TC1-9/1-9.dat --approach seednode --numCommunity 294
python main.py --network ./data/TC1/TC1-10/1-10.dat --approach seednode --numCommunity 294
```

##### Example : Running CCD in Real-World dataset. 
```
python main.py --network ./data/real_world/dolphin/network.dat --approach seednode  --numCommunity 3
python main.py --network ./data/real_world/karate/network.dat --approach seednode --numCommunity 2
python main.py --network ./data/real_world/football/network.dat --approach seednode --numCommunity 8
python main.py --network ./data/real_world/mexican/network.dat --approach seednode  --numCommunity 3
python main.py --network ./data/real_world/railway/network.dat --approach seednode  --numCommunity 19
python main.py --network ./data/real_world/strike/network.dat --approach seednode --numCommunity 2
python main.py --network ./data/real_world/polbooks/network.dat --approach seednode --numCommunity 5
```

### (2) Running Truss-based Community Detection (TCD)
```
python main.py --network <network_path> --approach seedsubgraph --numCommunity <the number of communities>
```

##### Example : Running TCD in TC1 dataset. 
```
python main.py --network ./data/TC1/TC1-1/1-1.dat --approach seedsubgraph --numCommunity 137
python main.py --network ./data/TC1/TC1-2/1-2.dat --approach seedsubgraph --numCommunity 151
python main.py --network ./data/TC1/TC1-3/1-3.dat --approach seedsubgraph --numCommunity 171
python main.py --network ./data/TC1/TC1-4/1-4.dat --approach seedsubgraph --numCommunity 186
python main.py --network ./data/TC1/TC1-5/1-5.dat --approach seedsubgraph --numCommunity 209
python main.py --network ./data/TC1/TC1-6/1-6.dat --approach seedsubgraph --numCommunity 230
python main.py --network ./data/TC1/TC1-7/1-7.dat --approach seedsubgraph --numCommunity 256
python main.py --network ./data/TC1/TC1-8/1-8.dat --approach seedsubgraph --numCommunity 296
python main.py --network ./data/TC1/TC1-9/1-9.dat --approach seedsubgraph --numCommunity 294
python main.py --network ./data/TC1/TC1-10/1-10.dat --approach seedsubgraph --numCommunity 294
```

##### Example : Running TCD in Real-World dataset. 
```
python main.py --network ./data/real_world/dolphin/network.dat --approach seedsubgraph  --numCommunity 3
python main.py --network ./data/real_world/karate/network.dat --approach seedsubgraph --numCommunity 2
python main.py --network ./data/real_world/football/network.dat --approach seedsubgraph --numCommunity 8
python main.py --network ./data/real_world/mexican/network.dat --approach seedsubgraph  --numCommunity 3
python main.py --network ./data/real_world/railway/network.dat --approach seedsubgraph  --numCommunity 19
python main.py --network ./data/real_world/strike/network.dat --approach seedsubgraph --numCommunity 2
python main.py --network ./data/real_world/polbooks/network.dat --approach seedsubgraph --numCommunity 5
``` 



#### ❗❗ Required Arguments ❗❗
```--network```: File path of the network

```--numCommunity```: Specify the number of communities in the network 

```--approach```: Specify the approach to detect communities.
- Available approaches are:
  - ```seednode```: Centrality-based Community Detection (CCD)
      - ```--centrality``` : Specify the centrality measure to select seed nodes. (default: degree, eigenvector, local_clustering_coefficient, PageRank)
      - Available centrality measures are:
          - degree
          - eigenvector
          - local_clustering_coefficient
          - PageRank
          - betweenness
      - Our method uses **degree, eigenvector, local_clustering_coefficient, and PageRank** centrality measures to select seed nodes. (default setting)
      - Example Usage:
        ```
        python main.py --network <network_path> --approach seednode --numCommunity <the number of communities> --centrality <centrality_measure>
        ```
  - ```seedsubgraph```: Truss-based Community Detection (TCD)




##### Reference
[1] Newman, Mark EJ, and Gesine Reinert. "Estimating the number of communities in a network." Physical review letters 117.7 (2016): 078301. 
- [Link to paper](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.117.078301)
- [Source code](http://www.umich.edu/~mejn/communities/communities.zip)

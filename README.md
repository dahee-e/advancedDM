# Community Detection Based on Estimated Number of Communities
[Group10 : Dahee Kim,Eunyeong Sim, Euibun Bae]

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

### ✅ Update the K Value and Run the Estimation Code
1. Navigate to the `estimate_cmty` directory:
   ```
   cd estimate_cmty
   ```

2. Open the `communities.c` file and update the K value:
   - Locate line 22:
     ```c
     #define K 571
     ```
   - Change the value of K to the desired value. For example, to set K to 599:
     ```c
     #define K 599
     ```

3. Compile the code:
   ```
   make
   ```

4. Run the estimation code:
   ```
   ./communities < input.gml > output.txt
   ```

### K Values for Datasets

#### Synthetic Datasets (TC1-1 to TC1-10)

| Dataset | Avg Degree | K   | Dataset | Avg Degree | K   |
|:-------:|:----------:|:---:|:-------:|:----------:|:---:|
| TC1-1   | 16.6882     | 599 | TC1-6   | 16.9008     | 591 |
| TC1-2   | 17.2202     | 580 | TC1-7   | 17.4904     | 571 |
| TC1-3   | 17.175      | 582 | TC1-8   | 16.9754     | 589 |
| TC1-4   | 17.4428     | 573 | TC1-9   | 17.1318     | 583 |
| TC1-5   | 17.2476     | 579 | TC1-10  | 17.43       | 573 |

#### Real-World Datasets

|  Dataset  | Avg Degree | K   |
|:---------:|:----------:|:---:|
|  Karate   | 4.58823     | 7   |
|  Dolphin  | 5.1290      | 12  |
| Football  | 10.6609     | 10  |
|  Railway  | 8.13289     | 37  |
| Polbooks  | 8.4         | 12  |
|  Strike   | 3.16667     | 7   |
|  Mexican  | 6.68571     | 5   |




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
./communities < ../data/real_world/karate/network.gml > ./estimate_value/karate.txt
./communities < ../data/real_world/dolphin/network.gml > ./estimate_value/dolphin.txt
./communities < ../data/real_world/football/network.gml > ./estimate_value/football.txt
./communities < ../data/real_world/polbooks/network.gml > ./estimate_value/polbooks.txt
./communities < ../data/real_world/railway/network.gml > ./estimate_value/railway.txt
./communities < ../data/real_world/mexican/network.gml > ./estimate_value/mexican.txt
./communities < ../data/real_world/strike/network.gml > ./estimate_value/strike.txt
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
python main.py --network <network_path> --approach CCD --numCommunity <the number of communities>
```

##### Example : Running CCD in TC1 dataset. 
```
python main.py --network ./data/TC1/TC1-1/1-1.dat --approach CCD --numCommunity 137
python main.py --network ./data/TC1/TC1-2/1-2.dat --approach CCD --numCommunity 151
python main.py --network ./data/TC1/TC1-3/1-3.dat --approach CCD --numCommunity 171
python main.py --network ./data/TC1/TC1-4/1-4.dat --approach CCD --numCommunity 186
python main.py --network ./data/TC1/TC1-5/1-5.dat --approach CCD --numCommunity 209
python main.py --network ./data/TC1/TC1-6/1-6.dat --approach CCD --numCommunity 230
python main.py --network ./data/TC1/TC1-7/1-7.dat --approach CCD --numCommunity 256
python main.py --network ./data/TC1/TC1-8/1-8.dat --approach CCD --numCommunity 296
python main.py --network ./data/TC1/TC1-9/1-9.dat --approach CCD --numCommunity 294
python main.py --network ./data/TC1/TC1-10/1-10.dat --approach CCD --numCommunity 294
```

##### Example : Running CCD in Real-World dataset. 
```
python main.py --network ./data/real_world/dolphin/network.dat --approach CCD  --numCommunity 3
python main.py --network ./data/real_world/karate/network.dat --approach CCD --numCommunity 2
python main.py --network ./data/real_world/football/network.dat --approach CCD --numCommunity 8
python main.py --network ./data/real_world/mexican/network.dat --approach CCD  --numCommunity 3
python main.py --network ./data/real_world/railway/network.dat --approach CCD  --numCommunity 19
python main.py --network ./data/real_world/strike/network.dat --approach CCD --numCommunity 2
python main.py --network ./data/real_world/polbooks/network.dat --approach CCD --numCommunity 5
```

### (2) Running Truss-based Community Detection (TCD)
```
python main.py --network <network_path> --approach TCD --numCommunity <the number of communities>
```

##### Example : Running TCD in TC1 dataset. 
```
python main.py --network ./data/TC1/TC1-1/1-1.dat --approach TCD --numCommunity 137
python main.py --network ./data/TC1/TC1-2/1-2.dat --approach TCD --numCommunity 151
python main.py --network ./data/TC1/TC1-3/1-3.dat --approach TCD --numCommunity 171
python main.py --network ./data/TC1/TC1-4/1-4.dat --approach TCD --numCommunity 186
python main.py --network ./data/TC1/TC1-5/1-5.dat --approach TCD --numCommunity 209
python main.py --network ./data/TC1/TC1-6/1-6.dat --approach TCD --numCommunity 230
python main.py --network ./data/TC1/TC1-7/1-7.dat --approach TCD --numCommunity 256
python main.py --network ./data/TC1/TC1-8/1-8.dat --approach TCD --numCommunity 296
python main.py --network ./data/TC1/TC1-9/1-9.dat --approach TCD --numCommunity 294
python main.py --network ./data/TC1/TC1-10/1-10.dat --approach TCD --numCommunity 294
```

##### Example : Running TCD in Real-World dataset. 
```
python main.py --network ./data/real_world/dolphin/network.dat --approach TCD  --numCommunity 3
python main.py --network ./data/real_world/karate/network.dat --approach TCD --numCommunity 2
python main.py --network ./data/real_world/football/network.dat --approach TCD --numCommunity 8
python main.py --network ./data/real_world/mexican/network.dat --approach TCD  --numCommunity 3
python main.py --network ./data/real_world/railway/network.dat --approach TCD  --numCommunity 19
python main.py --network ./data/real_world/strike/network.dat --approach TCD --numCommunity 2
python main.py --network ./data/real_world/polbooks/network.dat --approach TCD --numCommunity 5
``` 



#### ❗❗ Required Arguments ❗❗
```--network```: File path of the network

```--numCommunity```: Specify the number of communities in the network 

```--approach```: Specify the approach to detect communities.
- Available approaches are:
  - ```CCD```: Centrality-based Community Detection (CCD)
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
        python main.py --network <network_path> --approach CCD --numCommunity <the number of communities> --centrality <centrality_measure>
        ```
  - ```TCD```: Truss-based Community Detection (TCD)




##### Reference
[1] Newman, Mark EJ, and Gesine Reinert. "Estimating the number of communities in a network." Physical review letters 117.7 (2016): 078301. 
- [Link to paper](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.117.078301)
- [Source code](http://www.umich.edu/~mejn/communities/communities.zip)

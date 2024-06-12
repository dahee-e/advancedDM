#estimate the number of communities
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

python main.py --network ./data/real_world/dolphin/network.dat --approach TCD  --numCommunity 3
python main.py --network ./data/real_world/karate/network.dat --approach TCD --numCommunity 2
python main.py --network ./data/real_world/football/network.dat --approach TCD --numCommunity 8
python main.py --network ./data/real_world/mexican/network.dat --approach TCD  --numCommunity 3
python main.py --network ./data/real_world/railway/network.dat --approach TCD  --numCommunity 19
python main.py --network ./data/real_world/strike/network.dat --approach TCD --numCommunity 2
python main.py --network ./data/real_world/polbooks/network.dat --approach TCD --numCommunity 5

python main.py --network ./data/real_world/dolphin/network.dat --approach CCD  --numCommunity 3
python main.py --network ./data/real_world/karate/network.dat --approach CCD --numCommunity 2
python main.py --network ./data/real_world/football/network.dat --approach CCD --numCommunity 8
python main.py --network ./data/real_world/mexican/network.dat --approach CCD  --numCommunity 3
python main.py --network ./data/real_world/railway/network.dat --approach CCD  --numCommunity 19
python main.py --network ./data/real_world/strike/network.dat --approach CCD --numCommunity 2
python main.py --network ./data/real_world/polbooks/network.dat --approach CCD --numCommunity 5

#ground truth
#python main.py --network ./data/TC1/TC1-1/1-1.dat --approach TCD --numCommunity 214
#python main.py --network ./data/TC1/TC1-2/1-2.dat --approach TCD --numCommunity 211
#python main.py --network ./data/TC1/TC1-3/1-3.dat --approach TCD --numCommunity 195
#python main.py --network ./data/TC1/TC1-4/1-4.dat --approach TCD --numCommunity 219
#python main.py --network ./data/TC1/TC1-5/1-5.dat --approach TCD --numCommunity 217
#python main.py --network ./data/TC1/TC1-6/1-6.dat --approach TCD --numCommunity 205
#python main.py --network ./data/TC1/TC1-7/1-7.dat --approach TCD --numCommunity 176
#python main.py --network ./data/TC1/TC1-8/1-8.dat --approach TCD --numCommunity 215
#python main.py --network ./data/TC1/TC1-9/1-9.dat --approach TCD --numCommunity 199
#python main.py --network ./data/TC1/TC1-10/1-10.dat --approach TCD --numCommunity 203
#
#python main.py --network ./data/TC1/TC1-1/1-1.dat --approach CCD --numCommunity 214
#python main.py --network ./data/TC1/TC1-2/1-2.dat --approach CCD --numCommunity 211
#python main.py --network ./data/TC1/TC1-3/1-3.dat --approach CCD --numCommunity 195
#python main.py --network ./data/TC1/TC1-4/1-4.dat --approach CCD --numCommunity 219
#python main.py --network ./data/TC1/TC1-5/1-5.dat --approach CCD --numCommunity 217
#python main.py --network ./data/TC1/TC1-6/1-6.dat --approach CCD --numCommunity 205
#python main.py --network ./data/TC1/TC1-7/1-7.dat --approach CCD --numCommunity 176
#python main.py --network ./data/TC1/TC1-8/1-8.dat --approach CCD --numCommunity 215
#python main.py --network ./data/TC1/TC1-9/1-9.dat --approach CCD --numCommunity 199
#python main.py --network ./data/TC1/TC1-10/1-10.dat --approach CCD --numCommunity 203
#
#python main.py --network ./data/real_world/dolphin/network.dat --approach TCD  --numCommunity 2
#python main.py --network ./data/real_world/karate/network.dat --approach TCD --numCommunity 2
#python main.py --network ./data/real_world/football/network.dat --approach TCD --numCommunity 12
#python main.py --network ./data/real_world/mexican/network.dat --approach TCD  --numCommunity 2
#python main.py --network ./data/real_world/railway/network.dat --approach TCD  --numCommunity 24
#python main.py --network ./data/real_world/strike/network.dat --approach TCD --numCommunity 3
#python main.py --network ./data/real_world/polbooks/network.dat --approach TCD --numCommunity 3
#
#python main.py --network ./data/real_world/dolphin/network.dat --approach CCD  --numCommunity 2
#python main.py --network ./data/real_world/karate/network.dat --approach CCD --numCommunity 2
#python main.py --network ./data/real_world/football/network.dat --approach CCD --numCommunity 12
#python main.py --network ./data/real_world/mexican/network.dat --approach CCD  --numCommunity 2
#python main.py --network ./data/real_world/railway/network.dat --approach CCD  --numCommunity 24
#python main.py --network ./data/real_world/strike/network.dat --approach CCD --numCommunity 3
#python main.py --network ./data/real_world/polbooks/network.dat --approach CCD --numCommunity 3
#

##scalability test
python main.py --network ./data/scalability/tc11.dat --approach TCD --numCommunity 111
python main.py --network ./data/scalability/tc12.dat --approach TCD --numCommunity 202 &&
python main.py --network ./data/scalability/tc13.dat --approach TCD --numCommunity 306 &&
python main.py --network ./data/scalability/tc14.dat --approach TCD --numCommunity 522 &&
python main.py --network ./data/scalability/tc15.dat --approach TCD --numCommunity

python main.py --network ./data/scalability/tc11.dat --approach CCD --numCommunity 111
python main.py --network ./data/scalability/tc12.dat --approach CCD --numCommunity 202
python main.py --network ./data/scalability/tc13.dat --approach CCD --numCommunity 306
python main.py --network ./data/scalability/tc14.dat --approach CCD --numCommunity 522
python main.py --network ./data/scalability/tc15.dat --approach CCD --numCommunity
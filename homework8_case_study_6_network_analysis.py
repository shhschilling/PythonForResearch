#------------------------------------------------
# Homework 8 - Case Study 6 of course "Python for Research"
# HarvardX -  PH526xEdX, EdX
# Social Network Analysis
#------------------------------------------------
#Exercise 1--------------------
from collections import Counter
def frequency(chars):
    values=chars.values()
    return(Counter(values))

def chance_homophily(chars):
      import numpy as np
      total_N=len(chars.keys())
      f=list(frequency(favorite_colors).values())
      f=np.array(f)
      p=f/total_N
      return(sum(p**2))

#Test case
favorite_colors = {
    "ankit":  "red",
    "xiaoyu": "blue",
    "mary":   "blue"
}

color_homophily = chance_homophily(favorite_colors)
print(color_homophily)

#Exercise 2--------------------
import pandas as pd
df  = pd.read_stata(data_filepath + "individual_characteristics.dta")
df1 = df.loc[df['village'] == 1]
df2 = df.loc[df['village'] == 2]

#Exercise 3--------------------
#set index to pid
df11=df1.set_index('pid')
df22=df2.set_index('pid')

#transform to dictionary with method .to_dict()
sex1=df11.resp_gend.to_dict()
caste1=df11.caste.to_dict()
religion1 =df11.religion.to_dict()


sex2=df22.resp_gend.to_dict()
caste2=df22.caste.to_dict()
religion2 =df22.religion.to_dict()


#Exercise 4--------------------
print("Village 1 chance of same sex:", chance_homophily(sex1))
# Enter your code here.
print("Village 1 chance of same caste:", chance_homophily(caste1))
print("Village 1 chance of same religion:", chance_homophily(religion1))

print("Village 2 chance of same sex:", chance_homophily(sex2))

print("Village 2 chance of same caste:", chance_homophily(caste2))
print("Village 2 chance of same religion:", chance_homophily(religion2))





#Exercise 5--------------------
#set index to pid
def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties = 0
    num_ties = 0
    for n1, n2 in G.edges():
        if IDs[n1] in chars and IDs[n2] in chars:
            if G.has_edge(n1, n2):
                num_ties=num_ties+1
                if chars[IDs[n1]] == chars[IDs[n2]]:
                    num_same_ties=num_same_ties+1
    return (num_same_ties / num_ties)

#Exercise 6--------------------
#data_filepath on local installation

pid1  = pd.read_csv(data_filepath + "key_vilno_1.csv",header=None)
pid2  = pd.read_csv(data_filepath + "key_vilno_2.csv",header=None)

#Exercise 7--------------------
print("Village 1 observed proportion of same sex:", homophily(G1, sex1, pid1))
print("Village 1 observed proportion of same caste:", homophily(G1, caste1, pid1))
print("Village 1 observed proportion of same religion:", homophily(G1, religion1, pid1))

print("Village 1 chance of homophilyhily by same sexe:",chance_homophily(sex1))
print("Village 1 chance of homophily by same caste:",chance_homophily(caste1))
print("Village 1 chance of homophily by same religion:",chance_homophily(religion1))



print("Village 2 observed proportion of same sex:", homophily(G2, sex2, pid2))
print("Village 2 observed proportion of same caste:", homophily(G2, caste2, pid2))
print("Village 2 observed proportion of same religion:", homophily(G2, religion2, pid2))


print("Village 2 chance of homophilyhily by same sexe:",chance_homophily(sex2))
print("Village 2 chance of homophily by same caste:",chance_homophily(caste2))
print("Village 2 chance of homophily by same religion:",chance_homophily(religion2))

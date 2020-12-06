# Neccessary import
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from sklearn.decomposition import PCA # For principal components analysis
from sklearn.cluster import KMeans # For k-means cluster algorithm

file_2017 = pd.read_csv("2017.csv")
file_2018 = pd.read_csv("2018.csv")
file_2019 = pd.read_csv("2019.csv")

final_data = pd.concat([file_2017, file_2018, file_2019], axis=0)

country_list=pd.unique(final_data['country'])
type_list=pd.unique(final_data['event_type'])

type_count_data=pd.DataFrame(columns=type_list)


# Go through every single type of the conflicts in every country
# And make a count
index = 0
for country in country_list:
    for type_name in type_list:
        count=final_data[(final_data['country']==country) & (final_data['event_type']==type_name)].shape[0]
        type_count_data.loc[index, type_name] = count
    index += 1
type_count_data.head()

# Use PCA to do dimentionality reduction
def getPCAData(data,comp):
    PCA_data = PCA(n_components=comp, whiten=True)
    PCA_data.fit(data)
    result = PCA_data.transform(data) # Dimension reduction
    return result
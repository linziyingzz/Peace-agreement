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

def getKMeansData(PCA_data,k):
    kmeans_data = pd.DataFrame(columns=['x', 'y'])
    for index, value in enumerate(PCA_data):
        new_row={'x': value[0], 'y': value[1]}
        kmeans_data=kmeans_data.append(new_row, ignore_index=True)
    kmeans_model=KMeans(n_clusters=k).fit(PCA_data)
    labels=kmeans_model.labels_.astype(int)
    kmeans_data['country']=country_list
    kmeans_data['predicted_label']=labels
    return kmeans_data

def drawKMeansResult(kmeans_data):
    plt.figure(figsize=(10,7))
    sns.scatterplot(x=kmeans_data['x'], y=kmeans_data['y'], hue="predicted_label", 
                data=kmeans_data,palette="muted");

PCA_data=getPCAData(type_count_data, 2)
kmeans_data=getKMeansData(PCA_data, 5)
drawKMeansResult(kmeans_data)
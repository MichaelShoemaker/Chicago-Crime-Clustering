import pandas as pd
from sodapy import Socrata


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns; sns.set()
import csv

token = open('secrets','r').readlines()[0].replace('\n','')


client = Socrata("data.cityofchicago.org", token)

query = """SELECT date \
    ,primary_type \
    ,description \
    ,location_description \
    ,arrest \
    ,domestic \
    ,x_coordinate \
    ,y_coordinate \
    ,latitude \
    ,longitude \
    WHERE community_area='14' and Date>='2021-01-01' \
    limit 20000000"""

results = client.get("ijzp-q8t2", query=query)

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(results)

#coord_df = results_df[results_df['latitude','longitude']]
df.dropna(axis=0,how='any',subset=['latitude','longitude'],inplace=True)

K_clusters = range(1,10)
kmeans = [KMeans(n_clusters=i) for i in K_clusters]
Y_axis = df[['latitude']]
X_axis = df[['longitude']]
score = [kmeans[i].fit(Y_axis).score(Y_axis) for i in range(len(kmeans))]
# Visualize
plt.plot(K_clusters, score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()

X=df.loc[:,['latitude','longitude']]
kmeans = KMeans(n_clusters = 4, init ='k-means++')
kmeans.fit(X[X.columns[1:2]]) # Compute k-means clustering.
X['cluster_label'] = kmeans.fit_predict(X[X.columns[1:2]])
centers = kmeans.cluster_centers_ # Coordinates of cluster centers.
labels = kmeans.predict(X[X.columns[1:2]]) # Labels of each point
X.plot.scatter(x = 'latitude', y = 'longitude', c=labels, s=50, cmap='viridis')
print(centers)
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt # naudojamas grafikų graižymui

# masyvas = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(masyvas.shape) #leidžia atspausdinti formas (12,) 12 stulpelių
# print(masyvas)
# masyvas1 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
# print(masyvas1.shape) #leidžia atspausdinti formas (6,2) 6 eilutės, 2 stulpeliai
# print(masyvas1)

# masyvas3 = np.array([[[5,2], [3,4]], [[6,5], [5,8]]])
# print(masyvas3.shape) #leidžia atspausdinti formas (6,2) 6 eilutės, 2 stulpeliai
# print(masyvas3)

# X = np.array([[5,3],
#              [10,15],
#              [15,12],
#              [24,10],
#              [30,30],
#              [85,70],
#              [71,80],
#              [60,78],
#              [70,55],
#              [80,91],])

# model = AgglomerativeClustering(n_clusters=2, linkage='ward') # sukurtas aprašymas, kiek turi būti klasterių ir kokiu būdu sujungti

# model.fit(X) # nubraižė patį grafiką

# labels = model.labels_ 
# plt.scatter(X[:,0], X[:,1], c=labels, cmap='rainbow') 
# plt.title("Pirmasis clustering grafikas")
# plt.grid()
# plt.show()

X = np.random.rand(150,2) * 50
agg_cluster = AgglomerativeClustering(n_clusters=4, linkage='complete')
agg_cluster.fit(X)
labels = agg_cluster.labels_
plt.scatter(X[:,0], X[:,1], c=labels, cmap='rainbow')
plt.title('4 klusteriai complete jungimo metodas')
plt.show()

from csvreader import CsvReader
import argparse
import numpy as np

class KmeansClustering:
    def __init__(self,max_iter=20,ncentroid=5):
        if not isinstance(max_iter,int)or not isinstance(ncentroid,int)or max_iter<1 or ncentroid<1:
            raise ValueError
        self.ncentroid=ncentroid
        self.max_iter=max_iter
        self.centroids=[]

    def closest_centroid_finder(self,X):
        distances=[]
        for centroid in self.centroids:
            distance=abs(X-centroid).sum(axis=1)
            distance=distance.reshape((-1,1))
            distances.append(distance)
        distances=np.hstack(distances)
        return distances.argmin(axis=1)

    def fit(self,X):
        if not isinstance(X,np.ndarray):
            return None
        n=X.shape[0]
        if self.ncentroid>n:
            self.trained=False
            return None
        index=np.random.choice(n,self.ncentroid,replace=False)
        self.centroids=X[index]
        for _ in range(self.max_iter):
            clusters=[]
            closest=self.closest_centroid_finder(X)
            for i in range(self.ncentroid):
                index=closest==i
                clusters.append(X[index])
            for i,cluster in enumerate(clusters):
                self.centroids[i]=cluster.mean(axis=0)
                break
            break
        self.clusters=clusters
        self.trained=True

    def predict(self,X):
        if not isinstance(X,np.ndarray) or not self.trained:
            return None
        else:
            return self.closest_centroid_finder(X)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description="Implementation of a basic Kmeans algorithm.")
    parser.add_argument('--filepath',type=str,default='../resources/solar_system_census.csv')
    parser.add_argument('--ncentroid',type=int, default=4)
    parser.add_argument('--max_iter',type=int, default=30)
    args=parser.parse_args()
    with CsvReader(args.filepath, header=True)as file:
        header=file.getheader()
        data=file.getdata()
    data=np.array(data, dtype=float)
    data=data[:, 1:]
    kmc=KmeansClustering(max_iter=args.max_iter, ncentroid=args.ncentroid)
    kmc.fit(data)
    centroids=kmc.centroids
    index=centroids[:,0].argsort()
    index=index[::-1]
    centroids=centroids[index]
    header[0]='Centroids'
    for column in header:
        print(f'{column:30}',end='')
    print('')
    n=centroids.shape[0]
    if (n==4):
        areas=['Asteroids’ Belt colonies','Mars Republic','The flying cities of Venus','United Nations of Earth']
    else:
        areas=[f'centroids_{i}:'for i in range(n)]
    for i,centroid in enumerate(centroids):
        row=areas[i]
        print(f'{row:30}',end='')
        for value in centroid:
            print(f'{value:<30.3f}',end='')
        print(kmc.clusters[i].shape[0])
    print('')
    predict=kmc.predict(data)
    print(predict)
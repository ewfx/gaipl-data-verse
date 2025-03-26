from sklearn.cluster import KMeans
import pandas as pd
import joblib

data = pd.read_csv("data/tickets.csv")
X = data[["category"]]

model = KMeans(n_clusters=3)
model.fit(X)

joblib.dump(model, "models/clustering_model.pkl")

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Principal Component Analysis(PCA)
# %% [markdown]
# Principal Component Analysis, or PCA, is a dimensionality-reduction method that is often used to reduce the dimensionality of large data sets, by transforming a large set of variables into a smaller one that still contains most of the information in the large set.
# %% [markdown]
# Reducing the number of variables of a data set naturally comes at the expense of accuracy, but the trick in dimensionality reduction is to trade a little accuracy for simplicity. Because smaller data sets are easier to explore and visualize and make analyzing data much easier and faster for machine learning algorithms without extraneous variables to process.
# So to sum up, the idea of PCA is simple — reduce the number of variables of a data set, while preserving as much information as possible.

# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# %%
from sklearn.datasets import load_breast_cancer


# %%
cancer=load_breast_cancer()


# %%
cancer.keys()


# %%
print(cancer['DESCR'])


# %%
df=pd.DataFrame(cancer['data'],columns=cancer['feature_names'])


# %%
df.head(5)


# %%
from sklearn.preprocessing import StandardScaler


# %%
scaler=StandardScaler()
scaler.fit(df)


# %%
scaled_data=scaler.transform(df)


# %%
scaled_data


# %%
from sklearn.decomposition import PCA


# %%
pca=PCA(n_components=2)


# %%
pca.fit(scaled_data)


# %%
x_pca=pca.transform(scaled_data)


# %%
scaled_data.shape


# %%
x_pca.shape


# %%
scaled_data


# %%
x_pca


# %%
plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'])
plt.xlabel('First principle component')
plt.ylabel('Second principle component')



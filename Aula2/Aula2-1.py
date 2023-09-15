import numpy as np
import pandas as pd
import warnings 
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

#https://dontpad.com/aula_quinta_25_08@2023

# Documentação pandas: 
# https://pandas.pydata.org/docs/

warnings.filterwarnings("ignore")

df = pd.read_csv('/workspaces/Aulas-python/Aula2/Mall_Customers.csv', sep=',', encoding='iso-8859-1')

#head = df.head()
# print(head)

#tail = df.tail()
# print(tail)

#shape = df.shape
# print(shape)

#describe = df.describe()
# print(describe)

# describe_2 = df.describe().T
# print(describe_2)

# métodos de estatística
# df.mean()
# df.std()
# df.median()
# df.mode()
# df.var()
# df.count()
# df.min()

# hist = px.histogram(df, x = "Age", nbins=60)
# hist.update_layout(width=600, height= 400, title_text="Distribuição das idades")
# hist.show()

# genre = df['Genre'].value_counts()
# print(genre)

# spending_score = df['Spending Score (1-100)'].value_counts().sort_index()
# print(spending_score)


# snscountplot = sns.countplot(x='Genre', data=df);
# print(snscountplot)

df.info()

# df.rename(columns={'CustomerID': 'identificacao'}, inplace=True)
# df.rename(columns={'Genre': 'genero'}, inplace=True)
# df.rename(columns={'Age': 'idade'}, inplace=True)
# df.rename(columns={'Annual Income (k$)': 'rendimento','Spending Score (1-100)':'pontuacao'}, inplace=True)

boxplot = px.box(df, y='rendimento')
boxplot.show()

filtro  = df['rendimento'] < 137
df1 = df[filtro]

boxplot = px.box(df, x='rendimento')
boxplot.show()

boxplot = px.box(df, y='idade')
boxplot.show()


sns.catplot(data=df, x='genero', y='rendimento', kind="box")

# fig = px.box(df1, x='genero',y='rendimento')
# fig.show()

#df.hist(bins=8,figsize=(5,5),color='#7178d7')

f,ax = plt.subplots(figsize=(10,10));
sns.heatmap(df1.isnull());


df2 = df.drop(labels = 'identificacao', axis = 1)
df2.head(2)


df2['genero'].replace({'Female': 0, 'Male': 1}, inplace=True)

df2.head(3)

f,ax = plt.subplots(figsize=(4,4));
sns.heatmap(df2[['genero','idade', 'rendimento','pontuacao']].corr(),annot=True, cmap='Blues');





















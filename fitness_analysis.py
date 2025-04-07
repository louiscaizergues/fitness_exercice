# 🏋️‍♂️ Fitness Sales Analysis

# 🎯 Objectifs
# - Identifier les produits les plus performants
# - Analyser les canaux de vente et les zones géographiques les plus rentables
# - Extraire des insights business actionnables

# 📦 Chargement et préparation des données
import pandas as pd
from google.colab import files
import matplotlib.pyplot as plt
import seaborn as sns

uploaded = files.upload()
df = pd.read_csv("fitness_sales_data.csv")

df['order_date'] = pd.to_datetime(df['order_date'])
df['total_sales'] = df['price'] * df['quantity']
df['month'] = df['order_date'].dt.to_period('M')

print(df.head())

# 🔍 Analyse exploratoire

# Top 5 produits en volume
top_produits = df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(5)
print(top_produits)

# Top 5 produits en chiffre d'affaires
top_sales_products = df.groupby('product_name')['total_sales'].sum().sort_values(ascending=False).head(5)
print(top_sales_products)

# Évolution mensuelle du CA
monthly_trend = df.groupby('month')['total_sales'].sum()
print(monthly_trend)

# Répartition du CA par région
region = df.groupby('region')['total_sales'].sum()
print(region)

# Répartition du CA par canal de vente
channel = df.groupby('sales_channel')['total_sales'].sum()
print(channel)

# 📊 Visualisations

# Top 5 produits par CA avec Seaborn
top_df = top_sales_products.reset_index()
top_df.columns = ['product_name', 'total_sales']

plt.figure(figsize=(8,5))
sns.barplot(data=top_df, x='total_sales', y='product_name', palette='viridis')
plt.title("Top 5 produits par chiffre d'affaires")
plt.xlabel("Total des ventes (€)")
plt.ylabel("Produit")
plt.tight_layout()
plt.show()

# Répartition du CA par canal avec Plotly
!pip install plotly
import plotly.express as px

channel_df = channel.reset_index()
channel_df.columns = ['sales_channel', 'total_sales']

fig = px.pie(channel_df, values='total_sales', names='sales_channel',
             title="Parts de CA par canal de vente",
             color_discrete_sequence=px.colors.sequential.RdBu)
fig.show()

# 💡 Recommandations
# - Mettre en avant les produits générant le plus de CA dans les promos
# - Cibler les canaux les plus rentables (site web ou app ?) pour booster la conversion
# - Optimiser l’offre en fonction des régions les plus actives

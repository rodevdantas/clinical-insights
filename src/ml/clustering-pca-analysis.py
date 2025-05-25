import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import os
# %%

base_dir = os.path.dirname(__file__)
path_pacientes = os.path.join(base_dir, '..', '..', 'data', 'dados_pacientes.csv')
pacientes_df = pd.read_csv(path_pacientes)

pacientes_df['data_nascimento'] = pd.to_datetime(pacientes_df['data_nascimento'])
data_hoje = pd.to_datetime('today')
pacientes_df['idade'] = (data_hoje - pacientes_df['data_nascimento']).dt.days // 365
# %%

pacientes_df['sexo'] = pacientes_df['sexo'].astype(str).str.strip().str.upper()

sexo_map_for_plotting = {'M': 'Masculino', 'F': 'Feminino'}
pacientes_df['sexo'] = pacientes_df['sexo'].map({'M': 1, 'F': 0})

plano_dict = {
    'Popular': 0,
    'Executivo': 1,
    'Premium': 2
}

plano_map_for_plotting = {v: k for k, v in plano_dict.items()}
pacientes_df['plano_saude'] = pacientes_df['plano_saude'].map(plano_dict)
# %%

colunas_cluster = ['idade', 'sexo', 'plano_saude']
X = pacientes_df[colunas_cluster]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# %%

inercia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inercia.append(kmeans.inertia_)

plt.plot(range(1, 11), inercia, marker='o')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('Inércia')
plt.title('Elbow Method')
plt.grid(True)
plt.show()
# %%

kmeans = KMeans(n_clusters=4, random_state=42)
pacientes_df['cluster'] = kmeans.fit_predict(X_scaled)
# %%

# visualizando as colunas x clusters
plt.figure(figsize=(8, 5))
sns.boxplot(x='cluster', y='idade', data=pacientes_df, palette='Set2')
plt.title('Distribuição da Idade por Cluster')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='cluster', hue=pacientes_df['sexo'].map({0: 'Feminino', 1: 'Masculino'}), data=pacientes_df, palette='Set2')
plt.title('Distribuição do Sexo por Cluster')
plt.xlabel('Cluster')
plt.ylabel('Contagem')
plt.legend(title='Sexo')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='cluster', hue=pacientes_df['plano_saude'].map({0: 'Popular', 1: 'Executivo', 2: 'Premium'}), data=pacientes_df, palette='Set2')
plt.title('Distribuição dos Planos por Cluster')
plt.xlabel('Cluster')
plt.ylabel('Contagem')
plt.legend(title='Plano de Saúde')
plt.grid(True)
plt.show()
# %%

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

pacientes_df['PCA1'] = X_pca[:, 0]
pacientes_df['PCA2'] = X_pca[:, 1]

plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='PCA1', y='PCA2',
    hue='cluster',
    palette='Set2',
    data=pacientes_df,
    s=60
)
plt.title('Visualização dos Clusters com PCA')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend(title='Cluster')
plt.grid(True)
plt.show()


















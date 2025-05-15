import pandas as pd
from faker import Faker
import random
import os
# %%
Faker.seed(42)
random.seed(42)
fake = Faker('pt-BR')
num_pacientes = 2000
planos = ['Popular', 'Executivo', 'Premium']
sexos = ['M', 'F']

dados_pacientes = []

for i in range(1, num_pacientes + 1):
    sexo = random.choice(sexos)
    nome = fake.name_male() if sexo == 'M' else fake.name_female()
    data_nascimento = fake.date_of_birth(minimum_age=8, maximum_age=90)
    cidade = fake.city()
    plano = random.choices(planos, weights=[0.7, 0.2, 0.1])[0]
    possui_doenca_cronica = random.choices([True, False], weights=[0.15, 0.85])[0]
    data_cadastro = fake.date_between(start_date='-15y', end_date='today')
    dados_pacientes.append([
        i,
        nome,
        sexo,
        data_nascimento,
        cidade,
        plano,
        possui_doenca_cronica,
        data_cadastro
        ])
    
df_pacientes = pd.DataFrame(dados_pacientes, columns=[
    'id_paciente',
    'nome',
    'sexo',
    'data_nascimento',
    'cidade',
    'plano_saude',
    'possui_doenca_cronica',
    'data_cadastro'
    ])
# %% 

base_dir = os.path.dirname(__file__)
output_path = os.path.join(base_dir, '..', '..', 'data', 'dados_pacientes.csv')

df_pacientes.to_csv(output_path, index=False, encoding='utf-8', errors='replace')


    
    
    





































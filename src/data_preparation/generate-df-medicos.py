import pandas as pd
from faker import Faker
import random
import os
# %%
Faker.seed(42)
random.seed(42)
fake = Faker('pt-BR')

num_medicos = 250
especialidades = ['Cardiologista', 'Pediatra', 'Oftalmologista', 'Dermatologista', 'Ortopedista', 'Ginecologista', 'Urologista']
sexos = ['M', 'F']

dados_medicos = []

for i in range(1, num_medicos + 1):
    sexo = random.choice(sexos)
    if sexo == 'M':
        nome = fake.name_male()
        titulo = 'Dr.'
    else:
        nome = fake.name_female()
        titulo = 'Dra.'
    if 'Dr.' not in nome and 'Dra.' not in nome:
        nome = f"{titulo} {nome}"
    especialidade = random.choice(especialidades)
    crm = f"CRM{random.randint(100000, 999999)}"
    cidade = fake.city()
    telefone = fake.phone_number()
    dados_medicos.append([
        i,
        nome,
        sexo,
        especialidade,
        crm,
        cidade,
        telefone
        ])

df_medicos = pd.DataFrame(dados_medicos, columns=[
    'id_medico',
    'nome',
    'sexo',
    'especialidade',
    'crm',
    'cidade',
    'telefone'
    ])
# %% 

base_dir = os.path.dirname(__file__)
output_path = os.path.join(base_dir, '..', '..', 'data', 'dados_medicos.csv')

df_medicos.to_csv(output_path, index=False, encoding='utf-8', errors='replace')


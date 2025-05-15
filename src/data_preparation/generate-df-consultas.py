from faker import Faker
import pandas as pd
import random
import os
# %%

base_dir = os.path.dirname(__file__)
pacientes_path = os.path.join(base_dir, '..', '..', 'data', 'dados_pacientes.csv')
pacientes = pd.read_csv(pacientes_path)

# %%
Faker.seed(42)
random.seed(42)
fake = Faker('pt-BR')

num_consultas = 6753

def get_valor_consulta(plano):
    if plano == 'Popular':
        return 0
    elif plano == 'Executivo':
        return 100
    elif plano == 'Premium':
        return 500
    
consultas = []
for i in range(1, num_consultas + 1):
    paciente_id = random.choice(range(1,2001))
    medico_id = random.choice(range(1,251))
    data_consulta = fake.date_between(start_date='-1y', end_date='today')
    plano = pacientes[pacientes['id_paciente'] == paciente_id]['plano_saude'].values[0]
    valor_consulta = get_valor_consulta(plano)
    consultas.append([
        paciente_id, 
        medico_id, 
        data_consulta,
        valor_consulta
        ])
    
df_consultas = pd.DataFrame(consultas, columns=[
    'id_paciente',
    'id_medico',
    'data_consulta',
    'valor_consulta'
    ])
# %%

output_path = os.path.join(base_dir, '..', '..', 'data', 'dados_consultas.csv')
df_consultas.to_csv(output_path, index=False, encoding='utf-8', errors='replace')





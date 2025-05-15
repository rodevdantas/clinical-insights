import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
# %% 

dotenv_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path)

usuario = os.getenv('DB_USER', '').strip()
senha = os.getenv('DB_PASSWORD', '').strip()
host = os.getenv('DB_HOST', '').strip()
porta = os.getenv('DB_PORT', '').strip()
database = os.getenv('DB_NAME', '').strip()

string_conexao = f'mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{database}'
# %% 

base_dir = Path(__file__).resolve().parent.parent.parent 
data_dir = base_dir / 'data'

df_pacientes = pd.read_csv(data_dir / 'dados_pacientes.csv')
df_medicos = pd.read_csv(data_dir / 'dados_medicos.csv')
df_consultas = pd.read_csv(data_dir / 'dados_consultas.csv')
# %% 

engine = create_engine(string_conexao)

df_pacientes.to_sql('pacientes', con=engine, if_exists='replace', index=False)
df_medicos.to_sql('medicos', con=engine, if_exists='replace', index=False)
df_consultas.to_sql('consultas', con=engine, if_exists='replace', index=False)

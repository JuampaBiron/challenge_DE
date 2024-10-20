from typing import List, Tuple
from datetime import datetime
from base import Base
import pandas as pd
from memory_profiler import profile, memory_usage
import cProfile
from concurrent.futures import ThreadPoolExecutor
import numpy as np

file_path = Base().twiter_file_path

def process_chunk(chunk):
    chunk['date'] = pd.to_datetime(chunk['date']).dt.date
    chunk['user'] = chunk['user'].apply(lambda x: x['username'] if isinstance(x, dict) else None)
    
    # Obtener los 10 usuarios más comunes por fecha
    top_dates = chunk['date'].value_counts().nlargest(10).index
    df_top_dates = chunk[chunk['date'].isin(top_dates)]
    
    return df_top_dates.groupby('date')['user'].agg(lambda x: x.value_counts().idxmax()).reset_index()

@profile
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:#1521 MiB, 6.5s
    # Leer el archivo JSON directamente en pandas (asumiendo un formato JSON por línea)
    df = pd.read_json(file_path, lines=True)

    # Dividir el DataFrame en bloques para el procesamiento en paralelo
    num_workers = 4
    chunks = np.array_split(df, num_workers)

    # Procesar en paralelo usando ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(process_chunk, chunks))

    # Combinar los resultados
    combined_result = pd.concat(results).groupby('date')['user'].agg(lambda x: x.value_counts().idxmax()).reset_index()

    # Convertir a lista de tuplas
    return list(combined_result.itertuples(index=False, name=None))

if __name__ == "__main__":
    cProfile.run("q1_time(file_path)", sort="tottime")


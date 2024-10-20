import json
from typing import List, Tuple
from datetime import datetime
from base import Base
import pandas as pd
from memory_profiler import profile, memory_usage
import cProfile

file_path = Base().twiter_file_path

@profile
def q1_time(file_path) -> List[Tuple[datetime.date, str]]: #1490 MiB max, 26.44s
    # Leer el archivo JSON directamente en pandas (asumiendo un formato JSON por línea)
    df = pd.read_json(file_path, lines=True)
    df['date'] = pd.to_datetime(df['date']).dt.date
    df['user'] = df['user'].apply(lambda x: x['username'] if isinstance(x, dict) else None)

    # Obtener las 10 fechas con más tweets
    top_dates = df['date'].value_counts().nlargest(10).index

    # Filtrar los tweets en las 10 fechas principales
    df_top_dates = df[df['date'].isin(top_dates)]

    # Obtener el usuario con más tweets por cada una de las fechas principales
    result = df_top_dates.groupby('date')['user'].agg(lambda x: x.value_counts().idxmax()).reset_index()

    # Convertir a lista de tuplas
    return list(result.itertuples(index=False, name=None))

if __name__ == "__main__":
    q1_time(file_path)
    cProfile.run("q1_time2(file_path)", sort="tottime")


import json
from typing import List, Tuple
from datetime import datetime
from base import Base
import pandas as pd
from memory_profiler import profile, memory_usage
import cProfile
from collections import defaultdict, Counter

file_path = Base().twiter_file_path

#@profile
def q1_memory_1(file_path) -> List[Tuple[datetime.date, str]]: #474 MiB max, 31.97s
    content_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
            for obj in file:
                    data = json.loads(obj)
                    tweet_data = {
                    'date': data.get('date'),
                    'user': data.get('user'),
                                }
                    content_list.append(tweet_data)
    # Crear un DataFrame de pandas con los datos
    df = pd.DataFrame(content_list)
    # Extraer las fechas y usuarios
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
@profile
def q1_memory(file_path) -> List[Tuple[datetime.date, str]]:
    date_user_count = defaultdict(Counter)  # Almacena conteos de usuarios por fecha

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            date = data.get('date')
            user = data.get('user')

            if isinstance(user, dict):
                username = user.get('username')
                if date and username:
                    date_user_count[date][username] += 1  # Contar tweets por usuario en cada fecha

    # Obtener las 10 fechas con más tweets
    top_dates = sorted(date_user_count.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]

    # Obtener el usuario con más tweets por cada una de las fechas principales
    result = [(date, user_count.most_common(1)[0][0]) for date, user_count in top_dates]

    return result

if __name__ == "__main__":
    q1_memory(file_path)
    cProfile.run("q1_memory(file_path)", sort="tottime")
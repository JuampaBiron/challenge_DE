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
def q1_memory(file_path) -> List[Tuple[datetime.date, str]]: #150.9 MiB 14.4s   
    date_user_count = defaultdict(Counter)  # Almacena conteos de usuarios por fecha

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            date = data.get('date')
            user = data.get('user')

            if isinstance(user, dict):
                username = user.get('username')
                if date and username:
                    # Convertir la fecha a formato datetime.date
                    date_only = datetime.fromisoformat(date).date() if isinstance(date, str) else None
                    if date_only:
                        date_user_count[date_only][username] += 1  # Contar tweets por usuario en cada fecha
    # Obtener las 10 fechas con más tweets
    top_dates = sorted(date_user_count.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]

    # Obtener el usuario con más tweets por cada una de las fechas principales
    result = [(date, user_count.most_common(1)[0][0]) for date, user_count in top_dates]

    return result

if __name__ == "__main__":
    cProfile.run("q1_memory(file_path)", sort="tottime")
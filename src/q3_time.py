from typing import List, Tuple
import json
import re
from collections import defaultdict
from typing import List, Tuple, Generator
from base import Base
from memory_profiler import profile, memory_usage
import cProfile
import pandas as pd
from collections import Counter

file_path = Base().twiter_file_path
mention_pattern = re.compile(r'[@＠]([a-zA-Z0-9_]{1,20})(/[a-zA-Z][a-zA-Z0-9_-]{0,24})?')

def extract_usernames(content: str) -> List[str]:
    return [match.group(1) for match in mention_pattern.finditer(content)] #almacenamos resultados en una lista. Almacenar en una lista puede reducir el tiempo total de ejecución.

@profile
def q3_time_2(file_path: str) -> List[Tuple[str, int]]: #1465 MiB, 10.52 s
    username_count = Counter()  # Usar Counter para contar usernames
    df = pd.read_json(file_path, lines=True)  # Leer el archivo JSON

    # Procesar la columna 'content' del DataFrame
    for content in df['content'].dropna():  # Omitir NaN directamente
        if isinstance(content, str):  # Verificar si el contenido es una cadena
            # Extraer usernames y actualizar el contador
            username_count.update(extract_usernames(content))

    # Obtener los 10 usernames más comunes
    top_usernames = username_count.most_common(10)
    return top_usernames

if __name__ == "__main__":
    q3_time_2(file_path)
    cProfile.run("q3_time_2(file_path)", sort='tottime')


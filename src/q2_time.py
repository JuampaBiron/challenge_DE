from typing import List, Tuple
from collections import Counter
from memory_profiler import profile, memory_usage
import cProfile
from base import Base
import pandas as pd
import emoji
from concurrent.futures import ThreadPoolExecutor
import numpy as np

file_path = Base().twiter_file_path

# Función para procesar un bloque de contenido
def process_chunk(content_chunk, emoji_set):
    emoji_count = Counter()
    for content in content_chunk.dropna():
        if isinstance(content, str):
            emoji_count.update(c for c in content if c in emoji_set)
    return emoji_count

#@profile
def q2_time(file_path: str) -> List[Tuple[str, int]]:#1462.6 MiB max 7.16 s
    emoji_set = set(emoji.EMOJI_DATA)
    df = pd.read_json(file_path, lines=True)
    # Seteamos el número de threads
    num_workers = 4

    # Procesar en paralelo usando ThreadPoolExecutor
    chunks = np.array_split(df['content'], num_workers)  # Dividimos el DataFrame en bloques
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        results = executor.map(process_chunk, chunks, [emoji_set]*num_workers)  # Pasamos los bloques y el set de emojis

    # Combinar los contadores de emojis
    emoji_count = Counter()
    for result in results:
        emoji_count.update(result)

    # Obtener los 5 emojis más comunes
    top_emojis = emoji_count.most_common(5)
    return top_emojis

if __name__ == "__main__":
    # Llamada a la función
    #q2_time_2(file_path)
    cProfile.run("q2_time(file_path)", sort='tottime')
from typing import List, Tuple
from collections import Counter
from memory_profiler import profile, memory_usage
import cProfile
import json
import os
from base import Base
import pandas as pd
import emoji

file_path = Base().twiter_file_path
@profile
def q2_time_2(file_path: str) -> List[Tuple[str, int]]: #1462.6 MiB max 148.20 s
    emoji_count = Counter()
    emoji_set = set(emoji.EMOJI_DATA) 
    df = pd.read_json(file_path, lines=True)
    for content in df['content'].dropna():
        if isinstance(content, str):
            emoji_count.update(c for c in content if c in emoji_set)
    # Obtener los 5 emojis más comunes
    top_emojis = emoji_count.most_common(5)

    return top_emojis

if __name__ == "__main__":
    # Llamada a la función
    q2_time_2(file_path)
    #cProfile.run("q2_time_2(file_path)", sort='tottime')
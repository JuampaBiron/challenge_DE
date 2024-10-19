from typing import List, Tuple
from collections import Counter
from memory_profiler import profile, memory_usage
import cProfile
import json
import os
import pandas as pd
import emoji

file_path = "input\\farmers-protest-tweets-2021-2-4.json"
complete_file_path = os.path.join(os.getcwd(), file_path)

@profile
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emoji_count = Counter()

    # Leer el archivo JSON línea por línea y procesar en una sola pasada
    with open(file_path, 'r', buffering=8192) as file:  # Aumentar el tamaño del buffer
        for line in file:
            json_object = json.loads(line)  # Cargar un objeto JSON a la vez
            content = json_object.get('content')  # Obtener el contenido
            
            if content:  # Solo procesar si el contenido no es nulo
                # Contar emojis directamente en el contenido
                # Usar un conjunto para verificar la existencia de emojis
                emojis_in_content = (c for c in content if c in emoji.EMOJI_DATA)
                emoji_count.update(emojis_in_content)

    # Obtener los 5 emojis más comunes
    top_emojis = emoji_count.most_common(5)
    return top_emojis
q2_time(complete_file_path)
cProfile.run("q2_time(complete_file_path)", sort='tottime')
from typing import List, Tuple
from collections import Counter
from memory_profiler import profile, memory_usage
import cProfile
import json
import os
import pandas as pd
import emoji
from base import Base

file_path = Base().twiter_file_path

#@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]: #104.4 MiB max 304.64s
    emoji_count = {}  # Diccionario para contar emojis
    # Procesar el archivo línea por línea
    with open(file_path, 'r', encoding='utf-8') as file:  # Asegúrate de abrir el archivo con la codificación correcta
        for line in file:
            data = json.loads(line)  # Cargar el objeto JSON
            content = data.get('content')  # Obtener contenido
            # Contar emojis en el contenido
            if isinstance(content, str):
                for c in content:
                    if c in emoji.EMOJI_DATA:  # Verificar si el carácter es un emoji
                        if c in emoji_count:
                            emoji_count[c] += 1  # Incrementar el contador si ya existe
                        else:
                            emoji_count[c] = 1  # Inicializar el contador si no existe
    # Obtener los 5 emojis más comunes
    top_emojis = sorted(emoji_count.items(), key=lambda x: x[1], reverse=True)[:5]
    return top_emojis

if __name__ == "__main__":
    # Llamar a la función con el path correcto
    q2_memory(file_path)
    cProfile.run("q2_memory(file_path)", sort='tottime')
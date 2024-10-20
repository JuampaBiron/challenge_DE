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
def q3_memory(file_path: str) -> List[Tuple[str, int]]: #103.5 MiB max 12.89 s
    dict_username_count = defaultdict(int)  # Usar un diccionario simple

    with open(file_path, 'r', buffering=8192) as file:
        for line in file:
            try:
                json_object = json.loads(line)  # Cargar un objeto JSON a la vez
                content = json_object.get('content')

                if content:  # Solo procesar si el contenido del tweet no es nulo
                    for username in extract_usernames(content):  # Extraer usernames
                        dict_username_count[username] += 1  # actualizamos el diccionario con el username encontrado

            except json.JSONDecodeError:
                continue  # Ignorar líneas que no sean JSON válidos

    # Obtener los 5 usernames más comunes
    top_usernames = sorted(dict_username_count.items(), key=lambda x: x[1], reverse=True)[:5]
    return top_usernames

if __name__ == "__main__":
    # Llamar a la función con el path correcto
    q3_memory(file_path)
    cProfile.run("q3_memory(file_path)", sort='tottime')
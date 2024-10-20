from typing import List, Tuple
import re
from base import Base
from memory_profiler import profile, memory_usage
import cProfile
import pandas as pd
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import numpy as np

file_path = Base().twiter_file_path
mention_pattern = re.compile(r'[@＠]([a-zA-Z0-9_]{1,20})(/[a-zA-Z][a-zA-Z0-9_-]{0,24})?')

def extract_usernames(content: str) -> List[str]:
    return [match.group(1) for match in mention_pattern.finditer(content)] #almacenamos resultados en una lista. Almacenar en una lista puede reducir el tiempo total de ejecución.

# Function to process chunks of data in parallel
def process_chunk(chunk: pd.Series) -> Counter:
    username_count = Counter()
    for content in chunk.dropna():
        if isinstance(content, str):
            username_count.update(extract_usernames(content))
    return username_count

@profile
def q3_time(file_path: str) -> List[Tuple[str, int]]:#1470 MiB, 6.7s
    df = pd.read_json(file_path, lines=True)
    num_workers = 4
    chunks = np.array_split(df['content'], num_workers)

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(process_chunk, chunks))

    username_count = Counter()
    for result in results:
        username_count.update(result)

    top_usernames = username_count.most_common(10)
    return top_usernames

if __name__ == "__main__":
    cProfile.run("q3_time(file_path)", sort="tottime")


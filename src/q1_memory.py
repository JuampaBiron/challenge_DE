import json
from typing import List, Tuple
from datetime import datetime
from base import Base
import pandas as pd
from memory_profiler import profile, memory_usage
import cProfile

class Q1Memory(Base):
    def __init__(self):
        super().__init__()  # Llamar al constructor de la clase Base
        self.file = self.datos

    def q1_memory_(self,file_path) -> List[Tuple[datetime.date, str]]:
        # Leer el archivo JSON
        # Lista para almacenar los datos extraídos
        data_list = []
        
        # Leer el archivo JSON
        with open(file_path, 'r') as file:
            json_objects = file.read().splitlines()  # Splitting the JSON objects by lines
            
            for obj in json_objects:
                data = json.loads(obj)  # Convertir la línea a un objeto JSON
                # Extraer los campos que te interesan
                tweet_data = {
                    'url': data.get('url'),
                    'date': data.get('date'),
                    'content': data.get('content'),
                    'renderedContent': data.get('renderedContent'),
                    'id': data.get('id'),
                    'user': data.get('user'),
                    'outlinks': data.get('outlinks'),
                    'replyCount': data.get('replyCount'),
                    'retweetCount': data.get('retweetCount'),
                    'likeCount': data.get('likeCount'),
                    'quoteCount': data.get('quoteCount'),
                    'conversationId': data.get('conversationId'),
                    'lang': data.get('lang'),
                    'source': data.get('source'),
                    'sourceUrl': data.get('sourceUrl'),
                    'sourceLabel': data.get('sourceLabel'),
                    'media': data.get('media'),
                    'retweetedTweet': data.get('retweetedTweet'),
                    'quotedTweet': data.get('quotedTweet'),
                    'mentionedUsers': data.get('mentionedUsers'),
                }
                data_list.append(tweet_data)  # Agregar los datos a la lista
        
        # Crear un DataFrame de pandas con los datos
        df = pd.DataFrame(data_list)
        df['date'] = pd.to_datetime(df['date']).dt.date
        df['user'] = df['user'].apply(lambda x: x['username'] if isinstance(x, dict) else None)
        # Agrupar por la columna 'date' y contar la cantidad de tweets
        top_dates = df['date'].value_counts().head(10)
        # Convertir a DataFrame para mayor claridad (opcional)
        top_dates_df = top_dates.reset_index()
        top_dates_df.columns = ['date', 'tweet_count']
        # Convertir las fechas y sus conteos en una lista de tuplas
        result = [(date, count) for date, count in top_dates.items()]

        return result  # Retornar la lista de tuplas
    
    @profile
    def q1_time(self,file_path) -> List[Tuple[datetime.date, str]]:
            # Leer el archivo JSON
            # Lista para almacenar los datos extraídos
            data_list = []
            
            # Leer el archivo JSON
            with open(file_path, 'r') as file:
                json_objects = file.read().splitlines()  # Splitting the JSON objects by lines
                
                for obj in json_objects:
                    data = json.loads(obj)  # Convertir la línea a un objeto JSON
                    # Extraer los campos que te interesan
                    tweet_data = {
                        'date': data.get('date'),
                        'user': data.get('user'),
                    }
                    data_list.append(tweet_data)  # Agregar los datos a la lista
            
            # Crear un DataFrame de pandas con los datos
            df = pd.DataFrame(data_list)
            df['date'] = pd.to_datetime(df['date']).dt.date
            df['user'] = df['user'].apply(lambda x: x['username'] if isinstance(x, dict) else None)
            # Agrupar por la columna 'date' y contar la cantidad de tweets
            top_dates = df['date'].value_counts().head(10)
            # Convertir a DataFrame para mayor claridad (opcional)
            top_dates_df = top_dates.reset_index()
            top_dates_df.columns = ['date', 'tweet_count']
            # Convertir las fechas y sus conteos en una lista de tuplas
            result = [(date, count) for date, count in top_dates.items()]

            return result  # Retornar la lista de tuplas
    
    @profile
    def q1_memory(self,file_path: str) -> List[Tuple[datetime.date, int]]:
        # Utilizar un diccionario para contar tweets por fecha
        tweet_counts = {}

        # Leer el archivo JSON línea por línea
        with open(file_path, 'r') as file:
            for line in file:
                data = json.loads(line)  # Convertir la línea a un objeto JSON
                
                # Extraer la fecha y el usuario
                tweet_date = data.get('date')
                user_info = data.get('user')
                username = user_info['username'] if isinstance(user_info, dict) else None
                
                # Solo continuar si hay fecha y nombre de usuario
                if tweet_date and username:
                    tweet_date = pd.to_datetime(tweet_date).date()  # Convertir a objeto fecha
                    
                    # Contar los tweets por fecha
                    if tweet_date in tweet_counts:
                        tweet_counts[tweet_date] += 1
                    else:
                        tweet_counts[tweet_date] = 1

        # Obtener las 10 fechas con más tweets
        top_dates = sorted(tweet_counts.items(), key=lambda x: x[1], reverse=True)[:10]        
        return top_dates  # Retornar la lista de tuplas


    def run_workflow(self):
        self.q1_memory(self.datos)
        



# Ejemplo de uso
if __name__ == "__main__":
    q1_mem = Q1Memory()
    cProfile.run("q1_mem.run_workflow()", sort='tottime')

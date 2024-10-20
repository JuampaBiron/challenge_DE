from q1_memory import q1_memory
from q1_time import q1_time
from q2_memory import q2_memory
from q2_time import q2_time
from q3_memory import q3_memory
from q3_time import q3_time
import logging
import cProfile
from typing import List, Tuple
from datetime import datetime
from base import Base  # Si necesitas la ruta del archivo desde Base

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


file_path = Base().twiter_file_path  # Ruta del archivo

def main():
    # Análisis de tiempo para las fechas con más tweets
    logging.info("Análisis de tiempo para las top 10 fechas con más tweets:")
    result_q1_time = q1_time(file_path)
    for date, user in result_q1_time:
        logging.info(f"Fecha: {date}, Usuario con más tweets: {user}")

    # Análisis de memoria para las fechas con más tweets
    logging.info("\nAnálisis de memoria para las top 10 fechas con más tweets:")
    result_q1_memory = q1_memory(file_path)
    for date, user in result_q1_memory:
        logging.info(f"Fecha: {date}, Usuario con más tweets: {user}")

    # Análisis de tiempo para los emojis más usados
    logging.info("\nAnálisis de tiempo para los top 10 emojis más usados:")
    result_q2_time = q2_time(file_path)
    for emoji, count in result_q2_time:
        logging.info(f"Emoji: {emoji}, Conteo: {count}")

    # Análisis de memoria para los emojis más usados
    logging.info("\nAnálisis de memoria para los top 10 emojis más usados:")
    result_q2_memory = q2_memory(file_path)
    for emoji, count in result_q2_memory:
        logging.info(f"Emoji: {emoji}, Conteo: {count}")

    # Análisis de tiempo para los usuarios más influyentes
    logging.info("\nAnálisis de tiempo para los top 10 usuarios más influyentes:")
    result_q3_time = q3_time(file_path)
    for user, mentions in result_q3_time:
        logging.info(f"Usuario: {user}, Conteo de menciones: {mentions}")

    # Análisis de memoria para los usuarios más influyentes
    logging.info("\nAnálisis de memoria para los top 10 usuarios más influyentes:")
    result_q3_memory = q3_memory(file_path)
    for user, mentions in result_q3_memory:
        logging.info(f"Usuario: {user}, Conteo de menciones: {mentions}")

if __name__ == "__main__":
    cProfile.run("main()", sort="tottime")  # Perfilando la función main

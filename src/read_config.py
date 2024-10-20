import json5
import os

class Config:
    def __init__(self):
        # Obtener el directorio raíz del proyecto
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_file_path = os.path.join(project_root, "config.jsonc")

        # Cargar el archivo de configuración
        with open(config_file_path, 'r') as file:
            self.config = json5.load(file)

    def get(self, key):
        # Método para obtener el valor de una variable de configuración
        return self.config.get(key)

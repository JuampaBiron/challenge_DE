import json5

class Config:
    def __init__(self, config_file):
        # Cargar el archivo de configuración
        with open(config_file, 'r') as file:
            self.config = json5.load(file)

    def get(self, key):
        # Método para obtener el valor de una variable de configuración
        return self.config.get(key)


# Ejemplo de uso
if __name__ == "__main__":
    # Cambia a la ruta correcta según donde esté tu archivo
    config_file_path = 'config.jsonc'
    print(Config(config_file=config_file_path).get("DATA_FILE_PATH"))


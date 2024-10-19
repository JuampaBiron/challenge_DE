
from read_config import Config
import os
class Base(Config):
    def __init__(self):
        super().__init__("config.jsonc")  # Llamar al constructor de la clase Config
        self.datos = os.path.join(os.getcwd(), self.get("DATA_FILE_PATH"))
        self.requirements = os.path.join(os.getcwd(), self.get("REQUIREMENTS"))  # Asignar el valor de REQUIREMENTS
        self.como_me_llamo = "juan pablo"  # Variable adicional que has agregado


    def print_info(self):
        print(f"Datos: {self.datos}")
        print(f"Requirements: {self.requirements}")



if __name__ == "__main__":
    # Instancia de Base
    base_instance = Base()
    
    # Imprimir la información de configuración
    base_instance.print_info()

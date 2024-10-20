
from read_config import Config
import os
class Base(Config):
    def __init__(self):
        super().__init__()  # Llamar al constructor de la clase Config
        self.project_folder = self.get("PROJECT_FOLDER")
        self.twiter_file_path = os.path.join(self.project_folder, self.get("DATA_FILE_PATH"))
        self.requirements = os.path.join(self.project_folder, self.get("REQUIREMENTS")) 


    def print_info(self):

        print(f"Datos: {self.datos}")
        print(f"Requirements: {self.requirements}")
        print(f"current working directory: {os.getcwd()}")



if __name__ == "__main__":
    # Instancia de Base
    base_instance = Base()
    print(base_instance.datos)
    # Imprimir la información de configuración
    base_instance.print_info()

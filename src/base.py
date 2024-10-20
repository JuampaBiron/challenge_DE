
from read_config import Config
import os
class Base(Config):
    def __init__(self):
        super().__init__()  # Llamar al constructor de la clase Config
        self.project_folder = self.get("PROJECT_FOLDER")
        self.twiter_file_path = os.path.join(self.project_folder, self.get("DATA_FILE_PATH"))
        self.requirements = os.path.join(self.project_folder, self.get("REQUIREMENTS")) 
        self.emoji_regex_pattern = self.get("REGEX_EMOJI_PATTERN")


if __name__ == "__main__":
    # Instancia de Base
    base_instance = Base()
    print(base_instance.emoji_regex_pattern)


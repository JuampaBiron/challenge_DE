# Análisis de Datos de Twitter

Este proyecto proporciona una implementación para procesar datos de Twitter, extrayendo información como usuarios mencionados y emojis en tweets, así como contando la cantidad de tweets por usuario y fecha.

## Clases

### `Config`

La clase `Config` se encarga de cargar la configuración del proyecto desde un archivo `config.jsonc`.

#### Métodos

- **`__init__()`**
  - Inicializa un objeto `Config` y carga la configuración del archivo.

- **`get(key: str)`**
  - Devuelve el valor asociado a una clave de configuración específica.

### `Base`

La clase `Base` hereda de `Config` y proporciona la base para acceder a rutas de archivos y patrones de expresión regular.

#### Métodos

- **`__init__()`**
  - Inicializa un objeto `Base` y establece las rutas necesarias para los archivos de datos.

### Funciones de análisis

El proyecto incluye varias funciones que realizan diferentes análisis en los datos de Twitter:

#### `q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]`
- Cuenta la cantidad de tweets por usuario en cada fecha, registrando el uso de memoria.

#### `q1_time(file_path: str) -> List[Tuple[datetime.date, str]]`
- Similar a `q1_memory`, pero optimiza el tiempo de ejecución utilizando procesamiento en paralelo.

#### `q2_memory(file_path: str) -> List[Tuple[str, int]]`
- Cuenta la cantidad de emojis en los tweets, registrando el uso de memoria.

#### `q2_time(file_path: str) -> List[Tuple[str, int]]`
- Similar a `q2_memory`, pero optimiza el tiempo de ejecución utilizando procesamiento en paralelo.

#### `q3_memory(file_path: str) -> List[Tuple[str, int]]`
- Extrae y cuenta los usernames mencionados en los tweets, registrando el uso de memoria.

#### `q3_time(file_path: str) -> List[Tuple[str, int]]`
- Similar a `q3_memory`, pero optimiza el tiempo de ejecución utilizando procesamiento en paralelo.

## Ejemplos de Uso

```python
from datetime import datetime
from base import Base
from q1_memory import q1_memory
from q1_time import q1_time
from q2_memory import q2_memory
from q2_time import q2_time
from q3_memory import q3_memory
from q3_time import q3_time

# Inicializar configuración
base = Base()

# Contar tweets por usuario y fecha (uso de memoria)
tweets_por_usuario = q1_memory(base.twiter_file_path)
print(f"Tweets por usuario: {tweets_por_usuario}")

# Contar tweets por usuario y fecha (optimización de tiempo)
tweets_por_usuario_rapido = q1_time(base.twiter_file_path)
print(f"Tweets por usuario (rápido): {tweets_por_usuario_rapido}")

# Contar emojis (uso de memoria)
emoji_contados = q2_memory(base.twiter_file_path)
print(f"Emojis contados: {emoji_contados}")

# Contar emojis (optimización de tiempo)
emoji_contados_rapido = q2_time(base.twiter_file_path)
print(f"Emojis contados (rápido): {emoji_contados_rapido}")

# Extraer y contar usernames (uso de memoria)
usernames_contados = q3_memory(base.twiter_file_path)
print(f"Usernames contados: {usernames_contados}")

# Extraer y contar usernames (optimización de tiempo)
usernames_contados_rapido = q3_time(base.twiter_file_path)
print(f"Usernames contados (rápido): {usernames_contados_rapido}")

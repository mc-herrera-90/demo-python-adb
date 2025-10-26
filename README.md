# Demo - Conexión OracleDB

Este proyecto utiliza **OracleDB** para conectarse a bases de datos Oracle y **python-dotenv** para manejar variables de entorno.

> Requiere **Python 3.14** o compatible (por ejemplo, 3.12 o superior).

---

## 🔧 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/mc-herrera-90/demo-python-adb.git
   cd demo-python-adb
   ```

2. **Instalar pipenv** (si no lo tienes)

   ```bash
   pip install pipenv
   ```

3. **Instalar dependencias**

   ```bash
   pipenv install
   ```

4. **Activar el entorno virtual**

   ```bash
   pipenv shell
   ```

---

## ⚙️ Configuración

Crea un archivo `.env` en la raíz del proyecto con las credenciales de tu base de datos. Por ejemplo:

```env
WALLET_LOCATION=Wallet_ADB2025
USERDB=admin
PASSWORDDB=TuPasswordDB
PASSWORDWALLET=TuPasswordWallet
TNS_ALIAS=adb2025_high
```

> No subas el archivo `.env` al repositorio.

---

## ▶️ Ejecución

Ejecuta tu script principal, por ejemplo:

```bash
python main.py
```
Si quieres probar una simple conexión, cambia el contenido de `main.py` por lo siguiente:

```python
import oracledb
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

wallet_path = os.getenv("WALLET_LOCATION")
tns_alias = os.getenv("TNS_ALIAS")
username = os.getenv("USERDB")
password = os.getenv("PASSWORDDB")
password_wallet = os.getenv("PASSWORDWALLET")

try:
    # Conexión a la base de datos
    connection = oracledb.connect(
        user=username,
        password=password,
        dsn=tns_alias,
        config_dir=wallet_path,
        wallet_location=wallet_path,
        wallet_password=password_wallet
    )
    print("Conexión exitosa ✅")

except oracledb.DatabaseError as e:
    print("❌ Error al conectar o consultar la base de datos:", e)
```

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

    cursor = connection.cursor()
    cursor.execute("ALTER SESSION SET CURRENT_SCHEMA = WKSP_ATP2025")
    cursor.execute("SELECT * FROM employees")

    # Obtener nombres de columnas
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()

    # Calcular ancho de cada columna
    col_widths = [len(col) for col in columns]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))

    # Función para imprimir una fila
    def print_row(row_values):
        row_str = " | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row_values))
        print("| " + row_str + " |")

    # Imprimir tabla
    print("\n📋 Datos de empleados:\n")
    # Encabezado
    print_row(columns)
    print("|" + "|".join("-" * (w + 2) for w in col_widths) + "|")
    # Filas
    for row in rows:
        print_row(row)

except oracledb.DatabaseError as e:
    print("❌ Error al conectar o consultar la base de datos:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
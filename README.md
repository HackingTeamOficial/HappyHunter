Happy Hunter - Herramienta de Automatización SQLi usando sqlmap
================================================================

🔍 Happy Hunter es un script en Python que automatiza la detección y enumeración de bases de datos vulnerables a SQL Injection mediante sqlmap, facilitando el pentesting y la auditoría de seguridad.

Características
---------------

- Detecta automáticamente el DBMS de la URL objetivo.
- Enumera bases de datos y tablas disponibles.
- Uso sencillo con argumentos mínimos.
- Salida en consola con colores para mejor lectura.
- Basado en la potencia de sqlmap.

Requisitos
----------

- Python 3.x instalado.
- sqlmap (https://github.com/sqlmapproject/sqlmap) instalado y accesible desde la consola.
- Conexión a internet para algunas funcionalidades de sqlmap.
- (Opcional) Consola que soporte colores ANSI para mejor visualización.

Instalación
-----------

1. Clona o descarga el script happy_hunter.py.

2. Asegúrate de tener python 3 y sqlmap instalados:

python3 --version
sqlmap --version


3. Ejecuta el script:

python3 happy_hunter.py


Uso Básico
----------

El script pedirá la URL objetivo y el parámetro vulnerable para iniciar el escaneo.

Ejemplo:

Ingresa la URL objetivo: http://miweb.com/vulnerable.php?id=1
Ingresa el parámetro vulnerable: id


El programa detectará el DBMS, enumerará bases y tablas mostrando los resultados en consola.

Explicación de funciones
------------------------

- detect_dbms(url, param): Detecta el motor de base de datos detrás de la URL.
- enumerate_dbs(url, param, dbms): Obtiene una lista de bases de datos disponibles.
- enumerate_tables(url, param, dbms, db_name): Lista las tablas dentro de una base de datos.

Notas importantes
-----------------

- Usa Happy Hunter únicamente en entornos autorizados o para pruebas propias.
- Sqlmap es una herramienta potente, úsala con responsabilidad.
- Puedes modificar el script para agregar más funcionalidades o adaptar a tus necesidades.

Contacto y comunidad
--------------------

Únete a nuestra comunidad para compartir conocimiento, dudas y mejoras:

Telegram: https://t.me/+74d-97oV7P05OTVk  

Nuestras RRSS

Telegram

https://t.me/+0hHSaKO7eI9mNWY8

https://t.me/PlantillasNucleiHackingTeam

https://t.me/TermuxHackingTeam

X

@HackingTeam777

Bluesky

https://bsky.app/profile/hackingteam.bsky.social

Discord

https://discord.gg/V4nPFbQX

Facebook

https://www.facebook.com/groups/hackingteam2022/?ref=share https://www.facebook.com/groups/HackingTeamCyber/?ref=share

Youtube

https://www.youtube.com/@HackingTeamOfficial

Canal de tiktok

https://www.tiktok.com/@hacking.kdea?_t=ZS-8vTtlaQrDTL&_r=1

#hackingteam #cibersecurity #infosec #eticalhacking #pentesting #dns #script #cracking #hack #security #bugbounty #payload #tools #exploit #cors #sqli #ssrf #python #c2 #poc #web #ramsomware #phishing #linux #osint #linux #windows #redteam #blueteam #spyware #digitalforensics #reverseengineeringtools #rat #malwareforensics #exploitdevelopment #sandboxing #apt #zerodayexploit #xss #github #cve #java #tools #termux #troyano #dev #sqlmap #waybackurls #copilot #ai #ia #kalilinux #parrot #dracos #susse #nessus #oswazap #burpsuite #wireguard

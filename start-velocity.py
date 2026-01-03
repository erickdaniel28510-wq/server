import subprocess
import os

# Ruta al .jar
jar_path = "/workspaces/server/proxy/server.jar"

# Comando Java
java_cmd = [
    "java",
    "-Dlog4j2.formatMsgNoLookups=true",
    "-Xms128M",
    "-Xmx1G",
    "-Dterminal.jline=false",
    "-Dcom.mojang.eula.agree=true",
    "-Dterminal.ansi=true",
    "-jar",
    jar_path
]

# Cambiar al directorio del jar
os.chdir("/workspaces/server/proxy")

# Ejecutar el comando
try:
    subprocess.run(java_cmd, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar Velocity: {e}")
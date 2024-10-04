#!/usr/bin/env python3
#Ailton Israel De La Cruz Salazar
#Carlos Alexis Vargas Flores
import subprocess
import re

# Ejecutar el script de Bash y capturar su salida
result = subprocess.run(['./monitor_conexiones.sh'], capture_output=True, text=True)

# Puertos estándar
standard_ports = {22, 25, 80, 465, 587, 8080}

# Expresión regular para extraer puertos
port_regex = re.compile(r':(\d+)\s')

# Analizar las conexiones
suspicious_connections = []
for line in result.stdout.splitlines():
    match = port_regex.search(line)
    if match:
        port = int(match.group(1))
        if port not in standard_ports:
            suspicious_connections.append(line)

# Generar el reporte
with open('Conexiones.txt', 'w') as report_file:
    report_file.write('Conexiones sospechosas:\n')
    for connection in suspicious_connections:
        report_file.write(connection + '\n')

print("Reporte generado en 'Conexiones.txt'")

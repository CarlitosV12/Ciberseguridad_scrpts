# Usar la API de Have I been pwn?
import requests
import json
import logging
import getpass
import re

def validar_correo(correo):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, correo)

p = getpass.getpass(prompt='API KEY: ')
if p.lower() == '':
    print('Entrando')
    key = ''
    headers = {}
    headers['content-type']= 'application/json'
    headers['api-version']= '3'
    headers['User-Agent']='python'
#Place that API key here
    headers['hibp-api-key']=key
#Preguntar correo a revisar
    email = input("Ingrese el correo a investigar")#'falso@hotmail.com'
    if not validar_correo(email):
        print("El formato del correo electrónico no es válido.")
    else:
        
            #solicitud
        url = 'https://haveibeenpwned.com/api/v3/breachedaccount/'+\
            email+'?truncateResponse=false'
        try:
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                data = r.json()
                encontrados = len(data)
                if encontrados > 0:
                    print("Los sitios en los que se ha filtrado el correo",email,"son:")
                    # Guardar en archivo txt
                    with open('filtraciones.txt', 'w') as f:  
                        f.write(f"Filtraciones para {email}:\n")
                        for filtracion in data:
                            sitio = filtracion["Name"]
                            print(sitio)
                            f.write(f"{sitio}\n")
                    msg = f"{email} Filtraciones encontradas: {encontrados}"
                    print(msg)
                    logging.basicConfig(filename='hibpINFO.log',
                                        format="%(asctime)s %(message)s",
                                        datefmt="%m/%d/%Y %I:%M:%S %p",
                                        level=logging.INFO)
                else:
                    print("El correo",email,"no ha sido filtrado")
            
            
            logging.error(msg)

        except requests.exceptions.HTTPError as errh:
                    print("Error HTTP:", errh)
                    logging.basicConfig(filename='hibpERROR.log',
                                        format="%(asctime)s %(message)s",
                                        datefmt="%m/%d/%Y %H:%M:%S",
                                        level=logging.ERROR)
                    logging.error(f"HTTPError: {errh}")




else:
    print('Denegao')



#Fuentes: https://rico-schmidt.name/pymotw-3/getpass/index.html
# https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples
#https://www.zerobounce.net/es/email-guides/python-email-verification/
#https://www.freecodecamp.org/espanol/news/lectura-y-escritura-de-archivos-en-python-como-crear-leer-y-escribir-archivos/
#https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module

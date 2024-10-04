import pyautogui
import datetime
import subprocess

#Integrantes
#Ailton Israel De La Cruz Salazar
#Carlos Alexis Vargas Flores    

try:
    #Toma la captura y la guarda
    ima = pyautogui.screenshot()
    fecha = datetime.datetime.now()
    nombre = r'SS_'
    nombre += str(fecha.strftime("%Y-%m-%d_%H-%M-%S"))
    nombre +='.png'
    ima.save(nombre)
except:
    print("Ocurrio un errorsillo")


def proce():
    #Listar procesos con taklist y salida del archivo
    result = subprocess.run(['tasklist'], capture_output=True, text=True, shell=True)
    fechatext = fecha.strftime("%Y-%m-%d_%H-%M-%S")
    arch = f"Subprocesos_{fechatext}.txt"
    with open(arch, "w") as file:
        file.write(result.stdout)


def main():
    proce()

if __name__ == "__main__":
    main()

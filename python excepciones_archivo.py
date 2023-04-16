import re

def validar_email(email):
    if not re.search(".+@.+\..+", email):
        raise ValueError("La dirección de correo electrónico no es válida")
    else:
        return True

def ingresar_email():
    while True:
        try:
            email = input("Introduzca su dirección de correo electrónico -> ")
            validar_email(email)
            return email
        except ValueError as e:
            print(str(e))

def main():
    try:
        email = ingresar_email()
        print("¡Bienvenido {}!".format(email.split("@")[0]))
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")

if __name__ == "__main__":
    main()
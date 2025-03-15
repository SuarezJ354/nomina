

##US1//REGISTER
users = {}

def createUser():
    user = []
    id = int(input("Ingrese su Documento de Identidad "))
    user.append(id)
    user_name =  input("Ingrese un nombre ")
    user.append(user_name)
    user_last_name = input("Ingrese su apellido ")
    user.append(user_last_name)
    phone = input("Ingrese su telefono ")
    user.append(phone)
    user_email = input("Ingrese su correo ")
    user.append(user_email)
    user_password = input("Ingrese su contraseña ")
    user.append(user_password)
    users.update(user)

createUser()
createUser()
createUser()

print(users)
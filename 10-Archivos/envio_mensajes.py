with open("10-Archivos/-mbox.txt") as fd:
    lstEmail = []
    for linea in fd:
       if linea.startswith("From:"):
          correo = linea.split()[1] + " enviado [ok]\n"
          if correo not in lstEmail:
              lstEmail.append(correo)

lstEmail.reverse()          # Otro metodo: [::-1]

with open("10-Archivos/-Correos_enviados.txt", "w") as fd:
    fd.writelines(lstEmail)


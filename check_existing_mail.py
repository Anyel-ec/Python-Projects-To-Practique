import smtplib

def verificar_correo_existente(correo):
    try:
        dominio = correo.split('@')[1]
        # Conectarse al servidor SMTP del dominio
        servidor_smtp = smtplib.SMTP(dominio)
        servidor_smtp.set_debuglevel(0)
        # Intente enviar un correo al usuario sin enviar realmente el correo
        servidor_smtp.verify(correo)
        servidor_smtp.quit()
        return True
    except smtplib.SMTPConnectError:
        return False
    except smtplib.SMTPHeloError:
        return False
    except smtplib.SMTPAuthenticationError:
        return False
    except smtplib.SMTPSenderRefused:
        return False
    except smtplib.SMTPRecipientsRefused:
        return False
    except smtplib.SMTPDataError:
        return False
    except Exception as e:
        print("Error inesperado:", str(e))
        return False

# Ejemplo de uso
correo = "correo_que_existe@gmail.com"
if verificar_correo_existente(correo):
    print(f"{correo} es una dirección de correo electrónico válida y existe en el servidor.")
else:
    print(f"{correo} no es una dirección de correo electrónico válida o no existe en el servidor.")

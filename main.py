import ftplib
import os
from dotenv import load_dotenv

load_dotenv()

# FTP Data
ftp_servidor = os.environ.get('FTP_SERVIDOR')
ftp_user = os.environ.get('FTP_USER')
ftp_password = os.environ.get('FTP_PASSWORD')
ftp_root = os.environ.get('FTP_ROOT')

# File Data
file_destination = 'nomina.xlsx'
file_source = f'C:\\Users\\Media\\Desktop\\{file_destination}'


# Servidor connection
try:
    conn = ftplib.FTP(ftp_servidor, ftp_user, ftp_password)
    try:
        with open(file_source, 'rb') as f:
            conn.cwd(ftp_root)
            conn.storbinary('STOR %s' % file_destination, f)
            print(f'El Archivo {file_destination} se ha enviado')
            conn.quit()
    except Exception as e:
        print('No se ha encontrado el fichero', e)
except Exception as e:
    print('No se ha podido conectar al servidor' + ftp_servidor, e)
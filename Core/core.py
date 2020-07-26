import pyAesCrypt
from Core import decor
import os

bufferSize = 64 * 1024


def encrypt(file, password):
    output = file + ".aes"
    if not file.__contains__('.'):
        mes = (decor.red + "File has no extension" + decor.reset)
        return mes
    out = pyAesCrypt.encryptFile(file, output, password, bufferSize)
    print(decor.green + "[+] Completed" + decor.reset)

def decrypt(ext, file, password):
    if not file.__contains__('.aes'):
        mes = (decor.red + "File has no '.aes' end" + decor.reset)
        return mes
    symbs = len(ext)
    out = file[:-symbs]
    pyAesCrypt.decryptFile(file, out, password, bufferSize)
    print(decor.green + "[+] Completed" + decor.reset)

from Core import core
from Core import decor


print(decor.banner)


while True:
    print(decor.menu)
    choose = int(input(decor.yellow + "Enter number >> "))

    if choose == 1:
        file = input(decor.yellow + "Enter filename with extension (file.txt) >> ")
        password = input(decor.yellow + "Enter password for file (remember it) >> ")
        try:
            core.encrypt(file, password)
            break
        except:
            print(decor.red + "[!] Error [!]")
            continue
    elif choose == 2:
        ext = input(decor.yellow + "Enter file extension (txt | py | data | ini | etc) >> ")
        file = input(decor.yellow + "Enter filename with extension (file.txt.aes) >> ")
        password = input(decor.yellow + "Enter file password >> ")

        try:
            core.decrypt(ext, file, password)
            break
        except ValueError:
            print(decor.red + "[!] Wrong password [!]" + decor.reset)
            continue

    elif choose == 3:
        break

    else:
        print(decor.red + "[!] Inknown command [!]" + decor.reset)
        continue

import os
import time

with open('programa_pingmultiplo\hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('\n')
        print('-' * 60)
        print("Verificando o Ip: ", ip)
        print('-' * 60)
        os.system('ping -n 2 {}'.format(ip))
        print('-' * 60)
        time.sleep(5)

    
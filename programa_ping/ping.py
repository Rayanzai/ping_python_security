import os #importa biblioteca

print('#' * 60) 
ip_ou_host = input("Digite o Ip ou Host a ser verificado: ") #variáel que solicita Ip ou host
print('-' * 60)
os.system('ping -n 6 {}'.format(ip_ou_host)) #chama biblioteca, função system com parâmetros ping e 6 echo request da variável
print('-' * 60)
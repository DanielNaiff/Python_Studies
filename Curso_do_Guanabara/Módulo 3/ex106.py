c = ('\033[m', '\033[0;30;41m','\033[0;30;42m','\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[7;30m');
def ajuda(com):
  titulo(f'Acessando o manual do comando \'{com}\'',4)
  print(c[6], end='')
  help(com)
  print(c[0], end='')
def titulo(msg, cor=0):
    tam = len(msg) + 4
    cor = max(0, min(cor, len(c) - 1)) 
    print(c[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(c[0], end='')
comando = ''
while True:
  titulo('Sistema de ajuda pyHelp', 3)
  comando = str(input("Função ou biblioteca > "))
  if comando.upper() == 'FIM':
    break
  else:
    ajuda(comando)
titulo('Até logo', 1)
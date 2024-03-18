print('MANIPULANDO CADEIA DE TEXTOS')
# Frase == String (Cadeia de caractere)

print('-'*15)

print('Fatiamento:') 
frase = 'Curso em Vídeo Python'
print('Frase: {}'.format(frase))
print(frase[9])
# Print do caractere na posição [x] -> frase[0] == primeiro caractere
print(frase[9:14])
# [x : x-1] print dos carateres partindo da posição [x] até a posição [x-1]
print(frase[9:14:2])
# [x : x-1 : n] print dos caracteres partindo da posição [x] até a posição [x-1] saltando n posições
print(frase[:5])
# [ : x-1] print partindo do inicio da string até a posição x-1
print(frase[9:])
# [x : ] print partindo do caractere na posição [x] até o final da string
print(frase[::2])
# [ : : n] print partindo do inicio da string até o fim dela saltando n posições

print('-'*15)

print('Análise de string:')
frase = 'Aprendendo Python do Zero'
print('Frase: {}'.format(frase))
print(len(frase))
# Determina o comprimento da string -> print da quantidade de caractere
print(frase.count('o'))
# ('a' * n) print da quantidade de vezes que um determinado caractere aparece
print(frase.count('o', 0, 14))
# ('a', x, x-1) print da quantidade de vezes que um determinado caractere aparece partindo da posição x até x-1
print(frase.find('end'))
# ('end') print da posição em que se encontra um ou mais caracteres sequenciais
print(frase.find('Android'))
# Caso o caractere determinado não exista, retornará o valor -1
print('Zero' in frase)
# Sendo (in) um operador lógico, retornará 'True' ou 'False'

print('-'*15)

print('Transformação:')
frase = '   Python é uma Línguagem de Programação   '
print('Frase: {}'.format(frase))
print(frase.replace('Python', 'JavaScript'))
# Reposição ou troca de caracteres ou palavra
print(frase.upper())
# Caracteres minúsculos passam a ser maiúsculos
print(frase.lower())
# Caracteres maiúsculos passam a ser minúsculos
print(frase.capitalize())
# Mantém o primeiro caractere em maiúsculo, enquanto os outros passam a ser minúsculos
print(frase.title())
# O primeiro caractere de cada palavra passa a ser maiúsculo, mantendo ou tornando os outros minúsculos
print(frase.strip())
# Remove os espaços inúteis nas extremidades da string
print(frase.rstrip())
# Remove os espaços inúteis do final da string(right)
print(frase.lstrip())
# Remove os espaços inúteis do ínicio da string(left)

print('-'*15)

print('Divisão:')
frase = 'Rumo ao banco de dados'
print('Frase: {}'.format(frase))
print(frase.split())
# Divide as palavras ou caracteres isolados de uma string a partir dos espaços vazios existentes - gerando uma lista com a quantidade
print('-'.join(frase.split()))
# Une as strings da lista usando um determinado caractere '' formando uma única string
# Aceita um arquivo como input e fala qual é a extensão
arquivo = input ("Digite o nome do arquivo: ")
arquivo = arquivo.split(".")
print (f'O arquivo {arquivo[0]} apresenta a extensão {arquivo[1]}')

# Usaremos o ANSI para colorir o código.
# Para representar uma cor em python no sistema ANSI, representamos da seguinte maneira:
# \033[0;33;44m
# o primeiro número (0) é o estilo do texto 
#( 0 - nenhum 1 - negrito 4 - sublinhado 7 - negativo )
# o segundo número (33) é a cor do texto
#(dos números 30 a 37 possuem as cores de texto)
# o terceiro número (44) é a cor do background do texto
#(dos número 40 a 47 possuem as cores do background)

print('\033[7;31;42mHello World')

#Preto	\033[1;30m	 \033[1;40m                        # letras  \ fundo
#Vermelho	\033[1;31m	\033[1;41m
#Verde	\033[1;32m	\033[1;42m
#Amarelo	\033[1;33m	\033[1;43m
#Azul	\033[1;34m	\033[1;44m
#Magenta	\033[1;35m	\033[1;45m
#Cyan	\033[1;36m	\033[1;46m
#Cinza Claro	\033[1;37m	\033[1;47m
#Cinza Escuro	\033[1;90m	\033[1;100m
#Vermelho Claro	\033[1;91m	\033[1;101m
#Verde Claro	\033[1;92m	\033[1;102m
#Amarelo Claro	\033[1;93m	\033[1;103m
#Azul Claro	\033[1;94m	\033[1;104m
#Magenta Claro	\033[1;95m	\033[1;105m
#Cyan Claro	\033[1;96m	\033[1;106m
#Branco	\033[1;97m	\033[1;107m
#Negrito	\033[;1m	-
#Inverte	\033[;7m	-
#Reset (remove formatação)	\033[0;0m	-
import math  # para a questão 10 na utilização do PI

#Exemplos
#Inteiros (int)
print(4 + 2)
print(4 - 2)
print(4 * 2)
print(4 // 2)
print(4 % 2)

#Ponto Flutuante (float)
print(4.2 + 2)
print(4.2 - 2)
print(4.2 * 2)
print(4.2 / 2)
print(4.2 ** 2)

#String (str)
nome = "  Gustavo@gmail.com "
print(nome.upper())
print(nome.lower())
print(nome.strip())
print(nome.split("@"))
print(nome+nome)

#Booleanos(bool)
val1 = False
val2 = False

print(val1 and val2)


# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
try:
    num1 = int(input("Informe um número inteiro (soma): "))
    num2 = int(input("Informe um número inteiro: "))
    result = num1 + num2
    print(result)
except TypeError as e:
    print(e) # Imprimir msg de Erro.
else:
    print("sucesso")    
finally:
    print("soma dois números inteiros")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
try:
    num1 = int(input("Informe um número inteiro (resto): "))
    result = num1 % 5
    print(result)
except TypeError as e:
    print(e) # Imprimir msg de Erro.
else:
    print("sucesso")  
finally:
    print("resto da divisão")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
try:
    num1 = int(input("Informe um número inteiro (multiplique): "))
    num2 = int(input("Informe um número inteiro: "))
    result = num1 * num2
    print(result)
except TypeError as e:
    print(e) # Imprimir msg de Erro.
else:
    print("sucesso")  
finally:
    print("multiplique dois números fornecidos")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
try:
    num1 = int(input("Informe um número inteiro (divisão inteira): "))
    num2 = int(input("Informe um número inteiro: "))
    result = num1//num2
    print(result)
except TypeError as e:
    print(e) # Imprimir msg de Erro.
else:
    print("sucesso")    
finally:
    print("o importante que chegou aqui")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
try:
    num1 = int(input("Informe um número inteiro (quadrado): "))
    result = num1 ** 2
    print(result)
    print(pow(num1,2))

except TypeError as e:
    print(e) # Imprimir msg de Erro.
else:
    print("sucesso")    
finally:
    print("calcule o quadrado de um número fornecido")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
try:
    num1 = float(input("Informe um número FLUTUANTE (soma flutuantes): "))
    num2 = float(input("Informe um número FLUTUANTE: "))
    result = num1 + num2
    print(f"{result:.2f}")
except TypeError as e:
    print(e) # Imprimir msg de Erro.
else:
    print("sucesso")    
finally:
    print("soma dois números flutuante")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
try:
    num1 = float(input("Informe um número FLUTUANTE (média flutuantes): "))
    num2 = float(input("Informe um número FLUTUANTE: "))
    result = (num1 + num2) / 2
    print(f"{result:.2f}")
except TypeError as e:
    print(e) # Imprimir msg de Erro.
else:
    print("sucesso")    
finally:
    print("Média dois números flutuante")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
try:
    num1 = float(input("Informe a potência BASE (potência): "))
    num2 = float(input("Informe a potência EXPOENTE (potência): "))
    result = num1 ** num2
    print(f"{result:.2f}")
except TypeError as e:
    print(e) # Imprimir msg de Erro.
else:
    print("sucesso")    
finally:
    print("calcule a potência")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
try:
    temp = float(input("Informe a Temperatura em Celsius: "))
    result = (temp * 9/5) + 32
    print(f"{result:.2f}")
except TypeError as e:
    print(e) # Imprimir msg de Erro.
else:
    print("sucesso")    
finally:
    print("Celsius para Fahrenheit")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio_do_circulo = float(input("Informe o Raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
try:
    texto = input("Informe um texto qualquer (para MAIÚSCULAS): ")
    result = texto.upper()
    print(result)

except TypeError as e:
    print(e) # Imprimir msg de Erro.
else:
    print("sucesso")    
finally:
    print("string do usuário e a converta para MAIÚSCULAS")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
try:
    texto = input("Informe um texto qualquer (para minúsculas): ")
    result = texto.lower()
    print(result)

except TypeError as e:
    print(e) # Imprimir msg de Erro.
else:
    print("sucesso")    
finally:
    print("letras minúsculas")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
try:
    texto = input("Informe uma frase com espaços no início e fim (para minúsculas): ")
    result = texto.strip()
    print(result)

except TypeError as e:
    print(e) # Imprimir msg de Erro.
else:
    print("sucesso")    
finally:
    print("imprima esta frase sem espaços")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data_usuario = input("Informe uma data no formato dd/mm/yyyy: ")
lista_dia_mes_ano = data_usuario.split("/")
print(f"O dia é: {lista_dia_mes_ano[0]}")
print(f"O mês é: {lista_dia_mes_ano[1]}")
print(f"O ano é: {lista_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
try:
    texto1 = input("Informe o primeiro Texto (concatenar): ")
    texto2 = input("Informe o segundo Texto: ")
    result = texto1 + ' ' + texto2
    print(result)
except TypeError as e:
    print(e) # Imprimir msg de Erro.
else:
    print("sucesso")    
finally:
    print("concatene duas strings")



# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação

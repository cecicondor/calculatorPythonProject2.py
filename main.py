#Basic calculator in Pyhton

print("Calculadora Básica")
print("Escolha a operação desejada através dos números")
print("1. Soma (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")

#Receive the choice of user

opcao = input("Digite o número da operação (1,2,3,4):"

#Receive two numbers and covert it into decimal number (float)

num1 = float(input("Digite o primeiro número:")
num2 = float(input("Digite o segundo número:")

#Realize the calcule 

if opcao=='1':
	resultado = num1 + num2
	print (f"resultado: {num1}+{num2}= {resultado}")
	
	elif opcao == '2':
  resultado = num1 - num2
  print(f"Resultado: {num1} - {num2} = {resultado}")

elif opcao == '3':
  resultado = num1 * num2
  print(f"Resultado: {num1} * {num2} = {resultado}")

elif opcao == '4':
  # Tratamento para evitar erro de divisão por zero
  if num2 != 0:
    resultado = num1 / num2
    print(f"Resultado: {num1} / {num2} = {resultado}")

		else:
			print("Erro: Não é possível realizar cálculo")
	
else:
  print("Opção inválida! Reinicie o programa e escolha um número de 1 a 4.")
  
  ---the second else, became to the first option, the first else became to the division 

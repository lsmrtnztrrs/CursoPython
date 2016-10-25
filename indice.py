res=2
while res==2:
	p=int(input("Dame tu peso en Kg: "))
	e=float(input("Dame tu estatura en metros: "))
	imc=p/(e*e)
	if imc<18.5:
		print("Tu indice de masa corporal es: ", imc,"tienes bajo peso")
	elif imc<24.9:
		print("Tu indice de masa corporal es: ", imc,"tienes peso normal")
	elif imc<29.9:
		print("Tu indice de masa corporal es: ", imc,"tienes sobrepeso")
	
	res=int(input("Deseas salir:\n1)Salir \n2)continuar\n>"))
	if res==1:
		break
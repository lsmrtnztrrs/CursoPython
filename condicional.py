edad=int(input("Dame tu edad: "))
if edad<0:
	print("Esa edad no existe")
elif edad>=0 and edad<2:
	print("Eres un bebe")
elif edad>=2 and edad<10:
	print("Eres un niño")
elif edad>=10 and edad<13:
	print("Eres un puberto")
elif edad>=13 and edad<18:
	print("Eres un adolescente")
elif edad>=18 and edad<70:
	print("Eres un viejito")
else:
	print("No te creo")
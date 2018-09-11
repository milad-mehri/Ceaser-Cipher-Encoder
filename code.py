def encrypt():
	a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]#alphebet
	b = list(input("Plain text please?:").upper())
	c = int(input("Shift number 1 to 26:"))
	new_string = ""
	for e in b:
		for i in range(len(a)):
			if e == a[i]:
				new_string += a[i+c] 
	
	print(new_string.lower())


encrypt()

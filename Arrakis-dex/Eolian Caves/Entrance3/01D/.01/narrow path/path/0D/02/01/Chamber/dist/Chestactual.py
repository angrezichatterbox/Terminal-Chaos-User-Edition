def unlocked():
        with open("DarkBookI.txt","w") as file:
                file.write("a=65 72 62 6F 78 2F 47 6F 64 2D 53 75 69 74 65\n")

print("The noxious fumes of corruption encapsulates the chest. Use artifact containing holy light magic to disperse it and uncover the secrets the treasurous shrine holds..")
if "CSigVmaroAn"==input():
	print("SHEOOOOOOOHHHH")
	unlocked()
else:
	print("Invalid. Try again.")

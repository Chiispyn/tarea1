
menu=None
while menu !=5:
    pikachu = 4500
    otaku = 5000
    pulpo = 5200
    anguila = 4800
    cont1=0
    cont2=0
    cont3=0   
    cont4=0
    menu = print("Bienvenido al super delivery")
    menu = print("1.- Pikcachu rolla $4500")
    menu = print("2.- Otaku roll $5000")
    menu = print("3.- Pulpo venenoso roll $5200")
    menu = print("4.- Anguila venenosa roll $4800")
    menu = print("5.- Salir")
    menu = int(input("seleccione su opcion "))
    if menu==1:
            if menu==1: 
                print("ha seleccionado Pikachu rolls ")
                cont1 = int(input("Cuantos desea= "))
                print(f"ha agregado {pikachu*cont1} a su carrito")
            
    elif menu==2:
            if menu==2:
                print("ha seleccionado otaku rolls")
                cont2= int(input("Cuantos desea "))
            
    elif menu==3:
            if menu==3:
                print("Selecciono pulpo rolls  ")
                cont3 = int(input("Cuantos desea "))
                print(f"Agrego {pulpo*cont3}")
            
    elif menu==4:
            if menu == 4:
                print(f"Selecciono Anguila venenosa roll {pulpototal}")
                cont4 = int(input("Cuantos desea "))
                print(f"agrego {anguila*cont4}")
            
    elif menu==5:
           print("saliendo")  
pikachutotal = pikachu*cont1
otakutotal = otaku*cont2
anguilatotal = anguila*cont3
pulpototal = pulpo*cont4      
total=pikachutotal+anguilatotal+pikachutotal+pulpototal
print(f"su valor total es {total}")
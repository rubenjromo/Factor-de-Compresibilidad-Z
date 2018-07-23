presion_reducida = []
presionideal = []
error = []
z = []

def temperatura_reducida (temperatura, temperatura_critica):
    return "{0:.3f}".format (temperatura/temperatura_critica) 
    
def calcular_presion_reducida (presion_ideal, presion_critica):
    global presion_reducida
    pr = (presion_ideal/presion_critica)
    presion_reducida.append(pr)
    return presion_reducida[-1]

def calcular_presion_ideal(moles,temperatura,volumen):
    global presionideal
    pi = ((moles*0.082*temperatura)/volumen)
    presionideal.append(pi)
    return presionideal[-1]

def ingrese_valores_iniciales():
    global temperatura
    global volumen
    global moles
    global temperatura_critica
    global presion_critica
    temperatura = float(input('Ingrese temperatura en K: '))
    volumen = float(input('Ingrese volumen en litros: '))
    moles = float(input('Ingrese cantidad de moles: '))
    temperatura_critica = float(input('Ingrese temperatura critica en K: '))
    presion_critica = float(input('Ingrese presion critica en atm: '))

def verificar_error(presion_supuesta, presion_calculada):
    global error
    er = ((abs((presion_supuesta - presion_calculada)/presion_supuesta)*100))
    error.append(er)
    return error[-1]


def ingresar_z():
    global z
    zz = float(input('Ingrese valor z calculado en tabla: '))
    z.append(zz)
    return z[-1]

def presion_calculada(z,presion_ideal):
    global presionideal
    pc = (z*presion_ideal)
    presionideal.append(pc)
    return presionideal[-1]
    

while True:
    ingrese_valores_iniciales()
    print ('La presion ideal inicial es: ',calcular_presion_ideal(moles,temperatura,volumen))
    print('La temperatura reducida es: ',temperatura_reducida(temperatura, temperatura_critica))
    print('La presion reducida es: ', calcular_presion_reducida(presionideal[-1], presion_critica))
    print('Con la T reducida y la P reducida calcular valor de Z en las tablas')
    ingresar_z()
    presion_calculada(z[-1],presionideal[-1])
    if verificar_error(presionideal[-2],presionideal[-1]) <= 0.05:
        print('Error: ' , verificar_error(presionideal[-2],presionideal[-1]))
        print('Estimacion correcta')
        print('Valor z: ', z[-1])
        break
    else:
        while True:
            if error[-1] > 0.05 :
                print('Error: ' , verificar_error(presionideal[-2],presionideal[-1]))
                print('La temperatura reducida es: ',temperatura_reducida (temperatura, temperatura_critica))
                print('La presion reducida es: ', calcular_presion_reducida(presionideal[-1], presion_critica))
                print('Con la T reducida y la P reducida calcular valor de Z en las tablas')
                ingresar_z()
                presion_calculada(z[-1],presionideal[-1])
                print(presion_reducida) 
                print(presionideal)
                print(error)
                print(z)
            else:
                print('Error: ' , verificar_error(presionideal[-2],presionideal[-1]))
                print('Estimacion correcta')
                print('Valor z: ', z[-1])
                break
        break
        print('Error: ' , verificar_error(presionideal[-2],presionideal[-1]))
        print('Estimacion correcta')
        print('Valor z: ', z[-1])
        
    
            
        
            
            
            
        


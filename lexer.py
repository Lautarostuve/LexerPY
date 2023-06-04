def afd(cadena):
    estado_actual = 0
    estados_finales=[3,2]
    for caracter in cadena:
        if estado_actual == 0 and caracter =='a':
            estado_actual = 1
        elif estado_actual == 0 and caracter =='b':
            estado_actual = 0
        elif estado_actual == 0 and caracter == 'c':
            estado_actual = 0
    
    if estado_actual in estados_finales:
        print('la cadena es aceptada')
    else:
        print('cadena no aceptada')
        
        
afd('aabcaaabc')



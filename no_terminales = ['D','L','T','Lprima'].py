
no_terminales = ['D','L','T','Lprima']

terminales = ['int','float','id',',']


SD = { 
    'D' : {'int' : ['T', 'L'], 'float' : ['T','L'], 'id' : [], ',' : [], '#' : [] },
    
    'T' : {'int' : ['int'], 'float' : ['float'], 'id' : [], ',' : [], '#' : [] },
    
    'L' : {'int' : [], 'float' : [], 'id' : ['id','Lprima'], ',' : [], '#' : [] },
    
    'Lprima' : {'int' : [], 'float' : [], 'id' : [], ',' : [',','L'], '#' : [] }
    
    }



def parser(lista_tokens):                   #la lista de tokens viene del lexer
    datos_parser = {
        'tokens': lista_tokens,
        'posicion_indice': 0,
        'error': False,     
    }
    producciones = []
    
    
    def principal():
        pni('D')
        token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
        if token_actual != '#' or datos_parser['error']:
            print('la cadena no pertenece al lenguaje')
            return False
        else: 
            print ('la cadena pertenece')
            producciones.pop()
            print (producciones)

    def pni(no_terminal):
        terminal = datos_parser['tokens'][datos_parser['posicion_indice']][0]
        #print(terminal) acumulador
        parteDerecha = SD[no_terminal][terminal]          #no terminal es el tope de la pila, terminal es donde apunta el puntero en la cadena
        #print(parteDerecha) acumulador
        producciones.extend([no_terminal])
        producciones.extend(['->'])
        producciones.extend(parteDerecha)
        producciones.extend(['siguienteProduccion'])
        procesar(parteDerecha)
        
    
    def procesar(parteDerecha):  #ingresa una produccion
        for simbolo in parteDerecha:
            #print(simbolo)
            token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
            datos_parser['error']= False
            if simbolo in terminales:
                if simbolo == token_actual:
                    datos_parser['posicion_indice'] += 1
                    #print ('sumo 1')
                else:
                    datos_parser['error'] = True
                    break
        
            elif simbolo in no_terminales:
                pni(simbolo)
                if datos_parser['error']:
                    break
    
                
    return principal()


parser((['int','2'],['id','i'],[',',','],['id','j'],['#','#']))

parser((['int','2'],['id','i'],['#','#']))

parser((['float', 4,33],['id','a'],[",",','],['id','b'],[',',','],['id','caca'],['#','#']))

#parteDerecha = SD['L']['id']
#print (parteDerecha) 
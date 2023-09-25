from algoritmolexer import lexer

no_terminales = ['Program','ListaSentencias','ListaSentenciasPrima', 'Sentencia', 'SentenciaSi', 'SentenciaSiPrima',
                 'SentenciaRepetir', 'SentenciaAsig', 'SentenciaLeer', 'SentenciaMostrar',
                 'SentenciaFun', 'Proc', 'ListaPar', 'ListaParPrima', 'Expresion', 'ExpresionPrima', 'Expresion2', 'Expresion2Prima',
                 'Factor', 'Termino', 'TerminoPrima']

terminales = ["token_si","token_sino","token_entonces","token_finsi","token_finfunc",
              "token_func","token_repetir","token_hasta","token_leer","token_mostrar",
              "token_equal","token_id","token_num","token_oprel","token_parentesis1",
              "token_parentesis2","token_puntoycoma","token_opsuma","token_opmult",'#']
SD = { 
    'Program' : {"token_si" : ['ListaSentencias'],"token_func" : ['ListaSentencias'],
                 "token_repetir" : ['ListaSentencias'], "token_leer" : ['ListaSentencias'],
                "token_mostrar" : ['ListaSentencias'],"token_id" : ['ListaSentencias']},
                 
    
    'ListaSentencias' : {"token_si" : ['Sentencia','ListaSentenciasPrima'],
                 "token_func" : ['Sentencia','ListaSentenciasPrima'], "token_repetir" : ['Sentencia','ListaSentenciasPrima'],
                  "token_leer" : ['Sentencia','ListaSentenciasPrima'], "token_mostrar" : ['Sentencia','ListaSentenciasPrima'],
                 "token_id" : ['Sentencia','ListaSentenciasPrima']},
    
    'ListaSentenciasPrima' : { "token_sino" : [], "token_finsi" : [], "token_finfunc" : [''],
                 "token_hasta" : [], "token_puntoycoma" : ["token_puntoycoma", 'Sentencia', 'ListaSentenciasPrima'],'#':[]},
    
    'Sentencia' : {"token_si" : ['SentenciaSi'],"token_func" : ['SentenciaFun'], "token_repetir" : ['SentenciaRepetir'],
                   "token_leer" : ['SentenciaLeer'], "token_mostrar" : ['SentenciaMostrar'],
                 "token_id" : ['SentenciaAsig']},

    
    'SentenciaSi' : {"token_si" : ["token_si", 'Expresion', "token_entonces", 'ListaSentencias', 'SentenciaSiPrima']},
    
    'SentenciaSiPrima' : { "token_sino" : ["token_sino", 'ListaSentencias', "token_finsi"], "token_finsi" : ["token_finsi"]},
    
    'SentenciaRepetir' : { "token_repetir" : ["token_repetir", 'ListaSentencias', "token_hasta", 'Expresion']},
    
    'SentenciaAsig' : {"token_id" : ["token_id", "token_equal", 'Expresion']},
      
    'SentenciaLeer' : { "token_leer" : ["token_leer", "token_id"]},
       
    'SentenciaMostrar' : {"token_mostrar" : ["token_mostrar", 'Expresion']},
    
    'SentenciaFun' : {"token_func" : ["token_func", 'Proc', "token_finfunc"]},
    
    'Proc' : {"token_id" : ["token_id", "token_parentesis1", 'ListaPar', "token_parentesis2", 'ListaSentencias']},
    
    'ListaPar' : {"token_id" : ["token_id", 'ListaParPrima']},
    
    'ListaParPrima' : {"token_parentesis2" : [],"token_puntoycoma" : ["token_puntoycoma", "token_id" ,'ListaParPrima']},
    
    'Expresion' : {"token_id" : ['Expresion2', 'ExpresionPrima'], "token_num" : ['Expresion2', 'ExpresionPrima'],
                 "token_parentesis1" : ['Expresion2', 'ExpresionPrima']},
    
    'ExpresionPrima' : {"token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                   "token_hasta" : [], "token_oprel" : ["token_oprel", 'Expresion2'], "token_parentesis2" : [],
                "token_puntoycoma" : [],'#':[]},
    
    'Expresion2' : {"token_id" : ['Termino', 'Expresion2Prima'], "token_num" : ['Termino', 'Expresion2Prima'],
                    "token_parentesis1" : ['Termino', 'Expresion2Prima']},
    
    'Expresion2Prima' : {"token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                "token_hasta" : [], "token_oprel" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : ["token_opsuma", 'Termino', 'Expresion2Prima'],'#':[] },
    
    'Factor' : {"token_id" : ["token_id"], "token_num" : ["token_num"],
                "token_parentesis1" : ["token_parentesis1", 'Expresion', "token_parentesis2"]},
    
    'Termino' : {"token_id" : ['Factor', 'TerminoPrima'], "token_num" : ['Factor', 'TerminoPrima'],
                 "token_parentesis1" : ['Factor', 'TerminoPrima']},
    
    'TerminoPrima' : {"token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                        "token_hasta" : [],"token_oprel" : [],"token_parentesis2" : [],
                        "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : ["token_opmult", 'Factor', 'TerminoPrima'],'#':[]}
            
                        
}
def parser(lista_tokens):                   #la lista de tokens viene del lexer
    datos_parser = {
        'tokens': lista_tokens,
        'posicion_indice': 0,
        'error': False,     
    }
    producciones = []
    def principal():
        pni('Program')
        token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
        if token_actual != '#' or datos_parser['error']:
            print('la cadena no pertenece al lenguaje')
            return False
        else:
            print ('la cadena pertenece al lenguaje')
            producciones.pop()
            print (producciones)

    def pni(no_terminal):
        terminal = datos_parser['tokens'][datos_parser['posicion_indice']][0]
        if terminal in SD[no_terminal].keys():
            parteDerecha = SD [no_terminal][terminal] 
            producciones.extend([no_terminal])
            producciones.extend(['->'])
            producciones.extend(parteDerecha)
            producciones.extend(['siguienteProduccion'])
            procesar(parteDerecha)
        else:
            print('la cadena no pertence al lenguaje')
    
    def procesar(parteDerecha):  #ingresa una produccion
        for simbolo in parteDerecha:
            token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
            datos_parser['error']= False
            if simbolo in terminales:
                if simbolo == token_actual:
                    datos_parser['posicion_indice'] += 1
                else:
                    datos_parser['error'] = True
                    break
        
            elif simbolo in no_terminales:
                pni(simbolo)
                if datos_parser['error']:
                    break
                
    return principal()

##En esta primera prueba el parser deberia aceptarnos el leer variablex
print("leer variablex")
tokens=lexer("leer variablex")
tokens.extend([('#','#')])
parser(tokens)
##Esta cadena no pertenece al lenguaje
print("entonces si 4 / 5 entonces variable finsi")
tokens=lexer("entonces si 4 / 5 entonces variable finsi")
tokens.extend([('#','#')])
parser(tokens)

print("leer variable;vauxi equal 5")
tokens=lexer("leer variable;vauxi equal 5") 
tokens.extend([('#','#')])
parser(tokens)

print ("si 6>7 entonces leer id finsi")
tokens=lexer("si 6>7 entonces leer id finsi")
tokens.extend([('#','#')])
parser(tokens)

print("repetir leer vauxi hasta vauxi > variableprima")
tokens=lexer("repetir leer vauxi hasta vauxi > variableprima")
tokens.extend([('#','#')])
parser(tokens)

print ("func variable ( variable ; variable) repetir variable equal 3 hasta 4 finfunc")
tokens=lexer("func variable ( variable ; variable) repetir variable equal 3 hasta 4 finfunc")
tokens.extend([('#','#')])
parser(tokens)

print("mostrar 3 * 2 > 5 * 6")
tokens=lexer("mostrar 3 * 2 > 5 * 6")
tokens.extend([('#','#')])
parser(tokens)

print("si 3 > 4")
tokens=lexer("si 3 > 4")
tokens.extend([('#','#')])
parser(tokens)

print("id equal 3")
tokens=lexer("id equal 3")
tokens.extend([('#','#')])
parser(tokens)

print("si 4 > 3 entonces repetir leer id hasta 3 sino mostrar 4 finsi")         
tokens=lexer("si 4 > 3 entonces repetir leer id hasta 3 sino mostrar 4 finsi")
tokens.extend([('#','#')])
parser(tokens)

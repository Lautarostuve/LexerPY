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
    'Program' : {"token_si" : ['ListaSentencias'], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                "token_func" : ['ListaSentencias'], "token_repetir" : ['ListaSentencias'], "token_hasta" : [], "token_leer" : ['ListaSentencias'],
                "token_mostrar" : ['ListaSentencias'], "token_equal" : [], "token_id" : ['ListaSentencias'], "token_num" : [], "token_oprel" : [],
                "token_parentesis1" : [], "token_parentesis2" : [],"token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'ListaSentencias' : {"token_si" : ['Sentencia','ListaSentenciasPrima'], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : ['Sentencia','ListaSentenciasPrima'], "token_repetir" : ['Sentencia','ListaSentenciasPrima'], "token_hasta" : [],
                  "token_leer" : ['Sentencia','ListaSentenciasPrima'], "token_mostrar" : ['Sentencia','ListaSentenciasPrima'], "token_equal" : [],
                 "token_id" : ['Sentencia','ListaSentenciasPrima'], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'ListaSentenciasPrima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [''],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : ["token_puntoycoma", 'Sentencia', 'ListaSentenciasPrima'] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'Sentencia' : {"token_si" : ['SentenciaSi'], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : ['SentenciaFun'], "token_repetir" : ['SentenciaRepetir'], "token_hasta" : [], "token_leer" : ['SentenciaLeer'], "token_mostrar" : ['SentenciaMostrar'], "token_equal" : [],
                 "token_id" : ['SentenciaAsig'], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'SentenciaSi' : {"token_si" : ["token_si", 'Expresion', "token_entonces", 'ListaSentencias', 'SentenciaSiPrima'], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'SentenciaSiPrima' : {"token_si" : [], "token_sino" : ["token_sino", 'ListaSentencias, "token_finsi'], "token_entonces" : [], "token_finsi" : ["token_finsi"], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'SentenciaRepetir' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : ["token_repetir", 'ListaSentencias', "token_hasta", 'Expresion'], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'SentenciaAsig' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ["token_id", "token_equal", 'Expresion'], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
      
    'SentenciaLeer' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : ["token_leer", "token_id"], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
       
    'SentenciaMostrar' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : ["token_mostrar", 'Expresion'], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'SentenciaFun' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : ["token_func", 'Proc', "token_finfunc"], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'Proc' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ["token_id", "token_parentesis1", 'ListaPar', "token_parentesis2", 'ListaSentencias'], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'ListaPar' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ["token_id", 'ListaParPrima'], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : [],'#':[]},
    
    'ListaParPrima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : ["token_puntoycoma", "token_id" 'ListaParPrima'] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'Expresion' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ['Expresion2', 'ExpresionPrima'], "token_num" : ['Expresion2', 'ExpresionPrima'], "token_oprel" : [], "token_parentesis1" : ['Expresion2', 'ExpresionPrima'], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'ExpresionPrima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ['Termino', 'Expresion2Prima'], "token_num" : ['Termino', 'Expresion2Prima'], "token_oprel" : ["token_oprel", 'Expresion2'], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'Expresion2' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ['Termino', 'Expresion2Prima'], "token_num" : ['Termino', 'Expresion2Prima'], "token_oprel" : [], "token_parentesis1" : ['Termino', 'Expresion2Prima'], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[] },
    
    'Expresion2Prima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : ["token_opsuma", 'Termino', 'Expresion2Prima'], "token_opmult" : [],'#':[] },
    
    'Factor' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ["token_id"], "token_num" : ["token_num"], "token_oprel" : [], "token_parentesis1" : ["token_parentesis1", 'Expresion', "token_parentesis2"], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'Termino' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ['Factor', 'TerminoPrima'], "token_num" : ['Factor', 'TerminoPrima'], "token_oprel" : [], "token_parentesis1" : ['Factor', 'TerminoPrima'], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [],'#':[]},
    
    'TerminoPrima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : ["token_opmult", 'Factor', 'TerminoPrima'],'#':[]}
            
                        
}
def parser(lista_tokens):                   #la lista de tokens viene del lexer
    datos_parser = {
        'tokens': lista_tokens,
        'posicion_indice': 0,
        'error': False,     
    }
    
    def principal():
        pni('Program')
        token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
        if token_actual != '#' or datos_parser['error']:
            print('la cadena no pertenece al lenguaje')
            return False
        else:
            print ('la cadena pertenece al lenguaje')

    def pni(no_terminal):
        terminal = datos_parser['tokens'][datos_parser['posicion_indice']][0]
        parteDerecha = SD [no_terminal][terminal]           #no terminal es el tope de la pila, terminal es donde apunta el puntero en la cadena
        procesar(parteDerecha)
        
    
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

parser([("token_leer", "leer"),("token_id", "vauxi"),("#","#")])
parser([('token_entonces', 'entonces'), ('token_si', 'si'), ('token_num', '4'), ('token_opmult', '/'), ('token_num', '5'), ('token_entonces', 'entonces'), ('token_id', 'variable'), ('token_finsi', 'finsi')])
tokens=lexer("leer variable;vauxi equal 5") 
tokens.extend([('#','#')])
parser(tokens)
tokens=lexer("si 6>7 entonces leer id finsi")
tokens.extend([('#','#')])
print (tokens)
parser(tokens)
tokens=lexer("repetir leer vauxi hasta vauxi > variableprima")
tokens.extend([('#','#')])
parser(tokens)
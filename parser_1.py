no_terminales = ['Program','ListaSentencias','ListaSentenciasPrima', 'Sentencia', 'SentenciaSi', 'SentenciaSiPrima',
                 'SentenciaRepetir', 'SentenciaAsig', 'SentenciaLeer', 'SentenciaMostrar',
                 'SentenciaFun', 'Proc', 'ListaPar', 'ListaParPrima', 'Expresion', 'ExpresionPrima', 'Expresion2', 'Expresion2Prima',
                 'Factor', 'Termino', 'TerminoPrima']

terminales = ["token_si","token_sino","token_entonces","token_finsi","token_finfunc",
              "token_func","token_repetir","token_hasta","token_leer","token_mostrar",
              "token_equal","token_id","token_num","token_oprel","token_parentesis1",
              "token_parentesis2","token_puntoycoma","token_opsuma","token_opmult",'#', "lambda"]

SD = { 
    'Program' : {"token_si" : ['ListaSentencias'], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                "token_func" : ['ListaSentencias'], "token_repetir" : ['ListaSentencias'], "token_hasta" : [], "token_leer" : ['ListaSentencias'],
                "token_mostrar" : ['ListaSentencias'], "token_equal" : [], "token_id" : ['ListaSentencias'], "token_num" : [], "token_oprel" : [],
                "token_parentesis1" : [], "token_parentesis2" : [],"token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'ListaSentencias' : {"token_si" : ['Sentencia','ListaSentenciasPrima'], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : ['Sentencia','ListaSentenciasPrima'], "token_repetir" : ['Sentencia','ListaSentenciasPrima'], "token_hasta" : [],
                  "token_leer" : ['Sentencia','ListaSentenciasPrima'], "token_mostrar" : ['Sentencia','ListaSentenciasPrima'], "token_equal" : [],
                 "token_id" : ['Sentencia','ListaSentenciasPrima'], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'ListaSentenciasPrima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : ["token_puntoycoma", 'Sentencia', 'ListaSentenciasPrima'] , "token_opsuma" : [], "token_opmult" : [] "lambda" : []},
    
    'Sentencia' : {"token_si" : ['SentenciaSi'], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : ['SentenciaFun'], "token_repetir" : ['SentenciaRepetir'], "token_hasta" : [], "token_leer" : ['SentenciaLeer'], "token_mostrar" : ['SentenciaMostrar'], "token_equal" : [],
                 "token_id" : ['SentenciaAsig'], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'SentenciaSi' : {"token_si" : ["token_si", 'Expresion', "token_entonces", 'ListaSentencias', 'SentenciaSi'], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'SentenciaSiPrima' : {"token_si" : [], "token_sino" : ["token_sino", 'ListaSentencias, "token_finsi'], "token_entonces" : [], "token_finsi" : ["token_finsi"], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'SentenciaRepetir' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : ["token_repetir", 'ListaSentencias', "token_hasta", 'Expresion'], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'SentenciaAsig' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ["token_id", "token_equal", 'Expresion'], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
      
    'SentenciaLeer' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : ["token_leer", "token_id"], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
       
    'SentenciaMostrar' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : ["token_mostrar", 'Expresion'], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'SentenciaFun' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : ["token_func", 'Proc', "token_finfunc"], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'Proc' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ["token_id", "token_parentesis1", 'ListaPar', "token_parentesis2", 'ListaSentencias'], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'ListaPar' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ["token_id", 'ListaParPrima'], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'ListaParPrima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : ["token_puntoycoma", "token_id" 'ListaParPrima'] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'Expresion' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ['Expresion2', 'ExpresionPrima'], "token_num" : ['Expresion2', 'ExpresionPrima'], "token_oprel" : [], "token_parentesis1" : ['Expresion2', 'ExpresionPrima'], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'ExpresionPrima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ['Termino', 'Expresion2Prima'], "token_num" : ['Termino', 'Expresion2Prima'], "token_oprel" : ["token_oprel", 'Expresion2'], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'Expresion2' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : ['Termino', 'Expresion2Prima'], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : ["token_opsuma", 'Termino', 'Expresion2Prima'], "token_opmult" : [], "lambda" : []},
    
    'Expresion2Prima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'Factor' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : ["token_parentesis1", 'Expresion', "token_parentesis2"], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'Termino' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : ['Factor', 'TerminoPrima'], "token_num" : ['Factor', 'TerminoPrima'], "token_oprel" : [], "token_parentesis1" : ['Factor', 'TerminoPrima'], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : [], "lambda" : []},
    
    'TerminoPrima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : ["token_opmult", 'Factor', 'TerminoPrima'], "lambda" : []},
            
                

                
}
# matigay3pa


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

    def pni(no_terminal):
        terminal = datos_parser['tokens'][datos_parser['posicion_indice']]
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


parser(([token1,lexema1]),(token2,lexema2),...,('eof','eof'))
            

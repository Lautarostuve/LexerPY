no_terminales = ['Program','ListaSentencias','ListaSentenciasPrima', 'Sentencia', 'SentenciaSi', 'SentenciaSiPrima',
                 'SentenciaRepetir', 'SentenciaAsig', 'SentenciaLeer', 'SentenciaMostrar',
                 'SentenciaFun', 'Proc', 'ListaPar', 'ListaParPrima', 'Expresion', 'ExpresionPrima', 'Expresion2', 'Expresion2Prima',
                 'Factor', 'Termino', 'TerminoPrima']

terminales = ["token_si","token_sino","token_entonces","token_finsi","token_finfunc",
              "token_func","token_repetir","token_hasta","token_leer","token_mostrar",
              "token_equal","token_id","token_num","token_oprel","token_parentesis1",
              "token_parentesis2","token_puntoycoma","token_opsuma","token_opmult"]

producciones = {
    'Program':[['ListaSentencias']],
    'ListaSentencias' : [['ListaSentencias',"token_puntoycoma",'Sentencia'],['Sentencia']],
    
    'noterminalp':[[ladoderecho1],...,[ladoderechop]],
    
}

SD = { 
    'Program' : {"token_si" : ['ListaSentencias'], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'ListaSentencias' : {"token_si" : ['ListaSentencias'], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'ListaSentenciasPrima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'Sentencia' : {"token_si" : ['ListaSentencias'], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'SentenciaSi' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'SentenciaSiPrima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'SentenciaRepetir' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'SentenciaAsig' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
      
    'SentenciaLeer' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
       
    'SentenciaMostrar' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'SentenciaFun' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'Proc' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'ListaPar' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'ListaParPrima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'Expresion' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'ExpresionPrima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'Expresion2' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'Expresion2Prima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'Factor' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'Termino' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
    
    'TerminoPrima' : {"token_si" : [], "token_sino" : [], "token_entonces" : [], "token_finsi" : [], "token_finfunc" : [],
                 "token_func" : [], "token_repetir" : [], "token_hasta" : [], "token_leer" : [], "token_mostrar" : [], "token_equal" : [],
                 "token_id" : [], "token_num" : [], "token_oprel" : [], "token_parentesis1" : [], "token_parentesis2" : [],
                "token_puntoycoma" : [] , "token_opsuma" : [], "token_opmult" : []},
            
                

                
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
        if token_actual != 'eof' or datos_parser['error']:
            print('la cadena no pertenece al lenguaje')
            return False

    def pni(no_terminal):
        terminal = datos_parser['tokens'[datos_parser['posicion_indice']]]
        parteDerecha = SD [no_terminal[terminal]]           #no terminal es el tope de la pila, terminal es donde apunta el puntero en la cadena
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
            

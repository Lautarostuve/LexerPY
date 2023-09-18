no_terminales = ['Program','ListaSentencias', 'Sentencia', 'SentenciaSi',
                 'SentenciaRepetir', 'SentenciaAsig', 'SentenciaLeer', 'SentenciaMostrar',
                 'SentenciaFun', 'Proc', 'ListaPar', 'Expression', 'Expresion2', 'Factor',
                 'Termino']

terminales = ["token_si","token_sino","token_entonces","token_finsi","token_finfunc",
              "token_func","token_repetir","token_hasta","token_leer","token_mostrar",
              "token_equal","token_id","token_num","token_oprel","token_parentesis1",
              "token_parentesis2","token_puntoycoma","token_opsuma","token_opmult"]

producciones = {
    'Program':[['ListaSentencias']],
    'ListaSentencias' : [['ListaSentencias',"token_puntoycoma",'Sentencia'],['Sentencia']],
    
    'noterminalp':[[ladoderecho1],...,[ladoderechop]],
    
}
# HOLAAAAA


def parser(lista_tokens):                   #la lista de tokens viene del lexer
    datos_parser = {
        'tokens': lista_tokens,
        'posicion_indice': 0,
        'error': False,     
    }
    
    def principal():
        pni('S')
        token_actual = datos_parser['tokens'][datos_parser['posicion_indice']][0]
        if token_actual != 'eof' or datos_parser['error']:
            print('la cadena no pertenece al lenguaje')
            return False

    def pni(no_terminal):
        for parteDerecha in producciones[no_terminal]:
            posicion_a_retroceder = datos_parser['posicion_indice']
            procesar(parteDerecha)
            if datos_parser['error'] == True:
                datos_parser['posicion_indice'] = posicion_a_retroceder
            else:
                break
            
    
    def procesar(parteDerecha):
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
            

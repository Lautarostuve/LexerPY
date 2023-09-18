no_terminales = ['noterminal1',...,'noterminalp']
terminales = tokens_posibles

producciones = {
    'noterminal1':[['token1,Noterminalj',...,'tokenN'],...,[ladoderechok1]]
    ...
    'noterminalp':[[ladoderecho1],...,[ladoderechop]]
    
}


def parser(lista_tokens):
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
            

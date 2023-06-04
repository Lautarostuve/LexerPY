ESTADO_FINAL="Estado final"
ESTADO_TRAMPA="Estado trampa"
ESTADO_NO_FINAL="Estado aceptado"

TOKEN=[("tokenid",automataid),("tokennum",automatanum),
       ("tokenpalabrar",automatapalabrar),("tokenoprel",automataoprel),
       ("tokenopmat",automatamat), ("tokensigno",automatasigno)]
       
#comienza la locura

def automataid(lexema):
    estado = 0 #actual
    estado_final = [1] #listadeestadosfinales
    for caracter in lexema:
        if estado == 0 and caracter =='a':
            estado = 1
        elif estado == 0 and caracter =='b':
            estado = 0
        elif estado == 0 and caracter == 'c':
            estado = 0
        else:
            estado = -1
            break #llega a estado trampa
    
    if estado == -1:
        return ESTADO_TRAMPA       
    if estado in estado_final:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
    
#hacer todos los automatas
    
    
#algoritmo principal del lexer:

def lexer(codigo_fuente):
    tokens = [] #lista de tokens que va a devolver el lexer
    posicion_actual = 0
    while posicion_actual < len(codigo_fuente):
        while codigo_fuente[posicion_actual].isspace():
            posicion_actual = posicion_actual+1
        
        comienzo = posicion_actual
        posibles_tokens = []
        posibles_tokens_1mas = [] #posibles tokens si tomo el caracter siguiente
        lexema = "" #inicia el lexema que pasa a los afd
        todos_en_estado_trampa = False
        
        while not todos_en_estado_trampa:
            todos_en_estado_trampa = True
            lexema = codigo_fuente[comienzo:posicion_actual +1] #le paso del codigo fuente al lexema, las palabras desde el comienzo hasta la posicion actual +1
            posibles_tokens = posibles_tokens_1mas
            posibles_tokens_1mas = []
            
            for (un_tipo_de_token,afd) in TOKEN:
                simulacion_afd = afd(lexema)
                if simulacion_afd == ESTADO_FINAL:
                    posibles_tokens_1mas.append(un_tipo_de_token)
                    todos_en_estado_trampa= False
                elif simulacion_afd == ESTADO_NO_FINAL:
                    todos_en_estado_trampa= False
                    
            posicion_actual = posicion_actual + 1
            
            
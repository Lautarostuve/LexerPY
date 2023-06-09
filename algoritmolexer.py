ESTADO_FINAL="Estado final"
ESTADO_TRAMPA="Estado trampa"
ESTADO_NO_FINAL="Estado aceptado"

TOKEN=[("token_si",automatasi),("token_sino",automatasino),("token_entonces",automataentonces),("token_finsi",automatafinsi)
       ("token_finfunc",automatafinfunc),("token_func",automatafunc),("token_repetir",automatarepetir),("token_hasta",automatahasta)
       ("token_leer",automataleer),("token_mostrar",automatamostrar),("token_id", automataid),("token_num", automatanum),
       ("token_oprel", automataoprel), ("token_opmat", automatamat), ("token_signo", automatasigno)]
       
#ejemplo de automota facil

def automataid(lexema):
    estado = 0 #actual
    estado_final = [1] #listadeestadosfinales
    for caracter in lexema:
        if estado == 0 and caracter in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','u','x','w','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','U','X','W','Y','Z']:
            estado = 1
        elif estado== 1 and caracter in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','u','x','w','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','U','X','W','Y','Z','1','2','3','4','5','6','7','8','9','0']:
            estado=1
        else:
            estado = -1
            break #llega a estado trampa
    
    if estado == -1:
        return ESTADO_TRAMPA       
    elif estado in estado_final:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
    
#hacer todos los automatas
def automatanum(lexema):
    estado = 0 
    estados_finales = [1,2,4,12,17,24,20,31,36,40,47,48,51]
    for caracter in lexema:
        if estado == 0 and caracter in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
            estado = 48
        elif estado == 48 and caracter in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
            estado == 48
        else:
            estado = -1
            break
    
    if estado == -1:
        return ESTADO_TRAMPA       
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL  
    
def automataoprel(lexema):
    estado = 0
    estados_finales = [1,2,4,12,17,24,20,31,36,40,47,48,51]
    for caracter in lexema:
        if estado == 0 and caracter == '>':                 #Nose si esta bien, tome como estado final cada posible op de relacion
            estado = 51
        elif estado == 50 and caracter == '=':                 
            estado = 51
        else:
            estado =-1
            break
        
        if estado == 0 and caracter == '<':
            estado = 51
        elif estado == 50 and caracter == '=':
            estado = 51
        else:
            estado =-1
            break
        
        if estado == 0 and caracter == '=':
            estado = 49
        elif estado == 49 and caracter == '=':
            estado = 51
        else:
            estado =-1
            break

        if estado = 0 and caracter == '!':
            estado = 50
        elif estado == 50 and caracter == '=':
            estado = 51
        else:
            estado =-1
            break  

    if estado == -1:
        return ESTADO_TRAMPA       
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
#automata de palabras reservadas
def automatasi(lexema):
    estado = 0
    estados_finales = [2,4,12,17,24,20,31,36,40,47]
    for caracter in lexema:
        if estado == 0 and caracter == 's':
            estado = 1
        elif estado == 1 and caracter == 'i':
            estado = 2
            
        else:
            estado =-1
            break

    if estado == -1:
        return ESTADO_TRAMPA       
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def automatasino(lexema):
    estado = 0
    estados_finales = [2,4,12,17,24,20,31,36,40,47]
    for caracter in lexema:
        if estado == 0 and caracter == 's':
            estado = 1
        elif estado == 1 and caracter == 'i':
            estado = 2     
        elif  estado == 2 and caracter == 'n':
            estado = 3 
        elif estado == 3 and caracter == 'o':
            estado = 4

        else:
            estado =-1
            break

    if estado == -1:
        return ESTADO_TRAMPA       
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataentonces(lexema):
    estado = 0
    estados_finales = [2,4,12,17,24,20,31,36,40,47]
    for caracter in lexema:            
        if estado == 0 and caracter == 'e':
            estado = 5
        elif estado == 5 and caracter == 'n':
            estado = 6
        elif estado == 6 and caracter == 't':
            estado = 7
        elif estado == 7 and caracter == 'o':
            estado = 8
        elif estado == 8 and caracter == 'n':
            estado = 9
        elif estado == 9 and caracter == 'c':
            estado = 10
        elif estado == 10 and caracter == 'e':
            estado = 11
        elif estado == 11  and caracter == 's':
            estado = 12
        
        else:
            estado =-1
            break

    if estado == -1:
        return ESTADO_TRAMPA       
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

        
        
def automatafinsi(lexema):
    estado = 0
    estados_finales = [2,4,12,17,24,20,31,36,40,47]
    for caracter in lexema:             
        if estado == 0 and caracter == 'f':
            estado = 13
        elif estado == 13 and caracter == 'i':
            estado = 14
        elif estado == 14 and caracter == 'n':
            estado = 15
        elif estado == 15 and caracter == 's':
            estado = 16
        elif estado == 16 and caracter == 'i':
            estado = 17
        else:
            estado =-1
            break

    if estado == -1:
        return ESTADO_TRAMPA       
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

        
def automatafinfunc(lexema):
    estado = 0
    estados_finales = [2,4,12,17,24,20,31,36,40,47]
    for caracter in lexema:
        if estado == 0 and caracter == 'f':
            estado = 13
        elif estado == 13 and caracter == 'i':
            estado = 14
        elif estado == 14 and caracter == 'n':
            estado = 15            
        elif estado == 15 and caracter == 'f':
            estado = 21
        elif estado == 21 and caracter == 'u':
            estado = 22
        elif estado == 22 and caracter == 'n':
            estado = 23
        elif estado == 23 and caracter == 'c':
            estado = 24
        else:
            estado =-1
            break

    if estado == -1:
        return ESTADO_TRAMPA       
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
def automatafunc(lexema):
    estado = 0
    estados_finales = [2,4,12,17,24,20,31,36,40,47]
    for caracter in lexema:     
        if estado == 0 and caracter == 'f':
            estado =  13
        elif estado == 13 and caracter == 'u':
            estado = 18   
        elif estado == 18 and caracter == 'n':
            estado = 19   
        elif estado == 19 and caracter == 'c':
            estado = 20
        else:
            estado =-1
            break

    if estado == -1:
        return ESTADO_TRAMPA       
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
def automatarepetir(lexema):
    estado = 0
    estados_finales = [2,4,12,17,24,20,31,36,40,47]
    for caracter in lexema:           
        if estado == 0  and caracter == 'r':
            estado = 25
        elif estado == 25  and caracter == 'e':
            estado = 26
        elif estado == 26 and caracter == 'p':
            estado = 27
        elif estado == 27 and caracter == 'e':
            estado = 28
        elif estado == 28 and caracter == 't':
            estado = 29
        elif estado == 29 and caracter == 'i':
            estado = 30
        elif estado == 30  and caracter == 'r':
            estado = 31
        else:
            estado =-1
            break

    if estado == -1:
        return ESTADO_TRAMPA       
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
    
def automatarepetir(lexema):
    estado = 0
    estados_finales = [2,4,12,17,24,20,31,36,40,47]
    for caracter in lexema:          
        if estado == 0  and caracter == 'h':
            estado = 32
        elif estado == 32 and caracter == 'a':
            estado = 33
        elif estado == 33 and caracter == 's':
            estado = 34
        elif estado == 34 and caracter == 't':
            estado = 35
        elif estado == 35 and caracter == 'a':
            estado = 36
        else:
            estado =-1
            break

    if estado == -1:
        return ESTADO_TRAMPA       
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
def automataleer(lexema):
    estado = 0
    estados_finales = [2,4,12,17,24,20,31,36,40,47]
    for caracter in lexema:         
        if estado == 0 and caracter == 'l':
            estado = 37
        elif estado == 37 and caracter == 'e':
            estado = 38
        elif estado == 38 and caracter == 'e':
            estado = 39
        elif estado == 39 and caracter == 'r':
            estado = 40
        else:
            estado =-1
            break

    if estado == -1:
        return ESTADO_TRAMPA       
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
def automataleer(lexema):
    estado = 0
    estados_finales = [2,4,12,17,24,20,31,36,40,47]
    for caracter in lexema:     
        if estado == 0 and caracter == 'm':
            estado = 41
        elif estado == 41  and caracter == 'o':
            estado = 42
        elif estado == 42 and caracter == 's':
            estado = 43
        elif estado == 43 and caracter == 't':
            estado = 44
        elif estado == 44 and caracter == 'r':
            estado = 45
        elif estado == 45 and caracter == 'a':
            estado = 46
        elif estado == 46 and caracter == 'r':
            estado = 47
            
        else:
            estado =-1
            break

    if estado == -1:
        return ESTADO_TRAMPA       
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
                       
#algoritmo principal del lexer:

def lexer(codigo_fuente):
    tokens = [] #lista de tokens que va a devolver el lexer
    posicion_actual = 0
    while posicion_actual < len(codigo_fuente):
        while codigo_fuente[posicion_actual].isspace():
            posicion_actual = posicion_actual + 1
        
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
            
            for (un_tipo_de_token,afd) in TOKEN: #corre todos los afd para formar los tokens
                simulacion_afd = afd(lexema)
                if simulacion_afd == ESTADO_FINAL:
                    posibles_tokens_1mas.append(un_tipo_de_token) #agrega el token al final de la lista
                    todos_en_estado_trampa= False
                elif simulacion_afd == ESTADO_NO_FINAL:
                    todos_en_estado_trampa= False
                    
            posicion_actual = posicion_actual + 1
            
        if len(posibles_tokens) == 0:
            print('error:token desconocido' + lexema)
        
        un_tipo_de_token = posibles_tokens[0]
        token1 = (un_tipo_de_token, lexema)
        tokens.append(token1)
    
    return tokens

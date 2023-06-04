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
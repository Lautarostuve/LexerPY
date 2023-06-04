def si (cadena):
 estado_actual='A'
 estado_final=['F']
 for caracter in cadena:
        if estado_actual=='A' and caracter=='s':
         estado_actual ='B'
        elif estado_actual=='B' and caracter=='i':
          estado_actual='F'
 if estado_actual in estado_final:
  print('exito')
 else:
  print('no exito')
def sino (cadena):
  estado_actual='A'
  estados_finales=['F']
  for caracter in cadena:
        if estado_actual=='A' and caracter=='s':
         estado_actual ='B'
        elif estado_actual=='B' and caracter=='i':
          estado_actual='C'
        elif estado_actual=='C' and caracter=='n':
          estado_actual='D'
        elif estado_actual=='D' and caracter=='o':
          estado_actual='F'
  if estado_actual in estado_final:
    print('exito')
  else:
    print('no exito')

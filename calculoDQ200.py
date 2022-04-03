print('USE PONTO(.) E NÃO VÍRGULA NAS MEDIDAS')
print('===================================')
while True:
 try:
   medida_b1 = float(input('Valor do b¹: '))
 except ValueError:
   print(f'O valor Inválido, digite Novamente')
 else:
    break

while True:
  try:
     medida_b2 = float(input('Valor do b²: '))
  except ValueError:
     print(f'O valor Inválido, digite Novamente')
  else:
     break
     
B = float((medida_b1 + medida_b2)/2)
print(f'Valor de B: %.2f' %(B))
# O '%.2f' %() determina a qtd de casas decimais.
  
print('===================================')
while True:
  try:
    medida_a1_um = float(input('Valor do a1¹: '))
  except ValueError:
    print(f'O valor Inválido, digite Novamente')
  else:
      break

while True:
  try:
    medida_a1_dois = float(input('Valor do a1²: '))
  except ValueError:
    print('O valor Inválido, digite Novamente')
  else:
      break 

A1 = float((medida_a1_um + medida_a1_dois)/2)
print(f'Valor de A1 é: %.2f' %(A1))

print('===================================')

while True:
  try:
    medida_a2_um = float(input('Valor do a2¹: '))
  except ValueError:
    print(f'O valor Inválido, digite Novamente')
  else:
      break
      
while True:
  try:
    medida_a2_dois = float(input('Valor do a2²: '))
  except ValueError:
    print(f'O valor Inválido, digite Novamente')
  else:
      break 

A2 = float((medida_a2_um + medida_a2_dois)/2)
print(f'Valor de A2 é: %.2f' %(A2))

print('===================================')

tolerancia_da_embreagem_k1 = float(input('Valor de tolerancia de K1: '))
tolerancia_da_embreagem_k2 = float(input('Valor de tolerancia de K2: '))

print('===================================')

SK1 = (A1) - (B) + tolerancia_da_embreagem_k1
SK2 = (A2) - (B) + tolerancia_da_embreagem_k2
2
print('===================================')

print(f'O valor do calço de SK1 é %.2f' %(float(SK1)))
print(f'O valor do calço de SK2 é %.2f' %(float(SK2)))


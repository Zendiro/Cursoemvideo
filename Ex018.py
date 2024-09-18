import math
num = float(input('Digite o ângulo: '))
rad = math.radians(num)
cos = math.acos(rad)
sen = math.asin(rad)
tan = math.atan(rad)
print('O ângulo que você digitou é {}\nO cosseno é {}\nO seno é {}\nA tangente é {}'.format(num, math.floor(cos), math.floor(sen), math.floor(tan)))

import random
import string

"""
f = open('dados_1000000.txt', 'w')
size = 500000
for x in range (0,size):
    print(''.join(random.SystemRandom().choice(string.ascii_uppercase) + random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(4)),file=f)
"""

f = open('dados_50.txt', 'w')
size = 50
for x in range (0,size):
    print(''.join(random.SystemRandom().choice(string.ascii_uppercase) + random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(4)),file=f)




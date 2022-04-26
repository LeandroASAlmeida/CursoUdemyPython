
from collections import deque

deq = deque('geek')

print(deq)

deq.append('y')  # Adiciona no final

print(deq)


deq.appendleft('k')  # Adiciona no começo

print(deq)

print(deq.pop())  # Remove e retorna o último elemento

print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento

print(deq)

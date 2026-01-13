
# Leeres deque-Objekt:
test = deque()
# "Befüllen"  von rechts (ginge auch von links, mit appendleft):
for i in range(3):
    test.append(i)
    print(test)
# "Leeren" von links (ginge auch von rechts, mit pop):
for i in range(3):
    c = test.popleft()
    print(f'pop: {c}, Rest: {test}')

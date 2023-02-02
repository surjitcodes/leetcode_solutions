import random

max_val = 9999

count = 20
available = set([i for i in range(1, max_val+1)])

ran_list = []
i = 0
while count > 0:
    n = random.randint(1, max_val)
    if n not in available:
        continue
    available.remove(n)

    count -= 1
    ran_list.append(n)

    '''
    if n > priority:
        count -= 1
        ran_list.append(n)
        '''
ran_list.sort()
print(ran_list)

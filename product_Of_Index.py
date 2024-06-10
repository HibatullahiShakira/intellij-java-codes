index = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(4):
    for j in range(5):
        index[i][j] = i*j
        print(index[i][j], end=' ')
    print()

#outer_list = []
#for i in range(4):
    #inner_list = []
    #for j in range(5):
        #inner_list.append(i * j)
    #outer_list.append(inner_list)

#for a in range(4):
  #for b in range(5):
   #  print(outer_list[a][b], end=' ')
#print()

def even_number_list(number: list):
    number_list = []
    for i in number:
        if i % 2 == 0:
            number_list.append(i)
    return number_list

numbers = list(range(1, 11))
print(even_number_list(numbers))

def even_list(numbers: list):
    return [number for number in numbers if number % 2 == 0]




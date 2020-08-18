A, B, C = map(int, input().split())

list = [A, B, C]

def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

if list[0]<list[1]: 
    swap(list, 0, 1)
    if list[0]<list[2]:    #A<B<C
        swap(list, 0, 2)
        swap(list, 1, 2)
    else:                   #B>
        if list[1]<list[2]:
            swap(list, 1, 2)
else:                       
    if list[0]<list[2]:     #B<A<C
        swap(list, 0, 2)
        swap(list, 1, 2)
    else:                   #A>
        if list[1]<list[2]:
            swap(list, 1, 2)

print(int(list[1]))
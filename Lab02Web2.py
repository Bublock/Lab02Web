def work2():
    list_elem = [int(i) for i in input('Заполните список из положительных целых чисел: ').split()]
    list_elem1 = []
    for i in list_elem:
        if i%2==0 :
            list_elem1.append(i)
    print ('Числа, которые делятся на 2',list_elem1)
    list_elem2=[]
    for i in list_elem:
        if i%3==0 :
            list_elem2.append(i)
    print ('Числа, которые делятся на 3',list_elem2)
    list_elem3=[]
    for i in list_elem:
        if i%5==0 :
            list_elem3.append(i)
    print ('Числа, которые делятся на 5',list_elem3)
work2()
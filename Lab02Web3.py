def work3(): 
    value = int(input('Целое число : '))
    reverse = 0
    if value >0:
         while (value > 0):
             dig = value % 10
             reverse = reverse * 10 + dig
             value = value // 10
    else:
         value=value*-1
         while (value > 0):
             dig = value % 10
             reverse = reverse * 10 + dig
             value = value // 10
         reverse=reverse*-1
    print ('Обратное число: ',reverse)
work3()
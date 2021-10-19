def work1(): 
    num = int(input('Зададим целое число : '))
    n=num
    reverse = 0
    while (n > 0):
         dig = n % 10
         reverse = reverse * 10 + dig
         n = n // 10
    if num == reverse:
         print ('True')
         return True
    else:
         print ('False')
         return False
work1()

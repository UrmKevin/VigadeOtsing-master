print("*** ИГРЫ С ЧИСЛАМИ ***") #выводит в консоль "*** ИГРЫ С ЧИСЛАМИ ***"
print() #выводит в консоль пустую строку
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1: #цикл: бесконечный цикл
    try: #игнорирует ошибки
        a = (abs(int(input("Введите целое число => ")))) #переменная которую задает пользователь(число цельное, превращает отрицательное значение в положительное)
        break #выходит из цикла(ломает его)
    except ValueError: #игнорирует ошибки
         print("Это не целое число") #выводит в консоль "Это не целое число"
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0: #условие: если переменная а равна 0 то -->
    print("Нет смысла ничего делать с нулём") #выводит в консоль "Нет смысла ничего делать с нулём"
else: #условие: иначе -->
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр") #выводит в консоль "Определяем, сколько в числе чётных и сколько нечётных цифр"
    print() #выводит в консоль пустую строку
    c=b=a #переменная c и b равна переменной a
    paaris = 0 #переменная равна 0
    paaritu = 0 #переменная равна 0
    while b > 0: #цикл: пока переменная b больше 0 -->
            if b % 2 == 0: #
                    paaris += 1 #поменял "+" и "=" местами ///
            else: #
                    paaritu += 1 #поменял "+" и "=" местами ///
            b = b // 10 #
    
    print("Чётных цифр:",paaris) #выводит в консоль "Чётных цифр:" и переменную paaris
    print("Нечётных цифр:",paaritu) #выводит в консоль "Чётных цифр:" и переменную paaritu
    print() #выводит в консоль пустую строку
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число") #выводит в консоль "*Переворачиваем* введённое число"
    print() #выводит в консоль пустую строку
    b=0 #
    while a > 0: #
        number = a % 10 #
        a = a // 10 #
        b = b * 10 #
        b += number #поменял "+" и "=" местами /// 
    print("*Перевёрнутое* число", b) #выводит в консоль "*Перевёрнутое* число" и переменную b
    print() #выводит в консоль пустую строку
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз") #выводит в консоль "Проверяем гипотезу Сиракуз"
    print() #выводит в консоль пустую строку
    if c % 2 == 0: #
        print("с - чётное число. Делим на 2.") #выводит в консоль "с - чётное число. Делим на 2."
    else: #
        print("с - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.") #выводит в консоль "с - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2."
    while c != 1: #
            if c % 2 == 0: #
                    c = c / 2 # 
            else: #
                    c = (3*c + 1) / 2 #
            print(round(c), end=", ") #выводит в консоль округленную до нуля переменную c и ", "
    print() #выводит в консоль пустую строку
    print("Гипотеза верна") #выводит в консоль "Гипотеза верна"

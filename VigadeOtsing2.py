print("*** ИГРЫ С ЧИСЛАМИ ***") #выводит в консоль "*** ИГРЫ С ЧИСЛАМИ ***"
print() #выводит в консоль пустую строку
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1: #цикл: бесконечный цикл
    try: #игнорирует ошибки
        a = (abs(int(input("Введите целое число => ")))) #добавил 2 скобки /// переменная которую задает пользователь(число цельное, превращает отрицательное значение в положительное)
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
    c=b=a #оставил только 1 равно после переменной /// переменная c и b равна переменной a
    paaris = 0 #оставил только 1 знак равно после переменной /// переменная равна 0
    paaritu = 0 #оставил только 1 знак равно после переменной /// переменная равна 0
    while b > 0: #вместо ";" поставил ":" /// цикл: пока переменная b больше 0 -->
            if b % 2 == 0: #добавил еще 1 знак равно /// условие: если b % 2 равно 0 то -->
                    paaris += 1 #поменял "+" и "=" местами /// к переменной paaris добовляется 1
            else: #условие: иначе -->
                    paaritu += 1 #поменял "+" и "=" местами /// к переменной paaritu добовляется 1
            b = b // 10 #условие: если b // 2 равно 0 то -->
    
    print("Чётных цифр:",paaris) #поставил запятую после текста /// выводит в консоль "Чётных цифр:" и переменную paaris
    print("Нечётных цифр:",paaritu) #поставил запятую после текста /// выводит в консоль "Чётных цифр:" и переменную paaritu
    print() #выводит в консоль пустую строку
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число") #выводит в консоль "*Переворачиваем* введённое число"
    print() #выводит в консоль пустую строку
    b=0 #переменная b равна 0
    while a > 0: #поставил ":" после условия /// цикл: пока переменная a больше 0 -->
        number = a % 10 #переменная number равна a % 10
        a = a // 10 #переменная a равна a // 10
        b = b * 10 #переменная b равна b * 10
        b += number #поменял "+" и "=" местами /// поменял "+" и "=" местами /// к переменной b добовляется переменная number
    print("*Перевёрнутое* число", b) #выводит в консоль "*Перевёрнутое* число" и переменную b
    print() #выводит в консоль пустую строку
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз") #убрал 1 лишнию скобку /// выводит в консоль "Проверяем гипотезу Сиракуз"
    print() #выводит в консоль пустую строку
    if c % 2 == 0: #добавил еще 1 знак равно /// условие: если переменная c % 2 равна 0 то -->
        print("с - чётное число. Делим на 2.") #выводит в консоль "с - чётное число. Делим на 2."
    else: #условие: иначе -->
        print("с - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.") #выводит в консоль "с - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2."
    while c != 1: #цикл: пока переменная c не равна 1 -->
            if c % 2 == 0: #добавил еще 1 знак равно /// условие: если переменная c % 2 равна 0 то -->
                    c = c / 2 #оставил только 1 знак равно после переменной /// переменная c равна c / 2
            else: #условие: иначе -->
                    c = (3*c + 1) / 2 #оставил только 1 знак равно после переменной /// переменная c равна (3*c + 1) / 2
            print(round(c), end=", ") #округлил переменную "c" и исправил функцию end /// выводит в консоль округленную до нуля переменную c и ", "
    print() #выводит в консоль пустую строку
    print("Гипотеза верна") #поменял 2 апострофа на двоеточие /// выводит в консоль "Гипотеза верна"

"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def string_parsing(str1,str2):
    if (isinstance(str1, str) and isinstance(str2, str)) == False:
        return 0
    elif str1 == str2:
        return 1
    elif str1 != str2 and len(str1) > len(str2) and str2 == "learn": # сделал для проверки длинна больше и второе слово learn
        return f'{2} {3}'
    elif str1 != str2 and len(str1) > len(str2):
        return 2
    elif str1 != str2 and str2 == "learn":
        return 3
    
    
    

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(string_parsing("abc", 2))
    print(string_parsing("abc","abc"))
    print(string_parsing("abcd","abc"))
    print(string_parsing("abc","learn"))
    print(string_parsing("abcdef","learn"))    
    print(string_parsing("abc","dfasdearn")) 
    
if __name__ == "__main__":
    main()

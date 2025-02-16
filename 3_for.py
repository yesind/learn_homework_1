"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
  
    sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    list_of_all=[]
    M_COUNT=12
    print()
    for i in sales:
        print(f"Cуммарное количество продаж {i['product']} составляет {sum(i['items_sold'])}")
        print(f"Cреднее количество продаж {i['product']} в месяц составляет {round(sum(i['items_sold'])/len(i['items_sold']),2)}")
        print() 
        list_of_all+=i['items_sold']
    print()   
    print("Cуммарное количество продаж всех товаров\n", sum(list_of_all))
    print("Cреднее количество продаж всех товаров\n", round(sum(list_of_all)/M_COUNT,2))
    
if __name__ == "__main__":
    main()

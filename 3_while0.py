def find_person(name):
    name_list = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
    while len(name_list)!=1:
        if name_list[0]!= name:
            name_list.pop(0)
        else:
            return f"{name_list[0]} нашелся"
            break                         
    else:
        return f"{name} не нашелся"
      
print(find_person('Валера'))
print(find_person('Дима'))
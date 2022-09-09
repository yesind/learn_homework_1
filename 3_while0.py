def find_person(name):
    name_list = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
    while name_list:
        if name_list[0]!= name:
            name_list.pop(0)
        else:
            return f"{name_list[0]} нашелся/сь"                        
    else:
        return f"{name} не нашелся/сь"
      
print(find_person('Валера'))
print(find_person('Дима'))
print(find_person('Даша'))
      

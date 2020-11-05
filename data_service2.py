""" модуль для отримання даних про товарообіг
"""


def get_dovidnik():
    """ повертає вміст файла 'dovidnik.txt` у вигляді списка

 	Returns:
        'from_file' - список рядків файла
    """
    from_file = [
     
     "10;План розрахунків  бухгалтерського обліку підприємств;40" , 
     "20;ППП УЗПИКС;900",
     "30;ППП УТЕП;900",
     "40;ППП УОС;600",
     "50;ППП УФРО;1245",
     "60;АРМ бухгалтера матеріально-технічного відділу відділу;500", 
     "70;АРМ бухгалтера фінансового відділу;500" ,
     "80;ППП Облік договорів;150",  
     ]
  
    #Накопичувач клієнтів
    clients_list = []
    
    for line in from_file:
        line_list = line.split(";")
        clients_list.append((line_list))
    
    return from_file


def get_dovidnik():
    pass

dovidnik_list = get_dovidnik()

for line in dovidnik_list:
    print(line)
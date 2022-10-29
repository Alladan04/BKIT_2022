#from ast import operator
from operator import itemgetter
from Room import Room
from Computer import Computer
from Computers_in_room import Computers_in_room
room = [
    Room (1, "Иванов В.П."),
    Room (2,"Арпов А.А."),
    Room (3, "Игнатьев И.И."),
    Room (4, "Антошкин А.К."),
    Room (5, "Репкин В.В.") 
]
 
# COMPUTERS
comp = [
    Computer (1,"Васькин", 50000,1),
    Computer (2,"Пупкин", 52000,2),
    Computer (3,"Анюткин", 60000,1),
    Computer (4,"Гринев", 30000,3),
    Computer (5,"Одинцова", 31000,4),
    Computer (10, "Десятцова", 100000,4),
    Computer (6,"Базаров", 20000,3),
    Computer (7,"Твист", 100000,5),
    Computer (8,"Дван", 760000,5),
    Computer (9,"Кран", 50000,5)
]
 
comp_room = [
    Computers_in_room (1,1),
    Computers_in_room (2,2),
    Computers_in_room (3,3),
    Computers_in_room (4,4),
    Computers_in_room (5,5),
    
    Computers_in_room (1,6),
    Computers_in_room (2,7),
    Computers_in_room (3,8),
    Computers_in_room (4,9),
    Computers_in_room (5,1)

]
 
def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [ (e.User_name, e.Price, d.ID_room, d.Owner_name) 
        for d in room
        for e in comp
        if e.ID_room==d.ID_room
        ]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.Owner_name, ed.CompID, ed.RoomID) 
        for d in room
        for ed in comp_room
        if d.ID_room==ed.RoomID]
    
    many_to_many = [(e.User_name, e.Price, own_name, room_id) 
        for own_name, comp_id, room_id in many_to_many_temp
        for e in comp 
        if e.ID_computer==comp_id ]


    print('Задание Г1')
    res = sorted(one_to_many, key = itemgetter(3) )
    cache = ""
    for x in res:
        if cache != x[3] and x[3][0] == 'А':
            cache = x[3]
            print("\nКомната №{}\nOтветственный: {} \nСписок пользователей:".format(x[2],x[3]))
            print (x[0])
        elif x[3][0] == 'А':
            print (x[0])
        else: 
            break


    print('\nЗадание Г2')
    # Перебираем все ROOMS
    res2={}
    for d in room:
        # Список компьютеров комнаты
        room_list = list(filter(lambda i: i[2]==d.ID_room, one_to_many))     
        mx = float(0)
        #Собираем списки ключей и значений
        if len(room_list)>0:
            for r in room_list:
              if float(r[1])>mx:
                mx = float(r[1])  
            res2["Комната №{}".format(room_list[0][2])] = mx
    #Сортируем словарь по возрастанию значений
    res_tuples = sorted(res2.items(), key = itemgetter(1)) 
    print (res_tuples)
   


    print('\nЗадание Г3')
    res3 = {}
    # Перебираем все ROOMS
    for d in room:
         # Список ROOMS
        rm_comps = list(filter(lambda i: i[3]==d.ID_room, many_to_many))
        # Только UserName
        rm_comps_unm = [x for x,_,_,_ in rm_comps]
        res3["Комната №{}".format(d.ID_room)] = rm_comps_unm
    print (res3)
   
if __name__ == '__main__':
    main()

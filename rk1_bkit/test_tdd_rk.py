import unittest
from main import OTM,MTM,G1,G2,G3
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
otm = OTM(room,comp)
mtm = MTM(room,comp_room, comp)
class TestLab1_get_sqr_root (unittest.TestCase):
    def test_one (self):
         self.assertEqual (G1('А', otm),['Комната №4, Oтветственный: Антошкин А.К., Список пользователей:Одинцова Десятцова ', 'Комната №2, Oтветственный: Арпов А.А., Список пользователей:Пупкин '])
    def test_two(self):
         self.assertEqual (G2(room,otm),[('Комната №3', 30000.0), ('Комната №2', 52000.0), ('Комната №1', 60000.0), ('Комната №4', 100000.0), ('Комната №5', 760000.0)])
    def test_three (self):
        self.assertEqual(G3(room, mtm),{'Комната №1': ['Васькин', 'Одинцова'], 'Комната №2': ['Пупкин'], 'Комната №3': ['Анюткин'], 'Комната №4': ['Гринев'], 'Комната №5': ['Одинцова']})

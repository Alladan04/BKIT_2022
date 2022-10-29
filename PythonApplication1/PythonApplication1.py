import sys
import math
def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    flag = 1
    while flag==1:
        try:
            # Пробуем прочитать коэффициент из командной строки
            coef_str = sys.argv[index]
        except:
            # Вводим с клавиатуры
            print(prompt)
            coef_str = input()
        # Переводим строку в действительное число
        try:
            coef = float(coef_str)
            flag = 0
        except:
            print ('Try again, dummy')
            flag = 1
    return coef


def get_sqr_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    if a==0 and b == 0 and c == 0:
        result = [0]*5
        return result
    if a==0 and b == 0:
       return result
    
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        result.append(root1)
        result.append(root2)
    return result

def get_bisqr_roots (a,b,c):
    try:
        root = get_sqr_roots (a,b,c)
    except:
        root = get_sqr_roots(b,0.0,c)
        return root
        #если сделать ретурн здесь,  то выйдет ли он из всей функции или только из исключения??
        #судя по всему, из всей функции хех
    l = len(root)
    bi_root =[]
    for i in range (0,l) :
        if root[i]>0:
           bi_root.append(math.sqrt(root[i]))
           bi_root.append(-math.sqrt(root[i]))
        elif root[i] ==0:
            bi_root.append (0)
    return bi_root
def print_roots (root):
    l = len(root)
    if l == 5:
        print ("Infinity of roots")
    elif l ==0:
        print ("No roots")
    elif l == 1:
        print ('One root: {}'.format(root[0]))
    elif l == 2:
        print ('Two roots: {} and {}'.format(root[0],root[1]))
    elif l == 3:
        print ('Three roots: {}, {} and {}'.format(root[0],root[1],root[2]))
    else:
        print ('Four roots: {}, {}, {} and {}'.format(root[0],root[1],root[2],root[3]))
    return 

def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_bisqr_roots(a,b,c)
    # Вывод корней
    print_roots(roots)

# Если сценарий запущен из командной строки
if __name__ == "__main__":
      main()



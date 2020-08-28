import numpy as np


def my_array_fun(a, b):

    a = np.array([(3, 4, 5, 6), (12, 5, 6, 6)])

    b = np.array([(40, 6, 6, 7), (40, 12, 5, 6)])

    print(f'First Array {a}')
    print(f'Second Array:{b}')
    try:
        print(f'Shape of a:{a.shape}')
        print(f'Shape of b:{b.shape}')
    except:
        error = 'Error'
        print(error)
    try:
        print(f'Dimenstional of a:{a.ndim}')
        print(f'Dimenstional of b:{b.ndim}')
    except:
        error = 'Error'
        print(error)


my_array_fun(12, 56)


def adding_array(a, b):
    adding = np.add(a, b)
    print(f'addition of array:{adding}')


adding_array(12, 45)


def matrix_of_2_d(a, b):
    matrix = np.matrix(a)
    matrix_2 = np.matrix(b)

    print(f"matrix 1:{matrix}")
    print(f"matrix 2:{matrix_2}")


matrix_of_2_d(40, 24)


def zeros_of_array(a, b):
    a = np.array([(34, 34, 67, 34), (12, 45, 12, 2)])
    print(a)
    zeros = np.zeros((4, 2))
    print(zeros)


zeros_of_array(34, 12)


def ones_of_array():
    ones = np.ones((10, 40))
    print(ones)


ones_of_array()


def looping():
    wow = np.arange(10)
    try:
        print(f"Range:{wow}")
    except:
        print("Error")

    for i in np.nditer(wow):
        print(f'Each numbers{i}')


looping()


def trying_frombuffer():
    s = b'Dark Slayer'
    if len(s) > 2:

        ok = np.frombuffer(s, dtype='S1')
        print(ok)
    else:
        mylist_for_fun = [1,3,4,5,6,7]
        for i in mylist_for_fun:
            print(i)


trying_frombuffer()


def copying_array():
    a = np.array([(3,4,5),(3,4,5)])
    b = np.copy(a)
    b[0] = 4
    print(a)
    print(b)
    print(f'Numpy:{a.size}')
    print(f'B:{b.itemsize}')

copying_array()


def eye_function():
    try:
        eyes = np.eye(5,dtype=int)
        print(f'eye:{eyes}')
    except Exception:
        Error = "Error"
        print(Error)

eye_function()


def identity_of_array():
    try:
        identitys = np.identity(5,dtype=int)
        print(f'identity:{identitys}')
    except Exception:
        print("Error")

identity_of_array()
    


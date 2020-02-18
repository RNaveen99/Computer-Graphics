import numpy as np
import matplotlib.pyplot as plot
import math


def inputMatrix():
    n = int(input("Enter number of points: "))
    xpoints = np.empty(n)
    ypoints = np.empty(n)
    for i in range(n):
        xpoints[i], ypoints[i] = map(int, input(
            "Enter coordinates of point " + str(i + 1) + ": ").split())

    print(np.vstack((xpoints, ypoints, np.ones(n))))
    return np.vstack((xpoints, ypoints, np.ones(n)))


def show(matrix, newMatrix):
    if matrix is not None:
        x1 = np.append(matrix[0], matrix[0, 0])
        y1 = np.append(matrix[1], matrix[1, 0])
        plot.plot(x1, y1)
    # print(type(newObj))
    if newMatrix is not None:
        x2 = np.append(newMatrix[0], newMatrix[0, 0])
        y2 = np.append(newMatrix[1], newMatrix[1, 0])
        plot.plot(x2, y2)
    # print(x2)
    # print(y2)
    plot.axis('equal')
    plot.legend(['Original Object', 'Transformed Object'])
    plot.title('2D Transformations')
    plot.show()


def translation(matrix):
    if matrix is None:
        raise Exception("Create an object first!!!")
    dx = int(input("Enter translation factor along x-axis: "))
    dy = int(input("Enter translation factor along y-axis: "))
    # identity matrix
    T = np.eye(3)
    print(T)
    T[0, 2] = dx
    T[1, 2] = dy
    print(T)
    return T @ matrix


def scaling(matrix):
    if matrix is None:
        raise Exception("Create an object first!!!")
    dx = int(input("Enter scaling factor along x-axis: "))
    dy = int(input("Enter scaling factor along y-axis: "))
    # diagonal matrix
    T = np.diag((dx, dy, 1.0))
    print(T)
    print(T @ matrix)
    return T @ matrix


def rotation(matrix):
    if matrix is None:
        raise Exception("Create an object first!!!")
    dir = int(input("1.Clockwise\n2.Anti-clockwise\nDirection of rotation: "))
    deg = int(input("Enter degree of rotation: "))
    if dir == 2:
        deg *= -1
    angle = math.radians(deg)
    sinTheta = math.sin(angle)
    cosTheta = math.cos(angle)
    
    T = np.eye(3)
    if dir == 1:
        T[0, 0] = cosTheta
        T[0, 1] = sinTheta
        T[1, 0] = -sinTheta
        T[1, 1] = cosTheta
    elif dir == 2:
        T[0, 0] = cosTheta
        T[0, 1] = -sinTheta
        T[1, 0] = sinTheta
        T[1, 1] = cosTheta
    
    # print(T)
    return T @ matrix


def reflection(matrix):
    if matrix is None:
        raise Exception("Create an object first!!!")
    print("Let the equation of the line about which you want to reflect the object be 'y = mx + c'.")
    m, c = map(int, input("Enter values of m and c: ").split())
    T1 = np.eye(3)
    T1[1, 2] = -c
    T2 = np.eye(3)
    rad = -math.atan(m)
    T2[0, 0] = math.cos(rad)
    T2[0, 1] = math.sin(rad)
    T2[1, 0] = -math.sin(rad)
    T2[1, 1] = math.cos(rad)
    T3 = np.eye(3)
    T3[1, 1] = -1
    T4 = np.copy(T2)
    T4[0, 1] *= -1
    T4[1, 0] *= -1
    T5 = np.copy(T1)
    T5[1, 2] *= -1
    # print(T1, T2, T3, T4, T5)
    T = T1 @ T2 @ T3 @ T4 @ T5
    return T @ matrix


matrix = None
exitFlag = False


while not exitFlag:
    print('\n\n', '-'*35, 'Transformation', '-'*35)
    print("0.Exit")
    print("1.Enter new Object")
    print("2.Translate Object")
    print("3.Scale Object")
    print("4.Rotate Object")
    print("5.Reflect Object")
    menuOption = input('\nSelect option : ')

    if menuOption == '0':
        exitFlag = True

    elif menuOption == '1':
        matrix = inputMatrix()
        show(matrix, None)

    elif menuOption == '2':
        newMatrix = translation(matrix)
        show(matrix, newMatrix)

    elif menuOption == '3':
        newMatrix = scaling(matrix)
        show(matrix, newMatrix)
    
    elif menuOption == '4':
        newMatrix = rotation(matrix)
        show(matrix, newMatrix)
    
    elif menuOption == '5':
        newMatrix = reflection(matrix)
        show(matrix, newMatrix)
    
    else:
        print("Enter a valid choice!!")

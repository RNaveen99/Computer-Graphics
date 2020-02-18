import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math


def inputMatrix():
    n = int(input("Enter number of points: "))
    x_points = np.empty(n)
    y_points = np.empty(n)
    z_points = np.empty(n)
    for i in range(n):
        x_points[i], y_points[i], z_points[i] = map(int, input(
            "Enter coordinates of point " + str(i + 1) + ": ").split())

    return np.vstack((x_points, y_points, z_points, np.ones(n)))


def show(matrix, newMatrix):
    plt3D = plt.axes(projection = '3d')
    
    if matrix is not None:
        x_points_of_matrix = np.append(matrix[0], matrix[0, 0])
        y_points_of_matrix = np.append(matrix[1], matrix[1, 0])
        z_points_of_matrix = np.append(matrix[2], matrix[2, 0])
        plt3D.plot3D(x_points_of_matrix, y_points_of_matrix, z_points_of_matrix)
    
    if newMatrix is not None:
        x_points_of_newMatrix = np.append(newMatrix[0], newMatrix[0, 0])
        y_points_of_newMatrix = np.append(newMatrix[1], newMatrix[1, 0])
        z_points_of_newMatrix = np.append(newMatrix[2], newMatrix[2, 0])
        plt3D.plot3D(x_points_of_newMatrix, y_points_of_newMatrix, z_points_of_newMatrix)
    
    plt.legend(['Original Object', 'Transformed Object'])
    plt.title('3D Transformations')
    plt.show()

def translation(matrix):
    if matrix is None:
        raise Exception("Create an object first!!!")
    dx = int(input("Enter translation factor along x-axis: "))
    dy = int(input("Enter translation factor along y-axis: "))
    dz = int(input("Enter translation factor along z-axis: "))
    
    T = np.eye(4)
    T[:, -1] = dx, dy, dz, 1.0
    return T @ matrix


def scaling(matrix):
    if matrix is None:
        raise Exception("Create an object first!!!")
    dx = int(input("Enter scaling factor along x-axis: "))
    dy = int(input("Enter scaling factor along y-axis: "))
    dz = int(input("Enter scaling factor along z-axis: "))

    T = np.diag((dx, dy, dz, 1.0))
    print(T @ matrix)
    return T @ matrix


def rotation(matrix):
    if matrix is None:
        raise Exception("Create an object first!!!")
    dir = int(input("1.Clockwise\n2.Anti-clockwise\nDirection of rotation: "))
    deg = int(input("Enter degree of rotation: "))
    axis = int(input('Enter axis of rotation\n(1)x-axis\n(2)y-axis\n(3)z-axis\n'))
    if dir == 2:
        deg *= -1
    angle = math.radians(deg)
    sinTheta = math.sin(deg)
    cosTheta = math.cos(deg)
    
    rotationMatrix = np.eye(4)
    if dir == 1:
        if axis == 1:
            rotationMatrix[1, 1:3] = cosTheta, sinTheta
            rotationMatrix[2, 1:3] = -sinTheta, cosTheta
        elif axis == 2:
            rotationMatrix[0, 0:3:2] = cosTheta, sinTheta
            rotationMatrix[2, 0:3:2] = -sinTheta, cosTheta
        elif axis == 3:
            rotationMatrix[0, 0:2] = cosTheta, sinTheta
            rotationMatrix[1, 0:2] = -sinTheta, cosTheta    
    elif dir == 2:
        if axis == 1:
            rotationMatrix[1, 1:3] = cosTheta, -sinTheta
            rotationMatrix[2, 1:3] = sinTheta, cosTheta
        elif axis == 2:
            rotationMatrix[0, 0:3:2] = cosTheta, -sinTheta
            rotationMatrix[2, 0:3:2] = sinTheta, cosTheta
        elif axis == 3:
            rotationMatrix[0, 0:2] = cosTheta, -sinTheta
            rotationMatrix[1, 0:2] = sinTheta, cosTheta
        
    print(rotationMatrix)
    return rotationMatrix @ matrix

matrix = None
exitFlag = False


while not exitFlag:
    print('\n\n', '-'*35, 'Transformation', '-'*35)
    print("0.Exit")
    print("1.Enter new Object")
    print("2.Translate Object")
    print("3.Scale Object")
    print("4.Rotate Object")
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
    
    else:
        print("Enter a valid choice!!")

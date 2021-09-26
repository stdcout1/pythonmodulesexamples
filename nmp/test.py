import numpy as np
def qts1():
    a = np.array([0,1,2,3,4,5])
    a = a.reshape(2,3)
    print (a)
def qts2():
    matrix = np.array([[0,1,2,3,4,5],[10,11,12,13,14,15],[20,21,22,23,24,25],[30,31,32,33,34,35],[40,41,42,43,44,45],[50,51,52,53,54,55]])
    red = matrix[0:6,2]
    yellow = matrix[[0,0],[3,4]]
    blue = matrix[[4,5,4,5],[4,4,5,5]]
    print(matrix)
    print (red)
    print (yellow)
    print (blue)
def qts3():
    a = np.array([0,10,20,30,40,50,60,70])
    print(a[[1,2,-3]])

def qts4():
    a = np.arange(25).reshape(5,5)
    print(a)
    print(a[[0,1,2,3],[1,2,3,4]])
def qts5():
    a = np.arange(25).reshape(5, 5)
    print("c")
def qts6():
    a = np.array(([[[2, 3, 4, 5], [10, 11, 12, 13]], [[15, 16, 17, 18], [20, 21, 22, 23]]]))
    print ("a")
def qts7():
    edges = np.ones(5)
    start = np.zeros((5,5))
    for i in range(2):
        start[i-1,0:5] = edges
    for i in range(2):
        start[:,i-1] = edges
        start[2,2] = 9
    print(start)

print('question 1:')
qts1()
print('question 2:')
qts2()
print('question 3:')
qts3()
print('question 4:')
qts4()
print('question 5:')
qts5()
print('question 6:')
qts6()
print('question 7:')
qts7()

#This tutorial goes over how multiprocessing pool can be used
#to divide the work among multiple cores of your computer. 
#Multiprocessing Pool (Map Reduce)
#takiing a list, and sqaring the entire list of numbers, while using 3 processes at the same time

from multiprocessing import Pool


def f(n):
    return n*n

if __name__ == "__main__":
    p = Pool(processes=3) #its going to create 3 processes at the same time
    result = p.map(f,[1,2,3,4,5])#divides this work into 3 processes
    for n in result:
        print(n)

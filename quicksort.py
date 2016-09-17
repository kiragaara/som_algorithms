#!/usr/bin/python3.4

from random import random

def partition(A ,p , r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x :
            i = i + 1 
            A[j] , A[i] =  A[i] , A[j]
    A[r] , A[i+1] = A[i+1] , A[r]
    return i+1 


def quicksort(A , p , r ) :
    if  p < r : 
        q = partition(A , p , r)
        quicksort(A , p , q - 1)
        quicksort(A , q + 1 ,r)

def partition_random(A, p , r ):
    i = int(random() * r)
    A[i] , A[r] =  A[r] , A[i]
    return partition(A , p , r)
    

def quicksort_random(A , p , r ):
    if p < r : 
        q = partition_random(A ,p , r )
        quicksort_random(A , p , q - 1)
        quicksort_random(A , q + 1 , r)


def create_array(nbr):
    array = []
    for i in range(1,nbr):
        array.append(int(random()*nbr))
    return array



if __name__ == '__main__' :
    array = create_array(500)
    quicksort(array , 0 , len(array) - 1)
    print(array)
   

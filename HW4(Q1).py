#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Cesar Ramirez
#10/28/2019
#Homework 4


from itertools import islice 
import heapq

ML = []
RESULT = []
HEAP = []

#read in files for the 1000000 value test
theFile = open("C:/Users/cesar/Desktop/test/rand1000000.txt", 'r')
for val in theFile.read().split():
    ML.append(int(val))
theFile.close()


#-----------------Radix Sort---------------


def countingSort(arr, exp1): 
  
    n = len(arr) 

    output = [0] * (n) 
  
    count = [0] * (10) 
  
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[ int((index)%10) ] += 1

    for i in range(1,10): 
        count[i] += count[i-1] 
 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[ int((index)%10) ] -= 1
        i -= 1
   
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 

def radixSort(arr): 
    
    max1 = max(arr) 
   
    exp = 1
    while max1/exp > 0: 
        countingSort(arr,exp) 
        exp *= 10


        
#---------------Bucket Sort---------------

def bucketSort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp

        

#----------Splitting of the list----------

numberOfSubs = 9
length_to_split = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000] 

Inputt = iter(ML) 
Output = [list(islice(Inputt, elem)) 
          for elem in length_to_split]


for x in range(50): 
    radixSort(Output[x])

for x in range(50,100):
    Output[x] = bucketSort(Output[x])
       
    
    
#-----------------Merging-----------------

heapq.heapify(HEAP)

for x in range(100):
    heapq.heappush(HEAP,(Output[x][0], x))
    Output[x].pop(0)
    
for x in range(1000000):
    y = ((heapq.heappop(HEAP)))
    RESULT.append(y[0])

    if len(Output[y[1]]) != 0:
        heapq.heappush(HEAP,(Output[y[1]][0], y[1]))
        Output[y[1]].pop(0)
        
        
#----------------Printing----------------
  
print(RESULT)
    



# In[ ]:





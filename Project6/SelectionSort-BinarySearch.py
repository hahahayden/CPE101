#selection sort
#list -> list
def selectionsort( aList ):
  for i in range( len( aList ) ):
    minIndex = i
    for k in range( i + 1 , len( aList ) ):
      if aList[k] < aList[minIndex]:
        minIndex = k
 
    swap( aList, minIndex, i )
  return aList 
  
#swap the value
#list  int int ->
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

#Binary Serach on sorted list
#list -> bool
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found
	   
L=[4,8,-9,4,34,1,0,37]
print('L=',L)
print('Sorted L:', selectionsort(L))
print('find: ',binarySearch(L,34))
print('find: ',binarySearch(L,-34))

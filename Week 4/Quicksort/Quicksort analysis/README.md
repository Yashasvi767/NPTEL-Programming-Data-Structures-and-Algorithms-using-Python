# Quicksort
- Choose a pivot element: typically the first value in the array
- Partition A into lower and upper parts wrt pivot
- Move pivot between lower and upper partition
- Recursively sort the two partitions


# Analysis of Quicksort
- Worst case O(n<sup>2</sup>)
  - Pivot is either max or min
    -if this happens then one portion will be empty and the other portion will have size n-1
    - T(n) = T(n-1)+n = T(n-2)+(n-1)+n = ... = 1+2+...+n = O(n<sup>2</sup>)
   - Already sorted array is worst case input
     
- Randomization
  - worst case arises because of fixed choice of pivot, we typically choose the first element
  - This can happen for any fixed strategy(last element, midpoint), can work backwards to construct O(n<sup>2</sup>) worst case.
  - Instead, we will choose the pivot randomly, pick any index in range(0,n) with uniform probability and theregore expected running time is again O(n log n).  

 - Average case O(nlogn)
   - All permutations of n values, each equally likely
   - Average running time across all permutations
  
- Note:
   - when we use l.sort() function of python, python actually uses quicksort to sort the array.
   
 

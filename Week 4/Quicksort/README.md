# Merge Sort: Shortcomings
- Merging A and B creates a new array C which requires extra space for merging
- Extra storage can be costly
- It is inherently recursive, recursive call and return are expensive

## Divide and conquer without merging
- Suppose the median value in A is m
- Move all values <=m to the left half of A
  - Right half has values >m
  - This shifting can be done in place, in time O(n)
- Recursively sort left and right halves
- A is now sorted
- T(n) = 2T(n/2)+n = O(nlogn)

## How to find the median
  - Instead of finding a median, pick an element as pivot element (usually the very first element is the pivot)
  - 
  - 
  

<img width="1335" height="937" alt="image" src="https://github.com/user-attachments/assets/65cf0f43-3a13-4d3e-9bc6-be1d23a8307e" />

# Never re-evalutate a subproblem
- Build a table of values already computed: Memory table
- Remind yourself that this value has already been seen before: Memoization

<img width="1313" height="918" alt="image" src="https://github.com/user-attachments/assets/fedc05ff-f8c6-4ab5-809c-bf845805edb9" />

# Generalised skeleton
functionf(x,y,z):
 if ftable[x][y][z]:
   return(ftable[x][y][z])
 value = expression in terms of subproblems
 ftable[x][y][z]=value
 return(value)
 

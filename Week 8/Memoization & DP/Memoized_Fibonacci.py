def fib(n)
  if fibtable[n]:
    return(fibtable[n])
  if n==0 or n==1:
    value=n
  else:
    value=fib(n-1) + fib(n-2)
  fibtable[n] = value
  return(value)

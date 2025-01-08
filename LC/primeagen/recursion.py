def foo(n):
  if n == 1:
    return 1
  
  #pre recursion n +
  return n + foo(n-1)

print(foo(100))

#can do pre, recursion, post recursion. 
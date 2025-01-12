def pascal_triangle(n):
   r = [1]
   for i in range(n):
      print(r)
      tr = [0]+ r
      r = r + [0]
      nr = [x+y for x, y in zip(tr, r)]
      r = nr

pascal_triangle(5)
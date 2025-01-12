def minimum(*val, low_limit=None):
  if low_limit is None:
      return min(val)
  else:
      l = [x for x in val if x >=low_limit]
      return min(l)

print(minimum(1, 2, 3, 4, 5, low_limit=3)) # 3

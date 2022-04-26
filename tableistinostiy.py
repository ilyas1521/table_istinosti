print('x y z w')
for x in 0, 1:
  for y in 0, 1:
    for z in 0, 1:
      for w in 0, 1:
        #((y → x) ∧ (z ∨ w)) → ((x ∧ ¬w) ∨ (y ≡ z))
        f = ((y <= x) and (z or w)) <= ((x and (not(w))) or (y == z))
        if f == 0:
          print(x, y, z, w)
A = {'a', 'b', 'c', 'd', 'e'}
B = {'c', 'd', 'e', 'f', 'g', 'h', 'i'}
C = {'e', 'f', 'g', 'h', 'i', 'j', 'k'}

let_A = len(A)
let_B = len(B)

let_C = len(B - A - C)

i = B.intersection({'h', 'i', 'j', 'k'})
ii = B.intersection({'c', 'd', 'f'})
iii = A.symmetric_difference({'b', 'c', 'h'})
iv = B.symmetric_difference({'d', 'f'})
v = B.intersection({'c'})
vi = B.symmetric_difference({'l', 'm', 'o'})

print("Number of elements in set A:", let_A)
print("Number of elements in set B:", let_B)
print("Number of elements in B not part of A and C:", let_C)
print("i. Subset:", i)
print("ii. Subset:", ii)
print("iii. Subset:", iii)
print("iv. Subset:", iv)
print("v. Subset:", v)
print("vi. Subset:", vi)
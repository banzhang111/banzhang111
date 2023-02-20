a = [26,56,899,56,12]
for i in range(len(a)):
   for j in range(len(a)-1-i):
       if a[j] > a[j+1]:
          temp = a[j]
          a[j] = a[j+1]
          a[j+1] = a[j]
print(a)
         
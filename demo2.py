"Ñ¡ÔñÅÅÐò"
a = [12,56,19,45,69,55]
for i in range(len(a) - 1):
   for j in range(len(a) - i):
      if a[i] >a[j+i]
         temp = a[i]
         a[i] = a[j+i]
         a[j+i] = temp
print(a)
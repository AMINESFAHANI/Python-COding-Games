
arr=[43,32,51]

l = []
for i in range(len(arr)):
   dsumi=0
   for x in str(arr[i]):
        dsumi +=int(x)
   for j in range(i + 1, len(arr)):
        dsumj = 0
        for x in str(arr[j]):
            dsumj += int(x)
        if dsumi == dsumj:
            l.append(arr[i] + arr[j])
if not l:
    print(-1)
else:
    print(max(l))
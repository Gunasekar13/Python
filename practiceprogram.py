arr=list(map(int,input('Enter array element: ').strip().split()))
i=int(input('Enter starting index: '))
j=int(input('Enter ending index: '))
sum=0
for idx in range(i,j+1):
	sum+=arr[idx]
print('Output :',sum)
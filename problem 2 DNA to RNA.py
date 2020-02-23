print('enter the dna sequence')
s=input()
rna=''
for i in s:
	if i=='T':
	 rna=rna+'U'
	else:
	 rna= rna+i
print(rna)

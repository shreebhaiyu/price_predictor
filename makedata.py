def func():
	m1 = 2
	m2 = 3
	c = 9
	f = open("sample.txt","w")
	for i in range(1,10):
		for j in range(9,18):
			f.write(str(i)+" "+str(j)+" "+str(m1*i + m2*j + c) + "\n")

	f.close()

def func2():
	m = 3
	c = 9
	f = open("sample1.txt","w")
	for i in range(1,100):
		f.write(str(i)+" "+str(m*i+ c) + "\n")

	f.close()

func2()

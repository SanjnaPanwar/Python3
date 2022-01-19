banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
file=open("question3.txt","w")
i=0
while i in banks_list:
    file.write(i+"\n")
    i+=1
file.close()
var = input("law type: ")
fName = "SM-lawyer-"+var+".orig"
with open(fName, "w+") as r:
	for i in range(1,25):
		picnumber = str(i)
		r.write("("+var+"Law/"+picnumber+".png)\n")

fd = open("10-Archivos/data2.txt", "a")

lcad = ["\nNos vamos de azado\n", "Invita Anderson"]
fd.writelines(lcad)


fd.close
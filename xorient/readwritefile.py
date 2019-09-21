fr= open("input.txt","r")
fw= open("output.txt","w+")
if fr.mode == "r":
    fw.write(fr.read())


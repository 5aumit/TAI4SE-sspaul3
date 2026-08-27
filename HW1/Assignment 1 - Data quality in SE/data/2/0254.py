# 16th program - copyfile
import sys
if len(sys.argv) == 3:

    f1 = str(sys.argv[1])
    f2 = str(sys.argv[2])

    fs = open(f1, "r")
    fd = open(f2, "w")

    data = fs.read()
    fd.write(data)

    fs.close()
    fd.close()

    print("File copied successfully\nDestination data: ")

    fp = open(f2, "r")
    print(fp.read())

else:
    if len(sys.argv) > 3:
        print("Extra arguments entered")
    else:
        print("Insufficient data provided")

rad = float(input("input the radius of the circle: "))
print("the area of the circle is: ")
print( 3.142 * rad * rad)

-----------------------------------------------------------
***********************************************************
file_name = input("input the filename: ")
f = file_name.split(".")

if "py" in f:
    print("the extension is: ", "python")
if "c" in f:
    print("the extension is: ", "C")
if "xls" in f:
    print("the extension is: ", "excel")
if "class" in f:
    print("the extension is: ", "java")

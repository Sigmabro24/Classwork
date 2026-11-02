rows = int(input("Please enter the number of rows: "))
columns = rows * 3
dashes =""
for i  in range(columns):
    dashes += "_"
for j in range(rows):
    print(str(dashes))

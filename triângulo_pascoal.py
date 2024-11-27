cols = 1
elt = []

rows = int(input("Linhas: "))

for row in range(rows):
    el = []
    for col in range(cols):
        if col == 0:
            el.append("1")
        elif col == (cols-1):
            el.append("1")
        else:
            for i in range(1):
                n = int(elt[row-1][i+col-1]) + int(elt[row-1][i+col])
                el.append(str(n))            
                
    elt.append(el)
    print("\n", el)    
    cols+= 1
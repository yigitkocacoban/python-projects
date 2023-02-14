liste1 = [1,2,3,4,5,6]
liste2 = [7,8,9,10,11,12]
a, b = 7, 3
if a in liste2:
    if b in liste1:
        print("b listelde var, a liste2de var.")
    else:
        print("b listelde yok, a liste2de var.")
else:
    if b in liste1:
        print("b listelde var, a liste2de yok.")
    else:
        print("b listelde yok, a liste2de yok.")
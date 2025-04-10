from laba1 import table1, russian_alphabet1


def max_po_stolbikam(table1, russian_alpabet):
    table_for_work=table1._rows
    max_stolbiki=[0]*31
    idex=[0]*31
    print(table_for_work)
    table_for_work.pop[0][0]
    for i in range(len(russian_alpabet)):
        table_for_work.pop[i][0]

    print(table_for_work)
    for i in range(len(russian_alpabet)):
        max=table_for_work[i][0]
        k=0
        for j in range(russian_alpabet):
            if(max<table_for_work[i][j]):
                max=table_for_work[i][j]
                k=j
                
        max_stolbiki[i]=max
        idex[i]=k

    return max_stolbiki, idex


print(max_po_stolbikam(table1, russian_alphabet1))


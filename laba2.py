from laba1 import table1


def max_po_stolbikam(table1, russian_alpabet):
    table_for_work=table1._rows
    max_stolbiki=[0]*31
    idex=[0]*31
    
    for i in range(len(russian_alpabet)):
        table_for_work[i].pop(0)

 
    for i in range(len(russian_alpabet)):
        max=table_for_work[i][0]
        k=0
        for j in range(len(russian_alpabet)):
            if(max<table_for_work[i][j]):
                max=table_for_work[i][j]
                k=j
                
        max_stolbiki[i]=max
        idex[i]=k

    return max_stolbiki, idex


def max_5_shutuc(max_stolbiki, idex):
    indeckes=[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    for i in range(5):
        max=max_stolbiki[0]
        k=0
        for j in range(len(max_stolbiki)):
            if max< max_stolbiki[j]:
                max=max_stolbiki[j]
                k=j
        max_stolbiki[k]=0
        indeckes[i]=[k, idex[k]]
    return indeckes




russian_alphabet1 = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']
bigrams=[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

max_stolbiki, idex=max_po_stolbikam(table1, russian_alphabet1)

indeckes= max_5_shutuc(max_stolbiki, idex)
for i in range(5):
    print(indeckes[i][0])
    bigrams[i][0]=russian_alphabet1[indeckes[i][0]]
    bigrams[i][1]=russian_alphabet1[indeckes[i][1]]

print(bigrams)
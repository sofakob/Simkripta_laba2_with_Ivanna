from laba1 import table1, table2
'''
Щоби не ламати нічого в коді першої лабораторної то просто файл було перенесено сюди, і внесені деякі виправлення як видалення з 
алфавіту літери ё та ъ, через що були виправленні ще деякі штуку щоби перерахувати таблицю
'''

def max_po_stolbikam(table1, russian_alpabet):
    '''
    Функція рахує максимуми по кожному рядочку (я плутаю рядки і стовпці, тому така плутанина, але це не впливає на правильність виконання прогами)
    на вивод йдуть максимальні значенння в кожному рядочку та індекс кожного стовпця з якого обрали найбільше значення
    table1  в нас з PrettyTable, а до них не можна звертатися як до двовимірного списку, тому перша сторочка у функції створює 
    такий список з яким ми і будемо працювати
    два наступні списки створються для нашої зручності відразу з обнуленими значеннями
    '''


    table_for_work=table1._rows
    max_stolbiki=[0]*31
    idex=[0]*31
    
    for i in range(len(russian_alpabet)):
        table_for_work[i].pop(0)# при створення цього списку на нульових позиціях там літери, щоби вони не заважали роботі вони видаляються

 
    for i in range(len(russian_alpabet)):
        max=table_for_work[i][0]
        k=0
        for j in range(len(russian_alpabet)):
            if(max<table_for_work[i][j]):
                max=table_for_work[i][j]# шукаємо максимум і зберігаємо його індекс
                k=j
                
        max_stolbiki[i]=max
        idex[i]=k

    return max_stolbiki, idex


def max_5_shutuc(max_stolbiki, idex):
    '''
    Функція що знаходить 5 найбільших значень в таблиці, на вихід ідуть тількі індекси в цій таблиці. 
    Через цикл for знаходимо 5 разів найблільше значення, а щоби не попасти на нього декілька разів занулюємо значення, що вже виявилися
    найбільшими 
    '''
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

def bigram(indeckes, russian_alphabet1):
    bigrams=[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(5):
        bigrams[i][0]=russian_alphabet1[indeckes[i][0]]
        bigrams[i][1]=russian_alphabet1[indeckes[i][1]]
    return bigrams


russian_alphabet1 = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']


max_stolbiki, idex=max_po_stolbikam(table1, russian_alphabet1)
indeckes= max_5_shutuc(max_stolbiki, idex)
bigram_for_shifr=bigram(indeckes, russian_alphabet1)

print(bigram_for_shifr)

max_stolbiki, idex=max_po_stolbikam(table2, russian_alphabet1)
indeckes= max_5_shutuc(max_stolbiki, idex)
bigram_for_shifr=bigram(indeckes, russian_alphabet1)

print(bigram_for_shifr)

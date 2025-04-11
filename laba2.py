from laba1 import table1, table2
from gcd import gcd
from algoritm_evklida import algoritm_evklida_with_a_b

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


def encryption(plaintext, a, b, alphabet):
    
    m = 31
    ciphertext = []
    
    i = 0
    while i < len(plaintext):
        bigram = plaintext[i:i+2]
        
        x1 = alphabet.index(bigram[0])
        x2 = alphabet.index(bigram[1])
        
        X = x1*m + x2
        Y = (a * X + b) % (m**2)
        
        y1 = Y // m
        y2 = Y % m
        
        c1 = alphabet[y1]
        c2 = alphabet[y2]
        ciphertext.append(c1 + c2)
        
        i += 2
    
    return "".join(ciphertext)


def decryption(ciphertext, a, b, alphabet):
    
    m = 31
    plaintext = []
    
    inv_a = algoritm_evklida_with_a_b(a, m**2)
    
    i = 0
    while i < len(ciphertext):
        bigram = ciphertext[i:i+2]
        
        y1 = alphabet.index(bigram[0])
        y2 = alphabet.index(bigram[1])
        
        Y = y1*m + y2
        X = (inv_a * (Y - b)) % (m**2)
        
        x1 = X // m
        x2 = X % m
        
        p1 = alphabet[x1]
        p2 = alphabet[x2]
        plaintext.append(p1 + p2)
        
        i += 2
    
    return "".join(plaintext)


alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя"
a = 2
b = 1
plaintext = "привет"
ciphertext = encryption(plaintext, a, b, alphabet)
print(ciphertext)
print(decryption(ciphertext, a, b, alphabet))


def find_key(x1, x2, y1, y2, x3, x4, y3, y4):
    
    m = 31
    
    X1 = x1*m + x2
    print(X1)
    X2 = x3*m + x4
    print(X2)
    Y1 = y1*m + y2
    print(Y1)
    Y2 = y3*m + y4
    print(Y2)

    X = (X1 - X2)%m**2
    Y = (Y1 - Y2)%m**2
    
    a = porivniia(X, Y, m**2)
    print(a)

    if isinstance(a, int):
        b = (Y1 - a*X1) % (m**2)
        return (a%m**2, b)

    keys = []
    for a_i in a:
        b = (Y1 - a_i*X1) % (m**2)
        keys.append((a_i%m**2, b))

    return keys

#print(porivniia(155, 403, 961))
print(find_key(18, 14, 4, 28, 13, 14, 22, 28))
    

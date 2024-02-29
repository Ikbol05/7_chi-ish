# 1 chi masala
'''''
a, b, c = int(input("A chi sonni kriting: ")), int(input("B chi sonni kriting: ")), int(input("C chi sonni kriting: "))

def DigitCountSum (n):
    count = 0
    summa = 0

    while n > 0:
        count = +1
        summa = + n % 10
        n = n // 10
        return count,summa
    count_a, summa_a = DigitCountSum(a)
    count_b, summa_b = DigitCountSum(b)
    count_c, summa_c = DigitCountSum(c)

    print(f"1. {a} sonni raqamlari {count_a} ta, a sonni raqamlar yigindisi {summa_a}")
    print(f"2. {b} sonni raqamlari {count_b} ta, b sonni raqamlar yigindisi {summa_b}")
    print(f"3. {c} sonni raqamlari {count_c} ta, c sonni raqamlar yigindisi {summa_c}")
'''''


    #2 chi masala
'''''

def Invent_Digit(n):
    numbers = int(str(n)[ ::- 1 ])
    print(numbers)
    
a, b, c = int(input("A chi sonni kriting: ")), int(input("B chi sonni kriting: ")), int(input("C chi sonni kriting: "))

Invent_Digit(a)
Invent_Digit(b)
Invent_Digit(c)

'''''
# 3 chi masala
'''''
def addrightdigit (Text,Text1):
    if Text > 0:
        print(Text)
    else:
        print ("1 chi son 0 dan katta bulishu kerak")
    if 1 <= Text1 <= 9:
        print(Text1)
    else:
        print ("2 chi son 1 dan katta 9 dan kichkina bulishi kerak")
    natija = f"{Text} {Text1}"
    return natija

K = int(input("1 chi sonni kriting: "))
R = int(input("2 chi sonnni kriting: "))

print(addrightdigit(Text = K, Text1 = R))
'''''
# 4 chi masala
'''''
def addrightdigit (Text,Text1):
    if Text > 0:
        print(Text)
    else:
        print ("1 chi son 0 dan katta bulishu kerak")
    if 1 <= Text1 <= 9:
        print(Text1)
    else:
        print ("2 chi son 1 dan katta 9 dan kichkina bulishi kerak")
    natija = f"{Text1} {Text}"
    return natija

K = int(input("1 chi sonni kriting: "))
R = int(input("2 chi sonnni kriting: "))

print(addrightdigit(Text = K, Text1 = R))
'''''

# 5 chi masala
'''''
def doira_yuzi(Text1,Text2,Text3):

    pi = 3.1415

    d1 = pi * Text1 ** 2
    d2 = pi * Text2 ** 2
    d3 = pi * Text3 ** 2

    print("1 chi doiranyuzi", d1)
    print("2 chi doiranyuzi", d2)
    print("3 chi doiranyuzi", d3)


d1 = float(input("1 chi radiusni kriting: "))
d2 = float(input("2 chi radiusni kriting: "))
d3 = float(input("3 chi radiusni kriting: "))

print(doira_yuzi(Text1=d1,Text2=d2,Text3=d3))
'''''
# 6 chi masala
'''''
def ringS(Text1,Text2):

    pi = 3.1415

    R1 = pi * Text1 ** 2
    R2 = pi * Text2 ** 2

    natija = f"R1 {Text1}, R2 {Text2}"
    return natija

R1 = float(input("R1 ni kriting: "))
R2 = float(input("R2 ni kriting: "))

print(ringS(Text1=R1,Text2=R2))
'''''

# 7 chi masala
'''''
def triangleP(Text1,Text2):

    c = (Text1 ** 2 + Text2 ** 2) ** 0.5

    natija = Text1 + Text2 + c

    return natija

A = float(input("A katetni kriting: "))
B = float(input("B katetni kriting: "))

print("Perimetri")
print(triangleP(Text1=A,Text2=B))
'''''
# 8 chi masala
'''''
def sumrange(Text1,Text2):

    count = 0


    if Text1 > Text2:
        print("0")

    while Text1 <= Text2:

        count = count + 1

        Text1 = Text1 + 1

    return(Text1 + count)


a = int(input("A sonni kriting: "))
b = int(input("B sonni kriting: "))

print("Yig'gindisi")
print(sumrange(Text1=a,Text2=b))

'''''
# 9 chi masala
'''''

def calc(Text1,Text2,Text3):

    if Text3 == 1:
        res = Text1 + Text2

    elif Text3 == 2:
        res = Text1 - Text2

    elif Text3 == 3:

        if Text2 != 0:
            res = Text1 / Text2

        else:
            res = "0 ga bulish mumkin emas"

    elif Text3 == 4:
        res = Text1 * Text2

    else:
        res = "Notug'ri amal kritildi "

    return res

a = int(input("1 chi sonni kriting: "))
b = int(input("2 chi sonni kriting: "))
c = int(input("Amalni tanlang 1 - qushish, 2 - ayirish, 3 - bulish, 4 - kupaytrish: "))

print(calc(Text1=a,Text2=b,Text3=c))
'''''

# 10 chi masala
'''''
def even(Text1,Text2,Text3):

    if Text1 % 2 == 0:
        print("Juft")
    else:
        print("Toq")

    if Text2 % 2 == 0:
        print("Juft")
    else:
        print("Toq")

    if Text3 % 2 == 0:
        print("Juft")
    else:
        print("Toq")


a = int(input("1 chi sonni kriting: "))
b = int(input("2 chi sonni kriting: "))
c = int(input("3 chi sonni kriting: "))

print(even(Text1=a,Text2=b,Text3=c))
'''''

# 11 chi masala
'''''
def isprime(Text1,Text2,Text3):

    if Text1 % 2 == 0:
        print("Juft")
    else:
        print("Toq")

    if Text2 % 2 == 0:
        print("Juft")
    else:
        print("Toq")

    if Text3 % 2 == 0:
        print("Juft")
    else:
        print("Toq")


a = int(input("1 chi sonni kriting: "))
b = int(input("2 chi sonni kriting: "))
c = int(input("3 chi sonni kriting: "))

print(isprime(Text1=a,Text2=b,Text3=c))
'''''
# 12 chi masala






















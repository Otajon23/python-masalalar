#1 masala
a=int(input("son kiriting ="))
b=int(a/10000)
c=int((a-b*10000)/1000)
d=int((a-b*10000-c*1000)/100)
e=int((a-b*10000-c*1000-d*100)/10)
f=int((a-b*10000-c*1000-d*100-e*10))
S=b+c+d+e+f
n=a-S
print("Natija = ",n)

# 2 masala
a=int(input("1-katetni kiriting = "))
b=int(input("2-katetni kiriting = "))
S=a*b*0.5
print("yuzasi = ",S)

#3 masala
a=int(input("1-katet = "))
b=int(input("2-katet = "))
c=(a**2+b**2)**0.5
print("Gipotenuza=",c)

#4 masala
R=int(input("R = "))
pi=3.14
S=2*pi*R
print("S=",S)

# 5 masala
a=int(input("son kiriting ="))
b=int(a/10000)
c=int((a-b*10000)/1000)
d=int((a-b*10000-c*1000)/100)
e=int((a-b*10000-c*1000-d*100)/10)
f=int((a-b*10000-c*1000-d*100-e*10))
S=b+c+d+e+f
print("Yig'indisi = ",S)

# 6 masala tuliq emas
print("Pirojniy 2 so'm 50 tiyin")
a=5
b=50
n=int(input("pirojniy soni ="))
c=n*(a*100+b)
print("jami",c/100)

# 7 masala
a=int(input("3 xonali son="))
b=int(a%10)
print("oxirgi son=",b)

#8 masala
a=4564.56

if type(a)==int:
    print("butun son")
elif type(a)==float:
    print("kasrli son")
    print("kasr qismi=",a-int(a))

#9 masala
a=int(input("a="))
b=int(input("b="))
x=int(input("x="))
y=(a*(x**4)-b)/((2*x)**0.5+b)
print("y=",y)

#10 masala
print("kvadrat tomoni 125 ga teng")
print("kvadrat peremetri=",4*125)
print("kvadrat yuzi=",125**2)

#11 masala
print("Doiraning diametri 6 ga teng bulsa uning radiusi 3 ga teng buladi")
pi=3.14
s=pi*6**2
print("S=",s)

# 12 masala
a=54650.54
if a%2==0:
    print("juft son")
else:
    print("Toq son")

if a>0:
    print("Musbat son")
else:
    print("Manfiy son")

if type(a)==int:
    print("butun")
else:
    print("kasrli")

#13 masala
a=int(input("son kiriting="))
if a%12==0:
    print("3 ga 4 ga bo'linadi")
else:
    print("3 ga 4 ga bo'linmaydi")

#14 masala
x=int(input("x="))
y=x-(x**2+(3-x)/(x+5)*(x+1)**4)**1/3
print("y=",y)

#15 masala
a=int(input("3 xonali son kiriting="))
b=(a%100-a%10)/10
print("ikkinchi raqami = ",b)

# 16 masala
print("x^2-x-12=0")
a=1
b=-1
c=-12
x1=(-b+(b**2-4*a*c)**0.5)/2*a
x2=(-b-(b**2-4*a*c)**0.5)/2*a
print("x1=",x1)
print("x2=",x2)

# 17 masala
a=float(input("Ish haqi = "))
b=a*0.12
e=a-b
print("daromad solig'i - ",b)
c=e*0.01
print("kasaba uyushmasi - ",c)
d=e-c
print("xodim qo’liga oladigan mablag’i - ",d)
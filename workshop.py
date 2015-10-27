#! /usr/bin/python
# coding: utf8

# python2 vs python3 -> ör. encoding satırı
# Basit Araçlar -> ipython, pip vs.
# Style guide -> https://www.python.org/dev/peps/pep-0008

# Syntax

# Başlangıçta Class, main fonksiyonu gibi herhangi bir yapı tanımlamak zorunda değilim

1 + 1  # Noktalı virgül yok

a = 1 + 1  # Tipler implicit int a dememe gerek yok
a = "Merhaba Istanbulhs"

print("Hello World")  # Thank you captain obvious
a = raw_input("Hello World")  # python3'te input() girdi tipi her zaman string

a = True  # Boolean'lar büyük harfle başlar
a = False
# Boolean operators "and", "or", "not"

a, b = True, False  # Çoklu atama mümkün


# Data Structures
# List

a = []  # Uzunluk tanımlaması yok C array'inden ziyade Java'daki array list gibi
a[5]  # Listenin herhangi bir elemanına erişme
a[5] = 5  # NOPE Var olmayan bir liste elemanına atama yapılamaz
# Sonuç: IndexError: list assignment index out of range
a.append("Yeni eleman")  # Listeye eleman ekleme
a.insert(0, "Daha yeni eleman")  # Listenin bir tarafına eleman ekleme
a.remove("Yeni eleman")  # Listeden eleman çıkarma
a.pop(0)  # Listeden index ile eleman çıkarma ek olarak çıkartılan elemanı döndürür

# Lıst slıcıng a[from, to, step]
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Örnek liste
# a[x:y] x.elemandan y.elemana kadarki liste (x dahil y dahil değil)
a[3:5]  # Output: [3, 4]
# a[x:y:z] x.elemandan y.elemana kadarki liste ama z'ser aralıklarla
a[1:6:2]  # Output [1, 3, 5]
# Kullanmayacağım indisleri atlayabilirim
a[1::2]  # Output [1, 3, 5, 7, 9]
a[::2]  # Output [0, 2, 4, 6, 8]
# Liste elemanları negatif olabilir. -n'inci indis = sondan n.inci eleman
a[-1]  # Output 9
a[::-1]  # Output [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# DİKKAT: Bazı fonksiyonlar yeni listeyi döndürmez asıl listeyi değiştirir
# Ör: reverse(), sort()


# Tuple -> Unmutable list
a = 1, 2, 3
a = (1, 2, 3)
a[2]  # NOPE Immutable dedik ya
# Sonuç: TypeError: 'tuple' object does not support item assignment
# Ana fikri VİRGÜLE DİKKAT
a = 1,  # Output (1,)
# Büyük ihtimalle bunu yaparken tek elemanlı tuple yaratmak istemiyordun.
a, b = 1, 2,  # Output a -> 1 b -> (2,)


# Dictionary
a = {}  # Anahtar değer çifti. Hashmap, associative array vs. gibi
a = {"key": "value"}
a["key"]  # Herhangi bir keye erişim
a["key"] = "value"
a["boyle bir dunya yok"]  # Olmayan bir keye erişmeye çalışmak hata verir
# Sounç; KeyError: 'boyle bir dunya yok'
a.get("key")  # Güvenli erişim böyle bir key yoksa hata vermek yerine None döner.
# get() None yerine bizim istediğimiz bir şey de dönebilir.
a.get("boyle bir dunya yok", "basbaya var")  # Output: "Basbaya var"
a.pop("key")  # Dictionary'den key value çifti silmek
a.keys()  # Key listesi
a.values()  # Value listesi


# Set
a = set()  # Matematikteki küme yapısı
a = {1, 2, 3, 4, 5}  # DİKKAT: Boş küme parantezi dictionary
a = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5}  # Output: {1, 2, 3, 4, 5}
# Bir kümede aynı elemandan iki tane bulunamaz
a.update([3]) # Kümeye eleman ekleme
# DİKKAT update() iterable bir değer istiyor
b = {1, 3, 5, 7, 9}
c = {1, 3}
a.intersection(b)  # Output: {1, 3, 5}
# A kesişim B
a.difference(b)  # Output: {2, 4}
# A fark B
a.union(b)  # Output: {1, 2, 3, 4, 5, 7, 9}
# A birleşim B
c.issubset(a) # Output: True
# C A'nın alt kümesi mi ? Tersi issuperset()


# Scope tanımlamak için { } kullanılmıyor.
# Scope açmak için : kullanılır ve :'un altına indentlenmiş her satır o scope'a ait sayılır
# Boş scope tanımlamak için "pass" keyword'ü kullanılır.

if True:
    pass
# Indentation için 4 boşluk kullanılır, n boşluk da kullanılabilir ama yapmayın VURURLAR


# Conditionals
a = 10
if a == 5:
    pass
elif a > 5:  # DİKKAT else if değil elif
    pass
else:
    pass


# Loops

# C, Java tipi for yok. Bütün for'lar for each
for i in range(10):  # range() rakamlardan liste ureten fonksiyon
    print(i)

a = 1
while a <= 10:
    print(a)
    a += 1

# Python'da döngülerinde else ifadeleri var.
# Döngünün kırılmadığı durumlarda bu else'in içerisine girilir

for i in range(10):
    if i == 7:
        break
else:
    print("Kırılmadım ayaktayım")

a = {"key": "value", "key1": "value1"}

for key in a:  # Dictionary döngüde keyler içerisinde iterate eder. Evet toplantıyı set ettim.
    print(key, a[key])

for key, value in a.iteritems():  # Python3'te items()
    print(key, value)

# Döngüler birden fazla değer alabilir.
# Bunun üzerine oynayan faydalı fonksiyonlar var. Ör; zip(), enumerate()


# Functıons
def foo():
    return True

foo()  # Function call. Duh!
a = foo  # Python'da fonksiyonlar değişkenlere atanabilir, fonksiyonlara paramatre olarak geçilebilir vs.
a()


def foo(arg1, arg2, arg3):
    return arg1, arg2, arg3  # Böyle yapınca tuple dönmüş oluyorum


# Fonksiyon argümanları default değerler alabilir
def foo(arg1=True):
    return arg1

foo()  # Output: True
foo(False)  # Output: False

def foo(arg1=True, arg2):  # NOPE default değeri olan argümanlar her zaman listenin sonuna yazılmalı
    return arg1, arg2
# Sonuç: SyntaxError: non-default argument follows default argument


def foo(arg1, arg2, arg3):
    return arg1, arg2, arg3  # Böyle yapınca tuple dönmüş oluyorum

foo(*[1, 2, 3])  # Output: (1, 2, 3)
# yıldız ile bir listeyi fonksiyonun argümanları olarak yollayabilirim.

def foo(arg1=1, arg2=2, arg3=3):
    return arg1, arg2, arg3  # Böyle yapınca tuple dönmüş oluyorum

foo(**{"arg1": 2, "arg2": 4, "arg3": 6})  # Output: (2, 4, 6)
# Çift yıldız ile bir dictionary'i fonksiyonun argümanları olarak yollayabilirim.

# Python'da normal parametrelere argument, default değeri olan argümanlara ise keyword argument deniyor
def foo(*args, **kwargs):  # Bu fonksiyon istenildiği kadar argument ve keyword argument alabilir.
    return args, kwargs

foo(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)  # Output: ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), {})
foo(a=1, b=2, c=3, d=4)  # Output: ((), {'a': 1, 'b': 2, 'c': 3, 'd': 4})
foo(1, 2, 3, a=1, b=2, c=3)  # Output: ((1, 2, 3), {'a': 1, 'b': 2, 'c': 3})


# Comprehensions
# List Comprehensions
[x for x in range(10)]  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[x*2 for x in range(10)]  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
[x*2 for x in range(10) if x * 2 >= 10]  # Output: [10, 12, 14, 16, 18]

# Dict Comprehensions
{x: x for x in range(5)}  # Output: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
{x*2: x*3 for x in range(5)}  # Output: {0: 0, 2: 3, 4: 6, 6: 9, 8: 12}
{x*2: x*3 for x in range(5) if x*3 >= 5}  # Output: {6: 9, 8: 12}

# Lambda, map, filter, reduce
a = lambda x,y: x + y  # Tek satırlık fonksiyon tanımı
a(3, 5)  # Output: 8

# Map: bir fonksiyon ve bir iterable alıp o fonksiyonu o iterable'ın bütün
# elemanlarına uygular ve sonucu yeni bir iterable olarak döndürür.
map(lambda x: x * 2, range(10))  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Filter: bir predicate fonksiyonu ve bir iterable alıp
# o iterable içerisinde o predicate'i sağlayan elemanları içeren iterable'ı döndürür

filter(lambda x: x % 2 == 0, range(10))  # Output: [0, 2, 4, 6, 8]

# Reduce: bir fonksiyon ve bir iterable alıp o fonksiyonu o iterable'ın bütün
# elemanlarına uygular ve sonucu tek bir değer olarak döndürür.

reduce(lambda x, y: x+y, range(1,101))  # Output: 5050


# String Operations
a = "You'll be free, hackers, you'll be free"
a[0]  # Output: "Y"
a[5] = 'f'  # NOPE Python stringleri karakter karakter değiştirilemiyor
# Sonuç: TypeError: 'str' object does not support item assignment
"foo " + "bar"  # Output: 'foo bar'
'1' * 10  # Output: '1111111111'
# Bir stringi yüksek bir sayıyla çarpmamaya DİKKAT. Belleği Haşırt diye dolduruyor.

# List slicing aynen geçerli
a[16:23]  # Output: "Hackers"
a[::-1]  # Output: "eerf eb ll'uoy ,srekcah ,eerf eb ll'uoY"
a.upper()  # Output: "YOU'LL BE FREE, HACKERS, YOU'LL BE FREE"
a.lower()  # Output: "you'll be free, hackers, you'll be free"
"istanbulhs".capitalize()  # Output: "Istanbulhs"
a.swapcase()  # Output: "yOU'LL BE FREE, HACKERS, YOU'LL BE FREE"
b = a.split(" ")  # Output: ["You'll", 'be', 'free,', 'hackers,', "you'll", 'be', 'free']
" ".join(b)  # Output: "You'll be free, hackers, you'll be free"
a.startswith("You")  # Output: True
a.endswith("free")  # Output: True
a.replace("free", "open") # HAŞA Output: "You'll be open, hackers, you'll be open"
a = "You'll be free, hackers, you'll be free\n"
a.strip()  # Output: "You'll be free, hackers, you'll be free"

# Predicate'leri gostermeyi unutma
# a.isalnum()  a.isalpha()  a.isdigit()  a.islower()  a.isspace()  a.istitle()  a.isupper()

# Multi-line string
a = """Join us now and share the software;
You'll be free, hackers, you'll be free.
Join us now and share the software;
You'll be free, hackers, you'll be free.

Hoarders can get piles of money,
That is true, hackers, that is true.
But they cannot help their neighbors;
That's not good, hackers, that's not good.

When we have enough free software
At our call, hackers, at our call,
We'll kick out those dirty licenses
Ever more, hackers, ever more.

Join us now and share the software;
You'll be free, hackers, you'll be free.
Join us now and share the software;
You'll be free, hackers, you'll be free.
"""
a.splitlines()  # Shell'de göster

# String formatting

"Join us now and share the {}".format("software")  # Output: 'Join us now and share the software'
# Expected Output: "You'll be free, hackers, you'll be free."
"You'll be {0}, {1}, you'll be free.".format("free", "hackers")
"You'll be {0}, hackers, you'll be {0}.".format("free")
"You'll be {what}, {who}, you'll be free.".format(what="free", who="hackers")
"You'll be {what}, {who}, you'll be free.".format(**{"who": "hackers", "what": "free"})
"I actually wanted to write {0} {{}}".format("braces")  # Output: 'I actually wanted to write braces {}'


# Classes

class A(object):

    # Python'ın class'lara dair internal fonksiyonları __ ile başlayıp biter.
    def __init__(self):  # Constructor
        self.a = True  # self ~ this

    def method(self):  # Class'lar ait fonksiyonlara metod denir.
        return self.a

a = A()
a.method()  # Output: True

class A(object):

    @staticmethod
    def method():  # Python'da static metod @staticmethod dekoratörüyle tanımlanır.
        return True

A.method()  # Output: True

class A(object):

    def __method(self): # Python'da private fonksiyon veya değişkenler __ ile başlar
        return True

a = A()
a._method()  # NOPE AttributeError: 'A' object has no attribute '_method'
# Python'da aslında gerçek private yok ve private değerlere erişmenin bir yolu var
a._A__method()  # Output: True

# Inherıtance

class A(object):

    def __init__(self):
        self.a = 1

    def method1(self):
        return True

    def method2(self):
        return True

class B(A):

    def __init__(self):
        super(B, self).__init__()
        self.c = 2

    def method2(self):  # Override
        return False

b = B()
b.a  # Output: 1
b.c  # Output: 2
b.method1()  # Output: True
b.method2()  # Output: False

# Multiple Inheritance

class A(object):

    def __init__(self):
        self.z = 9
        self.y = 8

    def method1(self):
        return 7

    def method2(self):
        return 6


class B(object):

    def __init__(self):
        self.z = 1
        self.y = 2

    def method2(self):
        return 3

    def method3(self):
        return 4


class C(A, B):
    pass


class D(B, A):
    pass

c = C()
c.z  # Output: 9
c.y  # Output: 8
c.method1()  # Output: 7
c.method2()  # Output: 6
c.method3()  # Output: 4
d = D()
d.z  # Output: 1
d.y  # Output: 2
d.method1()  # Output: 7
d.method2()  # Output: 3
d.method3()  # Output: 4

# Polymorphism var ama Python'da pek bir işe yaramıyor
isinstance(c, A)  # Output: True

# Namespaces
# Python'da her .py dosyasına bir modül ve içinde __init__.py dosyası olan her klasöre bir paket denir.
# istanbulhs modülündeki workshop dosyasının içindeki bir sınıfa
# "from istanbulhs.workshop import sinif" diyerek ulaşılabilir
# DİKKAT: Ikı modul de birbirini import ediyorsa AttributeError hatası alınır


# Useful stdlib kısımlar

# math
import math

# os
import os
os.getcwd()  # Output: '/home/sentinel'
# O an içinde bulunulan dizin
os.chdir("/home/sentinel/workspace") # cwd'yi değiştirmek
os.listdir(os.getcwd())  # ls'in python içindeki karşılığı
# Output: ['istanbulhs-python', 'lt-cljs-tutorial.cljs', 'LightTable', 'solarchive', 'Sublime Text 2', 'pycharm-4.5.4']
os.environ # Ortam değişkenleri gösterirü
os.statvfs("a_mount_point")  # Bir mount point verildiğinde o diskin kullanım bilgisini gösterir

os.path.join("/home", "sentinel", "workspace")  # Output: '/home/sentinel/workspace'
os.path.abspath("istanbulhs-python")  # Output: '/home/sentinel/workspace/istanbulhs-python'
os.path.abspath(os.pardir)  # Output: '/home/sentinel'
os.path.exists("/home/sentinel/workspace/istanbulhs-python")  # Output: True
# os.walk'u göster

# Predicate fonksiyonlar
# os.path.isabs()    os.path.isdir()    os.path.isfile()   os.path.islink()   os.path.ismount()

# sys
import sys
sys.path  # Python path'ı eğer bir modül import edilemiyorsa path'i kontrol etmek faydalı olabilir
sys.modules  # Import edilmiş modüllerin bulunduğu dictionary
sys.argv  # Command line argümanları burada durur.

# datetime
import datetime
datetime.datetime.now()  # Mevcut tarih ve saat
a = datetime.datetime(2015, 9, 20, 15, 30)  # Elle tarih girmek
# Datetime aritmetiğini anlat
datetime.datetime.strftime # Datetime -> String
a.strftime("%d-%m-%Y %S:%M:%H")  # Output: '20-09-2015 00:30:15'
datetime.datetime.strptime # String -> Datetime
datetime.datetime.strptime('20-09-2015 00:30:15', "%d-%m-%Y %S:%M:%H")  # Output: datetime.datetime(2015, 9, 20, 15, 30)
# Format https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

# copy
import copy
a = range(10)
b = a  # Kopyasını yaratmıyor referans ataması
a[9] = 99
print(b)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 99]

a = range(10)
b = copy.deepcopy(a)  # Kopyasını yaratıyor
a[9] = 99
print(b)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Debugging

# Exception handling

try:
    raise Exception("bocuk")
except Exception:
    print("Aha yakaladım")

# Traceback

try:
    raise Exception("bocuk")
except Exception:
    import traceback
    traceback.print_exc()  # Stack trace'i ekrana bastırır
    traceback.format_exc() # Stack trace'i string olarak döndürür

# Debugger

import ipdb
ipdb.set_trace()

# Bazı debug trickleri

a = 5
print("!"*20, a)

class A(object):

    def __init__(self):
        self.z = 9
        self.y = 8

a = A()
a.__dict__  # Output: {'y': 8, 'z': 9}

# Logging

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Start doing something')

# Running terminal commands

# Stdlib'de bu işe yarayan modül subprocess fakat kullanım kolaylığı açısından envoy kullanacağız

import envoy
response = envoy.run("ls /home/sentinel")
response.command  # Hangi komutu çalıştırmıştım
response.status_code  # 0 değilse hata var
response.std_out  # Komut çıktısı buraya geliyor
response.std_err  # Hata mesajı buraya geliyor

# Subprocess'in gerektiği durumlar oluyor mu ?
# Bazen örneğin Python içerisinden cli kullanma
import subprocess
cmd_list = ["fdisk", "/dev/sda1"]  # Subprocess'e her parametre ayrı ayrı verilmek zorunda
cmd_str = "d\nn\np\n\n{0}\n\na\n1\nw\n"
p1 = subprocess.Popen(cmd_list, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)
p1.stdin.write(cmd_str)
res = p1.communicate()
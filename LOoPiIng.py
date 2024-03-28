#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Perulangan
#mencetak angka 1 - 10

for i in range(1,11):
    print(i, end=" ")


# In[6]:


#Mencetak angka 10 20 30 ---- 100

for i in range(1,11):
    print(i* 10, end=" ")


# In[7]:


#mencetak angka 10 20 30 ---- 100
for i in range(10,101,10):
    print(i, end=" ")


# In[2]:


#Mencetak angka 10 9 8 ---- 1
for i in range(1,11):
    print(11 - i, end = " ")


# In[3]:


for i in range(10,0,-1):
    print(i, end=" ")


# In[9]:


#Mencetak angka 1 -2 3 -4 5 -6 .... 10
sign = 1
for i in range(1,11):
    print(i*sign, end=" ")
    sign= sign * -1


# In[6]:


#Mencari bilangan faktorial
#input = 3, output= 3 * 2 * 1 = 6
#input = 4, output= 4 * 3 * 2 * 1 = 24

bil= int(input('Isikan bilangan: '))

hasil = 1
label =""

for i in range(1, bil+1):
    hasil = i * hasil
    if i < bil:
        label = label + str((bil+1) - i) + "*"
    else:
         label = label + str((bil+1) - i) 
            
            
print(f"{bil}! adalah {hasil}")
print(f"{label} = {hasil}")


# In[10]:


#Menghitung pangkat 

bil= int(input('Isikan Bilangan: '))
pangkat= int(input('Isikan pangkat: '))

label = " "
hasil = 1

for i in range(1, pangkat+1):
    hasil*= bil
    
print(f"{bil} pangkat {pangkat} adalah {hasil}")


# In[2]:


#Bilangan Prima adalah yang hanya bisa dibagi dengan 1 dan bilangannya sendiri => 2 Faktor
bil = int(input('Isikan bilangan: '))
jumlah = 0
for i in range(1, bil+1):
    sisa = bil % i
    if sisa == 0:
        jumlah = jumlah + 1
if jumlah == 2:
    print(f"{bil} adalah bilangan PRIMA")
    
else:
    print(f"{bil} bukan bilangan PRIMA")


# In[5]:


#Bilangan Prima adalah yang hanya bisa dibagi dengan 1 dan bilangannya sendiri => 2 Faktor
bil = int(input('Isikan bilangan: '))
keterangan = "Bilangan Prima"

for i in range(2, bil):
    sisa = bil % i
    if sisa == 0:
        keterangan = "Bukan Prima"
        break
print(f"{bil} adalah {keterangan}")


# In[8]:


#Break

for i in range(1,100):
    print(i, end=" ")
    if i==5:
        break
        
print()
for j in range(1,10):
    if j == 5:
        continue
    print(j, end=" ")


# In[11]:


#Looping untuk String, menghitung huruf fokal a=?, i=?, e=?, u=?, o=?
kalimat = input("Isikan Kalimat: ")
vokal_a = 0
vokal_i = 0
vokal_u = 0
vokal_e = 0
vokal_o = 0
for i in kalimat:
    if i=='a':
        vokal_a += 1
    elif i=='i':
        vokal_i += 1
    elif i=='u':
        vokal_u += 1
    elif i=='e':
        vokal_e += 1
    elif i=='o':
        vokal_o += 1
        
        
print(f"Jumlah huruf a:{vokal_a}")
print(f"Jumlah huruf i:{vokal_i}")
print(f"Jumlah huruf u:{vokal_u}")
print(f"Jumlah huruf e:{vokal_e}")
print(f"Jumlah huruf o:{vokal_o}")
total = vokal_a + vokal_i + vokal_u + vokal_e + vokal_o 
print(f"jumlah total huruf vokal: {total}")


# In[1]:


#Kalimat palindrome atau bukan
#palindrome adalah kalimat yang di baca dari kiri ke kanan == kiri ke kanan
#katak => palindrome
#Kasur rusak => palindrome
ulang = "Y"
while(ulang=="Y"):
    kalimat = input('Isikan Kalimat: ')
    panjang = len(kalimat)
    keterangan = "PALINDROME"
    
    for i in range(0,panjang):
        kika = kalimat[i].lower()
        kaki = kalimat[panjang - i-1]
        if kika != kaki:
            keterangan = "BUKAN PALINDROME"
            break

    print(f"{keterangan}")
    
    jawab =" "
    while(jawab!="Y" and jawab!="T"):
        jawab = input("Apakah mau mengulang program Y/T: ")
    ulang = jawab


# In[ ]:


#Nested FOR

for i in range(1,5):
    for j in range(1,5):
        print(f"i:")
    


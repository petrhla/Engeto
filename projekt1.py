print('----------------------------------------')
print('Welcome to the app. Please log in:')
TEXTS_1 = '''
Situated about 10 miles west of Kemmerer , 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley . '''

TEXTS_2 = '''At the base of Fossil Butte are the bright 
red, purple , yellow and gray beds of the Wasatch 
Formation . Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly . Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick .'''

TEXTS_3 = '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers , which lie some 
100 feet below the top of the butte . The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present .'''
login = input('Username: ') #uživatelské jméno
password = input('Password: ') #heslo
print('----------------------------------------')
database = {'bob' : '123', 'ann' : 'pass123', 'mike' : 'password123', 'liz' : 'pass123', } #slovník s loginy
if login in database.keys(): #prohledává jestli existuje uživatel
   if password == database.get(login): #prohledává jestli heslo odpovídá uživateli
      print('We have 3 texts to be analyzed')
      text_value = input('Enter a number btw. 1 and 3 to select: ')
      print('----------------------------------------')
      if text_value == '1': #slouží pro výběr článku 1
         texts_1a = TEXTS_1.split() #slouží pro to, aby kód šel jednoduše překopírovat pod další podmínky, rozděluje vybraný článek na slova
         count_0 = len(texts_1a) # vrací počet slov
         count_1 = 0 #proměnná pro počet slov začínající velkým písmenem
         count_2 = 0 #proměnná pro počet slov napsaných velkým písmem
         count_3 = 0 #proměnná pro počet slov napsaných malým písmem
         count_4 = 0 #proměnná pro počet čísel v textu
         suma = 0 #proměnná pro součet čísel v textu
         delka = 0 #pomocná proměnná pro délku jednotlivých slov
         kokos = [] #list pro uložení délky jednotlivých slov z celého textu
         for bigletter_1 in texts_1a: #hledáme slova začínající velkým písmenem
             if bigletter_1.istitle():
                count_1 = count_1 + 1
                continue
         for bigletter_2 in texts_1a: #hledáme slova psaná velkým písmenem
             if bigletter_2.isupper():
                count_2 = count_2 + 1
                continue
         for bigletter_3 in texts_1a: #hledáme slova psaná malým písmenem
             if bigletter_3.islower():
                count_3 = count_3 + 1
                continue
         for bigletter_4 in texts_1a: #hledáme čísla v textu
             if bigletter_4.isnumeric():
                count_4 = count_4 + 1
                suma = suma + int(bigletter_4) #sčítáme čísla v textu
                continue
         while texts_1a: #načítáme do listu kokos délku jednotlivých slov
               delka = len(texts_1a.pop())
               kokos.append(delka)
               continue
         print('There are', count_0, 'words in the selected text.') #vypisujeme výsledky
         print('There are', count_1, 'titlecase words')
         print('There are', count_2, 'uppercase words')
         print('There are', count_3, 'lowercase words')
         print('There are', count_4, 'numeric strings')
         print('----------------------------------------')
         a = max(kokos) #hledáme největší číslo v listu kokos
         while a: #vypisujeme graficky zastoupení slov dle délky od nejdelšího po nejkratší
             print(a, '*' * kokos.count(a))
             a = a - 1
             continue
         print('If we summed all the numbers in this text we would get: ', suma) #vypisujeme součet čísel
         print('----------------------------------------')
      if text_value == '2': #slouží pro výběr článku 2
         texts_1a = TEXTS_2.split() #umožní jednoduše překopírovat kód od řádku 42 do řádku 83
         count_0 = len(texts_1a)
         count_1 = 0
         count_2 = 0
         count_3 = 0
         count_4 = 0
         suma = 0
         delka = 0
         kokos = []
         for bigletter_1 in texts_1a:
             if bigletter_1.istitle():
                count_1 = count_1 + 1
                continue
         for bigletter_2 in texts_1a:
             if bigletter_2.isupper():
                count_2 = count_2 + 1
                continue
         for bigletter_3 in texts_1a:
             if bigletter_3.islower():
                count_3 = count_3 + 1
                continue
         for bigletter_4 in texts_1a:
             if bigletter_4.isnumeric():
                count_4 = count_4 + 1
                suma = suma + int(bigletter_4)
                continue
         while texts_1a:
               delka = len(texts_1a.pop())
               kokos.append(delka)
               continue
         print('There are', count_0, 'words in the selected text.')
         print('There are', count_1, 'titlecase words')
         print('There are', count_2, 'uppercase words')
         print('There are', count_3, 'lowercase words')
         print('There are', count_4, 'numeric strings')
         print('----------------------------------------')
         a = max(kokos)
         while a:
             print(a, '*' * kokos.count(a))
             a = a - 1
             continue
         print('If we summed all the numbers in this text we would get: ', suma)
         print('----------------------------------------')
      if text_value == '3': #slouží pro výběr článku 3
         texts_1a = TEXTS_3.split() #umožní jednoduše překopírovat kód od řádku 42 do řádku 83
         count_0 = len(texts_1a)
         count_1 = 0
         count_2 = 0
         count_3 = 0
         count_4 = 0
         suma = 0
         delka = 0
         kokos = []
         for bigletter_1 in texts_1a:
             if bigletter_1.istitle():
                count_1 = count_1 + 1
                continue
         for bigletter_2 in texts_1a:
             if bigletter_2.isupper():
                count_2 = count_2 + 1
                continue
         for bigletter_3 in texts_1a:
             if bigletter_3.islower():
                count_3 = count_3 + 1
                continue
         for bigletter_4 in texts_1a:
             if bigletter_4.isnumeric():
                count_4 = count_4 + 1
                suma = suma + int(bigletter_4)
                continue
         while texts_1a:
               delka = len(texts_1a.pop())
               kokos.append(delka)
               continue
         print('There are', count_0, 'words in the selected text.')
         print('There are', count_1, 'titlecase words')
         print('There are', count_2, 'uppercase words')
         print('There are', count_3, 'lowercase words')
         print('There are', count_4, 'numeric strings')
         print('----------------------------------------')
         a = max(kokos)
         while a:
             print(a, '*' * kokos.count(a))
             a = a - 1
             continue
         print('If we summed all the numbers in this text we would get: ', suma)
         print('----------------------------------------')
      else:
           print('Wrong article number')
   else:
       print('Password is incorrect') #heslo je neplatné
else:
     print('Login is incorrect') #login je neplatný





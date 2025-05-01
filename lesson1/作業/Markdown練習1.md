# 使用者輸入一個字串，顯示該字串的每一個字元索引

### 以下為程式內容

``` Python program
import os
os.system('cls')   # 清除終端機視窗

myString = input('Enter a string: ')

for i in range(len(myString)):
    print(f'Character \'{myString[i]}\' index is {i}')
```

### 以下為輸出結果


``` Python output
Enter a string: This is a test
Character 'T' index is 0 
Character 'h' index is 1 
Character 'i' index is 2 
Character 's' index is 3 
Character ' ' index is 4 
Character 'i' index is 5 
Character 's' index is 6 
Character ' ' index is 7 
Character 'a' index is 8 
Character ' ' index is 9 
Character 't' index is 10
Character 'e' index is 11
Character 's' index is 12
Character 't' index is 13

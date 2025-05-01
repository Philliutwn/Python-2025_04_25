# 輸入數個整數並儲存至串列中，直到輸入-9999結束，再將此串列轉換成元組 ，最後顯示該元組 以及長度、最大值、最小值、總和。

''' Python
>num = []

>while True:
>    n = int(input('輸入整數(輸入 -9999 結束)：'))
>    if n == -9999:
>        break
>    num.append(n)

>n_tuple = tuple (num)
>l_tuple = len(n_tuple)
>max_tuple = max(n_tuple)
>min_tuple = min(n_tuple)
>Sum = sum(n_tuple)
>print(n_tuple)
>print('Length:',l_tuple,'\nMax:',max_tuple,'\nMin:',min_tuple)
>print('Sum:',Sum)


輸出結果：
輸入整數(輸入 -9999 結束)：25
輸入整數(輸入 -9999 結束)：64
輸入整數(輸入 -9999 結束)：82
輸入整數(輸入 -9999 結束)：91
輸入整數(輸入 -9999 結束)：77
輸入整數(輸入 -9999 結束)：66
輸入整數(輸入 -9999 結束)：55
輸入整數(輸入 -9999 結束)：-9999
(25, 64, 82, 91, 77, 66, 55)
Length: 7 
Max: 91
Min: 25
Sum: 460

```
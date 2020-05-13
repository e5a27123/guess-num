# 猜數字遊戲
# 產生一個隨機數字1~100(不要印出來)
# 使用者重複輸入數字去猜
# 猜對 印出"猜對了"
# 猜錯 印出"比答案大/小"
import random

r = random.randint(1, 100)
while True :
    num = input('請猜數字: ')
    num = int(num)
    if r == num :
    	print('猜對了')
    	break
    elif r > num :
    	print('比答案小')
    elif r < num :
        print('比答案大')
# 猜數字遊戲
# 產生一個隨機數字1~100(不要印出來)
# 使用者重複輸入數字去猜
# 猜對 印出"猜對了"
# 猜錯 印出"比答案大/小"
import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True :
    count += 1
    num = input('請猜數字: ')
    num = int(num)
    if r == num :
        print('猜對了')
        print('這是你猜的第', count, '次')
        break
    elif r > num :
        print('比答案小')
    elif r < num :
        print('比答案大')
    print('這是你猜的第', count, '次')
import random
secret = random.randint(1, 100)
count = 0
print("猜数字小游戏开始！")
print("电脑已经想好了一个 1~100 之间的数字，来猜猜看吧！")
while True:
    guess = int(input("请输入你猜的数字："))
    count = count + 1
    if guess > secret:
        print("大了")
    elif guess < secret:
        print("小了")
    else:
        print(f"恭喜你猜对了！你一共猜了 {count} 次。")
        break
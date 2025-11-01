# 如果不小心進入無窮迴圈，用ctrl + c 強制程式停止

# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」


# answer = 25

# numin = input("請輸入0-100之間的數字")
# numin = int(numin)
# while numin == answer:
#     if numin > 100:
#         print("請輸入更小的數字")
#         numin = input("請繼續猜0-100之間的數字")
#     elif numin < 0:
#         print("請輸入更大的數字")
#         numin = input("請繼續猜0-100之間的數字")
#     print("恭喜中獎")

answer = 25
while True:
    numin = int(input("請輸入0-100的數字"))
    print(numin)
    if numin < 1 or numin >100:
        print("超出範圍請重新輸入")
    elif numin > answer:
        print("請輸入更小的數字")
    elif numin < answer:
        print("請輸入更大的數字")
    else:
        print("恭喜中獎")
        break


answer = 25
# 隨便把numin指定一個數讓程式進入迴圈
numin = 0 
while numin != answer:
    numin = int(input("請輸入 0-100 的數字"))
    if numin < 1 or numin >100:
        print("超出範圍請重新輸入")
    elif numin > answer:
        print("請輸入更小的數字")
    elif numin < answer:
        print("請輸入更大的數字")
print("恭喜中獎")
def missing(num):
    for ch in range(10,21):
        if ch in num:
            pass
        else:
            return ch
k=missing([10, 11, 12, 13, 14, 16, 17, 18, 19, 20])
print(f"missing number is :{k}")
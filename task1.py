def task1():
    n = int(input("Enter the Position: "))
    s = ""
    i = 1
    while len(s) < n:
        s += str(i)
        i += 1
    return s
print(task1())

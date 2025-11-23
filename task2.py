def task2():
    pos=int(input("Enter position: "))
    s=""
    n=1
    while len(s) < pos:
        s+=str(n)
        n+=1
    length=0
    for i in range(1, n):
        new_str=str(i)
        length+=len(new_str)
        if length>=pos:
            print("Number at that position is:", i)
task2()
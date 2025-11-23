# Task1
Requirements:
  1.Python 3.x
Features
  1.Reads a position n from the user.
  2.Builds a concatenated number string starting from 1.
  3.Continues until the string length is at least n.
  4.Prints the final generated string.
Setup
  Create a file named task1.py in project folder.
Code
  def task1():
    n = int(input("Enter the Position: "))
    s = ""
    i = 1
    while len(s) < n:
        s += str(i)
        i += 1
    return s
print(task1())

Code Explanation
1.n: The target position entered by the user.

2.s: A string that stores the concatenated numbers.

3.i: The current integer being appended to the string.

4.The while len(s) < n: loop keeps appending i (converted to string) to s and increments i until the string length reaches or exceeds n.

5.The function returns the final string, which is then printed.


#Task2
Requirements
  1.Python 3.x
Features
  1.Reads a position pos from the user.

  2.Builds the concatenated sequence of natural numbers as a string.

  3.Determines which number contains the digit at the given position.

  4.Prints that number
Setup
  1.Create a file named task2.py in your project folder.
Code
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

Code Explanation
  1.pos: The target position in the infinite concatenated sequence, entered by the user.

  2.s: A string that accumulates "123456789101112..." until its length reaches at least pos.

  3.n: The current integer being appended to the string while constructing the sequence.

  4.The first while len(s) < pos: loop concatenates numbers as strings until the required length is reached.

  5.length: A running total of digits counted when iterating again from 1 to n-1.

  6.In the for loop, each i is converted to new_str, its length is added to length, and when length >= pos, the script prints i as the number that contains the       requested position.

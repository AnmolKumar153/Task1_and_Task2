#Task2
About project
  This project contains a Python script that determines which integer appears at a given position in the infinite sequence formed by concatenating all positive integers (12345678910111213...).
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

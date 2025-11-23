# Task1
About Project
  This project contains a simple Python script that generates a continuous string of positive integers starting from 1 (like 123456789101112...) and prints the string up to at least a user-specified position.
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



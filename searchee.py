#!/usr/bin/env python3
# Searchee v1.0
# Coded by kaiz3n
# ~ツ~


import os, sys

print("Make sure you have Subfinder installed, and can open it directly with 'subfinder ..'!")
print("Let's run Subfinder and search for any file at the subdomains found.")
input1 = input("Which host would you like to scan? ")
file1 = input("Which file would you like to search for? (Eg, config.json): ")
command = 'subfinder -o results.txt -d ' + input1
os.system(command)
filepath = 'results.txt'
with open(filepath) as testy:
    line = testy.readline()
    count = 1
    while line:
        command1 = 'curl ' + line.strip() + '/' + file1 
        line = testy.readline()
        os.system(command1)
        print("-------------------------------------")
        print("Match: ",format(line.strip()))
        print()
print("Thanks for using Searchee! Now remember, use this information wisely and for the greater good!")

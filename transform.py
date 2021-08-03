import sys
import random

word = sys.argv[1]
all_letters = []
for i, l in enumerate(word):
 pick = random.choice([1,0])
 if i == 0 or pick == 1:
  all_letters.append(l.upper())
 else:
  all_letters.append(l.lower())
  
print("".join(all_letters))

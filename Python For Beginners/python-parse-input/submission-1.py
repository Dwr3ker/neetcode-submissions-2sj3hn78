from typing import List

def read_integers() -> List[int]:
    results = input()
    line = results.split(",")

    new_line = []
    for num in line:
        new_line.append(int(num))
    
    return new_line

# do not modify the code below

print(read_integers())
print(read_integers())
print(read_integers())

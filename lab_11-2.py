# Creator JM 1/31/2023

grades = {'Mid Year Project Presention': 100,
          'Mid Year Project Proposal': 90,
          'Mid Year Project Code': 97,
          'Mid Year Project Reflection': 93}

print(grades.values()) # print all grades

for k in grades: # Print all assignment names
    print(k)

for k in grades: # print all above 70
    if grades[k] > 70:
        print(f'{k} | Grade {grades[k]}')

for k in grades: # Print all below 50
    if grades[k] < 50:
        print(f'{k} | Grade {grades[k]}')

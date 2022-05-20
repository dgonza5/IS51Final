"""
The program is trying to determine from the students grades resulting from the final exam.
First, display the number of grades.
Second, display the average grade.
Third, display the percentage of grades that are above the average grade. 

Number of grades: 24
Average grade: 83.25
Percentage of grades above average: 54.17

There will be two functions to calculate the grades. 

Fuction-1 will kickstart the application, it will extract the information from the Final.txt
file and then calculate the average grade and then close the file. 
Function-2 will calculate the percentage of grades that are above the average grade. 
"""

"""
Main():
    set Final.txt = input()
    num_grades = list 
    average = sum(grades) len(grades)
    calculate above average percent

above_average():
    open in Final.txt
    read list and pull info
    close
"""
def main():
    infile = open("Final.txt", "r")
    grades = []
    for line in infile:
        grades.append(int(line.strip()))
    print("Number of grades: ", len(grades))

    average = 0
    for grade in grades:
        average += grade
    average /= len(grades)
    print("Average grade: ", average)
    print("Percentage of grades above average: {0:.2f}%".format(calculate_percent_above_average(grades, average)))
    infile.close()

def calculate_percent_above_average(grades, average):
    count = 0
    for grade in grades:
        if grade > average:
            count += 1
    return (count * 100) / len(grades)


main()
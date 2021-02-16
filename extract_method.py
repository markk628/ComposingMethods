import math 

def add_numbers():
    grade_list = []
    n_student = 5

    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    
    return grade_list

def calculate_mean(grade_list):
    total = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!

    for grade in grade_list:
        total = total + grade

    return total / len(grade_list)

def calculate_sd(grade_list, mean):
    sd = 0 # standard deviation
    sum_of_sqrs = 0

    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2

    return math.sqrt(sum_of_sqrs / len(grade_list))

def print_stat():
    grade_list = add_numbers()
    mean = calculate_mean(grade_list)
    sd = calculate_sd(grade_list, mean)
    
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

print_stat()
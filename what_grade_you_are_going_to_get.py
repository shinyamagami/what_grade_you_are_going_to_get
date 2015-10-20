# Shin Yamagami
# Oct 13th, 2015
# This program tell you what grade you are going to get.
#

def get_score():
    return int(input("What score did you get?: "))

def point_to_grade(point):
    if point >= 800:
        return 'A'
    elif point < 800 and point >= 700:
        return 'B'
    elif point < 700 and point >= 600:
        return 'C'
    elif point < 600 and point >= 500:
        return 'D'
    else:
        return 'F'
    
def print_grade(grade):
    print('Your grade is', grade)

def main():
    point = get_score()
    
    grade = point_to_grade(point)

    print_grade(grade)

main()

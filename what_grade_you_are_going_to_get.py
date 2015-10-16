# Shin Yamagami
# Oct 13th, 2015
# This program tell you what grade you are going to get.
#

def main():
#Get the score of users.
    point = int(input("What score did you get?: "))
#Convert point to grade
    point_to_grade(point)

def point_to_grade(point):
    if point >= 800:
        print('Your grade is A')
    elif point < 800 and point >= 700:
        print('Your grade is B')
    elif point < 700 and point >= 600:
        print('Your grade is C')
    elif point < 600 and point >= 500:
        print('Your grade is D')
    else:
        print('Your grade is F')

main()

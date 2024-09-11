print("python assignment")

#write a function to print sequence 1 to n

n=int(input("enter the value of n"))
def sequence():
    for i in range(1,n+1):
        print(i)

sequence()


#Write a function which takes first and last name as input and print in swap case

first_name=input("enter first name")
last_name=input("enter last name")

def sWap_Case():
    full_name=first_name+last_name
    print(full_name.swapcase())


sWap_Case()


# write a function that swaps the cases of all characters in a string

string=input("enter a string")

def sWap_Case():
    new_string=""
    new_string=string.swapcase()
    print(new_string) 

sWap_Case()

# create a function that determine leap year

def check_leapYear(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                print("this year is a leap year")
    else:
        print("not a leap year")

check_leapYear(2001)



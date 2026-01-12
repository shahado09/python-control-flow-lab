# ex1
def check_letter():
    letter = input('Enter enter a letter (a-z or A-Z): ').lower()

    if letter in ["a","e","i","o","u"]:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter}is a consonant.")

check_letter()

# ex2
def check_voting_eligibility():
    age =int( input('Please enter your age:'))

    if age<0:
        print('enter a valid number')
    elif age <18:
        print('Not eligible to vote')
    else:
        print('You are eligible to vote')

    

check_voting_eligibility()


# ex3
def calculate_dog_years():
    age =int( input('Input a dog age:'))

    if age>0:
        if age<=2:
            age1=  age *10
            print(f"The dog's age in dog years is {age1}.")
        elif age >2:
            age1=  (age-2)*7 +20
            print(f"The dog's age in dog years is {age1}.")

calculate_dog_years()

# ex4
def weather_advice():
    cold= input('The weather is cold: (yes/no) ').lower()
    raining= input('The weather is raining: (yes/no) ').lower()

    if cold =="yes" and raining=="yes" :
        print("Wear a waterproof coat.")
    elif cold =="yes" and raining=="no" :
        print("Wear a warm coat.")
    elif cold =="no" and raining=="yes" :
        print("Carry an umbrella.")
    elif cold =="no" and raining=="no" :
        print("Wear light clothing.")

weather_advice()



# ex5
def fizz_buzz():
    for i in range(1,51):

        if i %3==0:
            print("fizz")
        elif i %5==0:
            print("Buzz")
        elif i %3==0 and i%5==0:
            print("FizzBuzz")




fizz_buzz()
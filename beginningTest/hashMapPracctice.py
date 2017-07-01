from random import randint
# creates a hashmap full of names
# then gets random value to find out who the culprit is
# holds all the information for the crimes and people
crimes = {1: 'stole from', 2: 'murdered',
          3: 'kicked the shins of', 4: 'punched',
          5: 'assasinated',6: 'mugged',
          7: 'commtted adultery with'}
people = {1:'Rodney', 2 : 'Matt',3:'Julia',4:'Francesca',
          5:'Lucas',6: 'Maria', 7: 'Tom', 8 : 'Kelly',
          9:'Oliver', 10:'Ruth'}
print("Find out who did the crime!")
# print who did the crime and what it was. Loops until user types 'end'
looper = 99
iter = 1
while (looper != 0):

    print('-' * 25)
    print('Case',iter)
    iter = iter+1
    # sets all the names and crime for this case
    person1 = people[randint(1, people.__len__())]
    theCrime = crimes[randint(1, crimes.__len__())]
    person2 = people[randint(1, people.__len__())]
    # changes the name until we get a different name
    while(person2 == person1):
        person2 = people[randint(1, 3)]

    # prints the case and waits for input from the user
    print("\n"+person1, theCrime, person2+"!",":O\n")
    print("press enter to continue, type 'end' to exit")

    # checks to see if the user had typed 'end.
    user_input = input()
    if user_input == 'end':
        break
    print('-' * 25)

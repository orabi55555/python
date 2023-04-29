"""1--def reduce_adjacent_elements(numbers):
    reduced_numbers = [] #hn7ot l final numbers feha
    for number in numbers:
        if not reduced_numbers or number != reduced_numbers[-1]:
            reduced_numbers.append(number)
    return reduced_numbers

numbers=[1,2,3,4,5,5,5,5,6,6]
reduced_numbers = reduce_adjacent_elements(numbers)
print(reduced_numbers)
"""

""""______________________________________________________________________________"""


"""2 -def front_back(str):
  length = len(str)
  if length % 2 == 0:
    front = str[:length//2]
    back = str[length//2:]
  else:
    front = str[:(length//2)+1]
    back = str[(length//2)+1:]
  return front, back

def front_back_concatinate(a, b):
  a_front, a_back = front_back(a)
  b_front, b_back = front_back(b)
  return a_front + b_front + a_back + b_back"""


"""______________________________________________________________________________"""


"""3-  def all_different_number(numbers):
    return len(numbers) == len(set(numbers))

numbers1=[1,2,3,4,5]
numbers2=[1,1,1]

print(all_different_number(numbers1))
print(all_different_number(numbers2))"""

""""______________________________________________________________________________"""





"""  4- def bubble_sort(unordered_list):
    n = len(unordered_list)
    for i in range(n):
        for j in range(0, n-i-1):
             Swap if the element found is greater than the next element
             if unordered_list[j] > unordered_list[j+1] :
                unordered_list[j], unordered_list[j+1] = unordered_list[j+1], unordered_list[j]
    return unordered_list

list = [5,4,3,2,1]
print (bubble_sort(list))"""


"""______________________________________________________________________________"""



""" 5-  import random
def play_the_game(): #lma 7tetha function el number msh mtshafa tht??
    
 number = random.randint(1, 100)

# tries equal 10
tries = 10
previous_guesses = set()


# loop until the number is guessed
while tries > 0:
    # ask the user to enter a guess
    guess = int(input("Guess the number (between 1 and 100): "))
    #checks if the guess is already guessed
    if guess in previous_guesses:
        print("You already guessed that number. Please try again.")
        continue
    
    previous_guesses.add(guess)

    
    # check if the guess is correct
    if guess == number:
        print("Congratz!, You guessed the number in", 10-tries+1, "tries.")
        break
    
    # check if the guess is higher or lower than the  number he should guess
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    
    tries -= 1
    
    if tries == 0:
        print("Sorry, you ran out of tries. The number was", number)
        
def play_again():
    while True:
        choice = input("Do you want to play again? (Y/N): ")
        if choice.lower() == "y":
            return True
        elif choice.lower() == "n":
            return False
        else:
            print("Invalid input. Please enter Y or N.")
   """     
        
        
        










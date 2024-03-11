numbers = (1, 2, 3, 4, 5)

total_sum = sum(numbers)

#print("sum of numbers is: ", (total_sum))

favourite_books = ("Atomic habits",
                   "Psychology of money",
                   "Mein kempf",
                   "Life of stoics",
                   "African history")

#for books in favourite_books:
    #print(books)

Kariakoo : {} # type: ignore

Kariakoo["Location"] = input("Enter person's location: ") # type: ignore
Kariakoo["name"] = input("Enter person's name: ") # type: ignore
Kariakoo["Age"] = int(input("Enter person's age: ")) # type: ignore

#print("Locals info: ")
#print(Kariakoo)


    # Create an empty dictionary for person information
#person = {}
    
    # Accept user input for person information
#person["name"] = input("Enter person's name: ")
#person["age"] = int(input("Enter person's age: "))
#person["favorite_color"] = input("Enter person's favorite color: ")
    
    # Print the dictionary
#print("Person Information:")
#print(person)

# Accept user input to create two sets of integers
set1 = set(map(int, input("Enter integers for Set 1 (separate by space): ").split()))
set2 = set(map(int, input("Enter integers for Set 2 (separate by space): ").split()))
    
# Create a new set containing common elements
common_elements = set1.intersection(set2)
    
# Print the common elements
print("Common elements in the sets:", common_elements)

# List of words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    
# List comprehension to filter words with odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]
    
# Print the list of words with odd number of characters
print("Words with odd number of characters:")
for word in odd_length_words:
    print(word)
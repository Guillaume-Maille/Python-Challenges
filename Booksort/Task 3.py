# TASK 3 – Programs containing several components
# A library maintains a list of books. The list is saved in a text file, where each line of the file represents
# one book.

# TASK 3.1
# Consider the information that should be included in the text file other than the title and the author.

# TASK 3.2
# Consider that this is a text file, which means that all information will be saved in STRING format.
# Consider the implications of storing numeric information, such as the number of copies of each book.
# Define the format of each line of the file so that each piece of information may be easily extracted.


# TASK 3.3
# Design a program in pseudocode that has a menu-driven interface and will perform the following
# tasks:
# 1. Add a new book to the text file. Include validation of the different pieces of information as
# appropriate.
# 2. Search for books written by a given author. Output the title of any books found, or a suitable
# message if no books by the given author are found.
# 3. End the program.

# TASK 3.4 – Writing program code
# Convert your pseudocode into program code.

# TASK 3.5 – Testing
# Consider how the program produced in TASK 3.4 may be tested.

#OPENFILE "Books" FOR READ
#IsFound ← FALSE
#OUTPUT "Enter Author"
#INPUT Author
#REPEAT
#  READFILE "Books", FileAuthor
#    IF FileAuthor = Author
#      THEN
#        IsFound ← TRUE
#        OUTPUT "Title”
#    ENDIF
#UNTIL IsFound = TRUE OR EOF("Books")

#IF IsFound = FALSE
#   THEN
#     OUTPUT "No Author found"
#ENDIF

def task3():
    x = True
    found = True
    while x:
        uinput = input("What would you like to do? (1) Add a new book to the text file. (2) Search for books written by a given author. (3) End the program.")
        if uinput == '3':
            x = False
        if uinput == '1':
            bookname = input("Enter book name:")
            author = input("Enter author:")
            genre = input("Enter genre:")
            f = open("Books", "a")
            writeline = bookname + ',' + author + ',' + genre
            f.write(writeline)
            f.close()
        if uinput == '2':
            book_found = 0
            asearch = input("Book Author:")
            with open('Books') as c:
                for line in c:
                    parts = line.split(",")
                    if parts[1] in asearch:
                        while book_found == 0:
                            print("Book found!")
                            print("Book details (Name,Author,Genre):", line)
                            book_found = 1
                if book_found == 0:
                    print("Book not found.")

task3()

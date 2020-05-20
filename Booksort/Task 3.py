OPENFILE "Books" FOR READ
IsFound ← FALSE
OUTPUT "Enter Author"
INPUT Author
REPEAT
  READFILE "Books", FileAuthor
    IF FileAuthor = Author
      THEN
        IsFound ← TRUE
        OUTPUT "Title”
    ENDIF
UNTIL IsFound = TRUE OR EOF("Books")

IF IsFound = FALSE
   THEN
     OUTPUT "No Author found"
ENDIF

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

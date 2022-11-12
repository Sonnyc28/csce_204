FILE_NAME = "exercises/nov10/books.txt"

def read_books():
    books = []
    try:
        with open(FILE_NAME) as file:
            for line in file:
                book = line.strip()
                books.append(book)
        return books
    except FileNotFoundError:
        print("Sorry, your file doesn't exist.")

def write_books(books):
    try:
        with open(FILE_NAME, "w") as file:
            for book in books:
                file.write(f"{book}\n")
    except FileNotFoundError:
        print("Sorry, your file doesn't exist.")

def display_books(books):
    for book in books:
        print(f"- {book}")

def add_book(books):
    book = input("Enter book name: ").strip()
    books.append(book)
    print(f"{book} was successfully added")
    return books

books = read_books()

while True:
    choice = input("(V)iew, (A)dd, or (Q)uit: ").lower().strip()
    if choice == "q":
        break
    elif choice == "v":
        display_books(books)
    elif choice == "a":
        books = add_book(books)
    else:
        print("Sorry, invalid input")
        
write_books(books)

import json  # Import JSON module for file handling

LIBRARY_FILE = "library.txt"  # Define the filename where the book data will be saved

def load_library():
    """Load library data from a file."""
    try:
        with open(LIBRARY_FILE, "r") as file:  # Open the file in read mode
            return json.load(file)  # Read and return data from file
    except (FileNotFoundError, json.JSONDecodeError):  # If file doesn't exist or has errors
        return []  # Return an empty list

def save_library(library):
    """Save library data to a file."""
    with open(LIBRARY_FILE, "w") as file:  # Open the file in write mode
        json.dump(library, file, indent=4)  # Convert list to JSON format and save

def add_book(library):
    """Add a book to the library."""
    title = input("Enter book title: ")  # Get book title from user
    author = input("Enter author: ")  # Get author name from user
    year = int(input("Enter publication year: "))  # Get publication year (convert to integer)
    genre = input("Enter genre: ")  # Get book genre
    read = input("Have you read it? (yes/no): ").strip().lower() == "yes"  # Convert user input to boolean
    
    book = {"title": title, "author": author, "year": year, "genre": genre, "read": read}  # Create book dictionary
    library.append(book)  # Add book to library list
    save_library(library)  # Save updated library to file
    print("Book added!\n")  # Confirm addition

def remove_book(library):
    """Remove a book by title."""
    title = input("Enter title to remove: ")  # Get title of book to remove
    for book in library:  # Loop through books
        if book["title"].lower() == title.lower():  # Check if title matches (case insensitive)
            library.remove(book)  # Remove book from list
            save_library(library)  # Save updated library to file
            print("Book removed!\n")  # Confirm removal
            return
    print("Book not found.\n")  # If book not found, show message

def search_book(library):
    """Search for a book by title or author."""
    keyword = input("Enter title or author: ").strip().lower()  # Get search keyword
    matches = [b for b in library if keyword in b["title"].lower() or keyword in b["author"].lower()]  # Find matches
    
    if matches:  # If matches found
        print("Matching books:")
        for book in matches:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matches found.\n")  # If no matches found, show message

def display_books(library):
    """Display all books in the library."""
    if not library:  # If library is empty
        print("Library is empty.\n")  # Show message
        return
    
    print("Your Library:")  # Print header
    for index, book in enumerate(library, 1):  # Loop through books with index
        print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")  # Display book info
    print()

def display_statistics(library):
    """Show total books and percentage of books read."""
    total = len(library)  # Count total books
    read_books = sum(1 for book in library if book["read"])  # Count books marked as read
    percentage_read = (read_books / total * 100) if total > 0 else 0  # Calculate percentage read
    
    print(f"Total books: {total}\nPercentage read: {percentage_read:.1f}%\n")  # Display statistics

def main():
    """Main function to run the menu system."""
    library = load_library()  # Load existing library from file
    
    while True:  # Infinite loop for menu
        print("\nMenu:")  # Print menu options
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Statistics")
        print("6. Exit")
        
        choice = input("Enter choice: ")  # Get user input
        
        if choice == "1":
            add_book(library)  # Call add book function
        elif choice == "2":
            remove_book(library)  # Call remove book function
        elif choice == "3":
            search_book(library)  # Call search book function
        elif choice == "4":
            display_books(library)  # Call display books function
        elif choice == "5":
            display_statistics(library)  # Call display statistics function
        elif choice == "6":
            save_library(library)  # Save library before exiting
            print("Goodbye!")  # Print goodbye message
            break  # Exit loop
        else:
            print("Invalid choice, try again.\n")  # Handle invalid input

if __name__ == "__main__":  # Run main function only if script is executed directly
    main()

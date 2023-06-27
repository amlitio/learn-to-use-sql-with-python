import sqlite3

# Connect to the database
conn = sqlite3.connect('notes.db')

# Create a cursor
cursor = conn.cursor()

def create_note():
    title = input("Enter the note title: ")
    content = input("Enter the note content: ")
    
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    print("Note created successfully!")

def display_notes():
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    
    if notes:
        for note in notes:
            print(f"ID: {note[0]}\nTitle: {note[1]}\nContent: {note[2]}\n")
    else:
        print("No notes found.")

def delete_note():
    note_id = int(input("Enter the ID of the note you want to delete: "))
    
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    print("Note deleted successfully!")

def main():
    while True:
        print("\n1. Create a new note")
        print("2. Display all notes")
        print("3. Delete a note")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_note()
        elif choice == "2":
            display_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
    
# Close the connection
conn.close()

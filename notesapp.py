def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", 'w') as file:
        file.write(note + "\n")
    print("Note added successfully.")

def view_notes():
    print("Your Notes:")
    with open("notes.txt", 'r') as file:
        notes = file.readlines()
        if notes:
            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note.strip()}")
        else:
            print("No notes found.")

def delete_note():
    view_notes() # Before
    with open("notes.txt", 'r') as file:
        notes = file.readlines()
        if notes:
            note_number = int(input("Enter the number of the note to delete: "))
            if 1 <= note_number <= len(notes):
                deleted_note = notes.pop(note_number - 1)
                with open("notes.txt", "w") as file:
                    file.writelines(notes)
                print(f"Note deleted successfully.")
                view_notes()
            else:
                print("Invalid note number.")
        else:
            print("No notes found.")
    print(f"Note deleted successfully.")
    view_notes() # After Delete

while True:
    print("\nMenu:")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        print("Exiting the Note App.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
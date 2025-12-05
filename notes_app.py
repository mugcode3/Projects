import datetime


def save_notes(note_list):
    with open("notes.txt", "w") as f:
        for note in note_list:
            f.write(note + "\n")


try:
    with open("notes.txt", "r") as f:
        notes = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    notes = []

while True:
    print("---Menu---")
    print("1. Show all notes")
    print("2. Add a note")
    print("3. Edit a note")
    print("4. Search notes")
    print("5. Delete a note")
    print("6. Quit")

    choice = input("Choose option: ")

    if choice == "1":
        print("---Notes---")
        if not notes:
            print("No notes yet!")
            continue
        else:
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")

    elif choice == "2":
        note = input("Add note: ")
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        new_note = "[" + timestamp + "] " + note
        notes.append(new_note)
        save_notes(notes)

    elif choice == "3":
        print("---Notes---")
        if not notes:
            print("No notes yet!")
            continue
        else:
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")

            user_input = input("Select note number to edit: ")

            try:
                note_num = int(user_input)
            except ValueError:
                print("invalid note number")
                continue

            if note_num < 1 or note_num > len(notes):
                print("out of range")
                continue

            actual_i = note_num - 1
            print(f"Current note: {notes[actual_i]}")

            note_edit = input("Edit note: ")
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

            metadata = timestamp + " EDITED"
            edited_note = "[" + metadata + "] " + note_edit

            notes[actual_i] = edited_note
            save_notes(notes)

            print("Note updated!")

    elif choice == "4":
        keyword = input("Enter Keyword: ")
        found = False

        print("---Notes---")

        for note in notes:
            if keyword.lower() in note.lower():
                print(note)
                found = True

        if not found:
            print("No results found.")

    elif choice == "5":
        print("---Notes---")
        if not notes:
            print("No notes yet!")
            continue
        else:
            for i, note in enumerate(notes, start=1):
                print(i, note)

            user_input = input("Select note number to delete: ")

            try:
                note_num = int(user_input)
            except ValueError:
                print("invalid note number")
                continue

            if note_num < 1 or note_num > len(notes):
                print("out of range")
                continue

            actual_i = note_num - 1
            del notes[actual_i]
            save_notes(notes)

            print("Note deleted")

    elif choice == "6":
        save_notes(notes)
        print("Notes saved. Goodbye!")
        break

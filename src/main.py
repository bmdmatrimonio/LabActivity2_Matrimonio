# ID (str) -> Details (dict)
students_db = {}


def create_student():
    """Adds a new student to the system."""
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ").strip()

    if student_id in students_db:
        print(f"Error: Student ID '{student_id}' already exists.")
        return

    name = input("Enter Name: ").strip()
    major = input("Enter Major: ").strip()

    # Contact details as an immutable (mymail, phone) tuple
    mymail = input("Enter Mymail: ").strip()
    phone = input("Enter Phone Number: ").strip()
    contact = (mymail, phone)

    # Enrolled courses stored in a list
    courses_input = input("Enter Courses (comma-separated, e.g., CS101, MATH101): ")
    courses = [c.strip() for c in courses_input.split(",") if c.strip()]

    # Storing record in nested dictionary
    students_db[student_id] = {
        "name": name,
        "major": major,
        "contact": contact,  # Tuple
        "courses": courses,  # List
    }
    print(f"Success: Record for '{name}' (ID: {student_id}) created.")


def read_student():
    """Displays details of a specific student."""
    print("\n--- View Student Details ---")
    student_id = input("Enter Student ID: ").strip()

    if student_id not in students_db:
        print(f"Error: No record found for ID '{student_id}'.")
        return

    s = students_db[student_id]
    mymail, phone = s["contact"]  # Unpacking tuple

    print("\n" + "=" * 35)
    print(f" ID:         {student_id}")
    print(f" Name:       {s['name']}")
    print(f" Major:      {s['major']}")
    print(f" Mymail:     {mymail}")
    print(f" Phone:      {phone}")
    print(f" Courses:    {', '.join(s['courses']) if s['courses'] else 'None'}")
    print("=" * 35)


def update_student():
    """Updates details of an existing student."""
    print("\n--- Update Student Record ---")
    student_id = input("Enter Student ID to update: ").strip()

    if student_id not in students_db:
        print(f"Error: No record found for ID '{student_id}'.")
        return

    s = students_db[student_id]
    print(f"Updating record for {s['name']}. Leave blank to keep current value.")

    # Update Major (String)
    new_major = input(f"New Major [{s['major']}]: ").strip()
    if new_major:
        s["major"] = new_major

    # Update Contact Info (Tuple)
    curr_mymail, curr_phone = s["contact"]
    new_mymail = input(f"New Mymail [{curr_mymail}]: ").strip() or curr_mymail
    new_phone = input(f"New Phone [{curr_phone}]: ").strip() or curr_phone
    s["contact"] = (new_mymail, new_phone)

    # Update Courses (List)
    add_course = input("Add a new course (or leave blank): ").strip()
    if add_course and add_course not in s["courses"]:
        s["courses"].append(add_course)

    print(f"Success: Record for ID '{student_id}' updated.")


def display_all_students():
    """Display: Lists all student records."""
    print("\n--- All Registered Students ---")
    if not students_db:
        print("No student records available.")
        return

    print(f"{'ID':<10} | {'Name':<20} | {'Major':<15} | {'Courses'}")
    print("-" * 65)
    for sid, details in students_db.items():
        courses_str = ", ".join(details["courses"])
        print(
            f"{sid:<10} | {details['name']:<20} | {details['major']:<15} | {courses_str}"
        )


def main():
    """Main menu-driven loop."""
    while True:
        print("\n==============================")
        print("   STUDENT DATA MANAGER")
        print("==============================")
        print("1. Add New Student (Create)")
        print("2. Search Student (Read)")
        print("3. Update Student Record (Update)")
        print("4. Display All Records (Display)")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            create_student()
        elif choice == "2":
            read_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            display_all_students()
        elif choice == "5":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
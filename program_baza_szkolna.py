class Student:
    def __init__(self, full_name, class_name):
        self.full_name = full_name
        self.class_name = class_name

class Teacher:
    def __init__(self, full_name, subject, classes):
        self.full_name = full_name
        self.subject = subject
        self.classes = classes

class FormTeacher:
    def __init__(self, full_name, class_name):
        self.full_name = full_name
        self.class_name = class_name

list_students = []
list_teachers = []
list_form_teachers = []

def create_user():
    while True:
        print("\nWybierz jedną z opcji: uczeń, nauczyciel, wychowawca, koniec")
        option = input().lower()
        if option == "uczeń":
            full_name = input("\nPodaj imię i nazwisko ucznia: ")
            class_name = input("Podaj klasę ucznia: ")
            list_students.append(Student(full_name, class_name))
            print(f"\nDodano ucznia {full_name} z klasy {class_name}")
        elif option == "nauczyciel":
            full_name = input("\nPodaj imię i nazwisko nauczyciela: ")
            subject = input("Podaj nazwę przedmiotu: ")
            print("Podaj nazwy klas, które prowadzi nauczyciel (po jednej w linii). Aby zakończyć wpisz pustą linię: ")
            classes = []
            while True:
                class_name = input()
                if class_name:
                    classes.append(class_name)
                else:
                    break
            list_teachers.append(Teacher(full_name, subject, classes))
            print(f"\nDodano nauczyciela {full_name}, który prowadzi przedmiot {subject}, w klasach {classes}")
        elif option == "wychowawca":
            full_name = input("\nPodaj imię i nazwisko wychowawcy: ")
            class_name = input("Podaj nazwę klasy, którą prowadzi wychowawca: ")
            list_form_teachers.append(FormTeacher(full_name, class_name))
            print(f"\nDodano wychowawcę {full_name}, który prowadzi klasę {class_name}")
        elif option == "koniec":
            break
        else:
            print("\nNiepoprawna opcja!")

def manage_users():
    while True:
        print("\nWybierz jedną z opcji: klasa, uczeń, nauczyciel, wychowawca, koniec")
        option = input().lower()
        if option == "klasa":
            class_name = input("\nPodaj nazwę klasy: ")
            students_exist = False
            teachers_exist = False
            for student in list_students:
                if student.class_name == class_name:
                    students_exist = True
                    break
            for supervisor in list_form_teachers:
                if supervisor.class_name == class_name:
                    teachers_exist = True
                    break
            if students_exist or teachers_exist:
                print(f"Uczniowie w klasie {class_name}: ")
                for student in list_students:
                    if student.class_name == class_name:
                        print(student.full_name)
                print(f"Wychowawca klasy {class_name}: ")
                for supervisor in list_form_teachers:
                    if supervisor.class_name == class_name:
                        print(supervisor.full_name)
            else:
                print("\nBrak klasy o podanej nazwie!")
        elif option == "uczeń":
            full_name = input("\nPodaj imię i nazwisko ucznia: ")
            student_exist = False
            for student in list_students:
                if student.full_name == full_name:
                    student_exist = True
                    print("Uczeń:", student.full_name)
                    print("Przedmioty: ")
                    for teacher in list_teachers:
                        if student.class_name in teacher.classes:
                            print(teacher.subject)
                    break
            if not student_exist:
                print("\nBrak ucznia o podanym imieniu i nazwisku!")
        elif option == "nauczyciel":
            full_name = input("\nPodaj imię i nazwisko nauczyciela: ")
            teacher_exist = False
            for teacher in list_teachers:
                if teacher.full_name == full_name:
                    teacher_exist = True
                    print("Nauczyciel:", full_name)
                    print("Klasy: ")
                    for class_name in teacher.classes:
                        print(class_name)
            if not teacher_exist:
                print("\nBrak nauczyciela o podanym imieniu i nazwisku!")
        elif option == "wychowawca":
            full_name = input("\nPodaj imię i nazwisko wychowawcy: ")
            form_teacher_exist = False
            for form_teacher in list_form_teachers:
                if form_teacher.full_name == full_name:
                    form_teacher_exist = True
                    print("Wychowawca", full_name)
                    print("Klasa:", form_teacher.class_name)
                    print("Uczniowie: ")
                    for student in list_students:
                        if student.class_name == form_teacher.class_name:
                            print(student.full_name)
                    break
            if not form_teacher_exist:
                print("\nBrak wychowawcy o podanym imieniu i nazwisku!")
        elif option == "koniec":
            break
        else:
            print("\nNiepoprawna opcja!")

print("Witaj w programie do zarządzania bazą szkolną!")

while True:
    print("\nWpisz jedną z komend: utwórz, zarządzaj, koniec")
    choice = input().lower()
    if choice == "utwórz":
        create_user()
    elif choice == "zarządzaj":
        manage_users()
    elif choice == "koniec":
        break
    else:
        print("\nNiepoprawna komenda!")
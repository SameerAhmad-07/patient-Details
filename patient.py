# patient.py

def check_test_result(value):
    if value < 70 or value > 110:
        return "ABNORMAL"
    else:
        return "Normal"


def patient_details(name, age, disease, room_no, tests):
    print("\n----- Patient Details -----")
    print("Name       :", name)
    print("Age        :", age)
    print("Disease    :", disease)
    print("Room No    :", room_no)

    print("\n----- Test Results -----")
    for i, value in enumerate(tests, start=1):
        status = check_test_result(value)
        print(f"Test {i}: {value} --> {status}")


def main():
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    disease = input("Enter disease: ")
    room_no = input("Enter room number: ")

    tests = []
    for i in range(3):
        value = int(input(f"Enter Test {i+1} result: "))
        tests.append(value)

    patient_details(name, age, disease, room_no, tests)


if __name__ == "__main__":
    main()

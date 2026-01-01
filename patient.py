# patient.py
import os
import sys


def check_test_result(value=90):
    if value < 70 or value > 110:
        return "ABNORMAL"
    return "Normal"


def patient_details(
    name="Unknown",
    age=0,
    disease="Not Specified",
    room_no="NA",
    tests=None
):
    if tests is None:
        tests = [90, 90, 90]

    print("\n----- Patient Details -----")
    print("Name       :", name)
    print("Age        :", age)
    print("Disease    :", disease)
    print("Room No    :", room_no)

    print("\n----- Test Results -----")
    for i, value in enumerate(tests, start=1):
        print(f"Test {i}: {value} --> {check_test_result(value)}")


def main():
    # 1️⃣ COMMAND-LINE ARGUMENTS (Jenkins BEST METHOD)
    # python patient.py Sameer 21 Fever 12A 95,120,85
    if len(sys.argv) == 5:
        name = sys.argv[1]
        age = int(sys.argv[2])
        disease = sys.argv[3]
        room_no = sys.argv[4]
        tests = list(map(int, sys.argv[5].split(",")))

        patient_details(name, age, disease, room_no, tests)
        return

    # 2️⃣ ENVIRONMENT VARIABLES (if Jenkins exports them)
    name = os.getenv("PATIENT_NAME")
    age = os.getenv("AGE")
    disease = os.getenv("DISEASE")
    room_no = os.getenv("ROOM_NO")
    tests_env = os.getenv("TESTS")

    if all([name, age, disease, room_no, tests_env]):
        tests = list(map(int, tests_env.split(",")))
        patient_details(name, int(age), disease, room_no, tests)
        return

    # 3️⃣ MANUAL INPUT (local run)
    try:
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        disease = input("Enter disease: ")
        room_no = input("Enter room number: ")

        tests = []
        for i in range(3):
            tests.append(int(input(f"Enter Test {i+1} result: ")))

        patient_details(name, age, disease, room_no, tests)

    except EOFError:
        # 4️⃣ FINAL FALLBACK
        patient_details()


if __name__ == "__main__":
    main()

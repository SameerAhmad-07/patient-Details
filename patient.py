# patient.py
import os


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
    try:
        # 🔹 Jenkins parameters (environment variables)
        name = os.getenv("PATIENT_NAME")
        age = os.getenv("AGE")
        disease = os.getenv("DISEASE")
        room_no = os.getenv("ROOM_NO")
        tests_env = os.getenv("TESTS")  # example: 95,120,85

        # If Jenkins parameters exist → use them
        if all([name, age, disease, room_no, tests_env]):
            tests = list(map(int, tests_env.split(",")))
            patient_details(
                name=name,
                age=int(age),
                disease=disease,
                room_no=room_no,
                tests=tests
            )
            return

        # 🔹 Manual input (local run)
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        disease = input("Enter disease: ")
        room_no = input("Enter room number: ")

        tests = []
        for i in range(3):
            tests.append(int(input(f"Enter Test {i+1} result: ")))

        patient_details(name, age, disease, room_no, tests)

    except EOFError:
        # 🔹 Final fallback (safe defaults)
        patient_details()


if __name__ == "__main__":
    main()

import sys


def check_test_result(value=90):
    if value < 70 or value > 110:
        return "ABNORMAL"
    return "Normal"


def patient_details(
    name="umar",
    age=21,
    disease="cancer",
    room_no="23",
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
    if len(sys.argv) >= 5:
        name = sys.argv[1]
        age = int(sys.argv[2])
        disease = sys.argv[3]
        room_no = sys.argv[4]

        if len(sys.argv) == 6:
            tests = list(map(int, sys.argv[5].split(",")))
        else:
            tests = [90, 90, 90]

        patient_details(name, age, disease, room_no, tests)
        return

    patient_details()


if __name__ == "__main__":
    main()

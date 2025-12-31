def patient_details():
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    disease = input("Enter disease: ")
    room_no = input("Enter room number: ")

    tests = []
    for i in range(3):
        value = int(input(f"Enter Test {i+1} result: "))
        tests.append(value)

    print("\n----- Patient Details -----")
    print("Name       :", name)
    print("Age        :", age)
    print("Disease    :", disease)
    print("Room No    :", room_no)


    print("\n----- Test Results -----")
    for i, value in enumerate(tests, start=1):
        if value < 70 or value > 110:
            print(f"Test {i}: {value}  --> ABNORMAL")
        else:
            print(f"Test {i}: {value}  --> Normal")


patient_details()
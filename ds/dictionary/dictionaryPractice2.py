'''
Hospital Management System (Hard)

Each patient stores

Patient ID
Name
Age
Diseases (Set)
Medicines (List)
Contact (Tuple)
Reports (Dictionary)

Example
data = {
    101: {
        "name": "Sujal",
        "age": 62,
        "disease": {"Diabetes", "BP"},
        "medicine": ["A", "B", "C"],
        "contact": ("9876543210", "Ahmedabad"),
        "reports": {
            "Blood": 90,
            "Sugar": 120
        }
    }
}
Operations

Register patient
Search patient
Update reports
Print critical patients (blood > 100  or sugar > 150)
Find common diseases
Print all medicines
Count disease occurrence
Find patient having maximum reports (max values)
'''
patients = {}


def registerPatient():
    patient_id = input("Enter Patient ID : ")

    if (searchPatient(patient_id) != -1):
        print("ID Exists")
    else:
        patient_name = input("Enter patient name : ")
        patient_age = input("Enter patient age : ")

        diseases = set()
        diseases1 = input("Enter Diseases 1 name : ")
        diseases2 = input("Enter Diseases 2 name : ")
        diseases.add(diseases1)
        diseases.add(diseases2)

        medicine = []
        medicine1 = input("Enter Medicine 1 name : ")
        medicine2 = input("Enter Medicine 2 name : ")
        medicine.append(medicine1)
        medicine.append(medicine2)

        reports = {}

        patient_blood = input("Enter Blood Pressure : ")
        patient_sugar = input("Enter Sugar Level : ")

        reports["blood"] = patient_blood
        reports["sugar"] = patient_sugar

        patients[patient_id] = {
            "name": patient_name,
            "age": patient_age,
            "diseases": diseases,
            "medicine": medicine,
            "reports": reports
        }


def searchPatient(id):
    if id in patients.keys():
        return id
    else:
        return -1


def printPatient():
    print("-" * 120)
    print(f"{'ID':<10}{'Name':<20}{'Age':<8}{'Diseases':<25}{'Medicines':<25}{'Blood':<12}{'Sugar':<12}")
    print("-" * 120)

    for patient_id, patient in patients.items():

        diseases = ", ".join(patient["diseases"])
        medicines = ", ".join(patient["medicine"])

        blood = patient["reports"].get("blood", "N/A")
        sugar = patient["reports"].get("sugar", "N/A")

        print(f"{patient_id:<10}"
              f"{patient['name']:<20}"
              f"{patient['age']:<8}"
              f"{diseases:<25}"
              f"{medicines:<25}"
              f"{blood:<12}"
              f"{sugar:<12}")

    print("-" * 120)


choice = 0
while choice != 4:
    choice = int(input(
        "\n1. Register a patient\n2. Search a Patient\n3. View All Patients\n4. Exit\nSelect Your Choice : "))

    match choice:
        case 1:
            registerPatient()
        case 2:
            id = input("Enter Patient ID : ")
            if (searchPatient(id) != -1):
                print(patients[id])
            else:
                print("No data Found")
        case 3:
            printPatient()
        case 4:
            print("Exiting the program")
        case _:
            print("Try Again")

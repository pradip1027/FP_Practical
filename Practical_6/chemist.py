import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

def load_medicines():
    medicines = {}
    try:
        with open('medicines.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    med_id = int(parts[0])
                    name = parts[1]
                    price = float(parts[2])
                    expiry = parts[3]
                    company = parts[4]
                    medicines[med_id] = {'name': name, 'price': price, 'expiry': expiry, 'company': company}
    except FileNotFoundError:
        pass
    return medicines

def save_medicines(medicines):
    with open('medicines.txt', 'w') as f:
        for med_id, details in medicines.items():
            f.write(f"{med_id},{details['name']},{details['price']},{details['expiry']},{details['company']}\n")

def add_medicine(medicines):
    med_id = int(input("Enter Medicine ID: "))
    name = input("Enter Medicine Name: ")
    price = float(input("Enter Price: "))
    expiry = input("Enter Expiry Date: ")
    company = input("Enter Company Name: ")
    medicines[med_id] = {'name': name, 'price': price, 'expiry': expiry, 'company': company}
    save_medicines(medicines)

def display_sorted(medicines):
    sorted_meds = sorted(medicines.items())
    for med_id, details in sorted_meds:
        print(f"{med_id},{details['name']},{details['price']},{details['expiry']},{details['company']}")

def remove_duplicates(medicines):
    unique = {}
    for med_id, details in medicines.items():
        if details not in unique.values():
            unique[med_id] = details
    medicines.clear()
    medicines.update(unique)
    save_medicines(medicines)

def find_top_3(medicines):
    top_3 = sorted(medicines.items(), key=lambda x: x[1]['price'], reverse=True)[:3]
    for med_id, details in top_3:
        print(f"{med_id},{details['name']},{details['price']},{details['expiry']},{details['company']}")


medicines = load_medicines()
while True:
    print("\nOptions:")
    print("1. Add or Update Medicine")
    print("2. Arrange Medicines in Ascending Order")
    print("3. Remove Duplicate Medicines")
    print("4. Display Medicine Details")
    print("5. Find Top 3 Selling Medicines")
    print("6. Exit")
    choice = input("Enter your choice: ")
        
    if choice == '1':
        add_medicine(medicines)
    elif choice == '2':
        display_sorted(medicines)
    elif choice == '3':
        remove_duplicates(medicines)
    elif choice == '4':
        display_sorted(medicines)
    elif choice == '5':
        find_top_3(medicines)
    elif choice == '6':
        break

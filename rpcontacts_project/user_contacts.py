def add_contact(name, last_name, phone_number):
    names.append(name)
    last_names.append(last_name)
    phone_numbers.append(phone_number)
    
    
def remove_contact(name):
    contact_to_remove = names.index(name)
    
    names.pop(contact_to_remove)
    last_names.pop(contact_to_remove)
    phone_numbers.pop(contact_to_remove)


def search_contact(name):
    contact_to_search = names.index(name)
    
    print("\nContact Found!\n")
    print("Name: " + names[contact_to_search])
    print("Last Name: " + last_names[contact_to_search])
    print("Phone Number: " + phone_numbers[contact_to_search])
    print()
    

def display_contacts_list():
    for index in range(len(names)):
        print("Name: " + names[index])
        print("Last Name: " + last_names[index])
        print("Phone Number: " + phone_numbers[index])
        print()


def display_menu():
    print("=" * 5 + " Contacts List " + "=" * 5)
    print("[A]dd Contact")
    print("[R]emove Contact")
    print("[S]earch Contact")
    print("[D]isplay Contact List")
    print("[E]xit")
    print("=" * 25)
    
    
if __name__ == "__main__":
    names = []
    last_names = []
    phone_numbers = []
    
    while True:
        display_menu()
        
        choice = input("Enter your choice: ")
        
        if choice.lower() == "a":
            name = input("\nEnter First Name: ")
            last_name = input("Enter Last Name: ")
            phone_number = input("Enter Phone Number: ")
                
            add_contact(name, last_name, phone_number)
            print("\nContact details saved!\n")
            continue
        elif choice.lower() == "r":
            if len(names) == 0:
                print("\nContact List is empty!\n")
                continue
            else:
                remove_name = input("\nEnter name of the user you want to delete: ")
                if remove_name in names:
                   remove_contact(remove_name)
                   print(f"\n{remove_name} deleted from Contacts list!\n")
                   continue
                else:
                    print(f"\n{remove_name} doesn't exist in your Contacts list!\n")
                    continue
        elif choice.lower() == "s":
            if len(names) == 0:
                print("\nContact List is empty!\n")
                continue
            else:
                search_name = input("\nEnter name of the user you want to search: ")
                if search_name in names:
                   search_contact(search_name)
                   continue
                else:
                    print(f"\n{search_name} doesn't exist in your Contacts list!\n")
                    continue
        elif choice.lower() == "d":
            if len(names) == 0:
                print("\nContact List is empty!\n")
                continue
            else:
                print("\n----Contacts List----\n")
                display_contacts_list()
        elif choice.lower() == "e":
            print("GoodBye! Exiting...")
            break
        else:
            print("\nInvalid Choice! Please enter any one of 'A', 'R', 'S', 'D' or 'E'.")
            continue
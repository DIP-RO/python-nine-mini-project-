contact = {}
def showfunction():
    print(contact.items())
    print("Name \t Conatct")
    for key in contact:
        print( "{}\t {}".format(key,contact.get(key)))
        
while True:
    choice = int(input("1.Add new contact \n" 
                   "2.Search the contact \ n"
                   "3.Display  The contact \n"
                   "4.Edit the contact\n"
                   "5.Delete the ccontact\n"
                   "6.Exit\n"
                   "Please write number between 1-6"))
    if choice == 1:
        name = input("Your Name:")
        phone = input("Add phone Number")
        contact[name] = phone
    elif choice == 2:
        search = input("serach conatct:")
        if search in contact:
            print(search ," contact number is" , contact[name] )
        else:
            print("Not found")       
    
    elif choice == 3:
        if not contact:
            print("No contact") 
        else:
            showfunction()     
    elif choice == 4:
        edit = input("Edit Contact:")
        if edit in contact:
            phone = input("New phone number:")
            contact[edit] = phone
            print("Edit contact successfully")
            showfunction()
        else:
            print("Not found")
    elif choice == 5:
        delete = input("Please input delete number")
        if delete in contact:
            deleteConfirm = input("Do you want to delete this contact y/n")
            if deleteConfirm == "y" or deleteConfirm =="Y":
                contact.pop(delete)
            showfunction()
        else:
            print("Not found")
    else:
        break
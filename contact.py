#CONTACT LIST
contact={}

def view_contact():
    print("name\t\tcontacts Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
    

    
while True:    
 options=int(input("1.ADD NEW CONTACT \n 2.SEARCH CONTACT \n 3.VIEW \n 4.UPDATE\n 5.DELETE CONTACT\n 6.EXIT\n Enter your choice:"))
 if options==1:
    name=input("Enter the contact name:")
    phone=int(input("Enter the phone number:"))
    contact[name]=phone
 elif options==2:
    search=input("Enter the searching name:")
    if search in contact:
        print(search,"contact number is",contact[name])
    else:
        print("Name is not found in contact book")
 elif options==3:
    if not contact:
        print("contact book is empty ")
    else:
        view_contact()
 elif options==4:
    edit_contct=input("Enter the contact you want to edit:")
    if edit_contct in contact:
        phone=int(input("enter phone number:"))
        contact[edit_contct]=phone
        print("Contact edited!")
    else:
        print("Nmae not found in contact")
 elif options==5:
    delete_cont=input("Enter the contact name you want to delete")
    if delete_cont in contact:
        confirm=input("Do you want to delete it?(Y/S):")
        if confirm=="Y" or confirm=="y":
            contact.pop(delete_cont)
        view_contact()
    else:
        print("Nmae is not found in this list")
 else:
    break
    break
  
    
#MAIN MENU
import part1#IMPORTING .py FILES
import part2
import part3
import part4
import part5




while True: #ASK INPUTS FROM USER WITHOUT ENDING PROGRAM
    print()
    print("......................................................................................................................................")
    print("---------------Main Menu---------------")
    print()

    print("1---> Student Version")#MENU FOR CHOICE TO USER
    print("2---> Student Version(Validation)")
    print("3---> Staff Version with Horizontal Histogram")
    print("4---> Staff Version with Vertical Histogram")
    print("5---> Alternative Staff Version (optional extension)!!!You can use only one time..if u want run this again..exit and restart program..")
    print("6---> Exit")
    
    choice = int(input("\nEnter Your Choice :  "))#GETTING USER'S CHOICE
    print()




    if choice == 1:
                part1.student_version()#IMPORTING USER DEFINED FUNCTION PROGRAM PARTS TO MAIN MENU
    elif choice == 2:
                part2.student_version_validation()
    elif choice == 3:
                part3.staff_version_with_histogram()
    elif choice == 4:
                part4.vertical_histogram()
    elif choice == 5:
                part5.alternative_staff()

    elif choice == 6:
        break
                
    else:
        
        print("\nEnter valid number between 1-6 !!!!!!")#IF USER ENTER INVALID
        
        continue 
        
                  




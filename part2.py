def student_version_validation():
    
    print("---------------Student Version (Validation)---------------")
    #CREATE VARIABLES
    credit_at_pass=0
    credit_at_defer=0
    credit_at_fail=0
    total=0

    list1=[]#EMPTY LIST FOR ADDING USER INPUTS IN TO THE LIST
    listed_credits=[0,20,40,60,80,100,120]#LIST FOR GETTING RANGE

    ##################################################################################################################################################
    while True:
        try:#CHECKING USER INPUT IS INTEGER
            credit_at_pass=int(input("\nPlease enter your credits at pass:\t"))
            
            if credit_at_pass in listed_credits:#CHECKING IS USER INPUT IN RANGE
                
                credit_at_defer=int(input("\nPlease enter your credits at defer:\t"))
                
                if credit_at_defer in listed_credits:
                    
                    credit_at_fail=int(input("\nPlease enter your credits at fail:\t"))
                    
                    if credit_at_fail in listed_credits:
                        
                        total = credit_at_pass+credit_at_defer + credit_at_fail#GETTING TOTAL SUM OF USER INPUTS
                        
                        if total==120:#CHECKING USER INPUTS TOTAL
                            break#STOP THE LOOP
                        
                        
                        else:
                            print("\nTotal incorrect")
                            
                    else:
                        print("\nOut of range")
                        
                else:
                    print("\nOut of range")
                    
            else:
                print("\nOut of range")
                
        except:
            print("\nInteger required")




    ##################################################################################################################################################
    #APPEND USER INPUTS TO LIST
    list1.append(credit_at_pass)
    list1.append(credit_at_defer)
    list1.append(credit_at_fail)


    #READING INPUT LIST AND GETTING OUTPUTS
    for x in list1:
        if list1[0]==120:
            print("\nProgress")
            break 
        elif list1[0]==100:
            print("\nProgress (module trailer)")
            break
        elif list1[2]>=80:
            print("\nExclude")
            break
        
        else:
            print("\nDo not progress – module retriever")
            break


    ##################################################################################################################################################



            



        
        
        
        

        
            

def vertical_histogram():
    
    print("-----------------Vertical Histogram (optional extension)-----------------")
    #CREATE VARIABLES
    credit_at_pass=0
    credit_at_defer=0
    credit_at_fail=0
    total=0

    list1=[]
    listed_credits=[0,20,40,60,80,100,120]
    list_Main=[]
    list_sub=[]


    progress_count=0
    progress_mtrailer_count=0
    exclude_count=0
    module_retriever_count=0
    choice=""
    count=0
    counting=0
        

        ##################################################################################################################################################

    while True:
        while True:
            try:#CHECKING USER INPUT IS INTEGER
                credit_at_pass=int(input("\nEnter your total PASS credits:\t"))
                
                if credit_at_pass in listed_credits:#CHECKING IS USER INPUT IN RANGE
                    
                    credit_at_defer=int(input("\nEnter your total DEFER credits:\t"))
                    
                    if credit_at_defer in listed_credits:
                        
                        credit_at_fail=int(input("\nEnter your total FAIL credits:\t"))
                        
                        if credit_at_fail in listed_credits:
                            
                            total = credit_at_pass+credit_at_defer + credit_at_fail#GETTING TOTAL SUM OF USER INPUTS
                            
                            if total==120:#CHECKING USER INPUTS TOTAL
                                break
                            
                            
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
        #APPEND USER INPUTS TO LIST1
        list1.append(credit_at_pass)
        list1.append(credit_at_defer)
        list1.append(credit_at_fail)


        #READING INPUT LIST AND GETTING OUTPUTS
        for x in list1:
            if list1[0]==120:
                
                print("\nProgress")            
                progress_count=progress_count+1#COUNTING RESULTS
                
                
                break
            elif list1[0]==100:
                
                print("\nProgress (module trailer)")
                progress_mtrailer_count=progress_mtrailer_count+1
                
                break
            elif list1[2]>=80:
                
                
                print("\nExclude")
                exclude_count=exclude_count+1
                
                break
            
            else:
                
                print("\nDo not progress – module retriever")
                module_retriever_count= module_retriever_count+1
                break
        


    ##################################################################################################################################################

        choice=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:\t")#ASK USER TO ENTER ANOTHER SET OF DATA
        choice=choice.lower()#IF USER ENTERED UPPERCASE LETTERS THEN IT CONVERTING TO LOWERCASE

        list1=[]#WE WANT EMPTY LIST TO RE APPEND USER INPUTS


        if choice == "y":#IF USER WANT TO ENTER ANOTHER SET OF DATA THEN CONTINUE PROGRAM
                continue
        
        
        elif choice== "q":#IF USER DOESN'T NEED TO ENTER ANOTHER SET OF DATA THEN PROGRAM PRINT VERTICAL HISTOGRAM AND STOP
            
            
            print("\n------------------------Vertical Histogram------------------------")
            result_list=[[progress_count*"*"],[progress_mtrailer_count*"*"],[module_retriever_count*"*"],[exclude_count*"*"]]
            print(result_list)
           
            
            counting = result_list.index(max(result_list))
            print(counting)
            
            
           
            while len(result_list[counting][0]) != 0:
                list_sub = []
                while True:
                    if len(result_list[0][0]) != 0:
                        list_sub.append("*")
                        result_list[0][0] = result_list[0][0][:-1]
                        print(result_list)
                    else:
                        list_sub.append(" ")

                    if len(result_list[1][0]) != 0:
                        list_sub.append("*")
                        result_list[1][0] = result_list[1][0][:-1]
                        print(result_list)
                    else:
                        list_sub.append(" ")

                    if len(result_list[2][0]) != 0:
                        list_sub.append("*")
                        result_list[2][0] = result_list[2][0][:-1]
                        print(result_list)
                    else:
                        list_sub.append(" ")

                    if len(result_list[3][0]) != 0:
                        list_sub.append("*")
                        result_list[3][0] = result_list[3][0][:-1]
                        print(result_list)
                    else:
                        list_sub.append(" ")

                    break
            print(list_sub)
                list_Main.append(list_sub)
            print(list_Main)
                
    ##################################################################################################################################################

                      

            print("     Progress",progress_count,"     \tMTrailer",progress_mtrailer_count,"    \tRetriever",module_retriever_count,"   \tExcluded",exclude_count  )

            for i in list_Main:
                print("\t",end="")
                for j in i:
                    print(j,end="\t\t")
                print()
            print(progress_count+progress_mtrailer_count+module_retriever_count+exclude_count," outcomes in total..")
            break

                
            

                   
        else:
            print("\nError..Error..Error..program automatically restarted..Please Enter y to continue or Enter q to quit next time...")#IF USER ENTER INPUT OTHER THAN 'y' OR 'q' THIS ERROR WILL PRINT
            continue

            

    ##################################################################################################################################################

        
        
        
        

        

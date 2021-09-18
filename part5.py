#CREATE VARIABLES
progress_count=0
progress_mtrailer_count=0
exclude_count=0
module_retriever_count=0
total_count1=0
count=0

listx=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]#USER DATA ADDED LIST IN LIST

def alternative_staff():
    print("----------Alternative Staff Version (optional extension)----------")


    ###############################################################################################################################################################
    def main():
        global progress_count#GETTING GLOBAL VARIABLES BECAUSE PROGRAM CAN'T READ USER DEFINED FUNCTION OUTSIDE VARIABLES
        global progress_mtrailer_count
        global exclude_count
        global module_retriever_count
        global total_count1
        

        while True:

            for i in listx:
                for x in i:#READ LIST IN LIST AND LOOP IT
                
                    if i[0]==120:
                        
                        print("\nProgress")            
                        progress_count=progress_count+1#COUNTING RESULTS
                        
                        break
                                        
                        
                    elif i[0]==100:
                                            
                        print("\nProgress (module trailer)")
                        progress_mtrailer_count=progress_mtrailer_count+1
                        
                        break
                        
                        
                    elif i[2]>=80:
                        
                        
                        print("\nExclude")
                        exclude_count=exclude_count+1
                        
                        break
                                            
                    
                    else:
                        
                        print("\nDo not progress – module retriever")
                        module_retriever_count= module_retriever_count+1
                        
                        break
                    
    ###############################################################################################################################################################                    
            total_count1=progress_count+progress_mtrailer_count+exclude_count+module_retriever_count#COUNTING TOTAL RESULTS COUNT
            
            if total_count1<10:#PROGRAM AUTOMATICALLY REPEAT UNTIL TOTAL COUNT 10
                continue

            else:
                return cond()
    ###############################################################################################################################################################
    def cond():

                
        global progress_count
        global progress_mtrailer_count
        global exclude_count
        global module_retriever_count
        global count
        global total_count1
        


        print("\n------Horizontal Histogram------")

        print("Progress\t - ",progress_count," : ",end="")
        while count<progress_count :
                count=count+1
                print("*",end="")
                
                                    
        count=0
        print("\nTrailer\t\t - ",progress_mtrailer_count," : ",end="")
        while count<progress_mtrailer_count :
                count=count+1
                print("*",end="")
                            

        count=0
        print("\nRetriever\t - ",module_retriever_count," : ",end="")
        while count<module_retriever_count :
                count=count+1
                print("*",end="")
                
                
               
        count=0
        print("\nExcluded\t - ",exclude_count," : ",end="")
        while count<exclude_count :
                count=count+1
                print("*",end="")
                
                

        print("\n ")
        print(total_count1," Outcomes in total..")
           
        
    ###############################################################################################################################################################    

    main()#RUN MAIN FUNCTION

    

    







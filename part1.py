def student_version():
    
    print("\n----------------Student Version----------------")
    #CREATE VARIABLES
    credit_at_pass=0
    credit_at_defer=0
    credit_at_fail=0

    #INPUT USER DATA
    credit_at_pass=int(input("\nPlease enter your credits at pass:\t"))
    credit_at_defer=int(input("\nPlease enter your credits at defer:\t"))
    credit_at_fail=int(input("\nPlease enter your credits at fail:\t"))

    #GETTING OUTPUTS
    if credit_at_pass == 120:
        print("\nProgress")

    elif credit_at_pass== 100:
        print("\nProgress module trailer")

    elif credit_at_fail>= 80:
        print("\nExclude")
           
    else:
        print("\nDo not progress – module retriever")


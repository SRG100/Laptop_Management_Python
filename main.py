import read
import operations
import write
loop1=True

# for the program to run in loop
while loop1== True:

    print("\n\t\t\t\t\t\t\tShreyash Electronics ")
    print("\t\t\t\t\tBudhanilkantha-3, Kathmandu | Phonoe no.9845986232")

    #input from admin
    Admin_name_loop=True
    while Admin_name_loop==True:
        Admin_name=input("\nPlease Enter Your Name Admin(User's Name): ")
        if(Admin_name.isalpha()):
            Admin_name_loop=False        
        else:
             print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Please Enter Valid Admin Name !!! xxxxxxxxxxxxxxxxxxxxxxx")
             
    loop_correct_password=True
    while loop_correct_password==True:
        Password=input("\nEnter the password(7777): ")
        #For a level of security
        if Password=="7777":
            loop_correct_password=False
            print("\n\t\t\t\tWelcome to the System "+Admin_name +" Admin! I hope you hace a good day ahead!")
            
            loop2=True
            while loop2==True:

                #asking the user to select purpose
                a=input("\nPlease Select your purpose:-Sell/Buy/Exit ").lower()

                #when sell is entered
                if a=="sell":
                    #creating list to add bought data 
                    Total_laptop_sold=[]
                    customers_first_name_loop=True
                    while customers_first_name_loop==True:
                        customers_first_name=input("\nEnter the customer's first name: ")
                        if(customers_first_name.isalpha()):
                            customers_first_name_loop=False
                        else:
                            print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Please Enter Valid Customer First Name !!! xxxxxxxxxxxxxxxxxxxxxxx")
                    customers_last_name_loop=True
                    while customers_last_name_loop==True:
                        customers_last_name=input("\nEnter the customer's last name: ")
                        if(customers_last_name.isalpha()):
                            customers_last_name_loop=False
                        else:
                            print("n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Please Enter Valid Customer Last Name !!! xxxxxxxxxxxxxxxxxxxxxxx")
                    customers_name=customers_first_name+' '+customers_last_name
                    loop_phone_number=True
                    #creating loop for exceptional handling
                    while loop_phone_number==True:  
                        try:
                            customers_phone=int(input("\nEnter the customer's mobile number: "))
                            if len(str(customers_phone))==10 and customers_phone>0 :
                                loop_phone_number=False
                            else:
                                loop_phone_number=True
                                print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Enter the customer's valid mobile number: !!! xxxxxxxxxxxxxxxxxxxxxxx")
                        except:
                            print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Invalid phone number !!! xxxxxxxxxxxxxxxxxxxxxxx")

                    #printing laptop's data
                    print("\n")
                    read.Laptop_print()
                    loop3=True
                    
                    #creating loop if user wants to sell again
                    while loop3 == True:
                        
                        #getting data from the user and creating loop for exception handling
                        try_laptopID=True
                        while try_laptopID==True:
                            try:
                                Laptop_id=int(input("\nEnter the laptop id the customer wants to purchase: "))
                                if Laptop_id==0 or Laptop_id<0:
                                    try_laptopID=True
                                    print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!!Laptop Id doesn't exist.Enter Valid input.!!! xxxxxxxxxxxxxxxxxxxxxxx")
                                    print("\n")
                                    read.Laptop_print()
                                else:
                                    try_laptopID=False
                            except:
                                    print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!!Laptop Id doesn't accept string value.!!! xxxxxxxxxxxxxxxxxxxxxxx")

                        #using function defined in operations to check and get valid ids 
                        Valid_ids=read.Valid_ids()
                        Validity_id=operations.check(Valid_ids,Laptop_id)
                        
                        #checking if laptop stock is avaliable or not
                        if Validity_id== True :
                            
                            total_no_laptops=read.Laptop_quantity(Laptop_id)
                            #checking whether the id is valid or not
                            if total_no_laptops!=0:
                                loop_valid_items=True
            
                                
                                #creating loop for valid quqntity of laptops
                                while(loop_valid_items==True):
                                    try_no_of_laptops=True
                                    
                                    #creating loop to handle exception
                                    while try_no_of_laptops==True:
                                        try:
                                            no_of_Laptop=int(input("\nEnter total number of laptops customer wants to purchase: "))
                                            if no_of_Laptop==0 or no_of_Laptop<0:
                                                print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!!  Please enter valid number of laptops !!! xxxxxxxxxxxxxxxxxxxxxxx")
                                                print("\n")
                                                read.Laptop_print()
                                            else:
                                                try_no_of_laptops=False
                                        except:
                                            print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!!  Quantity of laptops are not in string value.!!! xxxxxxxxxxxxxxxxxxxxxxx")
                                    validity_no_laptops=operations.check(total_no_laptops,no_of_Laptop)
                                    #checking whether entered quantity and stock are compatable with eachother
                                    if validity_no_laptops==True:
                                        loop_valid_items=False
                                        phone=str(customers_phone)
                                        new_no_laptops=operations.sub_items(total_no_laptops,no_of_Laptop)
                                        updated_dict=read.new_Laptop_quantity_dictionary(Laptop_id,new_no_laptops)
                                        write.new_Laptop_quantity_text(updated_dict)
                                        unit_price_laptop=read.Laptop_price(Laptop_id)
                                        total_price_laptop=operations.Total_price(unit_price_laptop,no_of_Laptop)
                                        Laptop_name= read.Laptop_Name(Laptop_id)
                                        read.Laptop_print()
                                        Total_laptop_sold.append([Laptop_id,Laptop_name,no_of_Laptop,unit_price_laptop,total_price_laptop])
                                        
                                        #asking user if the customer wants to buy more
                                        Valid_input_sell_again=True
                                        while Valid_input_sell_again==True:
                                            Sell_again=input("\nWould customers like to buy more?yes/no: ").lower()
                                            if Sell_again=="yes":
                                                loop3= True
                                                Valid_input_sell_again=False
                                            elif Sell_again=="no":
                                                loop3=False
                                                #calling to print bill
                                                deliver_loop=True
                                                while deliver_loop==True:
                                                    deliver=input("\nDo you want the item to be shipped or not?Yes/No").lower()
                                                    if deliver=="yes":
                                                        delivery_fee=100
                                                        deliver_loop=False
                                                    elif deliver=="no":
                                                        delivery_fee=0
                                                        deliver_loop=False
                                                    else:
                                                        print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Enter valid input.  !!! xxxxxxxxxxxxxxxxxxxxxxx \n")
                                                        print("\n")
                                                        read.Laptop_print()
                                                write.print_bill_sell(Total_laptop_sold,customers_name,phone,delivery_fee,Admin_name)
                                                write.write_bill_sell(Total_laptop_sold,customers_name,phone,delivery_fee,Admin_name)
                                                Valid_input_sell_again=False
                                            else:
                                                Valid_input_sell_again=True
                                                print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Please enter valid input !!! xxxxxxxxxxxxxxxxxxxxxxx ")
                                    else:
                                        print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!!Invalid Numbers Of Laptops !!! xxxxxxxxxxxxxxxxxxxxxxx ")
                            else:
                                print("\n\t\txxxxxxxxxxxxxxxxxxxxxxx !!!This item is out of stock.Sorry for the inconvinience !!! xxxxxxxxxxxxxxxxxxxxxxx ")
                                
                        else:
                            print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Please enter a Valid Id!!! !!! xxxxxxxxxxxxxxxxxxxxxxx")
                        
                #when buy is entered           
                elif a=="buy" :
                    #creating list to add bought data 
                    Total_laptop_bought=[]
                    manufactures_name_loop=True
                    while manufactures_name_loop==True:
                        manufacturers_name=input("\nEnter the manufacturer's name: ")
                        if(manufacturers_name.isalpha()):
                            manufactures_name_loop=False 
                        else:
                            print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! please enter valid manufacturer name !!! xxxxxxxxxxxxxxxxxxxxxxx")
                            manufactures_name_loop=True           
                    loop_phone_number=True  
                    #creating loop for exceptional handling
                    while loop_phone_number==True:  
                        try:
                            manufacturers_phone=int(input("\nEnter the manufacturer's mobile number: "))
                            if len(str(manufacturers_phone))==10 and manufacturers_phone>0:
                                loop_phone_number=False
                                
                            else:
                                loop_phone_number=True
                                print(" \n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Invalid phone number !!! xxxxxxxxxxxxxxxxxxxxxxx")
                        except:
                            print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Invalid phone number !!! xxxxxxxxxxxxxxxxxxxxxxx ")
                            
                    #printing laptop's data
                    read.Laptop_print()
                    item_add_loop=True
                    while item_add_loop==True:
                        new_item_check=input("\nIs it a new item to be added?(Yes/No)").lower()
                        if new_item_check!="yes" and new_item_check!="no":
                            print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Please Enter Valid input. !!! xxxxxxxxxxxxxxxxxxxxxxx ")
                        else:
                            item_add_loop=False
                    count=0
                    while new_item_check=="yes":
                        count+=1
                        total_existing_laptops=read.Valid_ids()
                        try_laptop_new_id=True
                        while try_laptop_new_id==True:
                            try:
                                laptop_id=int(input("\nEnter new laptop id:"))
                                if laptop_id!=total_existing_laptops+1:
                                    try_laptop_new_id=True
                                    print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Laptop id is incorrect.Enter Valid input. !!! xxxxxxxxxxxxxxxxxxxxxxx !!! \n")
                                else:
                                    try_laptop_new_id=False
                            except:
                                    print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Laptop  can't have string value. !!! xxxxxxxxxxxxxxxxxxxxxxx !!! \n")
                        
                        laptop_name =input("\nEnter the name of laptop: ")
                        laptop_company=input("\nEnter the company of laptop: ")
                        try_new_laptop_price=True
                        while try_new_laptop_price==True:
                            try:
                                laptop_price =int(input("\nEnter the price of laptop: "))
                                if laptop_price==0 or laptop_price<0:
                                    try_new_laptop_price=True
                                    print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Laptop price cannot be zero or less.Enter Valid input. !!! xxxxxxxxxxxxxxxxxxxxxxx !!! \n")
                                else:
                                    try_new_laptop_price=False
                            except:
                                    print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Laptop price can't have string value.!!! xxxxxxxxxxxxxxxxxxxxxxx  \n")
                        try_laptop_new_quantity=True
                        while try_laptop_new_quantity==True:
                            try:
                                laptop_quantity=int(input("\nEnter the quantity of laptop to be bought: "))
                                if laptop_quantity< 0 or laptop_quantity==0:
                                    try_laptop_new_quantity=True
                                    print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Laptop quantity is incorrect.Enter Valid input. !!! xxxxxxxxxxxxxxxxxxxxxxx\n")
                                else:
                                    try_laptop_new_quantity=False
                            except:
                                    print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx!!! Laptop price can't have string value. !!! xxxxxxxxxxxxxxxxxxxxxxx\n")

                        laptop_core=input("\nEnter the core of laptop: ")
                        laptop_GPU=input("\nEnter the GPU of laptop: ")
                        new_dict=read.Add_new_items_dictinonary(laptop_name,laptop_company,laptop_price,laptop_quantity,laptop_core,laptop_GPU)
                        write.Add_new_items_text(new_dict)
                        total_price=operations.Total_price(laptop_price,laptop_quantity)
                        Total_laptop_bought.append([laptop_id,laptop_name,laptop_quantity,laptop_price,total_price])
                        new_item_check=input("\nDo you want to add more new items?(Yes/No)").lower()
                        if new_item_check!="no" and new_item_check!="yes":
                            print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Please enter valid input !!! xxxxxxxxxxxxxxxxxxxxxxx")
                    if count==0:
                        loop4=True
                    else:
                        Check_valid_loop=True
                        while Check_valid_loop==True:
                            buy_existing=input("\nDo you want to buy existing items?(Yes/No)").lower()
                            
                            if buy_existing=="yes":
                                print("\n")
                                read.Laptop_print()
                                loop4=True
                                Check_valid_loop=False
                            elif buy_existing=="no":
                                print("\n")
                                read.Laptop_print()
                                loop4=False
                                Check_valid_loop=False
                                phone=str(manufacturers_phone)
                                write.print_bill_buy(Total_laptop_bought,manufacturers_name,phone,Admin_name)
                                write.write_bill_buy(Total_laptop_bought,manufacturers_name,phone,Admin_name)
                            else:
                                print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Please enter valid input !!! xxxxxxxxxxxxxxxxxxxxxxx")
                                Check_valid_loop=True
                    while loop4== True:
                    #getting data from the user and creating loop for exception handling
                        try_laptopID=True
                        while try_laptopID==True:
                            try:
                                Laptop_id=int(input("\nEnter the laptop id the you want to purchase: "))
                                if Laptop_id==0 or Laptop_id<0:
                                    try_laptopID=True
                                    print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Laptop Id doesn't exist.Enter Valid input. !!! xxxxxxxxxxxxxxxxxxxxxxx")
                                else:
                                    try_laptopID=False
                            except:
                                print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Laptop Id doesn't accept string value. !!! xxxxxxxxxxxxxxxxxxxxxxx")

                        #using function defined in operations to check and get valid ids 
                        Valid_ids=read.Valid_ids()
                        Validity_id=operations.check(Valid_ids,Laptop_id)
                        
                              
                        #checking whether the id is valid or not
                        if Validity_id== True:
                            total_no_laptops=read.Laptop_quantity(Laptop_id)
                            
                            try_no_of_laptops=True
                            #creating loop to handle exception
                            while try_no_of_laptops==True:
                                try:
                                    no_of_Laptop=int(input("\nEnter total number of laptops you want to purchase: "))
                                    if no_of_Laptop==0 or no_of_Laptop<0:
                                        try_no_of_laptops=True
                                        print("\n\t\t\txxxxxxxxxxxxxxx !!! Quantity of Laptop cannot be zero or less.Enter Valid input. !!! xxxxxxxxxxxxxxx !!! \n")
                                       
                                    else:
                                        try_no_of_laptops=False
                                except:
                                    print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Quantity of laptops are not in string value. !!! xxxxxxxxxxxxxxxxxxxxxxx")                      
                            phone=str(manufacturers_phone)
                            new_no_laptops=operations.add_items(total_no_laptops,no_of_Laptop)
                            updated_dict=read.new_Laptop_quantity_dictionary(Laptop_id,new_no_laptops)
                            write.new_Laptop_quantity_text(updated_dict)

                            unit_price_laptop=read.Laptop_price(Laptop_id)
                            total_price_laptop=operations.Total_price(unit_price_laptop,no_of_Laptop)
                            Laptop_name= read.Laptop_Name(Laptop_id)
                            read.Laptop_print()
                            Total_laptop_bought.append([Laptop_id,Laptop_name,no_of_Laptop,unit_price_laptop,total_price_laptop])
                            
                            #asking user if the customer wants to buy more
                            valid_input_loop=True
                            while valid_input_loop==True:
                                buy_again=input("\nWould you like to buy more?yes/no: ").lower()
                                if buy_again=="yes":
                                    loop4= True
                                    valid_input_loop=False
                                elif buy_again=="no" :
                                    valid_input_loop=False
                                    loop4=False
                                    #calling to print bill
                                    write.print_bill_buy(Total_laptop_bought,manufacturers_name,phone,Admin_name)
                                    write.write_bill_buy(Total_laptop_bought,manufacturers_name,phone,Admin_name)
                                else:
                                    valid_input_loop=True
                            
                        else:

                            print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Please enter a Valid Id !!! xxxxxxxxxxxxxxxxxxxxxxx")
                elif a=="exit":
                    print("\n\t\t\t\t\tThank You.Have a great day ahead admin... :)")
                    loop1=False
                    loop2=False
                else:
                    print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Please enter a valid input. !!! xxxxxxxxxxxxxxxxxxxxxxx")
        else:
            print("\n\t\t\txxxxxxxxxxxxxxxxxxxxxxx !!! Invalid Password !!! xxxxxxxxxxxxxxxxxxxxxxx")
            loop_correct_password=True

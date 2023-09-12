def Laptop_print():
    print("  ---------------------------------------------------------------------------------------------------------------------------")
    print("\tId\tLaptop Model\t\tCompany\t\tPrice($)\tNo.of Items\tLaptop Core\t\tGPU")
    print("  ---------------------------------------------------------------------------------------------------------------------------")
    file=open("laptop.txt","r")
    id_=1
    for line in file:
        print("\t",id_,"\t",line.replace(",","\t\t"))
        id_+=1
    print("  --------------------------------------------------------------------------------------------------------------------------")
    file.close()

def Valid_ids():        
    laptop=open("laptop.txt","r")
    Laptop_data={}
    id_=1
    for line in laptop:
        line=line.replace("\n","");
        Laptop_data.update({id_:line.split(",")})
        id_+=1
    laptop.close()
    return(len(Laptop_data))

def Laptop_quantity(laptop_id):        
    laptop=open("laptop.txt","r")
    Laptop_data={}
    id_=1
    for line in laptop:
        line=line.replace("\n","");
        Laptop_data.update({id_:line.split(",")})
        id_+=1
    no_of_items=int(Laptop_data[laptop_id][3])
    laptop.close()
    return(no_of_items)

def Laptop_price(laptop_id):        
    laptop=open("laptop.txt","r")
    Laptop_data={}
    id_=1
    for line in laptop:
        line=line.replace("\n","");
        Laptop_data.update({id_:line.split(",")})
        id_+=1
    price_of_items=int(Laptop_data[laptop_id][2])
    laptop.close()
    return(price_of_items)

def Laptop_Name(laptop_id):
    laptop=open("laptop.txt","r")
    Laptop_data={}
    id_=1
    for line in laptop:
        line=line.replace("\n","");
        Laptop_data.update({id_:line.split(",")})
        id_+=1
    name_of_laptop=Laptop_data[laptop_id][0]
    laptop.close()
    return(name_of_laptop)

def new_Laptop_quantity_dictionary(Laptop_id,new_quantity):        
    laptop=open("laptop.txt","r")
    Laptop_data={}
    id_=1
    for line in laptop:
        line=line.replace("\n","")
        Laptop_data.update({id_:line.split(",")})
        id_+=1
    Laptop_data[Laptop_id][3]=new_quantity
    laptop.close()
    return(Laptop_data)

def Add_new_items_dictinonary(Laptop_Name,Company,Price,Quantity,Laptop_core,GUI):
    laptop=open("laptop.txt","r")
    Laptop_data={}
    id_=1
    for line in laptop:
        line=line.replace("\n","")
        Laptop_data.update({id_:line.split(",")})
        id_+=1
    Laptop_data.update({id_:[Laptop_Name,Company,Price,Quantity,Laptop_core,GUI]})
    laptop.close()
    return(Laptop_data)









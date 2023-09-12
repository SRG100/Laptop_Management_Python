import datetime
time=datetime.datetime.now()
year=str(time.year)
month=str(time.month)
day=str(time.day)
hour=str(time.hour)
minute=str(time.minute)
second=str(time.second)
unique_id=year+month+day+hour+minute+second
date=year+'-'+month+'-'+day

def Add_new_items_text(LaptopData):
    laptop_new=open("laptop.txt","w")
    for i in LaptopData.values():
        laptop_new.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+"\n")
    laptop_new.close()

def new_Laptop_quantity_text(updated_dict):  
    laptop_new=open("laptop.txt","w")
    for i in updated_dict.values():
        laptop_new.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+"\n")
    laptop_new.close()

def Add_new_items_text(LaptopData):
    laptop_new=open("laptop.txt","w")
    for i in LaptopData.values():
        laptop_new.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+"\n")
    laptop_new.close()


def print_bill_sell(Total_laptop_sold,name,contact,delivery_fee,admin_name):
    print("\n---------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\tShreyash Electronics ")
    print("\t\t\t\t\tBudhanilkantha-3, Kathmandu | Phone no.9845986232 ")
    print("\t\t\t\t\t\t\tInnovation and Us")
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("Customer's Name:",name,"\t\t\t\t\t\t\t\t\t\tSold By:",admin_name)
    print("Contact Number:",contact,"\t\t\t\t\t\t\t\t\t\tTime:",date)
    print("\n---------------------------------------------------------------------------------------------------------------------------------")
    print("Laptop Name\t\t\tNo of Laptop\t\t\tUnit Price Laptop\t\t\tTotal Price")
    print("---------------------------------------------------------------------------------------------------------------------------------")
    i=0
    sub_total=0
    for each in Total_laptop_sold:
        laptop_id=Total_laptop_sold[i][0]
        print(Total_laptop_sold[i][1],"\t\t\t",Total_laptop_sold[i][2],"\t\t\t\t\t",Total_laptop_sold[i][3],"\t\t\t\t",Total_laptop_sold[i][4])
        sub_total=sub_total+Total_laptop_sold[i][4]
        i+=1
    grand_total=sub_total+delivery_fee
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("Sub total\t\t\t\t\t\t\t\t\t\t\t\t",sub_total)
    print("Delivery fee\t\t\t\t\t\t\t\t\t\t\t\t",delivery_fee)
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("Grand total\t\t\t\t\t\t\t\t\t\t\t\t",grand_total)
    print("---------------------------------------------------------------------------------------------------------------------------------")
    
def write_bill_sell(Total_laptop_sold,Name,contact,delivery_fee,Admin_name):
    Bill_generate=open(str(Name)+"_"+str(contact)+"_"+str(unique_id)+".txt","w")
    Bill_generate.write("\n---------------------------------------------------------------------------------------------------------------------------------\n")
    Bill_generate.write("\t\t\t\t\t\t\tShreyash Electronics \n")
    Bill_generate.write("\t\t\t\t\tBudhanilkantha-3, Kathmandu | Phone no.9845986232\n ")
    Bill_generate.write("\t\t\t\t\t\t\tInnovation and Us\n")
    Bill_generate.write("---------------------------------------------------------------------------------------------------------------------------------\n")
    Bill_generate.write("Customer's Name:"+str(Name)+"\t\t\t\t\t\t\t\t\t\tSold By :"+str(Admin_name)+ "\n")
    Bill_generate.write("Contact Number:"+str(contact)+"\t\t\t\t\t\t\t\t\t\tTime:" + str(date)+"\n")
    Bill_generate.write("\n---------------------------------------------------------------------------------------------------------------------------------\n")
    Bill_generate.write("Laptop Name\t\t\tNo of Laptop\t\t\tUnit Price Laptop\t\t\tTotal Price")
    Bill_generate.write("\n---------------------------------------------------------------------------------------------------------------------------------\n")
    i=0
    sub_total=0
    for each in Total_laptop_sold:
        laptop_id=Total_laptop_sold[i][0]
        Bill_generate.write(Total_laptop_sold[i][1]+"\t\t\t"+str(Total_laptop_sold[i][2])+"\t\t\t\t\t"+str(Total_laptop_sold[i][3])+"\t\t\t\t"+str(Total_laptop_sold[i][4])+"\n")
        sub_total=sub_total+Total_laptop_sold[i][4]
        i+=1
    grand_total=sub_total+delivery_fee
    Bill_generate.write("---------------------------------------------------------------------------------------------------------------------------------\n")
    Bill_generate.write("Sub total\t\t\t\t\t\t\t\t\t\t\t\t"+str(sub_total))
    Bill_generate.write("\nDelivery fee\t\t\t\t\t\t\t\t\t\t\t\t"+str(delivery_fee))
    Bill_generate.write("\n---------------------------------------------------------------------------------------------------------------------------------\n")
    Bill_generate.write("Grand total\t\t\t\t\t\t\t\t\t\t\t\t"+str(grand_total))
    Bill_generate.write("\n---------------------------------------------------------------------------------------------------------------------------------\n")
    


def print_bill_buy(Total_laptop_bought,name,contact,admin_name):
    print("\n---------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\tShreyash Electronics ")
    print("\t\t\t\t\tBudhanilkantha-3, Kathmandu | Phone no.9845986232 ")
    print("\t\t\t\t\t\t\tInnovation and Us")
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("Manufacturer's Name:",name,"\t\t\t\t\t\t\t\t\t\tSold By:",admin_name)
    print("Contact Number:",contact,"\t\t\t\t\t\t\t\t\t\tTime:",date)
    print("\n---------------------------------------------------------------------------------------------------------------------------------")
    print("Laptop Name\t\t\tNo of Laptop\t\t\tUnit Price Laptop\t\t\tTotal Price")
    print("---------------------------------------------------------------------------------------------------------------------------------")
    sub_total=0
    i=0
    for each in Total_laptop_bought:
        laptop_id=Total_laptop_bought[i][0]
        print(Total_laptop_bought[i][1],"\t\t\t",Total_laptop_bought[i][2],"\t\t\t\t\t",Total_laptop_bought[i][3],"\t\t\t\t",Total_laptop_bought[i][4])
        sub_total=sub_total+Total_laptop_bought[i][4]
        i+=1
    print("\n")
    Vat_amount=(13/100)*sub_total
    grand_total=sub_total+Vat_amount
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("Sub total\t\t\t\t\t\t\t\t\t\t\t\t",sub_total)
    print("Vat Amount\t\t\t\t\t\t\t\t\t\t\t\t",Vat_amount)
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("Grand total(With VAT)\t\t\t\t\t\t\t\t\t\t\t",grand_total)
    print("---------------------------------------------------------------------------------------------------------------------------------")
    
def write_bill_buy(Total_laptop_sold,name,contact,admin_name):
    Bill_generate=open(str(name)+"_"+str(contact)+"_"+str(unique_id)+".txt","w")
    Bill_generate.write("\n---------------------------------------------------------------------------------------------------------------------------------\n")
    Bill_generate.write("\t\t\t\t\t\t\tShreyash Electronics \n")
    Bill_generate.write("\t\t\t\t\tBudhanilkantha-3, Kathmandu | Phone no.9845986232\n ")
    Bill_generate.write("\t\t\t\t\t\t\tInnovation and Us\n")
    Bill_generate.write("---------------------------------------------------------------------------------------------------------------------------------\n")
    Bill_generate.write("Manufacturer's Name:"+str(name)+"\t\t\t\t\t\t\t\t\t\tSold By :"+str(admin_name)+ "\n")
    Bill_generate.write("Contact Number:"+str(contact)+"\t\t\t\t\t\t\t\t\t\tTime:" + str(date)+"\n")
    Bill_generate.write("\n---------------------------------------------------------------------------------------------------------------------------------\n")
    Bill_generate.write("Laptop Name\t\t\tNo of Laptop\t\t\tUnit Price Laptop\t\t\tTotal Price")
    Bill_generate.write("\n---------------------------------------------------------------------------------------------------------------------------------\n")
    i=0
    sub_total=0
    for each in Total_laptop_sold:
        laptop_id=Total_laptop_sold[i][0]
        Bill_generate.write(Total_laptop_sold[i][1]+"\t\t\t"+str(Total_laptop_sold[i][2])+"\t\t\t\t\t"+str(Total_laptop_sold[i][3])+"\t\t\t\t"+str(Total_laptop_sold[i][4])+"\n")
        sub_total=sub_total+Total_laptop_sold[i][4]
        i+=1
    Bill_generate.write("\n")
    Vat_amount=(13/100)*sub_total
    grand_total=sub_total+Vat_amount
    Bill_generate.write("---------------------------------------------------------------------------------------------------------------------------------\n")
    Bill_generate.write("Sub total\t\t\t\t\t\t\t\t\t\t\t\t"+str(sub_total))
    Bill_generate.write("\Vat Amount \t\t\t\t\t\t\t\t\t\t\t\t"+str(Vat_amount))
    Bill_generate.write("\n---------------------------------------------------------------------------------------------------------------------------------\n")
    Bill_generate.write("Grand total(With VAT)\t\t\t\t\t\t\t\t\t\t\t\t"+str(grand_total))
    Bill_generate.write("\n---------------------------------------------------------------------------------------------------------------------------------\n")
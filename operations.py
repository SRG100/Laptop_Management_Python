def check(total,user_given):
    value=False
    if total>user_given or total==user_given :
        value =True
    else:
        value =False
    return(value)
        

def add_items(Old_items,required_items):
    new_items=Old_items+required_items
    return(new_items)
    
def sub_items(Old_items,required_items):
    new_items=Old_items-required_items
    return(new_items)

def Total_price(unit_price,quantity):
    total_price=unit_price*quantity
    return(total_price) 

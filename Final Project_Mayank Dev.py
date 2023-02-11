#!/usr/bin/env python
# coding: utf-8

# # Final Project

# # Admin

# In[10]:


import sys
import json
class Admin:
    def __init__(self):
        self.food_item={}
        self.food_id=len(self.food_item)+1
        self.Admin_profile={}
        self.Admin_id=len(self.Admin_profile)+1
    def Adm_register(self):
        start=input("Welcome to Registration portal of our Food Ordering App. \n DO you wish to Register, Press Y or hit any key to exit:")
        if start=='y' or start=='Y':
            self.A_name = input("Enter Name: ")
            self.A_email_id = input("Enter Email ID: ")
            self.A_phone_no = int(input("Enter Phone No. "))
            self.A_address = input("Enter Address: ")
            self.A_password = input("Create Password: ")
            self.Admin={"Name":self.A_name,"Email ID":self.A_email_id,"Contact No.":self.A_phone_no,"Address":self.A_address,"Password":self.A_password}
            self.Admin_id=len(self.Admin_profile)+1
            self.Admin_profile[self.Admin_id]=self.Admin
            with open("Admin_profile","w") as f:
                json.dump(self.Admin,f)
        else:
            print("Thank you for visiting us: have a nice day")
            sys.exit()
    
    def Adm_login(self,emailid,pass_word):
        if self.A_email_id==emailid and self.A_password==pass_word:
            print("\n>>>>>>Welcome to Food Ordering Service<<<<<<") 
            print("\n Thank you, You can Start ordering with us!!!")
        else:
            print("\nAccess Denied, enter correct details")
            sys.exit()
    
    def add_new_food(self):
        print("Welcome to Food ordering App - Admin Control","\nupdate new food item")
        self.Name = input(" Enter Food Name: ")
        self.Quantity = int(input("Enter the Quantity: "))
        self.Price = int(input("Enter the Price: "))
        self.Discount = int(input(" Enter the Discount : "))
        self.Stock = input("Enter Stock: ")
        print("Thank you for updating the Food Item", self.Name, "Find details below")
        self.item ={"Food name: ":self.Name, "Quantity: ":self.Quantity, "Price: ":self.Price, "Discount: ":self.Discount, "Stock available: ": self.Stock}
        self.food_id=len(self.food_item)+1
        self.food_item[self.food_id]=self.item
        with open("Food_items1.json","w") as f:
            json.dump(self.food_item,f)
        return self.food_item
    
    def remove_item(self):
        food_item=int(input("Enter the Food Id to delete the item:"))
        del self.food_item[food_item]
        print("Food item",food_item,"successfully Deleted from the MENU")
        print("updated Food Items List", self.food_item)
        with open("Food_items1.json","w+") as f:
            json.dump(self.food_item,f)
        
   
    def edit_food(self):
        food_id=int(input("Enter the Food Id to edit the item:"))
        #self.food_item[self.food_id]=self.item
        self.Name = input(" Enter Food Name: ")
        self.Quantity = int(input("Enter the Quantity: "))
        self.Price = int(input("Enter the Price: "))
        self.Discount = int(input(" Enter the Discount : "))
        self.Stock = input("Enter Stock: ")
        print("Thank you for updating the Food Item", self.Name)
        self.food_id=len(self.food_item)
        self.food_item[self.food_id]=self.item
        with open("Food_items1.json","w+") as f:
            json.dump(self.food_id,f)
        #return self.food_item

    def list_view(self):
        print("Updated List of Items in the Menu")
        return self.food_item
        
c=Admin()
print(c.Adm_register())
print("\n\n>>>>>Welcome to Admin Login Portal of Food Ordering App<<<<<")
emailid = input("\nEnter your Email ID:")
pass_word = input("\nEnter your password")
print(c.Adm_login(emailid,pass_word))
print(c.add_new_food())
print(c.add_new_food())
print(c.remove_item())
print(c.edit_food())
print(c.list_view())


# # User

# In[29]:


import numpy as np
import sys
import json
class user:
    def __init__(self):
        self.x={}
        self.user_profile={}
        self.user_id=len(self.user_profile)+1
    def register(self):
        start=input(">>>>Welcome to Registration portal of our Food Ordering App<<<<. \nIf you wish to proceed Press Y  ")
        if start=='y' or start=='Y':
            self.name = input("Enter Name: ")
            self.email_id = input("Enter Email ID: ")
            self.phone_no = int(input("Enter Phone No. "))
            self.address = input("Enter Address: ")
            self.password = input("Create Password: ")
            self.user={"Name":self.name,"Email ID":self.email_id,"Contact No.":self.phone_no,"Address":self.address,"Password":self.password}
            self.user_id=len(self.user_profile)+1
            self.user_profile[self.user_id]=self.user
            with open("user_profile","w") as f:
                json.dump(self.user,f)
            return self.user
            # "\nThank you Registering with us!!"
           
        else:
            print("Thank you for Visiting us!!! \n visit and Follow our instagram channel for more updates")
            sys.exit()
    def login(self,emailid,pass_word):
        if self.email_id==emailid and self.password==pass_word:
            print("\n>>>>>>Welcome to Food Ordering Service<<<<<<") 
            print("\n Thank you, You can Start ordering with us!!!")
        else:
            print("\nAccess Denied, enter correct details")
            sys.exit()
        return ""
    def options(self):
        a = np.array(["1_Tandoori_Chicken_4pc_INR_240", "2_Vegan_Burger_1_Pc_INR_320", "3_Truffle_Cake_500gm_INR_900"])
       
        order=[]
        print("Enter The Choice")
        print("Menu \n",a)
        print("Enter your choice: ")
        option=int(input("\n 1.Place the Order, \n 2. Order History \n 3. Update Profile\n 4. Exit \n"))
        if option==1:
            a = np.array(["1_Tandoori_Chicken_4pc_INR_240", "2_Vegan_Burger_1_Pc_INR_320", "3_Truffle_Cake_500gm_INR_900"])
            print("Menu \n",a)
            b=eval(input("Enter choice: "))
            order.append(b)
            with open("order_history.json","w+") as f:
                json.dump(order,f)
            confirm=int(input("\n Press one to confirm"))
            if confirm==1:
                print("\n Order confirmed")
                print(a[order])
            print("You can select your choice Again")
            self.options()
        elif option==2:
            #print("Your Order History is available below: \n")
            if order is not None :
                #ds=json.loads(s)
                print(order)
                #print(" previous order history:",x)
            else:
                print("No order history")
            #print("  ",Food_items.json)
        elif option==3:
            print("You can Update your profile now :\n")
            self.edit_profile()
        elif option==4:
            print("*"*50)
            print(">>>>>>>>Thank you for visiting us<<<<<<<<")
            sys.exit()
        else:
            print("Enter the correct choice...")
            print("You can select your choice Again")
        self.options()
    def edit_profile(self):
        #food_id=int(input("Enter the Food Id to edit the item:"))
        #self.food_item[self.food_id]=self.item
        self.name = input(" Enter Name : ")
        self.email_id = input("Enter Email ID ")
        self.phone_no = int(input("Enter the Contact no. "))
        self.address = input(" Enter Address : ")
        self.password = input("Enter password: ")
        print("Thank you for updating your profile - ", self.name)
        self.user={"Name":self.name,"Email ID":self.email_id,"Contact No.":self.phone_no,"Address":self.address,"Password":self.password}
        self.user_id=len(self.user_profile)+1
        self.user_profile[self.user_id]=self.user
        with open("user_profile","w") as f:
            json.dump(self.user,f)
        print("You can select your choice Again")
        self.options()
    

c=user()
print(c.register())
print("\n\n>>>>>Welcome to Login Portal of Food Ordering App<<<<<")
emailid = input("\nEnter your Email ID:")
pass_word = input("\nEnter your password")
print(c.login(emailid,pass_word))
print(c.options())


# In[ ]:





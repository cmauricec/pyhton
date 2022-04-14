# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 19:27:06 2022

@author: Mauri
"""
global funds


funds = 1000000

def check():
    

def main():
    amount = float(input("How much are you seeking: "))
   
    if(amount <= funds):
        typ = input("what type of Equipment are you looking to buy: ")
        revenue = float(input("Annual Revenue: "))
        years = int(input("Operational years: "))
        
       
        price = float(input("Equipment price: "))
        down_payment = float(input("down_payment: "))
        #down payment needs to be 5%-20% of the equipment price 
        
        
        
        credit = int(input("Credit score: "))
        rate = 9/100 
    else: 
        print("Error")
            
main()


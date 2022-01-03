'''
@Author: Hitesh Patil

@Date: 03-01-2022 10:00:56

@Last Modified by: Hitesh Patil

@Last Modified time: 03-01-2022 12:00:00

@Title : Get ATM withdrawal by Available Stock of Notes
'''

amount=int (input("Enter Amount: "))    #available stock of notes 
notes_stock=[1000,500,100,10,1]            
notes = [0, 0, 0, 0, 0]           #setting form of notes list & 2nd inital value list 

print("\nAvailable Noteswise operation: ")  
 
##Merging two Values list  together by zip

for i, n in zip(notes_stock, notes):  #generating two vars, corresponding to the current value of each loop

    if amount >= i:               #loop will continue till amount > equal to 0 as per stock vailable for amount as per notes 
        
        n = amount // i           # doing floor division eg:2458/1000

        amount = amount - n * i   #sutracting remaining amount & calculating Notes count

        print (i ," : ", n)       #printing loop by loop noteswise operation
exit
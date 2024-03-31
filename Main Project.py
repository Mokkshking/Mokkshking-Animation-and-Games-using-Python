# The Project is made by Mokksh and Samarjeet
import time
print('WELCOME TO THE GREAT GAME BY MOKKSH AND SAMAR')
print('plz choose what you want to run')
O1 = input('Choose weather you want to run " G " for game or " A " for animation :')

n=3
for i in range(n):
    print('.')

if O1 == 'G':
    print(' Thank you for opting game section ')
    print(' we have two games available for you which one do you want to play')
    print("1)Fidget Spinner [F]")
    print("2)Snake Game [S]")
    O1_2 = input('Choose your game :')

    n=2
    for i in range(n):
        print('.')

    if O1_2 == 'F':
        import importlib
        moduleName = 'spinner(F)'
        importlib.import_module(moduleName)

    if O1_2 == 'S':
        import importlib
        moduleName = 'snake game'
        importlib.import_module(moduleName)
        

if O1 == 'A':
    print('Thank you for opting annimation section ')
    print('we have 3 Animations available for you which one do you want to See')
    print("1)Turtle Race [R]")
    print("2)Design[T]")
    print("3)heart[H]")

    O1_2 = input('Choose your game :')
    n=2
    for i in range(n):
        print('.')

    if O1_2 == 'R':
        import importlib
        moduleName = 'turtle race(F)'
        importlib.import_module(moduleName)

    if O1_2 == 'T':
        import importlib
        moduleName = 'A1'
        importlib.import_module(moduleName)
            
    if O1_2 == 'H':
        import importlib
        moduleName = 'heart(F)'
        importlib.import_module(moduleName)
      
        
    
        
        
        
         

        

      
        
        



    
        


        

    


    
    




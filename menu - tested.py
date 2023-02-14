from os import system, name

def clear():
  if name == 'nt':
    _ = system("cls")
  else:
    _ = system("clear")
  print("""
  WRONG CHOICE! 
  Please choose correct number!
  *****************************""")

def get_menu_option():
  
  menu_option = int(input("""  Choose your game option \u2193
  -------------------------
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI
  Your choice: """))
  
  if menu_option < 1 or menu_option > 4:
    clear()
    get_menu_option()
  else:
    return menu_option
 
if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print("If the user selected 1, it should print 1")
    print(option)   
  

  

  
   
  
 

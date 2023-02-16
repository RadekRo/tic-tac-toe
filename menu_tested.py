from os import system, name

def clear():
  if name == 'nt':
    _ = system("cls")
  else:
    _ = system("clear")

def get_menu_option():
  show_error_msg = 0
  while True:
    clear()
    if show_error_msg == 1:
      print("""  INPUT ERROR. WRONG CHOICE!
  You can choose only from numbers between 1 and 4!
  *************************************************
      """)
    menu_option = int(input("""  Choose your game option \u2193
  -------------------------
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI
  Your choice: """))
  
    if menu_option > 0 and menu_option < 5:
      return menu_option
    else:
      show_error_msg = 1

if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print("If the user selected 1, it should print 1")
    print(option)   
  

  

  
   
  
 

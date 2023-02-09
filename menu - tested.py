from os import system, name
def clear():
  if name == 'nt':
    _ = system("cls")
  else:
    _ = system("clear")

def get_menu_option(msg):
  if msg != "":
    print(msg)
  menu_option = int(
    input("""choose your game option
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI
: """))
  if  menu_option < 1 or menu_option > 4:
   clear()
   get_menu_option("please choose correct number")

  else:
    return get_menu_option("") 
  
get_menu_option("")
  
  

  

  
   
  
 

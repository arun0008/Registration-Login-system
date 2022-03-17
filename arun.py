import re 
login = []
register = []
pw = []

mail = "^[a-z-A-Z-0-9]+@+[gmail-yahoo]+.com"

while True:
  register=input('Register\n Email/Username: ')
  if re.match(mail,register):
    break
    
  else:
    print("Not a valid Email/Username, should contain '@' and end with gmail.com/yahoo.com")


while True:
  pw = input('Password: ')
  SpecialSym ="^['$', '@', '#', '%']"

  if len(pw) <5:
    print("Length should not be less than 5 characters")
    val=False

  if len(pw) >16:
    print("Length should not be greater than 16")
    val=False

  if not any(char.isdigit() for char in pw):
    print('Password should have at least one numeral')
    val = False
          
  if not any(char.isupper() for char in pw):
    print('Password should have at least one uppercase letter')
    val = False
          
  if not any(char.islower() for char in pw):
    print('Password should have at least one lowercase letter')
    val = False
          
  if not any(char in SpecialSym for char in pw):
    print('Password should have at least one of the symbols $@#')
    val = False
  
  if re.match(SpecialSym,pw):
    print("Successfully Registered!!")
    continue
    
  else:
    break

def main():               # saving password in file
  pw = 'Doubble@#123'
  
  if (pw_check(pw)):
    print("Password is valid")
  else:
    print("Invalid Password !!")

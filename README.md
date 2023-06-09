# redi
Welcome to the Project named "SMART CALCULATOR NIK"
The aim to make this project is to do mathematical operations based on user input.
the program takes text based input which should contain an operation ans two operand, opeartion can be HCF,LCM,SUBTRACTION,MULTIPLICATION,ADDITION AND DIVIDE.
to get answer we are utilising  dict data type to get a valid operation.
operations ={"PLUS":add,"ADDITION":add,"SUM":add,"ADD":add,"MINUS":sub,"SUBTRACTION":sub,"SUB":sub,"MULTIPLY":multiply,"MULTIPLICATION":multiply,"DIVIDE":divison,"LCM":lcm,"LOWEST COMMON MULTIPLE":lcm,"HCF":hcf,"HIGHEST COMMON FACTOR":hcf}
commands = {"NAME":myname,"END":end,"EXIT":end,"close":end}
if user input contains a text which matches any of the key from opearions dict, a corresponding function for value of the matched key choosen.
operand are extracted and result of the opration is printed.
incase of any unexpected input either the program exit or will ask user to reinter the input.
if incase of a user input contains any words like exit end then program is exited.



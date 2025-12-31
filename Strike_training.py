import random
import os 

def clear_scren():
   """خاصية تنظيف الشاشة مدعومة في كل من أجهزة ميكروسوفت والأنظمة المعتمدة على نواة لينكس."""
   os.system("cls" if os.name == "nt" else "clear")

def acceptition_input(user_input):
   """دالة تحقق من المدخل"""
   correct_entry=True
   otput=()
   special_word=["clear","exit","info",]
   if (user_input not in special_word) and (not user_input.isdigit()):
      Correct_entry=False
      otput=(user_input,correct_entry)
   return otput
while True:
	x=random.randint(0,10)
	y=random.randint(0,10)
	print(f"{x} x {y}")
	result=x*y
	user_answer=acceptition_input(input(">>>"))
	if user_answer == str(result):
		print ("you win...✅ ")
	elif user_answer== "exit":
		break
	elif user_answer== "info":
		print("قم بالإجابة بالرقم الصحيح فقط.")
	elif user_answer == "clear":
		clear_scren()
	else :
		correct_answer=str(x*y) + "="+ str(x) +"x"+ str(y) 
		print(correct_answer,"❌قد أخطأت ..." )
		print("___________")


#لا داعي لقول هذا لكن قراءة الكود يبدء من فهم المنطق و قراءة الأسطر التنفيذية انتقالا للدوال و فهم عملها 
import random
import  os
#___________متغيرات و دوال أساسية ___________
CARDS=[2,3,4,5,6,7,8,9,10,"A","Q","J","K"]
TANS=["Q","K","J"]
#====دوال=========
def Give_card():#سحب بطاقة
   return  random.choice(CARDS)
#----
def clear_screen():#تنظيف شاشة 
   os.system("clear")
#___________دوال مرحلة اولى____________________________________
def evaluate_initial_hand(list_of_cards):#تمرر قائمة مكونة من بطاقتين 
   new_list=[]
   for x in list_of_cards:
      new_card=10 if x in TANS  else x  
      new_list.append(new_card)#["K" ,4]→[10,4] | "A"→"A"
   if "A" in new_list:
      if "A" == new_list[0] and "A" == new_list[1]:
         new_list=[12]#["A","A"]→[12]
      elif new_list.index("A")==0:#اكبر يسار أصغر يمين
         new_list=[new_list[1]+11,new_list[1]+1]#["A",1]→[12,2]
      else: 
         new_list=[new_list[0]+11,new_list[0]+1]#[1,"A"]→[12,2]
   return  new_list
#----
def first_displayP(list_of_numbers,list_of_cards):
   if "A" in list_of_cards and len(list_of_numbers)>1:
        return str(list_of_numbers[0])+"/"+str(list_of_numbers[1])
   else:
      return str(sum(list_of_numbers))#مخرج دائما str 
#----
def first_displayR(first_numbersR,cards_robot):
   if "A"in cards_robot:
      if cards_robot.index("A")==0:
           otput= "11/1"
      else:
           otput= str("10" if cards_robot[0] in TANS  else cards_robot[0] )
   else: 
      otput= str(first_numbersR[0])#مخرج دائما str 
   return  otput
      
#__________دوال مخصصة للمرحلة الثانية_______________
def second_displayR(list_of_cards,list_of_numbers):
     if "A" in list_of_cards:
        otput=list_of_numbers[0]#[a,b]→a: أكبر رقم في قائمة الأرقام 
     else:
        otput=sum(list_of_numbers)#[g,h]→g+h
     return str(otput)#int→str
   
#______________دوال مخصصة للمرحلة الثالثة الجزء الأول __________
def display_numbersP(list_of_cards,numbers_str):
   resolution=True #في حالة انفجار مجموع اللاعب تصبح False
   otput=""#مخرج
   new_list=[]#قائمة تم تحويل قيم KJQ
   list_only_numbers=[]#قائمة تملك فقط ارقام 
   for card in list_of_cards:#تحول KJQ الى 10 من نوع int 
      card_update= 10 if card in TANS else card
      new_list.append(card_update)
   for card2 in new_list:#تختار فقط ارقام للقائمة المستهدفة 
      if card2 != "A":
         list_only_numbers.append(card2)
         
   if sum(list_only_numbers)== 0:#كل البطاقاتA
      otput=str(12+(len(new_list)-2))
   elif "/" in numbers_str and new_list[-1]== "A":#كان A سابقا أو لم يكن و لدينا A 
      smallest_value=int(numbers_str.split("/")[0])
      otput=str(smallest_value+1)
   elif "/" in numbers_str:#كان A سابقا او لم يكن وحصلنا على بطاقة ثابتة 
      large_namber=int(numbers_str.split("/")[0])#رقم أكبر]
      smal_number=int(numbers_str.split("/")[1])#رقم اصغر 
      fixed_number=new_list[-1]#اخر بطاقة 
      if (large_namber+fixed_number)<=21:
         otput=str(large_namber+fixed_number)+"/"+str(smal_number+fixed_number)
      else:
         otput=str(smal_number+fixed_number)
   elif "/" not in numbers_str and new_list[-1]== "A" :#لا خيارات سابقا و حصلنا على A 
      number1=int(numbers_str)+1
      number2=int(numbers_str)+11 
      if number2<=21:
         otput=str(number1)+"/"+str(number2)
      else:
         otput=str(number1)
   elif "/" not in numbers_str :#لا خيارات سابقا و حصلنا على رقم ثابت 
     fixed_number=new_list[-1] 
     otput= str(int(numbers_str)+fixed_number)
   
   if int(otput.split("/")[-1]) > 21:
      otput=str(int(otput.split("/")[-1]))
      resolution=False #انفجرت القيم 
   if "21" in otput:
      otput="21" #الاعب حصل على 21  
   return (otput,resolution)

#==========================مرحلة أولى==================================
cards_robot=[Give_card(),Give_card()]#بطاقات الروبوت 
cards_player=[Give_card(),Give_card()]#بطاقات اللاعب 
numbersR=evaluate_initial_hand(cards_robot)#قائمة أرقام  او رقم 12
numbersP=evaluate_initial_hand(cards_player)#قائمة أرقام او رقم 12 

for_desplay_numbersR1=first_displayR(numbersR,cards_robot)#مخصص للطباعة 
for_desplay_numbersP1=first_displayP(numbersP,cards_player)#مخصص للطباعة +مجموع مرحلة ثالثة جزء 1 
number_for_desplayP=for_desplay_numbersP1#تهيئة للمرحلة الثالثة جزء1 
repitation=True#تهيئة للوب المرحلة الثالثة الجزء 1 
print(f"The robot has : [{cards_robot[0]},??] and is {for_desplay_numbersR1}")
print(f"You  have : {cards_player} and is {for_desplay_numbersP1}")
#===============مرحلة ثانية=======================================
if 21 in numbersP:
   clear_screen()
   second_numberR=second_displayR(cards_robot,numbersR)
   print(f"The robot has : {cards_robot} and is {second_numberR}")
   print(f"You  have : {cards_player} and is 21 ")
   results="You win"if int(second_numberR)!=21 else "Draw"#نتيجة مباراة
   print(results)
#===============مرحلة ثالثة ======================================
#==========مرحلة ثالثة = جزء أول====================================
else:
    while repitation:
      user_choice= input("Do you need to hant or stop [h/s..]:").lower()== "h"#يحفظ bool
      if not user_choice:#إذا لم يدخل h 
         repitation=False
         explosion=False #انفحار اللاعب 
         continue
      if user_choice:#حالة قبول سحب 
        cards_player.append(Give_card())
        info_and_repitition= display_numbersP(cards_player,number_for_desplayP)
        number_for_desplayP=info_and_repitition[0]
        print(f"You  have : {cards_player} and is {number_for_desplayP} ")
        repitation=info_and_repitition[1]
        explosion=repitation#انفجار اللاعب
      else:#حالة رفض السحب 
         print("good it's work  ")
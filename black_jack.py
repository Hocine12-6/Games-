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

#==========================مرحلة أولى====================°°°°°°°°°°°°°°°
cards_robot=[Give_card(),Give_card()]#بطاقات الروبوت 
cards_player=[Give_card(),Give_card()]#بطاقات اللاعب 
numbersR=evaluate_initial_hand(cards_robot)#قائمة أرقام  او رقم 12
numbersP=evaluate_initial_hand(cards_player)#قائمة أرقام او رقم 12 

for_desplay_numbersR=first_displayR(numbersR,cards_robot)#مخصص للطباعة 
for_desplay_numbersP=first_displayP(numbersP,cards_player)#مخصص للطباعة 


print(f"The robot has : [{cards_robot[0]},??] and is {for_desplay_numbersR}")
print(f"You  have : {cards_player} and is {for_desplay_numbersP}")
#===============مرحلة ثانية=======================================
if 21 in numbersP:
   clear_screen()
   second_numberR=second_displayR(cards_robot,numbersR)
   print(f"The robot has : {cards_robot} and is {second_numberR}")
   print(f"You  have : {cards_player} and is 21 ")
   results="You win"if int(second_numberR)!=21 else "Draw"
   print(results)
#===============مرحلة ثالثة ======================================
def desplay_numbersP(list_of_cards):
   new_list=[]
   for card in list_of_cards:
      card_update= 10 if card in TANS else card
      new_list.append(card_update)
      
#==========مرحلة ثالثة = جزء أول====================================
else :
   user_choice= input("Do you need ro hant or stop [h/s..]:").lower()== "h"#يحفظ bool
   if user_choice:#حالة قبول سحب 
#ملاحظة مؤقتة تأتي البطاقات من الشطل الخام و المطلوب حسابها تكون من الشكل list فيها حروف و ارقام حسب الحالة او ارقام فقط 
      cards_player.append(Give_card())
      number_for_desplayP=0
      print(f"You  have : {cards_player} and is عدد ")
      
   else:
      print("good it's work  ")
      
      
      
      
      
      
      
import random
import  os
#___________متغيرات و دوال أساسية ___________
CARDS=[2,3,4,5,6,7,8,9,10,"A","Q","J","K"]
def Give_card():#سحب بطاقة
   return  random.choice(CARDS)
#----
def clear_screen():#تنظيف شاشة 
   os.system("clear")
#___________دوال مرحلة اولى____________________________________
def evaluate_initial_hand(list_of_cards):#تمرر قائمة مكونة من عنصرين 
   new_list=[]
   for x in list_of_cards:
      new_card=10 if x=="J" or x=="K" or x=="Q"  else x  
      new_list.append(new_card)
   if "A" in list_of_cards:
      if "A" == list_of_cards[0] and "A" == list_of_cards[1]:
         new_list=[12]
      elif new_list.index("A")==0:#اكبر يمين أصغر يسار 
         new_list=[new_list[1]+11,new_list[1]+1]
      else:#اكبر يمين أصغر يسار 
         new_list=[new_list[0]+11,new_list[0]+1]
   return  new_list#مخرج يكون قائمة فيها أرقام أو رقم حسب الحال  
#----
def first_nambers_printP(list_of_nambers,list_of_cards):
   if "A" in list_of_cards and len(list_of_nambers)>1:
        return str(list_of_nambers[0])+"/"+str(list_of_nambers[1])
   else:
      return str(sum(list_of_nambers))#مخرج دائما str 
#----
def first_nambers_printR(first_nambersR,cards_robot):
   if "A"in cards_robot:
      if cards_robot.index("A")==0:
           return "11/1"
      else:
           return str("10" if cards_robot[0] == "J" or cards_robot[0] == "K" or cards_robot[0] == "Q"  else cards_robot[0] )
   else: 
      return str(first_nambersR[0])#مخرج دائما str 
#==========================مرحلى أولى===========
cards_robot=[Give_card(),Give_card()]#متغير عام يستعامل في المرحلة الثانية 
cards_player=[Give_card(),Give_card()]#متغير عام يستخدم في المرحلة الثانية
first_nambersR=evaluate_initial_hand(cards_robot)#قائمة أرقام 
first_nambersP=evaluate_initial_hand(cards_player)#قائمة أرقام 

first_nambersR=first_nambers_printR(first_nambersR,cards_robot)#مخصص للطباعة 
for_nambersP=first_nambers_printP(first_nambersP,cards_player)#مخصص للطباعة 


print(f"The robot has : [{cards_robot[0]},??] and is {first_nambersR}")
print(f"You  have : {cards_player} and is {for_nambersP}")
#=================نهاية المرحلة الأولى و بداية مرحلة التقرير و السحب ==========

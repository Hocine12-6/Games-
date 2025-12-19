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
def evaluate_initial_hand(list_of_cards):#تمرر قائمة مكونة من بطاقتين 
   new_list=[]
   for x in list_of_cards:
      new_card=10 if x=="J" or x=="K" or x=="Q"  else x  
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
cards_robot=[Give_card(),Give_card()]#متغير يستخدم  في المرحلة الثانية 
cards_player=[Give_card(),Give_card()]#متغير يستخدم في المرحلة الثانية
first_nambersR=evaluate_initial_hand(cards_robot)#قائمة أرقام  او رقم 12
first_nambersP=evaluate_initial_hand(cards_player)#قائمة أرقام او رقم 12 

for_nambersR=first_nambers_printR(first_nambersR,cards_robot)#مخصص للطباعة 
for_nambersP=first_nambers_printP(first_nambersP,cards_player)#مخصص للطباعة 


print(f"The robot has : [{cards_robot[0]},??] and is {for_nambersR}")
print(f"You  have : {cards_player} and is {for_nambersP}")
#=================نهاية المرحلة الأولى و بداية مرحلة التقرير و السحب ==========
#__________دوال مخصصة للمرحلة الثانية_______________
def robot_second_display(list_of_cards,list_of_nambers):
     if "A" in list_of_cards:
        otput=list_of_nambers[0]
     else:
        otput=sum(list_of_nambers)
     return str(otput)
   
#===============مرحلة ثانية=======================================
if 21 in first_nambersP:
   clear_screen()
   second_namberR=robot_second_display(cards_robot,first_nambersR)
   print(f"The robot has : {cards_robot} and is {second_namberR}")
   print(f"You  have : {cards_player} and is 21 ")
   results="You win"if int(second_namberR)!=21 else "Draw"
   print(results)
else :
   print()
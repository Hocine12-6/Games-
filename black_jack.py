#ملاحظات :
   #ارقام العرض تعتبر أرقام المجموع 
    #اكبر يسار أصغر يمين
import random
import  os
#___________متغيرات و دوال أساسية ___________
CARDS= [2,3,4,5,6,7,8,9,10,"A","Q","J","K"]*4
TANS=["Q","K","J"]
#====دوال=========
def Give_card():#سحب بطاقة
   return  random.choice(CARDS)
#----
def clear_screen():#تنظيف شاشة 
   os.system("cls" if os.name== "nt" else "clear")
#_____متغيرات هامة_________________
explosionP=False 
explosionR=False
#___________دوال مرحلة اولى____________________________________
def two_card_numbers(list_of_cards):#تمرر قائمة مكونة من بطاقتين 
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
   return  new_list #تعيد قائمة أرقام 
#----
def display_for2card(list_of_numbers,list_of_cards):#@
   if "A" in list_of_cards and len(list_of_numbers)>1:
        return str(list_of_numbers[0])+"/"+str(list_of_numbers[1])
   else:
      return str(sum(list_of_numbers))#مخرج دائما str 
#----
def first_display_numbersR(first_numbersR,cards_robot):
   if "A"in cards_robot:
      if cards_robot.index("A")==0:
           otput= "11/1"
      else:
           otput= str("10" if cards_robot[0] in TANS  else cards_robot[0] )
   else: 
      otput= str(first_numbersR[0])#مخرج دائما str 
   return  otput #تعيد قيمة اول بطاقة فحسب 
      
#__________دوال مخصصة للمرحلة الثانية_______________
def second_displayR(list_of_cards,list_of_numbers):#حالة حسم يد من بطاقتين 
     if "A" in list_of_cards:
        otput=list_of_numbers[0]#[a,b]→a: أكبر رقم في قائمة الأرقام 
     else:
        otput=sum(list_of_numbers)#[g,h]→g+h
     return str(otput)#int→str
   
#______________دوال مخصصة للمرحلة الثالثة الجزء الأول __________
def after_total2card(list_of_cards,numbers_str):
   control_loop=True #في حالة انفجار مجموع اللاعب تصبح False
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
      smal_number=int(numbers_str.split("/")[-1])
      large_number=int(numbers_str.split("/")[0])
      if large_number+11 >21 and large_number+1  <= 21:
         otput =str(large_number+1) +"/"+str(smal_number+1)
      elif large_number+11 <= 21:
         otput= str(large_number+11)+"/"+str(smal_number+11)
   elif "/" in numbers_str:#كان A سابقا او لم يكن وحصلنا على بطاقة ثابتة 
      large_namber=int(numbers_str.split("/")[0])#رقم أكبر]
      smal_number=int(numbers_str.split("/")[1])#رقم اصغر 
      fixed_number=new_list[-1]#اخر بطاقة 
      if (large_namber+fixed_number)<=21:
         otput=str(large_namber+fixed_number)+"/"+str(smal_number+fixed_number)
      else:
         otput=str(smal_number+fixed_number)
   elif "/" not in numbers_str and new_list[-1]== "A" :#لا خيارات سابقا و حصلنا على A 
      large_namber=int(numbers_str)+11#أكبر رقم 
      smal_number=int(numbers_str)+1 # أصغر رقم 
      if large_namber<=21:#لم ينفجر 
         otput=str(large_namber)+"/"+str(smal_number) #أكبر يسار أصغر يمين 
      else:
         otput=str(smal_number)
   elif "/" not in numbers_str :#لا خيارات سابقا و حصلنا على رقم ثابت 
     fixed_number=new_list[-1] 
     otput= str(int(numbers_str)+fixed_number)
   
   if int(otput.split("/")[-1]) > 21:#إذا انفجرت القيم 
      otput=str(int(otput.split("/")[-1]))
      control_loop=False #انفجرت القيم تعيد False 
   elif  "21" in otput:
      otput="21" #الاعب حصل على 21  
   return (otput,control_loop)
#______________دوال مخصصة للمرحلة الثالثة الجزء الثاني__________
#إعادة إستخدام للدوال السابقة 
#==========================مرحلة أولى==================================
cards_robot=[Give_card(),Give_card()]#بطاقات الروبوت 
cards_player=[Give_card(),Give_card()]#بطاقات اللاعب 
numbers_first2cardR=two_card_numbers(cards_robot) 
numbers_first2cardP=two_card_numbers(cards_player) 

for_desplay_numbersR1=first_display_numbersR(numbers_first2cardR,cards_robot)
for_desplay_numbersP1=display_for2card(numbers_first2cardP,cards_player)

print(f"The robot has : [{cards_robot[0]},??] and is {for_desplay_numbersR1}")
print(f"You  have : {cards_player} and is {for_desplay_numbersP1}")
#===============مرحلة ثانية=======================================
if 21 in numbers_first2cardP:
   clear_screen()
   second_numberR=second_displayR(cards_robot,numbers_first2cardR)
   print(f"The robot has : {cards_robot} and is {second_numberR}")
   print(f"You  have : {cards_player} and is 21 ")
   results="You win"if int(second_numberR)!=21 else "Draw"#نتيجة مباراة
   print(results)
#==========مرحلة ثالثة = جزء أول====================================
else:
    number_str_P2=for_desplay_numbersP1
    final_total_numbersP=number_str_P2.split("/")[0]
    repitation=True 
    repitation2=True
    
    while repitation:
      stop= input("Do you need to hant or stop [h/s..]:").lower()!= "h"#يحفظ bool
      if stop:#إذا لم يدخل h 
         repitation=False #ايقاف اللوب 
         explosionP=False #عدم انفجار اللاعب  
         continue
      else:#حالة قبول سحب (إدخال h)
        cards_player.append(Give_card())
        info_and_repitition= after_total2card(cards_player,number_str_P2)
        number_str_P2=info_and_repitition[0]
        final_total_numbersP=number_str_P2
        print(f"You  have : {cards_player} and is {number_str_P2} ")
        repitation=info_and_repitition[1]
        explosionP= not repitation#تقرير انفجار اللاعب
        if "21" == number_str_P2 :
          break

#==========مرحلة ثالثة = جزء ثاني====================================
    if "21" == number_str_P2:#حصول اللاعب على 21
       final_total_numbersR=display_for2card(numbers_first2cardR,cards_robot).split("/")[0]
 
    elif explosionP:#إنفجار قيم اللاعب 
       final_total_numbersR=display_for2card(numbers_first2cardR,cards_robot).split("/")[0]
       
    else:#حالة عادية أي لم يحصل 21 و لم تنفجر قيمه و لكن أوقف السحب يدويا 
       final_total_numbersR=display_for2card(numbers_first2cardR,cards_robot)
       while True :
          cards_robot.append(Give_card())
          info_and_explosion=after_total2card(cards_robot,final_total_numbersR)
          final_total_numbersR=info_and_explosion[0]
          explosionR=not info_and_explosion[-1]
          if int(final_total_numbersR.split("/")[-1]) >=17 :
             break
#==================مرحلة رابعة =======================================

    final_total_numbersP=final_total_numbersP.split("/")[0]
    final_total_numbersR=final_total_numbersR.split("/")[0]
    clear_screen()
    print(f"The robot : {cards_robot} and is {final_total_numbersR}")
    print(f"You have : {cards_player} and is {final_total_numbersP}")
    if explosionP and explosionR:#إنفجار كلا من اللاعب و الروبوت 
       print("Draw")
    elif explosionP:#انفحار اللاعب فقك 
       print("The robot win")
    elif explosionR:#إنفجار الروبوت فقط 
       print("You win")
    else:#حالة عادية
       if final_total_numbersP==final_total_numbersR:#إذا كانت القيم متادساوية 
          print("Draw")
       elif int(final_total_numbersP)>int(final_total_numbersR):#إذا كانت قيم اللاعب أكبر 
          print("You win")
       else:#إذا كانت قيم الروبوت أكبر
          print("The robot win")
          
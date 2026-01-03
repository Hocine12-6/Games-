import random
import os 
import  time 

additions={"info":"لعرض تعليمات تصويب المدخلات",
                  "exit": "للخروج من البرنامج" ,
                  "clear":"لتنظيف الشاشة",
                  "help":"لعرض قائمة ضرب مساعدة",
                  "limits":"لتغيير حدود الإختيار العشوائي لـ x و y "
                  }
good_jobtxt= ["عمل جيد " ,"أنت أسطورة ","ممتاز"]

def clear_screen():
   """خاصية تنظيف الشاشة مدعومة في كل من أجهزة ميكروسوفت والأنظمة المعتمدة على نواة لينكس."""
   os.system("cls" if os.name == "nt" else "clear")

def show_additions():
   """عرض الإظافات"""
   for addi in additions:
        print("إدخال " + addi, additions[addi])

def input_errur(answer):#مدخل خاطئ
            """عرض رسالة خطأ """
            print(f"{Color.RED}المدخل '{answer}' غير صحيح .")
            print(f"\n -يرجى إستعمال info لعرض الخيارات المتوفرة{Color.END}")

def help_extintion():
     """عرض قائمة ضرب محددة"""
     clear_screen()
     number_for_help = input("-Enter a number :")
     if number_for_help.isdigit():
         for r in range(11):
             print(f" {Color.CYAN}{number_for_help}x{r}= {int(number_for_help)*r}")
         print(Color.END+"_________")
     else:
        print(f"{Color.RED}input error \n<<{number_for_help}>> is not a number{Color.END}")
            
def change_limits_extantion(target_str , now_limit_start,now_limit_end):#دالة تغيير قيمة محددة 
   """تستعمل لتغيير الأرقام العشوائية التي ستختار"""
   limits={"new_limit_start":now_limit_start,
   "new_limit_end":now_limit_end}
   
   print("----الحدود هي القيم التي يمكن أن تظهر للمستخدم في العملية--- ")
   print("____________")
   print(f"{now_limit_start}→..→ {now_limit_end}")
   print("Æ1→..→ Æ2")
   print("____________")
   print("",("Æ x Y = " if target_str=="x" else "X x Æ  =")+"####")
   
   for limit in limits.keys():        
        while True :
             new_limit=input(f"-يرجى إدخال الحد الجديد ليوضع مكان {limits[limit]}:")
             if not new_limit.isdigit():
                print(f"{Color.RED} يبدو أن مدخلك غير صحيح {Color.END}")
                continue
             else:
                limits[limit]=int(new_limit)
             if limits[limit] in [0,1]:
                  limits[limit]=2
                  print("  تم تحديد الحد تلقائيا على أنه2")
                  print("يا صاح من يضع 0 أو 1 ليتدرب عليها؟")
             else:
                 print(f"تم تحديد الحد الجديد على أنه {new_limit}")
             break

   input("إضغط على انتر للمتابعة...")
   new_limit_start=limits["new_limit_start"]
   new_limit_end=limits["new_limit_end"]
   if new_limit_start ==new_limit_end:
      new_limit_end=new_limit_end+2
      print(f"قيم بداية و نهاية متساوية تم تحديد اخر قيمة {new_limit_end}")
   elif new_limit_end<new_limit_start:
      number_start=new_limit_start
      number_end=new_limit_end
      new_limit_start=number_end
      new_limit_end=number_start
      print("قيم البداية أكبر من قيم النهاية ")
      print("تم تغيير البداية و النهاية")
   return  new_limit_start,new_limit_end

   
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    INVERT="\033[7m"

def main():
    start_x=0
    start_y=0
    limit_x=5
    limit_y=10

    while True:
        x = random.randint(start_x, limit_x)
        y = random.randint(start_y, limit_y)
        print(f" {x} x {y}", end="")
        start_time = time.time()
        result = x * y
        answer = input(" = ").strip()

        if (not answer.isdigit()) and (answer not in additions): #حالة مدخل خاطئ 
           input_errur(answer)
           
        elif answer == str(result): #حالة اجابة صحيحة
            print(random.choice(good_jobtxt))
            end_time = time.time()
            result_time = round(end_time - start_time, 2)
            print(f"الوقت المستغرق للإجابة : {result_time} ثانية")

        elif answer == "exit": #خروج
            break

        elif answer == "info": #مساعدة 
            print("تعليمات إستخدام البرانامح :")
            print("-قم بالإجابة بالرقم الصحيح للعملية .")
            print("الإضافات:")
            show_additions()

        elif answer == "clear":
            clear_screen()

        elif "help" == answer: #طباعة قائمة ضرب رقم محدد  حتى 10 
             
             help_extintion()
             continue

        elif answer == "limits":#تغيير الحدود 
           clear_screen()
           change_x=change_limits_extantion("x",start_x,limit_x)
           change_y=change_limits_extantion("y",start_y,limit_y)
           start_x=change_x[0]
           limit_x=change_x[1]
           start_y=change_y[0]
           limit_y=change_y[1]
           clear_screen()
        else:
            correct_operition = f'{x}x{y} = {x*y}'
            print(" خطأ ...")
            print(f"<<{Color.GREEN+Color.INVERT}{correct_operition}{Color.END}>>")
            print("___________")

main()
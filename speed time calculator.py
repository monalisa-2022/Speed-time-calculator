from time import*
import random as r

#mistake() will detect mistakes occured while typing
def mistake(paratest,usertest):
    error=0
    for i in range(len(paratest)):
        try:
            if paratest[i]!= usertest[i]:
                error=error+1
        except:
            error=error+1
    return error


#speed_time() will calculate time of typing speed
def speed_time(starttime,endtime,userinput):
    delaytime=endtime-starttime
    roundoftime=round(delaytime,2)
    speed=len(userinput)/roundoftime
    return round(speed)

while True:
    ck=input("ready for test:yes/no:")
    if ck=="yes":



        paragraph=["In Java, virtual functions are achieved through method overriding",
                   " which is a fundamental concept in object-oriented programming. "
             "When a subclass defines a method with the same signature as a method in its superclass",
                   "it overrides the superclass method." ,
             " This allows Java to achieve runtime polymorphism, where the actual method that" ,
             " Gets called is determined at runtime based on the type of the object." ,
            "Data structures are applied extensively in areas such as software development, database management, algorithm design, "
            "networking, artificial intelligence, and system optimization."]

        test1=r.choice(paragraph)
        print("     *********TYPING SPEED********     ")
        print(test1)
        print()
        print()
        time1= time()
        user_input=input("Start test: ")
        time2= time()
        print("SPEED:  ", speed_time(time1,time2,user_input),"w/sec")
        print("ERROR:" ,  mistake(test1,user_input))

    elif ck=='no':
        print("THANK YOU")
        break

    else:
        print("WRONG INPUT")



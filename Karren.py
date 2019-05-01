#Codoffee-karren:---------------------------------------------------------------
import os
import time
import playsound
import random
import wikipedia
import speech_recognition as sr
from gtts import gTTS
from datetime import datetime
from weather import Weather, Unit
from threading import Thread
#showing info:------------------------------------------------------------------
print("Codoffee Karren V1.3 :)")
print("(c) 2018 Codoffee Inc. | All rights reserved.")
#reading ArriveDB:--------------------------------------------------------------
file=open("DBs/db1.db","r")
v1=file.read()
file.close()
file=open("DBs/db2.db","r")
manorwoman=file.read()
file.close()
playsound.playsound('Codoffee Audio.mp3', True)
now=datetime.now()
times=int("%s"%(now.hour))
ran=random.randint(1,6)
if(ran==1):
   playsound.playsound(manorwoman+'//hello.mp3', True)
elif(ran==2):
   playsound.playsound(manorwoman+'//havegoodday.mp3', True)
elif(ran==3):
   if(times>=3)and(times<10):
      playsound.playsound(manorwoman+'//gmor.mp3', True)
   if(times>=10)and(times<20):
      playsound.playsound(manorwoman+'//gasr.mp3', True)
   if(times>=20)and(times<24):
      playsound.playsound(manorwoman+'//gnight.mp3', True)
elif(ran==4):
   playsound.playsound(manorwoman+"//hellosir.mp3")
elif(ran==5):
   playsound.playsound(manorwoman+"//happytoseeyou.mp3")
elif(ran==6):
   playsound.playsound(manorwoman+"//dontired.mp3")
#progress Start:----------------------------------------------------------------
if(v1=="not"):
   playsound.playsound(manorwoman+"//salam.mp3")
   file=open("DBs/db1.db","w")
   v1=file.write("")
   file.close()
while True:
   try:
        m=input("\n<< ")
        if(m==""):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("\nSTT <<",end=" ")
                playsound.playsound(manorwoman+"//say.mp3")
                audio = r.listen(source)   
            try:
                m=r.recognize_google(audio,language="fa")
                print(m)
            except:
                playsound.playsound(manorwoman+"//error.mp3")
#conversation:------------------------------------------------------------------
        if("سلام"in m.lower()):
            ran=random.randint(1,3)
            if(ran==1):
               playsound.playsound(manorwoman+'//hello.mp3', True)
            elif(ran==2):
               playsound.playsound(manorwoman+'//havegoodday.mp3', True)
            elif(ran==4):
               playsound.playsound(manorwoman+"//hellosir.mp3")
        elif(m=="شما"):
            playsound.playsound(manorwoman+"//salam.mp3")
        elif("چطوري" in m.lower())or("حالت چطور است" in m.lower())or("خوبي" in m.lower())or("حالت چطوره" in m.lower())or("خوبی" in m.lower())or("چطوری" in m.lower()):
            playsound.playsound(manorwoman+"//howareyou.mp3")
        elif("خروج" in m.lower())or("خارج" in m.lower())or("خداحافظ" in m.lower())or("بعدا ميبينمت" in m.lower())or("بعدا میبینمت"in m.lower()):
            print(">> .خروج از نرم افزار در 3 ثانيه آغاز شد")
            playsound.playsound(manorwoman+"//exitin3.mp3")
            playsound.playsound(manorwoman+"//3.mp3")
            time.sleep(0.5)
            playsound.playsound(manorwoman+"//2.mp3")
            time.sleep(0.5)
            playsound.playsound(manorwoman+"//1.mp3")
            time.sleep(0.5)
            if("صلوات" in m):
                playsound.playsound(manorwoman+"//sal.mp3")
            ran=random.randint(1,2)
            if(ran==1):
               playsound.playsound(manorwoman+"//seeyouagain.mp3")
            else:
               playsound.playsound(manorwoman+"//goodbye.mp3")
            os.startfile("close.cmd")
        elif("صلوات" in m.lower()):
           playsound.playsound(manorwoman+"//sal.mp3")
        elif(("خر" in m.lower()) or ("گاو" in m.lower()) or ("ابله"in m.lower()) or ("کودن" in m.lower()) or ("خنگول" in m.lower())or ("بیشعور"in m.lower())or ("نادون"in m.lower())or ("نادان"in m.lower())or ("کلنگ"in m.lower())or ("دراز"in m.lower())or ("نفهم"in m.lower())or ("احمق"in m.lower())or ("عوضی"in m.lower())or ("خنگ"in m.lower()))or ("اسکل"in m.lower())or ("حسیبی"in m.lower())or ("کریمی"in m.lower()):
           a=random.randint(0,4)
           if(a==1):
              playsound.playsound(manorwoman+"//khodeti.mp3")
           if(a==2):
              playsound.playsound(manorwoman+"//kheng.mp3")
           if(a==3):
              playsound.playsound(manorwoman+"//biadab.mp3")
#system.com:--------------------------------------------------------------------
        elif("خاموش" in m.lower()):
            print(">> .خاموش کردن دستگاه در 3 ثانيه آغاز شد")
            playsound.playsound(manorwoman+"//laptopshut3.mp3")
            playsound.playsound(manorwoman+"//3.mp3")
            time.sleep(0.5)
            playsound.playsound(manorwoman+"//2.mp3")
            time.sleep(0.5)
            playsound.playsound(manorwoman+"//1.mp3")
            time.sleep(0.5)
            if("صلوات" in m):
                playsound.playsound(manorwoman+"//sal.mp3")
            os.system("shutdown /p")
        elif("راه اندازي" in m.lower())or("راه اندازی"in m.lower()):
            print(">> .راه اندازي مجدد دستگاه در 3 ثانيه آغاز شد")
            playsound.playsound(manorwoman+"//restart3.mp3")
            playsound.playsound(manorwoman+"//3.mp3")
            time.sleep(0.5)
            playsound.playsound(manorwoman+"//2.mp3")
            time.sleep(0.5)
            playsound.playsound(manorwoman+"//1.mp3")
            time.sleep(0.5)
            if("صلوات" in m):
                playsound.playsound(manorwoman+"//sal.mp3")
            os.system("shutdown /r")
        elif("الارم"in m.lower())or("کوک کن"in m.lower())or("ساعت بزار"in m.lower())or("آلارم"in m.lower()):
           playsound.playsound(manorwoman+"//hourenter.mp3")
           saat=input("<< ساعت : ")
           saate=""
           if(saat==""):
              r = sr.Recognizer()
              with sr.Microphone() as source:
                 print("\nSTT <<",end=" ")
                 playsound.playsound(manorwoman+"//say.mp3")
                 audio = r.listen(source)
              try:
                 saat=r.recognize_google(audio,language="fa")
                 for i in range (0,len(saat)):
                    saate+=chr(ord(saat[i])-1728)
                 print(saate)
                 saat=saate
              except:
                 playsound.playsound(manorwoman+"//error.mp3")
           playsound.playsound(manorwoman+"//minutetoo.mp3")
           try:
              daghighe=input("\n<< دقيقه :")
              saatee=""
              if(daghighe==""):
                  r = sr.Recognizer()
                  with sr.Microphone() as source:
                      print("\nSTT <<",end=" ")
                      playsound.playsound(manorwoman+"//say.mp3")
                      audio = r.listen(source)   
                  try:
                      daghighe=r.recognize_google(audio,language="fa")
                      print(daghighe)
                      for i in range (0,len(daghighe)):
                         saatee+=chr(ord(daghighe[i])-1728)
                      print(saatee)
                      daghighe=saatee
                  except:
                      playsound.playsound(manorwoman+"//error.mp3")
           except:
              pass
           playsound.playsound(manorwoman+"//saat.mp3")
           playsound.playsound(manorwoman+"//"+saat+".mp3")
           playsound.playsound(manorwoman+"//"+"va.mp3")
           playsound.playsound(manorwoman+"//"+daghighe+".mp3")
           playsound.playsound(manorwoman+"//"+"got.mp3")
           playsound.playsound(manorwoman+"//alarmset.mp3")
           file=open("alarm1s.txt",'w')
           file.write(saat)
           file.close()
           file=open("alarm1d.txt",'w')
           file.write(daghighe)
           file.close()
           def alarm():
               while True:
                  now=datetime.now()
                  file=open("alarm1s.txt",'r')
                  file2=open("alarm1d.txt",'r')
                  filer=file.readline()
                  files=file2.readline()
                  if(now.hour==int(filer)):
                     if(now.minute>=int(files)):
                        file.close()
                        file2.close()
                        os.remove("alarm1s.txt")
                        os.remove("alarm1d.txt")
                        playsound.playsound(manorwoman+"//alarmmusic.mp3")
                  file.close()
                  file2.close()
           thread1=Thread(target=alarm,args=[])
           thread1.start()
        elif(("زمان"in m.lower())or(("ساعت" in m.lower()))):
            now=datetime.now()
            time="%s:%s" % (now.hour,now.minute)
            print("\n>> "+time)
            playsound.playsound(manorwoman+"//saat.mp3")
            playsound.playsound(manorwoman+"//"+str(now.hour)+".mp3")
            playsound.playsound(manorwoman+"//va.mp3")
            playsound.playsound(manorwoman+"//"+str(now.minute)+".mp3")
        elif("تاريخ"in m.lower())or("امروز چه روزیه"in m.lower())or("امروز چندمه"in m.lower())or("تاریخ"in m.lower()):
            now=datetime.now()
            date="%s/%s/%s" % (now.day,now.month,now.year)
            print("\n>> "+date)
            playsound.playsound(manorwoman+"//date.mp3")
            playsound.playsound(manorwoman+"//"+str(now.day)+".mp3")
            playsound.playsound(manorwoman+"//va.mp3")
            playsound.playsound(manorwoman+"//"+str(now.month)+".mp3")
        elif("هوا"in m.lower()):
            print("1")
            weather = weather(unit=Unit.CELSIUS)
            location = weather.lookup_by_location('tehran')
            condition = location.condition()
            forecasts = location.forecast()
            v=1
            hh=1
            for forecast in forecasts:
               if("پس در فردا" in m.lower()):
                  hh=4
               elif("پس فردا" in m.lower()):
                  hh=3
               elif("فردا" in m.lower()):
                  hh=2
               if(v==hh):
                   hct=forecast.high
                   lct=forecast.low
                   texc=forecast.text
                   datc=forecast.date
               v+=1
            if(hh==1):
               print("\n\n<< ",datc," :براي امروز")
            if(hh==2):
               print("\n\n<< ",datc," :براي فردا")
            if(hh==3):
               print("\n\n<< ",datc," :براي پس فردا")
            if(hh==4):
               print("\n\n<< ",datc," :براي پس در فردا")
            print("   ",texc," :وضيعت هوا")
            print("   ",hct,"*C :بيشترين دما")
            print("   ",lct,"*C :کمترين دما")
            if("cloudy" in texc.lower())or("cloud" in text.lower()):
               playsound.playsound(manorwoman+"//hava dar.mp3")
               playsound.playsound(manorwoman+"//tehran.mp3")
               playsound.playsound(manorwoman+"//abri.mp3")
               playsound.playsound(manorwoman+"//ast.mp3")
            elif("sunny" in texc.lower())or("sun" in text.lower()):
               playsound.playsound(manorwoman+"//hava dar.mp3")
               playsound.playsound(manorwoman+"//tehran.mp3")
               playsound.playsound(manorwoman+"//aftabi.mp3")
               playsound.playsound(manorwoman+"//ast.mp3")
            elif("rainy" in texc.lower())or("rain" in text.lower()):
               playsound.playsound(manorwoman+"//hava dar.mp3")
               playsound.playsound(manorwoman+"//tehran.mp3")
               playsound.playsound(manorwoman+"//barani.mp3")
               playsound.playsound(manorwoman+"//ast.mp3")
            elif("snowy" in texc.lower())or("snow" in text.lower()):
               playsound.playsound(manorwoman+"//hava dar.mp3")
               playsound.playsound(manorwoman+"//tehran.mp3")
               playsound.playsound(manorwoman+"//barfi.mp3")
               playsound.playsound(manorwoman+"//ast.mp3")
            hct=str(hct)
            lct=str(lct)
            playsound.playsound(manorwoman+"//w&cpredicted.mp3")
            playsound.playsound(manorwoman+"//hct.mp3")
            if("-" in hct):
               playsound.playsound(manorwoman+"//manfi.mp3")
               hct=hct[1:]
            hct+=".mp3"
            playsound.playsound(manorwoman+"//"+hct)
            playsound.playsound(manorwoman+"//va.mp3")
            playsound.playsound(manorwoman+"//lct.mp3")
            if("-" in lct):
               playsound.playsound(manorwoman+"//manfi.mp3")
               lct=lct[1:]
            lct+=".mp3"
            playsound.playsound(manorwoman+"//"+lct)
            playsound.playsound(manorwoman+"//cdgree.mp3")
        elif("ملودی" in m.lower())or("ملودي" in m.lower())or("اهنگ" in m.lower())or("موسیقی" in m.lower())or("موسيقي" in m.lower())or("پخش"in m.lower()):
           playsound.playsound(manorwoman+"//melodyname.mp3")
           melody=input("<< نام ملودي : ")
           if(melody==""):
              r = sr.Recognizer()
              with sr.Microphone() as source:
                 print("\nSTT <<",end=" ")
                 playsound.playsound(manorwoman+"//say.mp3")
                 audio = r.listen(source)
              try:
                 melody=r.recognize_google(audio)
                 melody=melody.lower()
                 print(melody)
              except:
                 playsound.playsound(manorwoman+"//error.mp3")
           playsound.playsound(manorwoman+"//melodys.mp3")
           melody+=".mp3"
           print(">> .پخش ملودي آغاز شد")
           try:
              def mediap():
                 try:
                    playsound.playsound("media//"+melody)
                 except:
                     playsound.playsound(manorwoman+"//error2.mp3")
                     playsound.playsound(manorwoman+"//error3.mp3")
              thread2=Thread(target=mediap,args=[])
              thread2.start()
           except:
              playsound.playsound(manorwoman+"//error2.mp3")
              playsound.playsound(manorwoman+"//error3.mp3")
        elif("سرچ" in m.lower())or("جست و جو"in m.lower()):
           #playsound.playsound("searchmenter.mp3")
           searchm=input("<< موضوع جست و جو :")
           if(searchm==""):
              r = sr.Recognizer()
              with sr.Microphone() as source:
                 print("\nSTT <<",end=" ")
                 playsound.playsound(manorwoman+"//say.mp3")
                 audio = r.listen(source)
              try:
                 searchm=r.recognize_google(audio)
                 searchm=searchm.lower()
                 print(searchm)
              except:
                 playsound.playsound(manorwoman+"//error.mp3")
           try:
              semm=wikipedia.summary(searchm)
              wikipedia.set_lang("fa")
              sem=wikipedia.summary(searchm)
              print(">> "+sem)
              playsound.playsound(manorwoman+"//findend.mp3")
           except:
              playsound.playsound(manorwoman+"//error.mp3")
        else:
           playsound.playsound(manorwoman+"//mote.mp3")
   except:
        playsound.playsound(manorwoman+"//error2.mp3")
        playsound.playsound(manorwoman+"//error3.mp3")
#end: 340 ---------------------------------------------------------------------------
#thanks-from-#izanlou-aria-#safarzadeh-amirhossain

    


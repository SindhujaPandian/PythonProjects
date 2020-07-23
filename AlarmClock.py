import winsound , time

def alarm():
    print("ALARMING......") 
    winsound.PlaySound('Welcome.wav', winsound.SND_FILENAME) 
    time.sleep(2)
    print('Alarm Stopped')

def wait(sec):
    time.sleep(sec)
    alarm()
    
print("##################### ALARM CLOCK #####################\n\n")
print("Note:")
print("The time format must be in 24 hours format")
print('The User input must be in this format :  " HH:MM:SS " \n')
try:
    Time = time.localtime()
    hh,mm,ss = map(int, time.strftime("%H:%M:%S",Time).split(':'))
    print('         --------------------------------------------------------------')
    print('        |                 The System time is '+str(hh)+' :'+str(mm)+' :'+str(ss)+'                 |' )
    print('         --------------------------------------------------------------')
    total_system_second = (hh*60*60)+(mm*60) + ss
        
    hour,minute,second=map(int,input('Enter the time you want to set an alarm : \n').split(':'))
    if((hour<24) and (minute<60) and (second<60)):
        total_second = (hour*60*60)+(minute*60)+second
        difference = abs(total_second - total_system_second)
        diff=difference
        s = difference % 3600
        difference //= 3600
        m = difference % 360
        difference //= 360
        h = difference % 60
        difference //= 60
        print("The alram set for "+str(h)+" hours "+str(m)+" minutes "+str(s)+"seconds from now")
        wait(diff-5)
    else:
        print("Oops: Please enter the valid time !!!")
    
except:
    print("The user input format hh:mm:ss does not match ||| \nTry again !!")




    

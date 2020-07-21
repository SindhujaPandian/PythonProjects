import bs4 as bs
import urllib.request

def horoscope(sign):
    try:
        source = urllib.request.urlopen("https://www.astrology-zodiac-signs.com/horoscope/"+sign+"/daily/").read()
        soup = bs.BeautifulSoup(source,'html.parser')
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!              Your Zodiac Name is "+sign+"             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^##^^#^^#^^")
        print("                                                                              DATE")
        spans = soup.find_all("span",class_="DailyDate")
        for span in spans:
            print(span.text)
        print("#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^##^^#^^#^^")
        table = soup.find_all("div",class_="dailyHoroscope")
        print("\n\n")
        print("@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@")
        print("                                                                              Your Fortune\n")
        for x in table:
                print(x.find('p').text)
        print("\n@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@$@")
    except:
        print("Sorry !! Something goes wrong")
while True:
    
    print("--*--*--*--*--*--*--*--*--*--*-*--*--*--*--*  FORTUNE TELLER --*--*--*--*--*--*--*--*--*--*-*--*--*--*--*\n")
    sign =["aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces"]
    print("Zodiac Name\tZodiac Number")
    print("---------------\t------------------")
    for i in range(12):
        if i==8:
            print(sign[i],"\t",i+1)
            continue
        print(sign[i],"\t\t",i+1)
    num=int(input("Choose your zodiac number  :  ")) 
    
    horoscope(sign[num-1])

    print("\nDo you Want to Chack again? \nY - Yes\nN - No\nYour Answer : ")
    val=input()
    if val[0].lower()=='y':
        continue
    else:
        break

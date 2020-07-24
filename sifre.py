key = ["1","2","q","-","|","a",".","<","£","*","4","/",";","h","=","[","é","X","h","n","à","`","_","Ç","A","#","Q","Ö","9","5"]
alfabe =["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"," "]

while 1:
    if_i = 0
    olay  = input("girdi(e)çöz(h):")
    if olay.lower() == "e":
        keyorn = input("->")
        for i in keyorn:
            while 1:
                if if_i == len(alfabe)-1:
                    if_i = 0
                else:
                    if_i += 1
                if i == alfabe[if_i]:
                    print(key[if_i] , end = "")
                    break
            
    elif olay.lower() == "h":
        cozum = input("->")
        for i in cozum:
            while 1:
                if if_i == len(key)-1:
                    if_i = 0
                else:
                    if_i += 1
                if i == key[if_i]:
                    print(alfabe[if_i] , end = "")
                    break

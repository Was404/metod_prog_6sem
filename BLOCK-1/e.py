
def check_skobok(stroka):
    #stroka.split('')
    slovar_skobok = {
        0 : "(",
        1 : ")",
        2 : "[",
        3 : "]",
        4 : "{",
        5 : "}"
    }
    n = 0
    for i in range(len(stroka) - 1):
            match stroka[i]:
                case "(":
                    if stroka[i+1] == slovar_skobok.get(1):
                        n += 1
                    else:
                        n = 0
                        break    
                case "[":
                    if stroka[i+1] == slovar_skobok.get(3):
                        n += 1
                    else:
                        n = 0
                        break  
                case "{":
                    if stroka[i+1] == slovar_skobok.get(5):
                        n += 1
                    else:
                        n = 0
                        break  
                case _:
                    continue
                                  
    if n > 1:
        print("yes")
    else:
        print('no')                                                                    

#if __name__ == "main":
#stroka = ["(", ")", "[", "]", "{", "}"]
stroka = input()
stroka.split()
check_skobok(stroka)

arr=["0","T","E","M","N","A","I","O","G","K","D","W","R","U","S","S.","O:","Q","Z","Y","C","X","B","J","P","A:","L","U:","F","V","H"]
##print(translatestring(".... ..    .... . _.__",arr))

def morsecode(m,arr,n):
    if len(m)==0:
        return ""
    if m[0]=="_":
        s=arr[2*n+1]
        if(m[1:]):
            s=morsecode(m[1:],arr,2*n+1)
    else:
        s=arr[2*n+2]
        if(m[1:]):
            s=morsecode(m[1:],arr,2*n+2)
    return s


def translatestring(string,arr):
    l=string.split("    ")
    s=""
    for elem in l:
        t=elem.split(" ")
        for letter in t:
            s+=morsecode(letter,arr,0)
        s+=" "
    return s

def tomorse(string,arr):
    l=string.split(" ")
    f=""
    for elem in l:
        for letter in elem:
            n=arr.index(letter.upper())
            st=lettertomorse(arr,n)
            f+=" "
            f+=st
        f+="    "
    return f
        


def lettertomorse(arr,n):
    if n==0:
        return ""
    else:
        s=""
        if n%2==0:
           s+="."
           s+=lettertomorse(arr,(n-2)/2)
        else:
            s+="_"
            s+=lettertomorse(arr,(n-1)/2)
    return s

print(tomorse("Hi HEY",arr))
    



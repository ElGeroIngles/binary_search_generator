import math
def generateSearch(min,max):
    mid = math.floor((min + max) / 2)
    output = ""
    filename = "./functions/frames/"+str(min)+"_"+str(max)+".mcfunction"
    if min != mid:
        output = "execute if score @s botw matches "+str(min)+".."+str(mid)+" run function botw:example/search_frame"
        generateSearch(min,mid)
    else:
        output = "execute if score @s botw matches "+str(min)+" run function botw:example/frames/"+str(min)

    if mid+1 != max:
        output += "\nexecute if score @s botw matches "+str(mid+1)+".."+str(max)+" run function botw:example/search_frame"
        generateSearch(mid+1,max)
    else:
        output += "\nexecute if score @s botw matches "+str(max)+" run function botw:example/frames/"+str(max)
    f = open(filename, "w")
    f.write(output)
    f.close()

generateSearch(0,79)
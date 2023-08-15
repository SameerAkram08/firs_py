def TOH(number,start,end,aux):
    if number == 1 :
        print("Move disk 1 from rod {} to rod {}".format(start,end))
        return
    TOH(number-1 ,start,end,aux)
    print("Move disk {} from rod {} to rod {}".format(number,start,end))
    TOH(number -1 ,start,end,aux)
disc = int(input("How many disks = "))
TOH(disc,"A","B","C")
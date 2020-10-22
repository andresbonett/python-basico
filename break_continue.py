def run():
    #continue
    for contador in range(20):
        if contador % 2 != 0:
            continue
        print(contador) # 2,4,6,8,10...
    
    #break
    for i in range(1000):
        print(i)        # print 0 - 230
        if i == 230:
            break 

    # break in string
    texto = input("Enter text: ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)

if __name__ == "__main__":
    run()
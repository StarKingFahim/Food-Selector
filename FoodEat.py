day = input("whats day is it?:mon/tue/wed/thu/fri/sat/sun")

if(day == 'mon'):

    print("Choose From the following")
    print("1)Continental")
    print("2)Turkish")
    print("3)HomeMade")
    food = input("What Would You Like to Eat ?")
    if(food == "Continental"):
        print("East-West Spring Rolls")
    elif(food == "Turkish"):
        print("Şiş kebap")
    elif(food == "HomeMade"):
        print("Jam Bread")

elif(day == 'tue'):

    print("Choose From the following")
    print("1)Italian")
    print("2)Chinese")
    print("3)HomeMade")
    food = input("What Would You Like to Eat ?")
    if(food == "Italian"):
        print("Pizza!")
    elif(food == "Chinese"):
        print("Chow Mein!")
    elif(food == "HomeMade"):
        print("Roti and Daal")

elif(day == 'wed'):

    print("Choose From the following")
    print("1)American")
    print("2)German ")
    print("3)HomeMade")
    food = input("What Would You Like to Eat ?")
    if(food == "American"):
        print("Sirloin Steak")
    elif(food == "German"):
        print("Asparagus with Hollandaise sauce")
    elif(food == "HomeMade"):
        print("Spinach and Paneer")

elif(day == 'thu'):
    
    print("Choose From the following")
    print("1)Arab")
    print("2)Hyderabadi")
    print("3)HomeMade")
    food = input("What Would You Like to Eat ?")
    if(food == "Arab"):
        print("Hummus with chickpeas")
    elif(food == "Hyderabadi"):
        print("Shami Kebab")
    elif(food == "HomeMade"):
        print("Potata Curry And Rice")

elif(day == 'fri'):

    print("Choose From the following")
    print("1)Nepalese")
    print("2)Mexican ")
    print("3)HomeMade")
    food = input("What Would You Like to Eat ?")
    if(food == "Nepalese"):
        print("Momo")
    elif(food == "Mexican"):
        print("Tortiyas!")
    elif(food == "HomeMade"):
        print("Sandwiches")

elif(day == 'sat'):

    print("Choose From the following")
    print("1)Spanish")
    print("2)Japanese")
    print("3)HomeMade")
    food = input("What Would You Like to Eat ?")
    if(food == "Spanish"):
        print("Churros")
    elif(food == "Japanese"):
        print("Oyakudon")
    elif(food == "HomeMade"):
        print("Aloo Pharata")

elif(day == 'sun'):

    print("Choose From the following")
    print("1)Mughlai")
    print("2)Lebanese")
    print("3)HomeMade")
    food = input("What Would You Like to Eat ?")
    if(food == "Mughlai"):
        print("Murgh musallam")
    elif(food == "Lebanese"):
        print("Shawarma")
    elif(food == "HomeMade"):
        print("Pancakes")
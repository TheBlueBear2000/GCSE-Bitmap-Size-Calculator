print("\n\nWelcome to the BitMap Size Calculator!")
while True:
    while True:
        try:
            imageWidth = int(input("Please input the width of the image:  "))
            break
        except:
            print("Invalid input")
    while True:
        try:
            imageHeight = int(input("Please input the height of the image:  "))
            break
        except:
            print("Invalid input")
    imageSize = (imageWidth,imageHeight)
    isDepth = input("Are you going to enter the image's colour depth or num of colours?  ")
    while True:
        try:
            imageColourNum = int(input("Please input the number of colours in the image:  " if not("d" in isDepth.lower()) else "Please input the colour depth of the image:  "))
            break
        except:
            print("Invalid input")
    colourDepth = 1
    while 2 ** colourDepth < imageColourNum:
        colourDepth += 1
    invalid = True
    if "d" in isDepth.lower():
        colourDepth = imageColourNum
    while invalid:
        invalid = False
        sizeFormat = input("Please input the output type:  ")
        multiplier = 0              # K, M, G, T
        multiplierType = 1000       # 1000, 1024
        bitOrByte = 1               # Bit, Byte
        if sizeFormat.lower().startswith("k"):
            multiplier = 1
        elif sizeFormat.lower().startswith("m"):
            multiplier = 2
        elif sizeFormat.lower().startswith("g"):
            multiplier = 3
        elif sizeFormat.lower().startswith("t"):
            multiplier = 4
        elif sizeFormat.lower().startswith("b"):
            multiplier = 0
        else:
            print("Invalid input (Max entry size format is T)")
            invalid = True
        if sizeFormat.lower()[2:4] == "bi":
            multiplierType = 1024
        if sizeFormat.lower().endswith("bits") | sizeFormat.lower().endswith("bit"):
            bitOrByte = 1
        elif sizeFormat.lower().endswith("bytes") | sizeFormat.lower().endswith("byte"):
            bitOrByte = 8
        else:
            print("Invalid input (Bit/Byte invalid)")
            invalid = True
    print("Answer is {} {}".format((imageWidth * imageHeight * colourDepth) / (bitOrByte * (multiplierType ** multiplier)), (sizeFormat if sizeFormat.endswith("s") else sizeFormat + "s")))
    doContinue = input("Continue? (y/n)  ")
    if "n" in doContinue.lower():
        print("Thank you for using the BitMap Size Calculator!")
        break
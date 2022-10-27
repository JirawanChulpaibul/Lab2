def calculate_bmi(height, weight) :
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    format_bmi = "{:.2f}".format(bmi) #to set decimal place to 2

    print("Your bmi is " + str(format_bmi))

calculate_bmi(height=1.75,weight=57)
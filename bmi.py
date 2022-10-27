def calculate_bmi(height, weight) :
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    format_bmi = "{:.2f}".format(bmi) #to set decimal place to 2

    print("Your bmi is " + str(format_bmi))

    if bmi<18.5 :
        print("Underweight")
    elif bmi>=18.5 or bmi<=25.0 :
        print("Normal Weight")
    else :
        print("Overweight")

calculate_bmi(height=1.75,weight=57)
def find_min_max(num):
    length = len(num) #get the length of the list of floats
    min = num[0]
    max = num[0]
    for i in range(1,length):
        if num[i] < min :
            min = num[i]
        elif num[i] > max :
            max = num[i]
    min_max = [min,max]
    print("The min and max are " ,min_max)
    return min_max

def get_user_input():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    num = input()
    num_split = num.split(", ")
    num_split = list(map(float, num_split)) #process and transform all items without using loop
    print(num_split)
    return num_split

def display_main_menu():
    print("display_main_menu")

def calc_average(num):
    length = len(num) #get the length of the list of floats
    total = num[0]
    for i in range(1,length):
        total = num[i] + total
    average = total/length
    print("The average is ",average)
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_split = get_user_input() #name of the variable has to be the same as the return variable of the function called
    find_min_max(num_split)
    calc_average(num_split)

if __name__ == "__main__":
    main()



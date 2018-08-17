from time import sleep

def main():
    timer_count = 1
    timer_list = []
    choice = True
    
    while choice:
        print("Enter timer " + str(timer_count) + " in number of seconds, q to quit: ")
        choice = str(input())
        if choice == "q":
            choice = False
        else:
            timer_list = timer_list + [int(choice)]
            timer_count += 1
            choice = True
    
    timer_count = 1
    for i in timer_list:
        print("\nTimer " + str(timer_count) + "\n")
        current = i
        while i >= 0:
            print(i)
            i -= 1
            sleep(1)
        timer_count += 1
            
main()
def total_user_numbers():
    total = 0
    number = int(input("enter a number (0 to end):"))
    while number != 0:
        total += number
        number = int(input("enter another number (0 to end):"))
    print(f"total:{total}")
    
def main():
    total_user_numbers()
main()
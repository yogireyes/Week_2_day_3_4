def calc_feet():
    total_square_footage = 0
    room_count = int(input("Enter the number of rooms in the house: "))

    for num in range(1, room_count + 1):
        length = float(input(f"Enter the length of room {num}: "))
        width = float(input(f"Enter the width of room {num}: "))
        square_footage = length * width
        total_square_footage += square_footage

    return total_square_footage

square_footage = calc_feet()
print("Total square footage:", square_footage)

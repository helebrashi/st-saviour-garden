

if __name__ == '__main__':

    # print without a line break using this function
    # print('🌷', end='') 

    for row in range(11):
        for col in range(11):
            print("🌼", end=" ")
        print('')
print("\n" + "="*30 + "\n")

for row in range(11):
    for col in range(11):
        if row % 2 == 0:
            print("🌷", end=" ")
        else:
            print("🌼", end=" ")
    print()
print("\n" + "="*30 + "\n")

for row in range(11):
    for col in range(11):
        if col % 2 == 0:
            print("🌷", end=" ")
        else:
            print("🌼", end=" ")
    print()
print("\n" + "="*30 + "\n")

for row in range(11):
    for col in range(11):
        if row == col:
            print("🌷", end=" ")
        else:
            print("🌼", end=" ")
    print()
print("\n" + "="*30 + "\n")

for row in range(11):
    for col in range(11):
        if row % 2 == 0 and col % 2 == 0:
            print("🌷", end=" ")
        else:
            print("🌼", end=" ")
    print()
print("\n" + "="*30 + "\n")

for row in range(11):
    for col in range(11):
        if row % 2 == 0 and col % 2 == 0:
            print("🌷", end=" ")
        else:
            print("🌼", end=" ")
    print()
print("\n" + "="*30 + "\n")

for row in range(11):
    for col in range(11):
        if row == col or row + col == 10:
            print("🌷", end=" ")
        else:
            print("🌼", end=" ")
    print()

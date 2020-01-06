# Minimal positive integer:
# Find minimal positive integer that is not in list. If list contains only numbers
# Example: [1,2,3,4,6] - Answer 5
# Example: [1,2,3] - Answer 4
# Example: [-1, -2, -6] - Answer 1

nums = input("Enter a list of numbers: ").split()
int_ = sorted([int(i) for i in nums])

if max(int_) <= 0:
    print(1)

else:
    for i in range(1, max(int_) + 2):
        if i > 0 and i not in int_:
            print(i)
            break

# else:
#     m = range(1, len(int_))
#     n = min(set(m) - set(int_))

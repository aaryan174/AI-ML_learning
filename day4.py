
marks = [56, 54, 56, 78,34,56,56,225,4564,564,64,45]

marks.append(10)
print(marks)

marks.insert(1, 2345)
print(marks)

marks.sort(reverse=True)
print(marks)

marks.reverse()
print(marks)

x = 4564
idx = 0

for val in marks:
    if(val == x):
        print(f" x found at id={idx}")
        break
    idx += 1
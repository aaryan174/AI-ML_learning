marks = {
    "aryan": 34,
    "ary" : 56,
    "dave": 89,
    0: "aryan",
    "age": [12,3,4,4,5,6]
}


for i in marks.items():
    print(marks)

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"aryan": 100, "rekha": 34})
print(marks.items())
print(marks.get("aryan"))
print(marks)
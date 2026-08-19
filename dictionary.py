marks = {
    "aryan": 34,
    "allo" : 56,
    "halllo": 89,
    0: "aryan"
}


print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"aryan": 100, "rekha": 34})
print(marks.items())
print(marks.get("aryan"))
print(marks)
marks = {
    "Sadha": 100,
    "niko": 89,  
    "pro max":97,
    0:"harry"
}
print(marks)
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"pro max":98,"Niko max":89})
print(marks)
print(marks.get("niko"))
print(marks["niko"])
#differece btw .get and normal marks
print(marks.get("niko2")) # prints node
print(marks["niko2"])     # prints error
# pop and more mothods are there see in chatgpt
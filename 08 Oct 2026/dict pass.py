#Dictionary with student ID, name, and scores
students = {
    1: {"name": "Ashutosh", "scores": [85, 90, 78]},
    2: {"name": "CHINU", "scores": [92, 88, 95]},
    3: {"name": "OMiee", "scores": [76, 2, 8]}
}
#average score using integer/float
for sid, details in students.items():
    avg = sum(details["scores"]) / len(details["scores"])
    details["average"] = avg
    details["PAssed"] = avg >= 50


#name of passed s
print("Student Details with Average and Pass Status:")
for sid, details in students.items():
    if details["PAssed"]:
        print(details["name"])
    
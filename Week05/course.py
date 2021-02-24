# Programme that stores students names, courses and grades
# Prints out students data
# Author: Saidhbh Foley

student = {
    "name":"Mary",
    "modules": [
        {
            "courseName": "Programming",
            "grade": 45
        },
        {
            "courseName":"History",
            "grade":99
        }
    ]
}
print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print ("\t {} \t: {}".format(module["courseName"], module["grade"] ))
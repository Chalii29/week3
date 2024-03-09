marks = 75
result = ""
if marks < 30:
    result = "Failed"
elif marks > 74.9:
    result = "Passed with distinction"
else:
    result ="Passed"

print(result)

def rate_student(marks):

 if marks >= 80:
    return "Distinction"
 elif marks >= 60 and marks < 70:
    return "Credit"
 elif marks >= 40 and marks < 50:
    return "Fair"
 else:
    return "Fail"

# Test the function with a sample marks
marks = 35
print(f"The student's performance is: {rate_student(marks)}")
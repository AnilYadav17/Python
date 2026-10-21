def main():

    file = open("students.txt", "r")
    result_file = open("result.txt", "w")
    error_file = open("error_log.txt", "w")

    for line in file:

        line = line.strip()

        if line == "":
            continue

        data = line.split(",")

        if len(data) < 4:
            error_file.write(line + " -> Marks missing\n")
            continue

        student_id = data[0]
        name = data[1]
        subject = data[2]
        marks = data[3]

        if marks.isdigit() == False:
            error_file.write(line + " -> Marks must be number\n")
            continue

        marks = int(marks)

        if marks < 0 or marks > 100:
            error_file.write(line + " -> Invalid marks\n")
            continue

        if marks >= 90:
            result = "Excellent"
        elif marks >= 75:
            result = "Very Good"
        elif marks >= 60:
            result = "Good"
        elif marks >= 40:
            result = "Pass"
        else:
            result = "Fail"

        result_file.write(
            student_id + " - " + name + " - " + subject + " - " + str(marks) + " - " + result + "\n"
        )

    file.close()
    result_file.close()
    error_file.close()

    print("Processing completed")


main()

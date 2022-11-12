# Author: Sonny Chen
FILE_NAME = "assignments/ass20/jobs.txt"
def read_assignments():
    jobList = {}
    try:
        with open(FILE_NAME) as file:
            for line in file:
                if line.strip == "":
                    continue
                job_student = line.split(":")
                job = job_student[0].strip().lower()
                student = job_student[1].strip().lower()
                jobList[job] = student
        return jobList
    except FileNotFoundError:
        print("Sorry, your file doesn't exist.")

def write_assignments(assignments):
    try:
        with open(FILE_NAME, "w") as file:
            for job in assignments:
                file.write(f"{job} : {assignments[job]}\n")
    except FileNotFoundError:
        print("Sorry, your file doesn't exist.")

def list_assignment(assignments):
    for job in assignments:
        print(f"{job} : {assignments[job]}")

def add_assignment(assignments):
    job = input("Enter Job: ").lower().strip()
    stud = input("Enter Student: ").lower().strip()
    if job in assignments:
        assignments[job] = stud
        print(f"{assignments[job]} was assigned to {job}")
    else:
        print("Invalid job")

jobList = read_assignments()
#list_assignment(jobList)

while True:
    choice = input("Enter (L)ist, (A)ssign Student, or (Q)uit: ").strip().lower()
    if choice == "q":
        break
    elif choice == "l":
        list_assignment(jobList)
    elif choice == "a":
        add_assignment(jobList)
write_assignments(jobList)

print("Goodbye")
#nandhini sri V(192521344)
"""
JOB SCHEDULING USING BACKTRACKING
Problem:
Assign jobs to employees such that:
1. Every job is assigned exactly once.
2. An employee can handle only one job at a time.
3. Every job must be completed before its deadline.

Technique Used:
Backtracking + Constraint Satisfaction + Pruning

Complexity:
Let:
n = Number of jobs
m = Number of employees

Time Complexity:
Worst Case = O(m^n)

Reason:
For each job, there are m possible employee choices.
Therefore total possibilities = m × m × m × ... (n times)
= O(m^n)

Space Complexity:
O(n)

Reason:
Recursive calls store at most n levels in the recursion stack.
"""
Input Data
jobs = ["J1", "J2", "J3", "J4"]

# Time required for each job
job_duration = {
    "J1": 2,
    "J2": 1,
    "J3": 3,
    "J4": 2
}

# Deadline of each job
deadline = {
    "J1": 4,
    "J2": 3,
    "J3": 6,
    "J4": 5
}

# Available employees
employees = ["E1", "E2"]

# Stores current completion time of each employee
employee_time = {
    "E1": 0,
    "E2": 0
}

# Stores final assignments
schedule = []
# Backtracking Function
def assign_jobs(job_index):

    # Base Case:
    # If all jobs are assigned, return True
    if job_index == len(jobs):
        return True

    # Select current job
    current_job = jobs[job_index]

    # Try assigning current job to every employee
    for emp in employees:

        # Completion time if employee performs current job
        completion_time = employee_time[emp] + job_duration[current_job]
        # PRUNING CONDITION
        # Assign only if job finishes before deadline
        if completion_time <= deadline[current_job]:

            # Save old time for backtracking
            previous_time = employee_time[emp]

            # Assign job
            employee_time[emp] = completion_time
            schedule.append((emp, current_job))

            # Recursive call for next job
            if assign_jobs(job_index + 1):
                return True

           
            # BACKTRACKING
            
            # Undo assignment if future assignment fails
            schedule.pop()
            employee_time[emp] = previous_time

    # No valid assignment found
    return False



# Main Program
if assign_jobs(0):

    print("Feasible Schedule Found\n")

    for emp, job in schedule:
        print(emp, "->", job)

else:
    print("No valid schedule exists.")

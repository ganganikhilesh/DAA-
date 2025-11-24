class Job:
    def __init__(self, id, dead_line, profit):
        self.id=id
        self.deadline=dead_line
        self.profit=profit
def job_sequencing(jobs,n):
    for i in range(n):
        for j in range(i+1,n):
            if jobs[i].profit<jobs[j].profit:
                jobs[i],jobs[j]=jobs[j],jobs[i]
    max_deadline=0
    for job in jobs:
        if job.deadline>max_deadline:
            max_deadline=job.deadline
    slot=[None]*max_deadline
    total_profit=0
    for i in range(n):
        for j in range(jobs[i].deadline-1,-1,-1):
            if slot[j]==None:
                slot[j]=jobs[i]
                total_profit+=jobs[i].profit
                break
    print("Scheduled jobs:")
    for i in range(max_deadline):
        if slot[i]!=None:
            print(f"Time_slot {i}-{i+1} is Job {slot[i].id} Profit is {slot[i].profit}")
        else:
            print(f"Time_slot {i}-{i+1} is Empty")
    print("Total Profit is", total_profit)
# jobs = [
#     Job('J1', 4, 70),
#     Job('J2', 1, 80),
#     Job('J3', 1, 30),
#     Job('J4', 2, 100),
#     Job('J5', 3, 40)
# ]
n=int(input("enter the no.of jobs:"))
jobs=[]
for i in range(n):
    c=input("enter the character:")
    d=int(input("enter the maximum deadline:"))
    p=int(input("enter the profit:"))
    jobs.append(Job(c,d,p))
job_sequencing(jobs, len(jobs))

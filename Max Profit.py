def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)  # (id, deadline, profit)
    maxd = max(j[1] for j in jobs)
    slots = [-1]* (maxd+1)
    profit = 0

    for job, d, p in jobs:
        for t in range(d,0,-1):
            if slots[t] == -1:
                slots[t] = job
                profit += p
                break
                
    return profit, [x for x in slots if x!=-1]

print(job_sequencing([("a",2,100),("b",1,19),("c",2,27),("d",1,25),("e",3,15)]))

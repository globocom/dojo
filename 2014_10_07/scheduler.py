from copy import deepcopy

def optimize_schedule(jobs):
    if len(jobs) == 1:
        return [jobs]
    results = []

    max_subset = 0
    for index, job in enumerate(jobs):
        result = schedule([], jobs[index:])

        if len(result) > max_subset:
            max_subset = len(result)

        results.append(result)

    return filter(lambda x: len(x) == max_subset, results)

def schedule(added_jobs, next_jobs):
    if not next_jobs:
        return added_jobs

    if len(added_jobs) == 0:
        added_jobs.append(next_jobs[0])
        return schedule(added_jobs, next_jobs[1:])
    else:
        best_branch = []

        for index, next_job in enumerate(next_jobs):
            if are_compatible(added_jobs[-1], next_job):
                added_jobs.append(next_job)

                branch = schedule(added_jobs, next_jobs[index+1:])
                if len(branch) > len(best_branch):
                    best_branch = deepcopy(branch)

                added_jobs.pop()

        return best_branch

def are_compatible(job1, job2):
    return job1[1] <= job2[0] or job2[1] <= job1[0]

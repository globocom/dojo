def optimize_schedule(jobs):
    if len(jobs) == 1:
        return [jobs]
    results = []

    results = schedule(results, jobs)

    return results

def schedule(added_jobs, next_jobs):
    if not next_jobs:
        return added_jobs

    if len(added_jobs) == 0:
        added_jobs.append(next_jobs[0])

    if are_compatible(added_jobs[-1], next_jobs[0]):
        added_jobs.append(next_jobs[0])

    return schedule(added_jobs, next_jobs[1:])

def are_compatible(job1, job2):
    return job1[1] <= job2[0] or job2[1] <= job1[0]

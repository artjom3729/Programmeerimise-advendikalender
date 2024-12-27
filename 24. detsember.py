input_str = """Kalle: Rämpsu prügikasti viimine-113 min;Joogid külma panna-8 min;Jäätise serveerimine-25 min;Mängude ja tegevuste planeerimine-22 min;Toolid valmis seada-29 min
Martin: Rämpsu prügikasti viimine-99 min;Joogid külma panna-19 min;Jäätise serveerimine-48 min;Mängude ja tegevuste planeerimine-62 min;Toolid valmis seada-21 min
Lennart: Rämpsu prügikasti viimine-67 min;Joogid külma panna-59 min;Jäätise serveerimine-62 min;Mängude ja tegevuste planeerimine-64 min;Toolid valmis seada-77 min"""


def parse_input(input_str):
    tasks = []
    people = []
    for line in input_str.strip().splitlines():
        name, chores = line.split(": ")
        people.append(name)
        chores = chores.split(";")
        person_tasks = []
        for chore in chores:
            task, time = chore.split("-")
            time = int(time.split()[0])
            person_tasks.append((task.strip(), time))
        tasks.append(person_tasks)
    return people, tasks


def find_optimal_distribution(people, tasks):
    num_people = len(people)
    num_tasks = len(tasks[0])

    # Initialize the minimum maximum time to a large value
    min_max_time = float("inf")
    best_assignment = None

    # Helper function to recursively assign tasks
    def assign_tasks(task_idx, person_times, current_assignment):
        nonlocal min_max_time, best_assignment

        if task_idx == num_tasks:
            max_time = max(person_times)
            if max_time < min_max_time:
                min_max_time = max_time
                best_assignment = current_assignment[:]
            return

        for person_idx in range(num_people):
            person_times[person_idx] += tasks[person_idx][task_idx][1]
            current_assignment[task_idx] = person_idx
            assign_tasks(task_idx + 1, person_times, current_assignment)
            person_times[person_idx] -= tasks[person_idx][task_idx][1]

    # Start the recursive assignment with an empty list of person times and assignments
    assign_tasks(0, [0] * num_people, [0] * num_tasks)

    return min_max_time, best_assignment


people, tasks = parse_input(input_str)
min_time, best_assignment = find_optimal_distribution(people, tasks)


for task_idx in range(len(tasks[0])):
    person_idx = best_assignment[task_idx]
    print(f"{tasks[person_idx][task_idx][0]}: {people[person_idx]}")


print(min_time) # Expected output: 67

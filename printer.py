from collections import deque

def solution(priorities, location):
    num_documents = len(priorities)
    priorities = deque(priorities)
    rotation_count = 0
    print_count = 0

    while priorities:
        priority = max(priorities)
        if priorities[0] < priority:
            priorities.append(priorities[0])
            priorities.popleft()
            rotation_count += 1
        else:
            priorities[0] = 0
            priorities.append(priorities[0])
            priorities.popleft()
            print_count += 1
            if (rotation_count + print_count - 1) % num_documents == location:
                return print_count

# Ryan Kelly (rpk2kn)

import urllib.request

def instructors(department):
    link = "http://cs1110.cs.virginia.edu/files/louslist/" + department.upper()
    stream = urllib.request.urlopen(link)
    teachers = set()
    for line in stream:
        decoded = line.strip().decode("UTF-8")
        entry = decoded.split("|")
        teachers.add(entry[4].strip("+1234567890"))
    instructor_list = list()
    for teacher in teachers:
        instructor_list.append(teacher)
    instructor_list.sort()
    return instructor_list

def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    link = "http://cs1110.cs.virginia.edu/files/louslist/" + dept_name.upper()
    stream = urllib.request.urlopen(link)
    classes = []
    include1, include2, include3, include4 = True, True, True, True
    for line in stream:
        decoded = line.strip().decode("UTF-8")
        entry = decoded.split("|")
        if has_seats_available:
            include1 = int(entry[15]) < int(entry[16])
        if level != None:
            include2 = str(entry[1])[0] == str(level)[0]
        if not_before != None:
            include3 = not_before <= int(entry[12])
        if not_after != None:
            include4 = not_after >= int(entry[12])
        if include1 and include2 and include3 and include4:
            classes.append(entry)
    return classes

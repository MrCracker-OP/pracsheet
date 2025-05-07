def process_data(data):
    if not data:
        return "No data to process."

    try:
        total = sum(data)
        average = total / len(data)
        return average
    except TypeError:
        return "Invalid data in list."

List1 = [1,2,3,4,5]
print(process_data(List1))

List2 = []
print(process_data(List2))

List1 = [1,2,3,"A",5]
print(process_data(List1))
from crime_data import crime_data

def mapper(data):
    return [(borough, stats['total_arrests']) for borough, stats in data.items()]

def reducer(mapped_data):
    reduced = {}
    for borough, arrests in mapped_data:
        reduced[borough] = reduced.get(borough, 0) + arrests
    return reduced

if __name__ == "__main__":
    mapped = mapper(crime_data)
    reduced = reducer(mapped)

    print("MapReduce Simulation: Total Arrests Per Borough")
    for borough, total in reduced.items():
        print(f"{borough}: {total}")

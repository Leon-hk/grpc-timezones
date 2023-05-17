import datetime

import grpc
from protos import timezones_pb2_grpc, timezones_pb2


# Instantiate stub class with local server
channel = grpc.insecure_channel('localhost:50051')
stub = timezones_pb2_grpc.TimeZonesStub(channel)

# Save timezones in a dictionary: {continent: {cities: offset} / general_timezone: offset}
timezones = {}
for timezone in stub.getTimezones(timezones_pb2.Empty()):
    elements = timezone.name.split("/")
    if len(elements) > 1:
        # continent/city
        if not timezones.__contains__(elements[0]):
            timezones[elements[0]] = {}
        timezones[elements[0]][elements[1]] = timezone.offset
    else:
        # general timezone
        timezones[timezone.name] = timezone.offset


def format_print(counter, region, timezone, value):
    string = str(counter) + " " * (4 - len(str(counter)))
    string += ": " + region + ", " + " " * (10 - len(str(region)))
    string += "cities" if timezone else "offset"
    string += ": " + str(value)
    print(string)


while True:
    # Select continent or general timezone
    counter = 0
    regions = []
    for region in timezones:
        counter += 1
        regions.append(region)
        if timezones[region].__class__ == 1.0.__class__:
            # general timezone
            format_print(counter, region, False, timezones[region])
        else:
            # continent
            format_print(counter, region, True, len(timezones[region]))

    pick = input("Pick a region or timezone: ")
    try:
        pick = int(pick)
        if 0 < pick <= counter:
            continent = regions[pick-1]
            break
    except:
        pass
    print("Choose a value between 1 and " + str(counter))

if timezones[continent].__class__ == 1.0.__class__:
    time = stub.getTime(timezones_pb2.TimeZone(name=continent, offset=timezones[continent]))
    print(continent + " is " + time.time)
else:
    while True:
        # Select city
        counter = 0
        cities = []
        for city in timezones[continent]:
            counter += 1
            cities.append(city)
            format_print(counter, city, False, timezones[continent][city])

        pick = input("Pick a city: ")
        try:
            pick = int(pick)
            if 0 < pick <= counter:
                ct = cities[pick-1]
                break
        except:
            pass
        print("Choose a value between 1 and " + str(counter))

    tz = continent + "/" + ct
    time = stub.getTime(timezones_pb2.TimeZone(name=tz, offset=timezones[continent][ct]))
    print("The local time in " + continent + " - " + ct + " is " + time.time)

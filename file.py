import json,copy

with open('drone_sequences/quad_simple/a.txt') as json_file:
    data = json.load(json_file)

points = data["points"]

print(points)



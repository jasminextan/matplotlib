import csv, matplotlib.pyplot

with open('astros.csv') as file:
    spacereader= csv.reader(file)
    inspace=list(spacereader)

iss = 0
tg = 0

for i in inspace:
    if i[1] == 'ISS':
        iss += 1
    if i[1] == 'Tiangong':
        tg += 1

stations = ['ISS','Tiangong']
statdata = [iss, tg]

matplotlib.pyplot.xlabel('Space Stations')
matplotlib.pyplot.ylabel('Number of People Currently There')
matplotlib.pyplot.bar(stations,statdata)
matplotlib.pyplot.show()
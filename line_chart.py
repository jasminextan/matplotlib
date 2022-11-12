import json, matplotlib.pyplot

with open('US.GDP.json', encoding= 'ascii') as f:
    text = f.read()
    usgdp_dict = json.loads(text)
    usgdp_data = usgdp_dict[1]

with open('CH.GDP.json', encoding= 'ascii') as f:
    text = f.read()
    chgdp_dict = json.loads(text)
    chgdp_data = chgdp_dict[1]

years = []
usgdp = []
chgdp = []

for i in range(len(usgdp_data)):
    years.append(usgdp_data[i]['date'])
    usgdp.append(usgdp_data[i]['value'])

for i in range(len(chgdp_data)):
    chgdp.append(chgdp_data[i]['value'])

years.reverse()
usgdp.reverse()
chgdp.reverse()

matplotlib.pyplot.plot (years, usgdp, label = "US")
matplotlib.pyplot.plot (years, chgdp, label = "China")
matplotlib.pyplot.legend(loc="upper left")
matplotlib.pyplot.xlabel ('Year')
matplotlib.pyplot.xticks(years)
matplotlib.pyplot.ylim(min(chgdp),max(usgdp))
matplotlib.pyplot.xticks(rotation=90, fontsize = 5)
matplotlib.pyplot.ylabel('GDP')
matplotlib.pyplot.title('US/China GDP Over Time')
matplotlib.pyplot.show()
import requests
from bs4 import BeautifulSoup
import csv



team1 = []
team2 = []
winner = []
margin = []
ground = []
date = []

years = [f"{year}-{year}" for year in range(2011, 2024)]


for year in years:

    page = requests.get("https://www.espncricinfo.com/records/year/team-match-results/" + year + "/one-day-internationals-2")
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for row in rows:
        data = row.find_all('span')
        
        team1.append(data[0].get_text())
        team2.append(data[1].get_text())
        winner.append(data[2].get_text())
        margin.append(data[3].get_text())
        ground.append(data[4].get_text())
        date.append(data[6].get_text())



data = list(zip(team1, team2, winner, margin, ground, date))

csv_file_name = "results.csv"
with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["team1", "team2", "winner", "margin", "ground", "date"])

    writer.writerows(data)
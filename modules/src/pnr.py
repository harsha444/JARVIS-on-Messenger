import os
import json
import bs4
import requests

def process():
	pnr_number = input("Enter the pnr number: ")
	res = requests.get('http://www.railyatri.in/pnr-status/' + str(pnr_number))
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	# print(soup)
	booked_time_stats = []
	current_stats = []
	i=2
	# To check the status at the booking time
	while(1):
		temp_booked = soup.select('#result > ul > table:nth-of-type(2)  > tr:nth-of-type('+str(i)+') > td:nth-of-type(2)')
		temp_current = soup.select('#result > ul > table:nth-of-type(2)  > tr:nth-of-type('+str(i)+') > td:nth-of-type(3)')
		if(temp_booked != []):
			booked_time_stats.append(temp_booked[0].text.strip())
			current_stats.append(temp_current[0].text.strip())
			i+=1
		else:
			break

	# If pnr nummber is invalid
	if(booked_time_stats == []):
		print("Enter a valid pnr number")
	print(booked_time_stats)
	print(current_stats)
	# print(soup.select('#result > ul > table:nth-of-type(2)  > tr:nth-of-type(2) > td:nth-of-type(3)'))
	for i in range(len(booked_time_stats)):
		print('Passenger '+str(i+1)+' booking time status : ' + booked_time_stats[i] + ' and current status: ' + current_stats[i])

process()

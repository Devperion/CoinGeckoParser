import requests
from fake_useragent import UserAgent
import json
from google_sheets import update_data_from_json
import time
import logging

ua = UserAgent()

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S', level=logging.WARNING)

def get_info_1():
	url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false"
	headers = {'user-agent': f'{ua.random}'}
	response = requests.get(url=url, headers=headers)

	with open("data_part_1.json", "w", encoding='utf8') as file:
		json.dump(response.json(), file, indent=4, ensure_ascii=False)

def get_info_2():
	url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=2&sparkline=false"
	headers = {'user-agent': f'{ua.random}'}
	response = requests.get(url=url, headers=headers)

	with open("data_part_2.json", "w", encoding='utf8') as file:
		json.dump(response.json(), file, indent=4, ensure_ascii=False)

def get_info_all():
	get_info_1()
	with open("data_part_1.json", encoding='utf8') as file:
		file1 = file.read()

	get_info_2()
	with open("data_part_2.json", encoding='utf8') as file:
		file2 = file.read()

	file1 += file2
	file1 = file1.replace("][", ",")

	with open ('data.json', 'w') as file: 
		file.write(file1)


def main():
	while True:
		get_info_all()
		update_data_from_json("data.json")
		logging.warning('Update completed')
		time.sleep(60 * 5)

if __name__ == "__main__":
	main()
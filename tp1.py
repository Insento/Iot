#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

import requests
import sys

demande = 'LIST'

while demande == 'LIST':

	req = requests.get('https://www.cryptocompare.com/api/data/coinlist/').json()

	print('La liste des crypto est dispo en tappant LIST')
	print('La valeur d une crypto est dispo en tappant son nom (sensible à la CASSE)')

	demande = input()
	if demande == 'LIST':
		result = requests.get('https://www.cryptocompare.com/api/data/coinlist/').json()
		datas = result['Data']
		for data in datas:
			print(data)
	else :
		result = requests.get('https://min-api.cryptocompare.com/data/price?fsym='+demande+'&tsyms=BTC,USD,EUR').json()

		print(result)

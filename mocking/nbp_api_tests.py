import datetime
import json
from unittest import mock

import pytest

from nbp_api import get_exchange_rate, NoData


JSON = """[{"table":"A","no":"217/A/NBP/2019","effectiveDate":"2019-11-08","rates":[{"currency":"bat (Tajlandia)","code":"THB","mid":0.1272},{"currency":"dolar amerykański","code":"USD","mid":3.8625},{"currency":"dolar australijski","code":"AUD","mid":2.6533},{"currency":"dolar Hongkongu","code":"HKD","mid":0.4935},{"currency":"dolar kanadyjski","code":"CAD","mid":2.9263},{"currency":"dolar nowozelandzki","code":"NZD","mid":2.4520},{"currency":"dolar singapurski","code":"SGD","mid":2.8406},{"currency":"euro","code":"EUR","mid":4.2638},{"currency":"forint (Węgry)","code":"HUF","mid":0.01278},{"currency":"frank szwajcarski","code":"CHF","mid":3.8797},{"currency":"funt szterling","code":"GBP","mid":4.9476},{"currency":"hrywna (Ukraina)","code":"UAH","mid":0.1577},{"currency":"jen (Japonia)","code":"JPY","mid":0.035324},{"currency":"korona czeska","code":"CZK","mid":0.1669},{"currency":"korona duńska","code":"DKK","mid":0.5706},{"currency":"korona islandzka","code":"ISK","mid":0.030964},{"currency":"korona norweska","code":"NOK","mid":0.4221},{"currency":"korona szwedzka","code":"SEK","mid":0.3991},{"currency":"kuna (Chorwacja)","code":"HRK","mid":0.5739},{"currency":"lej rumuński","code":"RON","mid":0.8956},{"currency":"lew (Bułgaria)","code":"BGN","mid":2.1800},{"currency":"lira turecka","code":"TRY","mid":0.6713},{"currency":"nowy izraelski szekel","code":"ILS","mid":1.1053},{"currency":"peso chilijskie","code":"CLP","mid":0.005206},{"currency":"peso filipińskie","code":"PHP","mid":0.0764},{"currency":"peso meksykańskie","code":"MXN","mid":0.2012},{"currency":"rand (Republika Południowej Afryki)","code":"ZAR","mid":0.2603},{"currency":"real (Brazylia)","code":"BRL","mid":0.9419},{"currency":"ringgit (Malezja)","code":"MYR","mid":0.9344},{"currency":"rubel rosyjski","code":"RUB","mid":0.0605},{"currency":"rupia indonezyjska","code":"IDR","mid":0.00027562},{"currency":"rupia indyjska","code":"INR","mid":0.054185},{"currency":"won południowokoreański","code":"KRW","mid":0.003337},{"currency":"yuan renminbi (Chiny)","code":"CNY","mid":0.5523},{"currency":"SDR (MFW)","code":"XDR","mid":5.2969}]}]"""
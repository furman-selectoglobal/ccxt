# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.foxbit import foxbit


class surbitcoin(foxbit):

    def describe(self):
        return self.deep_extend(super(surbitcoin, self).describe(), {
            'id': 'surbitcoin',
            'name': 'SurBitcoin',
            'countries': ['VE'],
            'has': {
                'CORS': False,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/27991511-f0a50194-6481-11e7-99b5-8f02932424cc.jpg',
                'api': {
                    'public': 'https://api.blinktrade.com/api',
                    'private': 'https://api.blinktrade.com/tapi',
                },
                'www': 'https://surbitcoin.com',
                'doc': 'https://blinktrade.com/docs',
            },
            'options': {
                'brokerId': '1',  # https://blinktrade.com/docs/#brokers
            },
        })

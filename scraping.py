# prepare review csv to analysis.
import os
import numpy as np
import pandas as pd
import requests
import sys
import time

from bs4 import BeautifulSoup

import modules


def make_reputation_csv(AREA_URL='https://travel.rakuten.co.jp/yado/aichi/A.html'):
    try:
        soup_area = modules.get_soup(AREA_URL)
        hotels = soup_area.select('section > div.htlHead> div.info > span')


        for hotel in hotels:

            hotel_ID = hotel['id'][-6:]
            hotel_review_url = f'https://travel.rakuten.co.jp/HOTEL/{hotel_ID}/review.html'

            # get data souce
            soup_hotel = modules.get_soup(hotel_review_url)

            # hotel name
            hotel_name = soup_hotel.select("#RthNameArea > h2")[0].text

            _reputations, _comments, _purposes, _companions, _dates = modules.make_object_lists(soup_hotel)

            # make df and to csv
            data = pd.DataFrame(
                        {'HotelName': hotel_name,
                         'Date': _dates, 
                         'Reputations': _reputations, 
                         'Comments': _comments, 
                         'Purposes': _purposes, 
                         'companions': _companions}
                    ).to_csv(f'./sample_csv/{hotel_ID}_reputation.csv', encoding='utf-8', index=False)

            time.sleep(2)
    except:
        print('実行は終了されました')


if __name__ == '__main__':
    if not os.path.exists('./sample_csv'):
        os.mkdir('./sample_csv')
    # エリアURLからホテルIDを一括で取得する
    # AREA_URL = 'https://travel.rakuten.co.jp/yado/aichi/A.html'
    try:
        AREA_URL = sys.argv[2]
        make_reputation_csv(AREA_URL)
    except:
        AREA_URL='https://travel.rakuten.co.jp/yado/aichi/A.html'
        make_reputation_csv(AREA_URL)
import numpy as np
import requests
import time

from bs4 import BeautifulSoup


def get_soup(url):
    """
    get the soup from url
    
    parameter:
        url: str you put the url from the rakuten travel website
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # save sever load
    time.sleep(2)
    return soup


def unpack_list(list):
    return [value for lst in list for value in lst]


def make_object_lists(soup_hotel):
    """
    Make the column list
    
    Parameter:
        soup_hotel: soup you make BeautifulSoup from hotel url
    
    Return 
        reputations, 
        comments, 
        purposes, 
        companions, 
        dates
    """
    
    # paging number
    page_number = soup_hotel.select('ul.pagingNumber > li > a')[-2].text
    
    _reputations = []
    _comments = []
    _purposes = []
    _companions = []
    _dates = []

    # to use the format in for-loop 
    format_url = soup_hotel.select('ul.pagingNumber > li > a')[0]['href'][:-2]

    # get all data of all pages
    page_number = range(int(page_number))
    
    for page_num in page_number:

        url = format_url+str(page_num*20)

        # get each data source
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(response.status_code)
        # save the server load
        time.sleep(np.random.randint(3, 10))

        _reputations.append([reputation.text for reputation in soup.select('p.commentRate > span.rate')])
        _comments.append([comment.text for comment in soup.select('dl.commentReputation > dd > p.commentSentence')])
        _purposes.append([purpose.text for purpose in soup.select('dl.commentPurpose > dd')[::3]])
        _companions.append([companion.text for companion in soup.select('dl.commentPurpose > dd')[1::3]])
        _dates.append([date.text for date in soup.select('dl.commentPurpose > dd')[2::3]])
        
    reputations = unpack_list(_reputations)
    comments = unpack_list(_comments)
    purposes = unpack_list(_purposes)
    companions = unpack_list(_companions)
    dates = unpack_list(_dates)
        
    return reputations, comments, purposes, companions, dates

    
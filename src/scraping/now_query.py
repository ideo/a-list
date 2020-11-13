import requests
from bs4 import BeautifulSoup
import re
import time
import random
import pandas as pd

from seleniumrequests import Chrome
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


def make_first_post_data(search = "jim hackett"):

    return {
        "chartx4": "n",
        "chooser": "seq",
        "clickType": "w",
        "allcoll": "n",
        "bigNgrams": "n",
        "isVC": "n",
    #     "whatdo":
    #     "whatdo1":
    #     "showHelp":
        "wl": 4,
        "wr": 4,
    #     "w1a":
        "p": search,
    #     "posDropdown":
    #     "posDropdown1":
    #     "w1b":
        "posWord2Dropdown": "Insert PoS",
    #     "w2":
        "posColDropdown": "Insert PoS",
        "submit1": "Find matching strings",
    #     "datepicker1":
    #     "datepicker2":
        "sec1": 0,
        "sec2": 0,
        "sortBy": "freq",
        "sortByDo2": "freq",
        "minfreq1": "freq",
        "freq1": 30,
        "freq2": 0,
        "numhits": 100,
        "kh": 200,
        "groupBy": "words",
        "whatshow": "raw",
        "saveList": "no",
        "ownsearch": "y",
    #     "changed":
    #     "word":
    #     "sbs":
    #     "sbs1":
    #     "sbsreg1":
    #     "sbsr":
    #     "sbsgroup":
    #     "redidID":
    #     "compared":
    #     "holder":
        "waited": "y",
    #     "user":
        "s1": 0,
        "s2": 0,
        "s3": 0,
        "perc": "mi",
    #     "r1":
    #     "r2":
        "didRandom": "y",
    }

def make_first_query(search):

    a = "/now/x3.asp?xx=1"
    b = ""
    for i, w in enumerate(search.split(), start=1):
        b += f"&w1{i}={w}"
    c = "&r="

    return a + b + c


def pull_page_number(s):

    p = re.findall(pattern="p=\d{,}", string=s)
    try:
        return int(p.pop().strip('p='))
    except:
        return None


def parse_page_table(pagenation_table):

    if "FIND SAMPLE" not in pagenation_table.text:
        print('Something is off with this pagenation table')


    begin_ref = ""
    prev_ref = ""
    next_ref = ""
    end_ref = ""

    for i, el in enumerate(pagenation_table.find('td')):
        if el.name in [None, 'br', 'font']:
            continue


        t = el.text.strip()
        if "<<" in t:
            begin_ref = el.get('href')
        elif t == "<":
            prev_ref = el.get('href')
        elif t == ">":
            next_ref = el.get('href')
        elif t == ">>":
            end_ref = el.get('href')


    p_prev = pull_page_number(prev_ref)
    p_next = pull_page_number(next_ref)
    try:
        current = int(( p_prev + p_next) / 2)
    except:
        current = 0

    parsed_info = {
        "begin_ref": begin_ref,
        "prev_ref": prev_ref,
        "next_ref": next_ref,
        "end_ref": end_ref,

        "prev_page": p_prev,
        "next_page": p_next,
        "current_page": current,
        "last_page": pull_page_number(end_ref),
    }

    return parsed_info

def parse_cols(cols):
    clean_cols = {}

    # 0. Index
    clean_cols['n'] = cols[0].text.strip()
    clean_cols['now_url'] = cols[0].find('a').get('href')


    # 1. Date + Country
    d = cols[1].text.strip()
    try:
        date, country = d.split()
    except:
        print(f'failed dateparse for {d}')
        date = d
        country =""
    clean_cols['date'] = date
    clean_cols['country'] = country

    # 2. Source
    clean_cols['source'] = cols[2].text.strip()
    clean_cols['source_url'] = cols[2].find('a').get('href')

    # 3-5. A,B,C ?
    # not sure what the deal is but saving it on the off chance that it has something?
    clean_cols['A'] = cols[3].text.strip()
    clean_cols['B'] = cols[4].text.strip()
    clean_cols['C'] = cols[5].text.strip()

    # 6. Text
    clean_cols['text'] = cols[6].text.strip()

    return clean_cols


def parse_data_table(table_element):

    rows = table_element.find_all('tr')
    table_data = []
    for r in rows:
        cols = r.find_all('td')
        clean_cols = parse_cols(cols)
        table_data.append(clean_cols)

    return pd.DataFrame(table_data)


def parse_query_response(response):
    soup = BeautifulSoup(response.text, 'html.parser')

    tables = soup.find_all('table')
    if len(tables) != 3:
        print('something is wrong with request response!')
        print(f'instead of 3 tables there are {len(tables)}')

    pagenation_table = tables[0]
    data_table = tables[2]

#     print(pagenation_table)

    pages = parse_page_table(pagenation_table)
    df = parse_data_table(data_table).set_index('n')
    return pages, df

def query_request(driver, query, last_query="/now/x2.asp"):

    headers = {
    "authority": "www.english-corpora.org",
    "method": "GET",
    "path": query,
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    # "cookie": "ASPSESSIONIDQETSSSSC=ANKHABECPLDCDBDEBHMKLEOD; _ga=GA1.2.1965950862.1605208178; _gid=GA1.2.1109076247.1605208178; ii=0",
    "referer": f"https://www.english-corpora.org{last_query}",
    "sec-fetch-dest": "frame",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",


    }
    request = driver.request('GET',
                        f"https://www.english-corpora.org/now/x3.asp?{query}",
                        headers=headers)
    return request

# pagenation_table = tables[0]
# pages = parse_page_table(pagenation_table)

# df = parse_data_table(data_table).set_index('n')
# df.shapes
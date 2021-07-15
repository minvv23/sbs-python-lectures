#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
import sys, os, glob
import requests, urllib.request, urllib.parse
import numpy as np, pandas as pd
import json
import time
from tqdm import tqdm
from itertools import chain
from collections import Counter

basic_header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
                "Accept":"text/html,application/xhtml+xml,application/xml;\q=0.9,imgwebp,*/*;q=0.8"}


# In[2]:



def str_palindrome_detector(x) :
    x_str = str(x)
    output_list = []
    for index in range(len(x_str)) :
        if x_str[index]==x_str[-(index+1)] :
            output = True
        else :
            output = False
        output_list.append(output)
    return print(all(output_list))


# In[ ]:


def url_to_soup(url) :
    session = requests.Session() #200
    req = session.get(url, headers=basic_header, allow_redirects=True)
    soup = BeautifulSoup(req.text, 'lxml')
    return soup


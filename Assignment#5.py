#!/usr/bin/env python
# coding: utf-8

# In[2]:


import argparse
import urllib.request
import csv
import re
import time

URL = "http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv"


def simulate_one_server(file_name):
    urllib.request.urlretrieve(URL, 'requests.csv')
    exec_time_list = []
    wait_time = []
    with open(file_name, 'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            wait_time.append(line[0:1])
            exec_time_list.append(line[2:3])
    exec_time_flat_list = [int(item) for sublist in exec_time_list for item in sublist]
    sum_exec_time = sum(exec_time_flat_list)
    wait_time_flat_list = [int(item) for sublist in wait_time for item in sublist]
    wait_time = [t - s for s, t in zip(wait_time_flat_list, wait_time_flat_list[1:])]
    sum_wait_time = sum(wait_time)
    row_count = sum(1 for line in open('requests.csv'))
    math = (sum_exec_time + sum_wait_time)/row_count
    print("average wait time for a request is {}".format(math))
    f.close()


def main_function():
    required_args = ['file_name']
    optional_args = ['servers']

    parser = argparse.ArgumentParser()
    for r in required_args:
        parser.add_argument("--{0}".format(r), required=True)
    for r in optional_args:
        parser.add_argument("--{0}".format(r), required=False)
    args = parser.parse_args()
    if args.servers:
        simulate_many_servers()
    simulate_one_server(args.file_name)


def simulate_many_servers():
    print("many")


# In[4]:


main_function


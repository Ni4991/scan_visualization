#!/usr/bin/env python

"""scan.py: Do network scanning and present the information in a graphical manner."""

# File:           scan.py
# Author:         Ni Luo
# Github:         Ni4991
# Date Created:   2018-03-21
# Date Modified:  2018-03-22
# Python Version: 3.6
#
# Purpose:        This is a program that visualizes csv data obtained from Wireshark. It plots the count of the types
#                 of packets and plots them in a bar graph.

import pandas as pd
import matplotlib.pyplot as plt
import sys


def run():
    
    pcap_data = pd.read_csv(sys.argv[1], index_col='No.')

    df = pcap_data.groupby('Source')['Source'].count().reset_index(name='count') \
                             .sort_values(['count'], ascending=False)
    df.plot(kind='bar')


    x = []
    label_x = []
    for index, row in df.iterrows():
       x.append(index)
       label_x.append(row['Source'])


    plt.title("IP Traffic by packages")
    plt.subplots_adjust(bottom=0.2)
    plt.xticks(x, label_x)
    plt.show()




if __name__ == '__main__':
    run()

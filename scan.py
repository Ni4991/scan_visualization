#!/usr/bin/env python

"""scan.py: Do network scanning and present the information in a graphical manner."""

__author__ = "Ni Luo"
__reference__ = "https://github.com/rshk/python-pcapng"

import pandas as pd
import matplotlib.pyplot as plt


def run():
    
    pcap_data = pd.read_csv('dump.csv', index_col='No.')

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

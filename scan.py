#!/usr/bin/env python

"""scan.py: Do network scanning and present the information in a graphical manner."""

__author__ = "Ni Luo"
__reference__ = "https://github.com/rshk/python-pcapng"

import pandas as pd
import matplotlib.pyplot as plt


def run():
    
    pcap_data = pd.read_csv('dump.csv', index_col='No.')

    df = pcap_data.groupby('Protocol')['Protocol'].count()

    df.plot(kind='bar')

    plt.show()


if __name__ == '__main__':
    run()

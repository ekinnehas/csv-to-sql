#!/usr/bin/python

import csv
import re
import sys


def get_distinct_client_count(client_list):
    dictionary = {}

    for client in client_list.values():
        dictionary[client] = 0
        for value in client_list.values():
            if client == value:
                dictionary[value] += 1
    return dictionary


def get_client_distinct_songs(pairs, client_ids):
    clients_distinct_songs = {}

    for client in client_ids:
        songs = set()
        for pair in pairs:
            if pair['CLIENT_ID'] == client:
                songs.add(pair['SONG_ID'])

        clients_distinct_songs[client] = len(songs)

    return clients_distinct_songs


def get_distinct_clients(pairs):
    client_ids = set()

    for item in pairs:
        client_ids.add(item['CLIENT_ID'])

    return client_ids


def get_list(reader):
    total_list = []
    date = '10/08/2016'
    regex = re.compile(date + '*')

    for row in reader:
        if re.findall(regex, row['PLAY_TS']):
            new_list = {'SONG_ID': int(row['SONG_ID']), 'CLIENT_ID': int(row['CLIENT_ID'])}
            total_list.append(new_list)

    return total_list


def main():
    with open('exhibitA-input.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')

        pairs = get_list(reader)
        client_ids = get_distinct_clients(pairs)
        client_list = get_client_distinct_songs(pairs, client_ids)
        distinct_counts = get_distinct_client_count(client_list)

	sys.stdout = open("Q1_Output.csv", "w+")
        print('{:>20s} {:>20s}'.format("DISTINCT_PLAY_COUNT", "CLIENT_COUNT"))
        for key in distinct_counts:
            print('{:>20d} {:>40d}'.format(key, distinct_counts[key]))


if __name__ == "__main__":
    main()

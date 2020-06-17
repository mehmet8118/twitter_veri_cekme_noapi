# -*- coding: utf-8 -*-
__author__ = 'mehmet şerif paşa'


import requests
import os
import sys
import json
import time


headers = {
    'Connection': 'close',
    'x-csrf-token': '',
    'Authorization': '',
    'Accept': '*/*',
    'User-Agent':'',
    'x-twitter-auth-type': 'OAuth2Session',
    'Cookie': '',

}




class sel:

    def __init__(self):
        pass

    def twitter_data(self,name,cursor=-1):
        self.name = name
        self.cursor = cursor

        self.req = requests.get("https://api.twitter.com/1.1/followers/list.json?cursor=" + str(self.cursor) +"&screen_name="+ str(self.name) +"&count=200", headers=header)
        self.veriler = self.req.text
        return self.veriler


dosya = open("veriler.txt", "w+")

a = -1

while True:

    veriler = sel().twitter_data(str(sys.argv[1]), a)
    json_veriler = json.loads(veriler)
    cursor = int(json_veriler['next_cursor'])
    user = json_veriler['users']


    for i in range(len(user)):

        kullanici_adi = user[i]['screen_name']
        kullanici_name = user[i]['name']
        location = user[i]['location']
        description = user[i]['description']
        takipci_sayisi = user[i]['normal_followers_count']
        takip_edilen = user[i]['friends_count']

        dosya.writelines(
                         "\nKullanıcı Adı: "+ kullanici_adi+" | \n"+
                         "İsmi: "+" | \n"+
                         "Lokasyon: " + location+" | \n"+
                         "Açıklama: " + description+" | \n"+
                         "Takipçi Sayisi: " + str(takipci_sayisi) + " | \n" +
                         "Takip Edilen: " + str(takip_edilen) + " | \n"
                            )


    if cursor == 0:

        break

    else:

        a = cursor
        continue







import os,sys,time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from colorama import init, Fore
init()
n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

def legend_dev():
    import random
    legend = [
 "          _                                _ _           ",
 "  __ _ ___| |_ _ __ __ _ _ __ ___   ___  __| (_) __ _ ___ ",
 " / _` / __| __| '__/ _` | '_ ` _ \ / _ \/ _` | |/ _` / __|",
 "| (_| \__ \ |_| | | (_| | | | | | |  __/ (_| | | (_| \__ \\",
 " \__,_|___/\__|_|  \__,_|_| |_| |_|\___|\__,_|_|\__,_|___/"]

    for dev in legend:
        print(f'{random.choice(colors)}{dev}{n}')
legend_dev()
def LEGEND_DEVty(message):
    for legend in message:
        sys.stdout.write(legend)
        sys.stdout.flush()
        time.sleep(0.02)
LEGEND_DEVty('========Buy Tool: T.me/UserMedias\n')
LEGEND_DEVty('========Developer : www.astramedias.com\n')
LEGEND_DEVty('Loading.....')
LEGEND_DEVty('.'*56+'100%\n')

colorama.init(autoreset=True)
print(Style.BRIGHT + Fore.RESET + 'Welcome To ASTRAMEDİAS Program\n')
import subprocess, requests, time, os


# hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
# r = requests.get('https://gist.github.com/cparty5858/ba548daca747027f938bc690c03a49c2')


print(Style.BRIGHT + Fore.GREEN + 'Bir Seçenek Belirleyin: ')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [1] Giriş Yap')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [2] BanFilresi + Banlı Numaraları Silme')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [3] Spamlı Numaraları Kontrol Etme + Ayırma')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [4] Grup Listesini Çekme')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [5] Gizli Gruba Giriş')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [6] Günlük Filtreleme')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [7] Haftalık Filtreleme')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [8] Grubun Mevcut Üyelerini Sil')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [9] Profil Resmi Ekle')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [10] Profil Resmi Silme')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [11] İsim,Soyisim Kullanıcı Adı Güncelle')
print(Style.BRIGHT + Fore.GREEN + 'Rehber Seçenekleri:')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [12] Rehbere Ekle - Telefon İçin')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [13] Pc Oto Kişi Rehbere ekle - Bilgisayar İçin')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [14] Kayıtlı Kişileri Sil')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [15] Çoklu Ekleyici')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [16] Tekli Ekleyici')
print(Style.BRIGHT + Fore.GREEN+ 'Grup Üyesi Ekleme Seçenekleri: ')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [17] Tekli Ekleyici')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [18] Telefon İçin Ekleyici')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [19] Çoklu Ekleme')
print(Style.BRIGHT + Fore.GREEN + 'Mesaj Gönderme Seçenekleri: ')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [20] Mesaj Gönderme')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [21] Çoklu Mesaj Gönder')
print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '                 [22] Çıkış')
This_is_normal_script_by_legend_dev = int(input('\nLütfen Seçenek Girin: '))

def login1():
    from telethon.sync import TelegramClient
    from telethon import utils
    import csv
    from csv import reader
    import configparser
    import colorama
    from colorama import Fore, Back, Style
    legend_devpost()


    colorama.init(autoreset=True)

    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1

            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            client = TelegramClient(f"sessions/{phone}", 2392599, '7e14b38d250953c8c1e94fd7b2d63550')
            client.start(phone)
            client.disconnect()
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to Exit')
    input()
def banfilter():
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()
    from telethon.sync import TelegramClient
    from telethon import utils
    from telethon.errors.rpcerrorlist import PhoneNumberBannedError
    import csv
    import configparser

    api_id = int(2392599)
    api_hash = str('7e14b38d250953c8c1e94fd7b2d63550')
    MadeByRexhacks = []

    done = False
    with open('phone.csv', 'r') as f:
        str_list = [row[0] for row in csv.reader(f)]

        po = 0
        for unparsed_phone in str_list:
            po += 1

            phone = utils.parse_phone(unparsed_phone)

            print(f"Login {phone}")
            client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
            # client.start(phone)
            client.connect()
            if not client.is_user_authorized():
                try:
                    print('This Phone Has Been Revoked')
                    rexhacks = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByRexhacks.append(Nero_op)
                    continue

                except PhoneNumberBannedError:
                    print('Ban')
                    rexhacks = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByRexhacks.append(Nero_op)

                    continue

            # client.disconnect()
            print()
        done = True
        print('List Of Banned Numbers')
        print(*MadeByRexhacks, sep='\n')
        print('Saved In BanNumers.csv')
        with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(MadeByRexhacks)


    def autoremove():
        import csv
        import os

        collection = []
        nc = []
        collection1 = []
        nc1 = []
        maind = []

        with open("phone.csv", "r") as infile:
            for line in infile:
                collection.append(line)

        for x in collection:
            mod_x = str(x).replace("\n", "")
            nc.append(mod_x)

        with open("BanNumbers.csv") as infile, open("outfile.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))

        with open("outfile.csv", "r") as outfile:
            for line1 in outfile:
                collection1.append(line1)

        for i in collection1:
            mod_i = str(i).replace("\n", "")
            nc1.append(mod_i)

        unique = set(nc)
        unique1 = set(nc1)

        itd = unique.intersection(unique1)

        for x in nc:
            if x not in itd:
                maind.append(x)

        with open('unban.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(maind)

        with open("unban.csv") as last, open("phone.csv", "w") as final:
            for line3 in last:
                mod_i = str(line3).replace("\n", "")
                final.write(mod_i)

        os.remove("phone.csv")
        os.rename("unban.csv", "phone.csv")
        print("Done,All Banned Number Have Been Removed")


    def dellst():
        import csv
        import os

        with open("phone.csv") as infile, open("unban.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))

        os.remove("phone.csv")
        os.rename("unban.csv", "phone.csv")

        print("complete")


    autoremove()
    dellst()

    input("Done!" if done else "Error!")
def spambotch():
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()
    from telethon.sync import TelegramClient
    from telethon.sync import TelegramClient
    from telethon import functions, types
    from telethon import utils
    from telethon.errors.rpcerrorlist import YouBlockedUserError
    import csv
    import time
    from csv import reader
    import configparser
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
    import subprocess, requests, time, os


    bot = 'SpamBot'
    rexhacks = "bird"
    MadeByRexhacks = []
    r = 0
    done = False
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {Style.RESET_ALL} {Style.BRIGHT + Fore.RESET} {phone}")
            client = TelegramClient(f"sessions/{phone}", 2392599, '7e14b38d250953c8c1e94fd7b2d63550')
            client.start(phone)
            client(functions.contacts.UnblockRequest(id='@SpamBot'))
            client.send_message(bot, '/start')
            time.sleep(1)
            msg = client.get_messages(bot)
            for message in msg:
                print(message.message)
            AstraMedias = str(msg)
            if rexhacks in AstraMedias:
                r += 1
            else:
                print('you are limited')
                Nero_op = str(pphone)
                MadeByRexhacks.append(Nero_op)
            client.disconnect()
            print()
            done = True
        print('List Of limited Numbers')
        print(*MadeByRexhacks, sep='\n')
    print(f'{r} - Accounts Are Usable')
    with open('legend1.csv', 'w', encoding='UTF-8') as writeFile:
        writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")
        writer.writerows(MadeByRexhacks)

    def forremove():
        import csv
        import os
        collection = []
        nc = []
        collection1 = []
        nc1 = []
        maind = []
        with open("phone.csv", "r") as infile:
            for line in infile:
                collection.append(line)
        for x in collection:
            mod_x = str(x).replace("\n", "")
            nc.append(mod_x)
        print(Style.BRIGHT + Fore.GREEN + 'Enter The File Name Where You Want To Save Your Limited Numbers :')
        rexfile = input()
        with open("legend1.csv") as infile, open(f"{rexfile}.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))
        with open(f'{rexfile}.csv', "r") as outfile:
            for line1 in outfile:
                collection1.append(line1)
        for i in collection1:
            mod_i = str(i).replace("\n", "")
            nc1.append(mod_i)
        unique = set(nc)
        unique1 = set(nc1)
        itd = unique.intersection(unique1)
        for x in nc:
            if x not in itd:
                maind.append(x)
        with open('legend2.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(maind)
        with open("legend2.csv") as last, open("phone.csv", "w") as final:
            for line3 in last:
                mod_i = str(line3).replace("\n", "")
                final.write(mod_i)
        os.remove("phone.csv")
        os.rename("legend2.csv", "phone.csv")
        print(Style.BRIGHT + Fore.RED + "Task Completed!!!!!!")

    def deletelist():
        import csv
        import os
        with open("phone.csv") as infile, open("legend2.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))

        os.remove("phone.csv")
        os.rename("legend2.csv", "phone.csv")
        os.remove("legend1.csv")

    forremove()
    deletelist()
    input("Done!" if done else "Error!")
def scraper1():
    from telethon.sync import TelegramClient
    import csv
    import configparser
    import logging, telethon
    from telethon.tl.functions.channels import JoinChannelRequest
    from telethon.tl.types import InputPeerEmpty, UserStatusOffline, UserStatusRecently, UserStatusLastMonth, \
        UserStatusLastWeek, PeerUser, PeerChannel
    from datetime import datetime, timedelta
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()
    import requests, time, os

    config = configparser.ConfigParser()
    config.read("config.ini")
    link1 = (config['AstraMedias']['FromGroup']).strip()
    links = link1.split(',')
    API_ID = 2392599
    HashID = '7e14b38d250953c8c1e94fd7b2d63550'
    phone = (config['AstraMedias']['PhoneNumber']).strip()

    logging.basicConfig(level=logging.WARNING)

    print(Style.BRIGHT + Fore.RESET + f'\nLogging For {phone}')
    try:
        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
        client.connect()
        if client.is_user_authorized():
            print(Style.BRIGHT + Fore.GREEN + f'login Done')
            count = 1
            today = datetime.now()
            last_week = today + timedelta(days=-7)
            last_month = today + timedelta(days=-30)
            f = open("data.csv", "w", encoding='UTF-8')
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])
            try:
                for link in links:
                    try:
                        client.get_entity(link)
                        pass
                    except Exception as e:
                        pass
                    print(Style.BRIGHT + Fore.YELLOW + f'Scrabing Members from {link} group.....')
                    all_participants = []
                    all_participants = client.get_participants(link, aggressive=True)
                    for user in all_participants:
                        if user.username:
                            username = user.username
                        else:
                            username = ""
                        if user.first_name:
                            name = user.first_name
                        else:
                            name = "Rexhacks"
                        if isinstance(user.status, UserStatusRecently):
                            date_online = today
                        else:
                            if isinstance(user.status, UserStatusLastMonth):
                                date_online = last_month
                            if isinstance(user.status, UserStatusLastWeek):
                                date_online = last_week
                            if isinstance(user.status, UserStatusOffline):
                                date_online = user.status.was_online
                        date_online_str = date_online.strftime("%Y%m%d")
                        writer.writerow([count, username, user.id, name, link, date_online_str])
                        count = count + 1
            except Exception as e:
                # print(1,e)
                pass
            f.close()
            print('Count : ', count)
        else:
            print(Style.BRIGHT + Fore.RED + f'login fail {phone}')
    except Exception as e:
        print(Style.BRIGHT + Fore.RED + f'login fail')

    # Filter by usname start from here
    lines = list()


    def main():
        lines = list()
        with open('data.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == '':
                        lines.remove(row)
        with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    def main1():
        lines = list()
        with open('1.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == 'username':
                        lines.remove(row)

        with open('2.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    main()
    main1()

    with open("2.csv", "r", encoding='UTF-8') as source:
        rdr = csv.reader(source)

        with open("data.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])
            i = 0
            for row in rdr:
                i += 1
                writer.writerow((i, row[1], row[2], row[3], row[4], row[5]))

    os.remove("1.csv")
    os.remove("2.csv")
    # os.remove("data.csv")
    print(Style.BRIGHT + Fore.GREEN + "Task completed")
    print(Style.BRIGHT + Fore.RESET + "Enter any key to exit")
    input()
def privategroupJoiner():
    import configparser
    from telethon.sync import TelegramClient
    from telethon.tl.functions.messages import ImportChatInviteRequest
    from telethon.errors import SessionPasswordNeededError
    config = configparser.ConfigParser()
    config.read("config.ini")
    API_ID = 2392599
    HashID = '7e14b38d250953c8c1e94fd7b2d63550'
    phone = (config['AstraMedias']['PhoneNumber']).strip()
    client = TelegramClient(f"sessions/{phone}", API_ID, HashID)

    client.connect()
    if not client.is_user_authorized():
        try:
            client.send_code_request(phone)
            client.sign_in(phone, input('Enter code: '))
            print('')
            client.sign_in(phone)
        except SessionPasswordNeededError:
            password = input('Enter password: ')
            print('')
            client.sign_in(password=password)

    gplink = input('Enter Private Group Hash : ')
    client(ImportChatInviteRequest(gplink))
    print('Joined Group Sucessfully........')
def dailyfilter():
    from telethon import TelegramClient, connection
    import logging, telethon
    from telethon import TelegramClient, sync
    from datetime import datetime, timedelta
    import csv, json
    from telethon.tl.types import PeerUser
    from telethon.tl.types import InputPeerEmpty, UserStatusOffline, UserStatusRecently, UserStatusLastMonth, \
        UserStatusLastWeek, PeerUser, PeerChannel
    import configparser
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()
    import requests, time, os


    def nfilter(client, link, last_day):
        today = datetime.now()
        last_week = today + timedelta(days=-7)
        last_month = today + timedelta(days=-30)
        today = today.strftime("%Y%m%d")
        a = [['sr. no.', 'username', 'user id', 'name', 'group', 'Status']]
        count = 1
        dialogs = client.get_dialogs()
        for i in link:
            print(Style.BRIGHT + Fore.RESET + f'Filter Members from {i} group.....')
            group = client.get_entity(i)
            try:
                all_participants = client.get_participants(group.id, aggressive=True)
            except Exception as e:
                continue
            for user in all_participants:
                if user.username != None:
                    try:
                        if isinstance(user.status, UserStatusRecently):
                            date_online = today
                        else:
                            if isinstance(user.status, UserStatusLastMonth):
                                date_online = last_month
                            if isinstance(user.status, UserStatusLastWeek):
                                date_online = last_week
                            if isinstance(user.status, UserStatusOffline):
                                date_online = user.status.was_online
                        date_online_str = date_online.strftime("%Y%m%d")
                        if (str(date_online_str) >= str(last_day)):
                            b = [count, str(user.username), str(user.id), str(user.first_name + ' ' + user.last_name),
                                 str(group.title), str(date_online_str)]
                            a.append(b)
                            count += 1
                    except:
                        pass
        if a:
            with open('data.csv', 'w', encoding="utf-8", newline='') as f:
                write = csv.writer(f)
                write.writerows(a)
        print('Members : ', count)
        client.disconnect()
        print()


    print(Style.BRIGHT + Fore.YELLOW + "\nEnter the day for filter :")
    n = int(input())
    n = n
    last_day = (datetime.now() + timedelta(days=-n)).strftime("%Y%m%d")
    dele = []

    config = configparser.ConfigParser()
    config.read("config.ini")
    links = (config['AstraMedias']['FromGroup']).strip()
    link = links.split(',')
    API_ID = 2392599
    HashID = '7e14b38d250953c8c1e94fd7b2d63550'
    phone = (config['AstraMedias']['PhoneNumber']).strip()

    logging.basicConfig(level=logging.WARNING)

    print(Style.BRIGHT + Fore.RESET + f'\nLogging For {phone}')
    try:
        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
        client.connect()
        if client.is_user_authorized():
            print(Style.BRIGHT + Fore.GREEN + f'login Done')
            a = nfilter(client, link, last_day)

        else:
            print(Style.BRIGHT + Fore.RED + f'{phone} login fail')
    except Exception as e:
        print(e)
        print(Style.BRIGHT + Fore.YELLOW + f'Please Enter Vailed Group')
    # username filter start from here
    lines = list()


    def main():
        lines = list()
        with open('data.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == '':
                        lines.remove(row)
        with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    def main1():
        lines = list()
        with open('1.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == 'username':
                        lines.remove(row)

        with open('2.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    main()
    main1()

    with open("2.csv", "r", encoding='UTF-8') as source:
        rdr = csv.reader(source)

        with open("data.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])
            i = 0
            for row in rdr:
                i += 1
                writer.writerow((i, row[1], row[2], row[3], row[4], row[5]))

    os.remove("1.csv")
    os.remove("2.csv")
    # os.remove("data.csv")
    print(Style.BRIGHT + Fore.GREEN + "Filter completed")
    print(Style.BRIGHT + Fore.YELLOW + "Enter any key to exit")
    input()
def weeklyfilter():
    from telethon import TelegramClient, connection
    import logging, telethon
    from telethon import TelegramClient, sync
    from datetime import datetime, timedelta
    import csv, json
    from telethon.tl.types import PeerUser
    from telethon.tl.types import InputPeerEmpty, UserStatusOffline, UserStatusRecently, UserStatusLastMonth, \
        UserStatusLastWeek, PeerUser, PeerChannel
    import configparser
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()
    import requests, time, os


    def nfilter(client, link, last_day):
        today = datetime.now()
        last_week = today + timedelta(days=-7)
        last_month = today + timedelta(days=-30)
        today = today.strftime("%Y%m%d")
        a = [['sr. no.', 'username', 'user id', 'name', 'group', 'Status']]
        count = 1
        dialogs = client.get_dialogs()
        for i in link:
            print(Style.BRIGHT + Fore.RESET + f'Filter Members from {i} group.....')
            group = client.get_entity(i)
            try:
                all_participants = client.get_participants(group.id, aggressive=True)
            except Exception as e:
                continue
            for user in all_participants:
                if user.username != None:
                    try:
                        if isinstance(user.status, UserStatusRecently):
                            date_online = today
                        else:
                            if isinstance(user.status, UserStatusLastMonth):
                                date_online = last_month
                            if isinstance(user.status, UserStatusLastWeek):
                                date_online = last_week
                            if isinstance(user.status, UserStatusOffline):
                                date_online = user.status.was_online
                        date_online_str = date_online.strftime("%Y%m%d")
                        if (str(date_online_str) >= str(last_day)):
                            b = [count, str(user.username), str(user.id), str(user.first_name + ' ' + user.last_name),
                                 str(group.title), str(date_online_str)]
                            a.append(b)
                            count += 1
                    except:
                        pass
        if a:
            with open('data.csv', 'w', encoding="utf-8", newline='') as f:
                write = csv.writer(f)
                write.writerows(a)
        print('counting : ', count)
        client.disconnect()
        print()


    print(Style.BRIGHT + Fore.YELLOW + "\nEnter the week for filter :")
    n = int(input())
    n = n * 7
    last_day = (datetime.now() + timedelta(days=-n)).strftime("%Y%m%d")
    dele = []

    config = configparser.ConfigParser()
    config.read("config.ini")
    links = (config['AstraMedias']['FromGroup']).strip()
    link = links.split(',')
    API_ID = 2392599
    HashID = '7e14b38d250953c8c1e94fd7b2d63550'
    phone = (config['AstraMedias']['PhoneNumber']).strip()

    logging.basicConfig(level=logging.WARNING)

    print(Style.BRIGHT + Fore.RESET + f'\nLogging For {phone}')
    try:
        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
        client.connect()
        if client.is_user_authorized():
            print(Style.BRIGHT + Fore.GREEN + f'Login Done')
            a = nfilter(client, link, last_day)

        else:
            print(Style.BRIGHT + Fore.RED + f'login fail {phone}')
    except Exception as e:
        print(e)
        print(Style.BRIGHT + Fore.YELLOW + f'Please Enter A Vailed Group')
    # Filter by usname start from here
    lines = list()


    def main():
        lines = list()
        with open('data.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == '':
                        lines.remove(row)
        with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    def main1():
        lines = list()
        with open('1.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == 'username':
                        lines.remove(row)

        with open('2.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    main()
    main1()

    with open("2.csv", "r", encoding='UTF-8') as source:
        rdr = csv.reader(source)

        with open("data.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])
            i = 0
            for row in rdr:
                i += 1
                writer.writerow((i, row[1], row[2], row[3], row[4], row[5]))

    os.remove("1.csv")
    os.remove("2.csv")
    # os.remove("data.csv")
    print(Style.BRIGHT + Fore.GREEN + "Filter completed")
    print(Style.BRIGHT + Fore.YELLOW + "Enter any key to exit")
    input()
def Deletealready():
    from telethon import TelegramClient, connection
    import logging, telethon
    from telethon import sync, TelegramClient, events
    from telethon.tl.functions.messages import GetDialogsRequest
    from telethon.tl.types import InputPeerEmpty, UserStatusOffline, UserStatusRecently, UserStatusLastMonth, \
        UserStatusLastWeek, PeerUser, PeerChannel
    import json
    from telethon.tl.functions.channels import GetChannelsRequest, GetFullChannelRequest, JoinChannelRequest, \
        InviteToChannelRequest
    from datetime import datetime, timedelta
    import csv, sys, time
    import configparser
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()
    import requests, time, os

    logging.basicConfig(level=logging.WARNING)

    config = configparser.ConfigParser()
    config.read("config.ini")
    link = (config['AstraMedias']['ToGroup']).strip()
    API_ID = 2392599
    HashID = '7e14b38d250953c8c1e94fd7b2d63550'
    phone = (config['AstraMedias']['PhoneNumber']).strip()

    # with open('data.csv', 'r' , encoding='utf-8') as f:
    #     existing_numbers = f.read().split('\n')
    #     print(type(existing_numbers))
    #     exit()

    with open('data.csv', 'r', encoding='utf-8') as f:
        users1 = csv.reader(f)
        users = [i for i in users1]

    with open('data.csv', 'r', encoding='utf-8') as f:
        users1 = csv.reader(f)
        userlist = [str(i[2]) for i in users1]

    client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
    client.connect()
    if not client.is_user_authorized():
        print(f'\nLogin fail, for number {phone} need Login first\n')
    else:
        chats = []
        last_date = None
        chunk_size = 200
        groups = []
        n = 0
        while n != -1:
            try:
                group = client.get_entity(link)
                if group.megagroup == True:
                    group_id = str(group.id)
                    all_participants = client.get_participants(group, aggressive=True)
                    results = []
                    results1 = []
                    count = 0
                    index1 = []
                    for user in all_participants:
                        try:
                            if str(user.id) in userlist:
                                index1.append(userlist.index(str(user.id)))
                        except:
                            print("Error get user")
                    f.close()
                    client.disconnect()
                    index1.sort(reverse=True)
                    for i in index1:
                        del users[i]
                    with open('data.csv', 'w', encoding="utf-8", newline='') as f:
                        write = csv.writer(f)
                        write.writerows(users)
                    n = -1
                else:
                    print(Style.BRIGHT + Fore.RED + "\nInvalid Group..\n")
                n = -1
            except telethon.errors.rpcerrorlist.ChatWriteForbiddenError:
                client(JoinChannelRequest(link))
            except ValueError:
                print(Style.BRIGHT + Fore.GREEN + "\nOnly Public Group Allowed..\n")
                n = -1
            except:
                print(Style.BRIGHT + Fore.RED + "\nInvalid Group....\n")
                n = -1
    # Filter by usname start from here
    lines = list()


    def main():
        lines = list()
        with open('data.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == '':
                        lines.remove(row)
        with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    def main1():
        lines = list()
        with open('1.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == 'username':
                        lines.remove(row)

        with open('2.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    main()
    main1()

    with open("2.csv", "r", encoding='UTF-8') as source:
        rdr = csv.reader(source)

        with open("data.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])
            i = 0
            for row in rdr:
                i += 1
                writer.writerow((i, row[1], row[2], row[3], row[4], row[5]))

    os.remove("1.csv")
    os.remove("2.csv")
    # os.remove("data.csv")

    print(Style.BRIGHT + Fore.RESET + "Already Member Deleted Done !")
    print(Style.BRIGHT + Fore.GREEN + 'Task Completed')
    print(Style.BRIGHT + Fore.YELLOW + "Press Enter to exit")
    input()
def addcontactforphone():
    from telethon.sync import TelegramClient
    import csv
    from telethon.tl.functions.messages import GetDialogsRequest
    from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, PeerUser
    from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, \
        UserAlreadyParticipantError
    from telethon.tl.functions.channels import InviteToChannelRequest
    from telethon import types, utils, errors, functions
    import configparser
    from telethon.errors.rpcerrorlist import UsernameInvalidError, ChannelInvalidError, PhoneNumberBannedError
    import re
    import os
    import traceback
    from csv import reader
    from telethon.sessions import StringSession
    from colorama import init, Fore

    init()
    r = Fore.LIGHTRED_EX
    gr = Fore.GREEN
    n = Fore.RESET
    bl = Fore.BLUE
    ye = Fore.YELLOW





    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


    clr()
    legend_devpost()

    api_id = []
    api_hash = []
    phone = []

    with open('phone.csv', 'r') as delta_obj:
        csv_reader = reader(delta_obj)
        list_of_phone = tuple(csv_reader)
        for phone_ in list_of_phone:
            phone.append(int(phone_[0]))


    pphone = phone

    print(f'{gr}Total account: {n} {r}{str(len(phone))}{n}')


    def autos():
        From = int(input(f'{bl}From Account No : {n}')) - 1
        Upto = int(input(f'{bl}Upto Account No : {n}'))
        rex = int(input(f'{bl}From where you want to start : {n}'))
        hacks = int(input(f'{bl}How many contacts you want to add in one Account : {n}'))

        with open('memory.csv', 'w', encoding='UTF-8') as file:
            writer = csv.writer(file, delimiter=",", lineterminator="\n")
            writer.writerow([rex, rex + hacks])
        a = 0
        indexx = 0
        for xd in pphone[From:Upto]:
            indexx += 1
            print(f'Index : {indexx}')
            phone = utils.parse_phone(xd)
            print(Style.BRIGHT + Fore.GREEN + f"Login {Style.RESET_ALL} {Style.BRIGHT + Fore.RESET} {phone}")
            client = TelegramClient(f"sessions/{phone}", 2392599, '7e14b38d250953c8c1e94fd7b2d63550')
            client.connect()
            if not client.is_user_authorized():
                print(f'{r}some thing has changed{n}')
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter the code: '))

            input_file = 'data.csv'
            users = []
            with open(input_file, encoding='UTF-8') as f:
                rows = csv.reader(f, delimiter=",", lineterminator="\n")
                next(rows, None)
                for row in rows:
                    user = {}
                    user['srno'] = row[0]
                    user['username'] = row[1]
                    user['id'] = int(row[2])
                    # user['access_hash'] = int(row[2])
                    user['name'] = row[3]
                    users.append(user)

            with open('memory.csv', 'r') as hash_obj:

                csv_reader = reader(hash_obj)

                list_of_rows = list(csv_reader)
                row_number = 1
                col_number = 1
                numnext = list_of_rows[row_number - 1][col_number - 1]

            startfrom = int(numnext)
            nextstart = startfrom + hacks

            with open('memory.csv', 'r') as hash_obj:
                csv_reader = reader(hash_obj)
                list_of_rows = list(csv_reader)
                row_number = 1
                col_number = 2
                numend = list_of_rows[row_number - 1][col_number - 1]

            endto = int(numend)
            nextend = endto + hacks

            with open("memory.csv", "w", encoding='UTF-8') as df:  # Enter your file name.

                writer = csv.writer(df, delimiter=",", lineterminator="\n")

                writer.writerow([nextstart, nextend])

            it = 0
            for user in users:
                if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
                    try:
                        it += 1
                        if user['username'] == "":
                            print(f"{r}no username, moving to next{n}")
                            continue

                        client(functions.contacts.AddContactRequest(
                            id=user['username'],
                            first_name=user['name'],
                            last_name='',
                            phone='gdf',
                            add_phone_privacy_exception=True))
                        status = f'{it} - done'





                    except errors.RPCError as e:
                        status = e.__class__.__name__





                    except:
                        traceback.print_exc()
                        print(f"{ye}Unexpected Error{n}")
                        continue

                    print(status)

            a += 1
        os.remove("memory.csv")
        again()


    def again():
        stat = input(f'{r}Done!\nChoose From Below:\n\n1 - Repeat The Script\nOR Just Hit Enter To Quit\n\nEnter: {n}')
        if stat == '1':
            autos()
        else:
            quit()


    autos()
def forpc():
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()

    print(Style.BRIGHT + Fore.YELLOW + "Go to Addcon folder and Run Automarge.py file")
    print(Style.BRIGHT + Fore.YELLOW + "Press Enter to exit")
    input()
def Deletecontact():
    from telethon.sync import TelegramClient
    import csv
    legend_devpost()
    from telethon.errors.rpcerrorlist import UsernameInvalidError, ChannelInvalidError, PhoneNumberBannedError
    from telethon.tl.functions.messages import ImportChatInviteRequest
    from telethon import types, utils, errors
    import re
    from telethon.tl.functions.channels import GetChannelsRequest, GetFullChannelRequest, JoinChannelRequest, \
        InviteToChannelRequest
    from telethon.tl.types import PeerChannel
    from telethon.tl.functions.contacts import GetContactsRequest, DeleteContactsRequest
    from telethon.tl.functions.messages import AddChatUserRequest
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)


    with open(f'phone.csv', 'r') as f:
        global phlist
        phlist = [row[0] for row in csv.reader(f)]
    print('Total account: ' + str(len(phlist)))

    Rexhacks_ne_script_banaya_hai = int(input('From Account No : ')) - 1
    telegram_script_banyane_ke_liye_rexhacks_ko_dm_kro = int(input('Upto Account No : '))
    indexx = 0
    global rexhackspro
    rexhackspro = 0
    for rexhacksonyt in phlist[Rexhacks_ne_script_banaya_hai:telegram_script_banyane_ke_liye_rexhacks_ko_dm_kro]:
        indexx += 1
        print(f'Index : {indexx}')
        phone = utils.parse_phone(rexhacksonyt)
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", 17476, '5bdea166e6097ce98a23')
        client.start(phone)

        contacts = client(GetContactsRequest(hash=0))

        rexadd = 0
        for rexop in contacts.users:
            rexadd += 1

            try:
                client(DeleteContactsRequest(id=[rexop]))
                print(Style.BRIGHT + Fore.GREEN + f"{rexadd} - {rexop.id} - DELETE")
            except errors.RPCError as e:
                erro = e.__class__.__name__
                print(f'{rexadd} - {rexop.id} - {erro}')
                continue
def legend_devpost():
    import random
    Legend = [
"            _                                _ _           ",
"   __ _ ___| |_ _ __ __ _ _ __ ___   ___  __| (_) __ _ ___ ",
"  / _` / __| __| '__/ _` | '_ ` _ \ / _ \/ _` | |/ _` / __|",
" | (_| \__ \ |_| | | (_| | | | | | |  __/ (_| | | (_| \__ \\",
"  \__,_|___/\__|_|  \__,_|_| |_| |_|\___|\__,_|_|\__,_|___/"]

    for dev in Legend:
        print(f'{random.choice(colors)}{dev}{n}')
    print(f'============Buy Tool : t.me/UserMedias{n}')
    print(f'============Developer : www.astramedias.com{n}')
def bulkadder():
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()

    from telethon.sync import TelegramClient
    import csv
    from telethon.errors.rpcerrorlist import UsernameInvalidError, ChannelInvalidError, PhoneNumberBannedError
    from telethon.tl.functions.messages import ImportChatInviteRequest
    from telethon import types, utils, errors
    import re
    import time

    from telethon import functions
    from telethon.tl.functions.channels import GetChannelsRequest, GetFullChannelRequest, JoinChannelRequest, \
        InviteToChannelRequest
    from telethon.tl.types import PeerChannel
    from telethon.tl.functions.contacts import GetContactsRequest
    from telethon.tl.functions.messages import AddChatUserRequest
    from colorama import Fore, Back, Style
    import configparser

    config = configparser.ConfigParser()
    config.read("config.ini")
    grouplink = config['AstraMedias']['ToGroup']
    groupid = config['AstraMedias']['GroupID']
    stopnum = config['AstraMedias']['EnterStop']
    stacno = config['AstraMedias']['StartingAccount']
    endacno = config['AstraMedias']['EndAccount']


    with open('phone.csv', 'r') as f:
        #global phlist
        phlist = [row[0] for row in csv.reader(f)]
    print('Total account: ' + str(len(phlist)))
    print(Style.BRIGHT + Fore.GREEN + 'Enter Y if group has private link else N (Y/N) : ')
    prchk = input()
    print(Style.BRIGHT + Fore.GREEN + 'In A Batch How many Members You Want To Add : ')
    Legenddevismain = int(input())
    print(Style.BRIGHT + Fore.GREEN + 'Enter Delay Time Per Request 0 For None : ')
    AstraMedias =int(input())
    if prchk == 'Y':
        id = int(groupid)
        prlink = grouplink
    elif prchk == 'N':
        id = int(groupid)
        prlink = grouplink
    stop = int(stopnum)
    start_from = int(stacno) - 1
    upto = int(endacno)
    indexx = 0
    global Legenddev_is_main_developer
    Legenddev_is_main_developer = 0
    for pythondeveloper in phlist[start_from:upto]:
        indexx += 1

        phone = utils.parse_phone(pythondeveloper)
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", 2284793, '85468d44607fcb5b9efe5ed61e4582a2')
        client.start(phone)
        print(f'Index : {indexx}')
        try:
            channel = client.get_entity(PeerChannel(id))
        except ValueError:
            if prchk == 'Y':
                client(ImportChatInviteRequest(prlink))
                channel = client.get_input_entity(PeerChannel(id))
            # This Script Is Made My T.Me/Rexhacks.
            elif prchk == 'N':
                client(JoinChannelRequest(prlink))
                time.sleep(5)
                channel = client.get_input_entity(PeerChannel(id))
        channelinfo = client(GetFullChannelRequest(channel=channel))
        Legenddev_is_main_developer = int(channelinfo.full_chat.participants_count)
        print(f'Members: {Legenddev_is_main_developer}')
        if Legenddev_is_main_developer >= stop:
            print(f'The Goal Of {stop} Has Been Completed')
            input()
            quit()

        members = client(GetContactsRequest(hash=0))
        user_to_add = members.users
        countcon = len(user_to_add)
        print(f'Total : {countcon}')

        batchcount = 0
        lol = 0
        while batchcount < countcon:
            semen = [delta for delta in user_to_add[:Legenddevismain]]
            # print(f'Left {len(lit)}')
            try:
                time.sleep(AstraMedias)
                client(functions.channels.InviteToChannelRequest(
                    channel=id,
                    users=semen
                ))
                # print(f'Added : {added}')
                batchcount += Legenddevismain
                for i in range(0, 10):
                    try:
                        del user_to_add[i]
                    except Exception as D:
                        continue
                print(Style.BRIGHT + Fore.GREEN + f'BATCH: {batchcount}')
            except errors.RPCError as e:
                erro = e.__class__.__name__
                print(str(erro))
                break
                # continue
def single():
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()
    from telethon.sync import TelegramClient
    import csv
    from telethon.errors.rpcerrorlist import UsernameInvalidError, ChannelInvalidError, PhoneNumberBannedError
    from telethon.tl.functions.messages import ImportChatInviteRequest
    from telethon import types, utils, errors
    import re
    from telethon.tl.functions.channels import GetChannelsRequest, GetFullChannelRequest, JoinChannelRequest, \
        InviteToChannelRequest
    from telethon.tl.types import PeerChannel
    from telethon.tl.functions.contacts import GetContactsRequest
    from telethon.tl.functions.messages import AddChatUserRequest
    from colorama import Fore, Back, Style
    import time
    import configparser

    config = configparser.ConfigParser()
    config.read("config.ini")
    grouplink = config['AstraMedias']['ToGroup']
    groupid = config['AstraMedias']['GroupID']
    stopnum = config['AstraMedias']['EnterStop']
    stacno = config['AstraMedias']['StartingAccount']
    endacno = config['AstraMedias']['EndAccount']

    with open('phone.csv', 'r') as f:
        #global phlist
        phlist = [row[0] for row in csv.reader(f)]
    print('Total account: ' + str(len(phlist)))

    print(Style.BRIGHT + Fore.GREEN + 'Enter Y if group has private link else N (Y/N) : ')
    prchk = input()
    print(Style.BRIGHT + Fore.GREEN + 'Enter Delay Time Per Request 0 For None : ')
    AstraMedias =int(input())
    if prchk == 'Y':
        id = int(groupid)
        prlink = grouplink
    elif prchk == 'N':
        id = int(groupid)
        prlink = grouplink
    stop = int(stopnum)
    Rexhacks_ne_script_banaya_hai = int(stacno) - 1
    telegram_script_banyane_ke_liye_rexhacks_ko_dm_kro = int(endacno)
    indexx = 0
    global RExhackspro
    RExhackspro = 0
    for deltaxd in phlist[Rexhacks_ne_script_banaya_hai:telegram_script_banyane_ke_liye_rexhacks_ko_dm_kro]:
        indexx += 1
        print(f'Index : {indexx}')
        phone = utils.parse_phone(deltaxd)
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", 2818286, '5f34bd560b5053ae7edc32b5c0246245')
        client.start(phone)
        try:
            channel = client.get_entity(PeerChannel(id))
        except ValueError:
            if prchk == 'Y':
                client(ImportChatInviteRequest(prlink))
                channel = client.get_input_entity(PeerChannel(id))

            elif prchk == 'N':
                client(JoinChannelRequest(prlink))
                time.sleep(5)
                channel = client.get_input_entity(PeerChannel(id))
        channelinfo = client(GetFullChannelRequest(channel=channel))
        RExhackspro = int(channelinfo.full_chat.participants_count)
        print(f'Members: {RExhackspro}')
        if RExhackspro >= stop:
            print(f'The Goal Of {stop} Has Been Completed')
            input()
            quit()
        contacts = client(GetContactsRequest(hash=0))

        deltaadd = 0
        for deltaop in contacts.users:
            deltaadd += 1

            try:
                client(InviteToChannelRequest(channel=id, users=[deltaop]))
                print(Style.BRIGHT + Fore.GREEN + f'{deltaadd} - {deltaop.id} - DONE')
                time.sleep(AstraMedias)
            except errors.RPCError as e:
                erro = e.__class__.__name__
                print(Style.BRIGHT + Fore.RED + f'{deltaadd} - {deltaop.id} - {erro}')
                continue
def setprofile():
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()
    from telethon.sync import TelegramClient
    from telethon import functions, types
    from telethon.sync import TelegramClient
    from telethon import utils
    import csv
    from csv import reader
    import configparser
    from colorama import Fore, Back, Style
    import subprocess, requests, time, os

    done = False
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1

            print(Style.BRIGHT + Fore.GREEN + f"Changing in {phone}")
            client = TelegramClient(f"sessions/{phone}", 2818286, '5f34bd560b5053ae7edc32b5c0246245')
            client.start(phone)
            result = client(functions.photos.UploadProfilePhotoRequest(
                file=client.upload_file('set.jpg'),
            ))
            print('done! profile pic has been changed')
            done = True
    input("Done!" if done else "Error!")
def Deleteprofile():
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()
    from telethon.sync import TelegramClient
    from telethon import functions, types
    from telethon.sync import TelegramClient
    from telethon.tl.functions.photos import DeletePhotosRequest
    from telethon import utils
    import csv
    from csv import reader
    import configparser
    from colorama import Fore, Back, Style
    import subprocess, requests, time, os

    done = False
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.RED + f"Deleting in {phone}")
            client = TelegramClient(f"sessions/{phone}", 2818286, '5f34bd560b5053ae7edc32b5c0246245')
            client.start(phone)
            client(DeletePhotosRequest(client.get_profile_photos('me')))
            print(Style.BRIGHT + Fore.GREEN + 'Profile Pic Deleted')
            done = True
    input("Done!" if done else "Error!")
def Adder():
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()
    from telethon.sync import TelegramClient
    from telethon.tl.functions.messages import GetDialogsRequest
    from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, PeerUser
    from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, \
        UserAlreadyParticipantError
    from telethon.tl.functions.channels import InviteToChannelRequest
    from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest
    from telethon.errors import SessionPasswordNeededError
    from telethon import types, utils, errors
    import configparser
    import sys
    import csv
    from csv import reader
    import traceback
    import time
    import random
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
    from telethon.sessions import StringSession

    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = int(2818286)
    api_hash = str('5f34bd560b5053ae7edc32b5c0246245')
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['AstraMedias']['ToGroup']


    def autos():

        channel_username = to_group
        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)

        user= client.get_me()
        if not user.last_name:
            LegendName = user.first_name
        else:
            LegendName = user.first_name +' '+user.last_name
        input_file = 'data.csv'
        users = []
        with open(input_file, encoding='UTF-8') as f:
            rows = csv.reader(f, delimiter=",", lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['srno'] = row[0]
                user['username'] = row[1]
                user['id'] = int(row[2])
                # user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)

        startfrom = int(input("Start From = "))
        endto = int(input("End To = "))

        for user in users:
            if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
                try:
                    status = 'AstraMedias'
                    if user['username'] == "":
                        print("no username, moving to next")
                        continue

                    client(InviteToChannelRequest(channel_username, [user['username']]))
                    status = Style.BRIGHT + Fore.GREEN + 'DONE'

                    print(Style.BRIGHT + Fore.YELLOW + "Please Wait...")
                    time.sleep(random.randrange(15, 30))

                except UserPrivacyRestrictedError:
                    status = Style.BRIGHT + Fore.RED + 'PrivacyRestrictedError'
                    time.sleep(random.randrange(3, 5))

                except UserAlreadyParticipantError:
                    status = 'ALREADY'

                except PeerFloodError as g:
                    status = 'PeerFloodError'
                    print(Style.BRIGHT + Fore.YELLOW + 'Script Are In Progress So Please Wait...')
                    time.sleep(random.randrange(60, 90))

                except ChatWriteForbiddenError as cwfe:
                    client(JoinChannelRequest(channel_username))
                    time.sleep(5)
                    continue

                except errors.RPCError as e:
                    status = e.__class__.__name__

                except Exception as d:
                    status = d

                except:
                    traceback.print_exc()
                    print("Unexpected Error")
                    continue
                channel_connect = client.get_entity(channel_username)
                channel_full_info = client(GetFullChannelRequest(channel=channel_connect))
                countt = int(channel_full_info.full_chat.participants_count)

                print(Style.BRIGHT + Fore.GREEN +f" {LegendName} {Style.BRIGHT+Fore.RESET} > Group Members {(countt)}{Style. RESET_ALL} {Style.BRIGHT+Fore.CYAN}>> {user['name']} >> {status}")
            elif int(user['srno']) > int(endto):
                print("Members Added Successfully!")
                input()
                exit()



    autos()
def adderforphone():
    from telethon.sync import TelegramClient
    from telethon.tl.functions.channels import GetChannelsRequest, GetFullChannelRequest, JoinChannelRequest, \
        InviteToChannelRequest
    import csv
    from telethon.tl.types import PeerChannel
    from telethon.tl.functions.messages import GetDialogsRequest , ImportChatInviteRequest
    from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, PeerUser
    from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, \
        UserAlreadyParticipantError
    from telethon.tl.functions.channels import InviteToChannelRequest
    from telethon import types, utils, errors, functions
    import configparser
    from telethon.errors.rpcerrorlist import UsernameInvalidError, ChannelInvalidError, PhoneNumberBannedError
    import re
    import os
    import traceback
    from csv import reader
    from telethon.sessions import StringSession
    from colorama import init, Fore
    import time
    import random

    init()
    r = Fore.LIGHTRED_EX
    gr = Fore.GREEN
    n = Fore.RESET
    bl = Fore.BLUE
    ye = Fore.YELLOW

    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    clr()
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()

    config = configparser.ConfigParser()
    config.read("config.ini")
    grouplink = config['AstraMedias']['ToGroup']
    groupid = config['AstraMedias']['GroupID']
    stopnum = config['AstraMedias']['EnterStop']
    stacno = config['AstraMedias']['StartingAccount']
    endacno = config['AstraMedias']['EndAccount']

    phone = []

    with open('phone.csv', 'r') as delta_obj:
        csv_reader = reader(delta_obj)
        list_of_phone = tuple(csv_reader)
        for phone_ in list_of_phone:
            phone.append(int(phone_[0]))
    pphone = phone

    print(f'{gr}Total account: {n} {r}{str(len(phone))}{n}')



    def autos():
        print(Style.BRIGHT + Fore.GREEN + 'Enter Delay Time Per Request 0 For None : ')
        AstraMedias = int(input())
        rexhacks = 'data.csv'
        rexlink = str(grouplink)
        id = int(groupid)
        From = int(stacno) - 1
        Upto = int(endacno)
        rex = int(1)
        hacks = int(50) - 1
        stop = int(stopnum)

        with open('memory.csv', 'w', encoding='UTF-8') as file:
            writer = csv.writer(file, delimiter=",", lineterminator="\n")
            writer.writerow([rex, rex + hacks])
        a = 0
        indexx = 0
        for xd in pphone[From:Upto]:
            indexx += 1
            print(f'Index : {indexx}')
            phone = utils.parse_phone(xd)
            print(f"Login {phone}")
            client = TelegramClient(f"sessions/{phone}", 2392599, '7e14b38d250953c8c1e94fd7b2d63550')
            client.connect()
            if not client.is_user_authorized():
                print(f'{r}some thing has changed{n}')
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter the code: '))

            input_file = rexhacks
            users = []
            with open(input_file, encoding='UTF-8') as f:
                rows = csv.reader(f, delimiter=",", lineterminator="\n")
                next(rows, None)
                for row in rows:
                    user = {}
                    user['srno'] = row[0]
                    user['username'] = row[1]
                    user['id'] = int(row[2])
                    # user['access_hash'] = int(row[2])
                    user['name'] = row[3]
                    users.append(user)

            with open('memory.csv', 'r') as hash_obj:

                csv_reader = reader(hash_obj)

                list_of_rows = list(csv_reader)
                row_number = 1
                col_number = 1
                numnext = list_of_rows[row_number - 1][col_number - 1]

            startfrom = int(numnext)
            nextstart = startfrom + hacks

            with open('memory.csv', 'r') as hash_obj:
                csv_reader = reader(hash_obj)
                list_of_rows = list(csv_reader)
                row_number = 1
                col_number = 2
                numend = list_of_rows[row_number - 1][col_number - 1]

            endto = int(numend)
            nextend = endto + hacks

            with open("memory.csv", "w", encoding='UTF-8') as df:  # Enter your file name.

                writer = csv.writer(df, delimiter=",", lineterminator="\n")

                writer.writerow([nextstart, nextend])

            client(JoinChannelRequest(rexlink))
            time.sleep(5)
            channel = client.get_input_entity(PeerChannel(id))
            channelinfo = client(GetFullChannelRequest(channel=channel))

            rexprodeltanoob = int(channelinfo.full_chat.participants_count)
            print(f'Members: {rexprodeltanoob}')
            if rexprodeltanoob >= stop:
                print(f'The Goal Of {stop} Has Been Completed')
                input()
                quit()

            it = 0
            for user in users:
                if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
                    try:
                        it += 1
                        if user['username'] == "":
                            print(f"{r}no username, moving to next{n}")
                            continue

                        client(functions.channels.InviteToChannelRequest(rexlink, [user['username']]))
                        print(f'{it} - done')
                        time.sleep(AstraMedias)


                    except ChatWriteForbiddenError as cwfe:
                        client(JoinChannelRequest(rexlink))
                        time.sleep(5)
                        continue



                    except errors.RPCError as e:
                        status = e.__class__.__name__
                        print(f'{it} - {status}')





                    except:
                        traceback.print_exc()
                        print(f"{ye}Unexpected Error{n}")
                        continue

            a += 1
        os.remove("memory.csv")


    def private():
        print(Style.BRIGHT + Fore.GREEN + 'Enter Delay Time Per Request 0 For None : ')
        AstraMedias = int(input())
        rexhacks = 'data.csv'
        rexlink = str(grouplink)
        id = int(groupid)
        From = int(stacno) - 1
        Upto = int(endacno)
        rex = int(1)
        hacks = int(50) - 1
        stop =int(stopnum)
        with open('memory.csv', 'w', encoding='UTF-8') as file:
            writer = csv.writer(file, delimiter=",", lineterminator="\n")
            writer.writerow([rex, rex + hacks])
        a = 0
        indexx = 0
        for xd in pphone[From:Upto]:
            indexx += 1
            print(f'Index : {indexx}')
            phone = utils.parse_phone(xd)
            print(f"Login {phone}")
            client = TelegramClient(f"sessions/{phone}", 2392599, '7e14b38d250953c8c1e94fd7b2d63550')
            client.connect()
            if not client.is_user_authorized():
                print(f'{r}some thing has changed{n}')
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter the code: '))

            input_file = rexhacks
            users = []
            with open(input_file, encoding='UTF-8') as f:
                rows = csv.reader(f, delimiter=",", lineterminator="\n")
                next(rows, None)
                for row in rows:
                    user = {}
                    user['srno'] = row[0]
                    user['username'] = row[1]
                    user['id'] = int(row[2])
                    # user['access_hash'] = int(row[2])
                    user['name'] = row[3]
                    users.append(user)

            with open('memory.csv', 'r') as hash_obj:

                csv_reader = reader(hash_obj)

                list_of_rows = list(csv_reader)
                row_number = 1
                col_number = 1
                numnext = list_of_rows[row_number - 1][col_number - 1]

            startfrom = int(numnext)
            nextstart = startfrom + hacks

            with open('memory.csv', 'r') as hash_obj:
                csv_reader = reader(hash_obj)
                list_of_rows = list(csv_reader)
                row_number = 1
                col_number = 2
                numend = list_of_rows[row_number - 1][col_number - 1]

            endto = int(numend)
            nextend = endto + hacks

            with open("memory.csv", "w", encoding='UTF-8') as df:  # Enter your file name.

                writer = csv.writer(df, delimiter=",", lineterminator="\n")

                writer.writerow([nextstart, nextend])

            client(ImportChatInviteRequest(rexlink))
            time.sleep(5)
            channel = client.get_input_entity(PeerChannel(id))
            channelinfo = client(GetFullChannelRequest(channel=channel))
            rexprodeltanoob = int(channelinfo.full_chat.participants_count)
            print(f'Members: {rexprodeltanoob}')
            if rexprodeltanoob >= stop:
                print(f'The Goal Of {stop} Has Been Completed')
                input()
                quit()

            it = 0
            for user in users:
                if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
                    print(f'Members: {rexprodeltanoob}')
                    try:
                        it += 1
                        if user['username'] == "":
                            print(f"{r}no username, moving to next{n}")
                            continue

                        client(functions.channels.InviteToChannelRequest(rexlink, [user['username']]))
                        print(f'{it} - done')

                        time.sleep(AstraMedias)

                    except ChatWriteForbiddenError as cwfe:
                        client(ImportChatInviteRequest(rexlink))
                        time.sleep(5)
                        continue



                    except errors.RPCError as e:
                        status = e.__class__.__name__

                        print(f'{it} - {status}')





                    except:
                        traceback.print_exc()
                        print(f"{ye}Unexpected Error{n}")
                        continue

            a += 1
        os.remove("memory.csv")


    rexchoose = str(input(f'{bl}Press Y if group is private else N : {n}'))
    if rexchoose == 'Y':
        private()
    elif rexchoose == 'N':
        autos()
def multipleadder():
    import subprocess
    import colorama
    from colorama import Fore, Back, Style
    import time
    import csv
    legend_devpost()

    with open('memory.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=",", lineterminator="\n")
        writer.writerow([1, 1, 50])
    a = int(input("How many accounts do you want to run ? => ")) - 1
    x = 0
    while x <= a:
        subprocess.Popen('python v1-1.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
        x = x + 1
        time.sleep(3)
    time.sleep(10)
    os.remove("memory.csv")
def sendmessage():
    import colorama
    from colorama import Fore, Back, Style

    colorama.init(autoreset=True)
    legend_devpost()
    from telethon.sync import TelegramClient
    from telethon.errors.rpcerrorlist import FloodWaitError
    from telethon.tl.functions.messages import GetDialogsRequest
    from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, PeerUser
    from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, \
        UserAlreadyParticipantError
    from telethon.tl.functions.channels import InviteToChannelRequest
    from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest
    from telethon.errors import SessionPasswordNeededError
    from telethon import types, utils, errors
    import configparser
    import sys
    from message import Message
    import csv
    from csv import reader
    import traceback
    import time
    import random
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
    from telethon.sessions import StringSession

    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())

    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = int(2818286)
    api_hash = str('5f34bd560b5053ae7edc32b5c0246245')
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['AstraMedias']['ToGroup']
    messagessss = Message
    legendfile = config['AstraMedias']['Message_file']


    def autos():

        channel_username = to_group
        AstraMedias_message = messagessss
        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)

        user = client.get_me()
        if not user.last_name:
            LegendName = user.first_name
        else:
            LegendName = user.first_name +' '+user.last_name
        input_file = 'data.csv'
        users = []
        with open(input_file, encoding='UTF-8') as f:
            rows = csv.reader(f, delimiter=",", lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['srno'] = row[0]
                user['username'] = row[1]
                user['id'] = int(row[2])
                # user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)

        startfrom = int(input("Start From = "))
        endto = int(input("End To = "))
        rex = 0
        for user in users:
            if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
                try:
                    rex += 1
                    status = 'AstraMedias'
                    receiver = client.get_input_entity(user['username'])
                    if user['username'] == "":
                        print("no username, moving to next")
                        continue

                    if not legendfile:
                         client.send_message(receiver, f"Hi {user['name']}\n {AstraMedias_message}")
                    else:
                        client.send_file(receiver, legendfile)
                        client.send_message(receiver, f"Hi {user['name']}\n {AstraMedias_message}")
                    status = Style.BRIGHT + Fore.GREEN + 'DONE'

                    # print("Waiting for 60-180 Seconds...")
                    time.sleep(random.randrange(3,6))

                except UserPrivacyRestrictedError:
                    status = 'PrivacyRestrictedError'


                except UserAlreadyParticipantError:
                    status = 'ALREADY'


                except PeerFloodError as g:
                    status = 'PeerFloodError :('
                except FloodWaitError as t:
                    stime = t.seconds
                    print(f"wait {stime} seconds")
                    time.sleep(stime)
                except errors.RPCError as e:
                    status = e.__class__.__name__

                except:
                    traceback.print_exc()
                    print("Unexpected Error")
                    continue
                print(Style.BRIGHT + Fore.GREEN +f" {LegendName} {Style.BRIGHT+Fore.RESET} > SENDING TO {Style. RESET_ALL} {Style.BRIGHT+Fore.CYAN}>> {user['name']} >> {status} >> {rex}")
            elif int(user['srno']) > int(endto):
                print(Style.BRIGHT + Fore.GREEN + "\nMessage Sended Successfully!\n")
                input()
                exit()


    autos()
def multisender():
    import subprocess
    import colorama
    from colorama import Fore, Back, Style
    import time
    import csv

    colorama.init(autoreset=True)
    legend_devpost()
    with open('memory.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=",", lineterminator="\n")
        writer.writerow([1, 1, 50])
    a = int(input("How many accounts do you want to run ? => ")) - 1
    x = 0
    while x <= a:
        subprocess.Popen('python v1-2.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
        x = x + 1
        time.sleep(3)
    time.sleep(10)
    os.remove("memory.csv")
def updateprof():
    import colorama
    colorama.init(autoreset=True)
    legend_devpost()
    from telethon.tl.functions.account import UpdateProfileRequest
    import random
    from telethon import functions
    from telethon.sync import TelegramClient
    from telethon import utils
    import csv
    from colorama import Fore, Style
    import time

    done = False
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1

            print(Style.BRIGHT + Fore.GREEN + f"Changing in {phone}")
            client = TelegramClient(f"sessions/{phone}", 2818286, '5f34bd560b5053ae7edc32b5c0246245')
            client.start(phone)
            while True:
                try:
                    change_name = int(input('Press 1 to change name / 2 to skip this account / 3 to Exit: '))
                    break
                except ValueError:
                    print('Invalid Input.')

            if change_name == 3:
                exit()

            if change_name == 1:
                first_name = input('First name : ')
                last_name = input('Last name : ')
                client(UpdateProfileRequest(
                    first_name=first_name,
                    last_name=last_name
                ))

                time.sleep(random.randint(4, 6))
                name = [first_name, last_name]
                random.shuffle(name)

                username = ''.join(name) + str(int(phone[8:]) + random.randint(100, 999))
                client(functions.account.UpdateUsernameRequest(
                    username=username
                ))
            user = client.get_me()
            print(Style.BRIGHT + Fore.GREEN + 'Your New Username Is ' + Style.BRIGHT + Fore.RED + user.username)
            print('done! profile has been changed \n')
            done = True

    input("Done!" if done else "Error!")

if __name__ == '__main__':
    if not os.path.exists('./sessions'):
        os.mkdir('./sessions')
    if not os.path.exists('phone.csv'):
        open("phone.csv", "w")

    if This_is_normal_script_by_legend_dev == 1:
        login1()
    elif This_is_normal_script_by_legend_dev == 2:
        banfilter()
    elif This_is_normal_script_by_legend_dev == 3:
        spambotch()
    elif This_is_normal_script_by_legend_dev == 4:
        scraper1()
    elif This_is_normal_script_by_legend_dev == 5:
        privategroupJoiner()
    elif This_is_normal_script_by_legend_dev == 6:
        dailyfilter()
    elif This_is_normal_script_by_legend_dev == 7:
        weeklyfilter()
    elif This_is_normal_script_by_legend_dev == 8:
        Deletealready()
    elif This_is_normal_script_by_legend_dev == 9:
        setprofile()
    elif This_is_normal_script_by_legend_dev == 10:
        Deleteprofile()
    elif This_is_normal_script_by_legend_dev == 11:
        updateprof()
    elif This_is_normal_script_by_legend_dev == 12:
        addcontactforphone()
    elif This_is_normal_script_by_legend_dev == 13:
        forpc()
    elif This_is_normal_script_by_legend_dev == 14:
        Deletecontact()
    elif This_is_normal_script_by_legend_dev == 15:
        bulkadder()
    elif This_is_normal_script_by_legend_dev == 16:
        single()
    elif This_is_normal_script_by_legend_dev == 17:
        Adder()
    elif This_is_normal_script_by_legend_dev == 18:
        adderforphone()
    elif This_is_normal_script_by_legend_dev == 19:
        multipleadder()
    elif This_is_normal_script_by_legend_dev == 20:
        sendmessage()
    elif This_is_normal_script_by_legend_dev == 21:
        multisender()
    elif This_is_normal_script_by_legend_dev == 22:
        exit()

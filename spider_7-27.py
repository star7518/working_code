# import requests
# import json
#
city_code = "AU"
check_date = "2024-08-12"
# headers = {
#     "accept": "application/json, text/plain, */*",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "content-type": "application/json",
#     "origin": "https://www.data.ai",
#     "priority": "u=1, i",
#     "referer": "https://www.data.ai/intelligence/top-apps/store-rank/ios",
#     "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
#     "x-csrftoken": "StMMJKAh9PtSh8xdtm2paTHW4rXhBRTS",
#     "x-origin": "/intelligence/top-apps/store-rank/ios",
#     "x-requested-with": "XMLHttpRequest"
# }
#
# cookies = {
#     "aa_language": "cn",
#     "aa_ver": "10212f14-1c8d-45a4-959c-34d292f76c12",
#     "csrftoken": "StMMJKAh9PtSh8xdtm2paTHW4rXhBRTS",
#     "rid": "495693bea4084fa29d16bc5cbb558550",
#     "_mkto_trk": "id:351-RWH-315&token:_mch-www.data.ai-1721904711315-90940",
#     "OptanonAlertBoxClosed": "2024-07-25T11:01:58.620Z",
#     "OptanonConsent": "isGpcEnabled=0&datestamp=Fri+Jul+26+2024+09%3A21%3A22+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=16ad364f-3047-44aa-b5c7-6c2dc1057d2d&interactionCount=3&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C4%3A1&AwaitingReconsent=false&geolocation=CN%3BGD",
#     "osano_consentmanager_uuid": "9bdcb821-844f-4e45-bf3c-1c4135f4baf1",
#     "osano_consentmanager": "bxpT0RVf69pInuq59RYWhnFx2RT03Xp7kITyfS2a655XkFp6X3paFjDspIXRyuM3sn-qpxQLV1O8pvEPBwebRe58PZyLtXxrPUC9f8911wcPFPjKOldFWj5qYGQkqEpzOzCdiePAYoY9qM7IKKIqMqmxkjevqhSkSJYKQPw5ATw-yXO38yaZ1abTm-OjV9T1LF4pWLdTaZ2s6qAi4HI7gACckM7PaUB4OJzvSqgVHNYQ1UouSneZxspXH_QM2Z416iRQp9OxAtQypbfB9vdcpIQiKEPD4ym9TeGTMLqpnJy_dYEbzDvTZYK_bq0mTJcVjmeE2POU1fI=",
#     "AMP_MKTG_8c78419905": "JTdCJTdE",
#     "MRDI": "gAN9cQBK9XYZAFggAAAAMWM5MDM3NWU4Mzc2NDYxYjg5OWY2OTE5ZTdlN2E4MzdxAXMu",
#     "aa_user_token": "\".eJxNzD0PATEYAOA6DAaLzWY0NequPlYmEmMTW_P27SvXuPRSbQ-DxJ-2Wwx-wPO8i1fozdUoY3roGmIdCjWTRBUIAgtlCVJucGnosrbCCqjEymzVRENOtc6RbtoAXsnb0D8vGGN3MuCheSaHkQNim33ie4h08JF8dMl1dGotNbsfG6jxX-ZsGB4_3ZRl_gViJjTh:1seY9v:Uu4VHvqlzZ81mvkELGrHi23SpIM\"",
#     "_ga": "GA1.2.1774182953.1721904709",
#     "_gid": "GA1.2.1593491742.1724240195",
#     "AMP_8c78419905": "JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJkMGJjMzYxMS1lMjY0LTQ3ZTctOWQ3Ni05MTVlMzQyZGQyMDclMjIlMkMlMjJ1c2VySWQlMjIlM0ExNjY4ODUzJTJDJTIyc2Vzc2lvbklkJTIyJTNBMTcyNDI0MDE5NDc0MiUyQyUyMm9wdE91dCUyMiUzQWZhbHNlJTJDJTIybGFzdEV2ZW50VGltZSUyMiUzQTE3MjQyNDAxOTcwNTglMkMlMjJsYXN0RXZlbnRJZCUyMiUzQTExNiU3RA==",
#     "sid": "7b093073-61f0-443d-855b-a8e0fa0af948",
#     "_ga_FHHFCC15CR": "GS1.1.1724240194.10.0.1724240198.0.0.0",
#     "bm_mi": "25A285909FC9E868703489CDD5389DD1~YAAQHf4ZuBgvKnGRAQAA+Kq5dBiUG5Jo04jA2vAFxr2kbNfyUzk1a1rEu9McfZVFr9TFgMXpmpb6nxDmGZRrcXDKtILERL6c5RrpW2t6KoD+tejOK3WPHKDS7XpZlybGemH1EfhFqJqU55EBU1YcH/r35W04/SgqigTdAjnXPM9HnHsFTvOoC5XnLhEDpNlHTonTGNbyjW9LJbMYkK3OH5zcLf4Tcb6L4FiPPzTC9BOFvBp+VHmQpz/sXPWl+u5fiTMU4z28w26J88u7uYm0Uuk5D/JIchACBGWDCsZAo5u8NYXgnA7hqoE8slU5CFzy9rx7JBWtXHmFB/50e18rE5A=~1",
#     "ak_bmsc": "EE8A5B2E4060A61951CD65BFF491D22E~000000000000000000000000000000~YAAQHf4ZuDsvKnGRAQAA/Ma5dBil0DAYSp9lggof8ezYaGvINOR49qRHBBbhyfLoZVgHAt6llt+xilTaQLDJsvLjHmXEW7EC6RRbaAXA6jRgczj6sprCseRH6NWBwR5OugGKk/H7vOqZuXFMaVs0SGfcp7FYxVPWUgu9AhaQp1fc4PNxNeKXaRPQ7lXNFSmv3Uxgy45S9IzWtr7B9bm+88xutLXp7PfxQxOJ6pRCIgiWz4NrKFU+ti85tQFqS85DC6FJAmpxOBfRp9CH4sEORSKrBHRzNirULorM+7OPLMXBQ9DT+BXC4HS/8gdWz1SAVxdrpBRe1/chE29B7skDxWv5V2Q7Q9mU5Ckz5cohloYvpNxiBbx9Caj3EiAJEZgiSZ4H7XiIylvvFBlJJ8nzB+WaLhTKFWAHldjrkAZP0wcxRWJ7fYochS0KueltFaNh+NbYMYjCR7ECgq56VLYc5GUIa8Y1yNxjCL+yJr6W0ABgsDsYIl6j7y2Iau/X8BDv1kDMpw==",
#     "sessionId": "\".eJxVjk1Lw0AURWOstaaIH-DClS5cKEiINYZma1cquigGZje8zLy0Q-OkkzdTqSC4Ev2brvwD7k1AFHeHyz3c--I_m5VjtuN5HiGRqvQca1JkUdu3rFeCnjiYYOYLbXy22dQ4ODvljrDmSl5_LfY9tvVnc9SQlyhvfNZpUiAl2WEDeTJIEhym6TCP4vNCplEh0uQsjgbJBRRxnPVtRdzNJViU72z3_1AOYoZasqiJHzEHDeXSKkEhCFE5bcMREF5pQk3KqgXeVhLLyx-p276rXC3wLtuGEmvLxRTFjFv1gKIdbCH4BbOaBeufvb3-0cHGx6mYL-1TwLP7UWA6J2Oz9jo2XRd-A4zFZHA:1sgjeN:RugBZaGB97X8sOpipgySSq0ArYc\"",
#     "django_language": "zh-cn",
#     "_abck": "09897E5ECFF864ADDDC84BE0DDB9BD36~0~YAAQRO9jaODa7HORAQAAG+L7dAwK9DatVJW5eX4sZXx3/7sE686H/+3aV3rOxxu3UGThaFe7ClZg+b00PGUaKuoHaD7lGWy9PUrCnmlDDkdyqsvqF8eT0+aHaMf7mhVzrE4soi1MewubxIsO1+F8MuseFVkO/iOUPEHBkERrAwDavN4l5Q2E+kTE+OmEluMQbWqZ7Y792mDWGSKImYKqPd5w/e1owv4a2VGQ5Hi//1kgf/skZEkW3ed+N1LbyjQJgILv2WPR4TPXQbSoK2ipys0JCJhO6LP0EDifmXIPGqdngZviRvtnlIjRqRjHxxE5cyErNURTBCfiLJGXRQ7qBHBCZ31T5SUvUH7o/JLz0I982NMbONqgqWGPo4xhBcjCqEgEIlSdsmFH8FEthn/cIt3SLDE83wrjLfarPXK0xjniAf5rd/pAbMst14vYjT/1CTbmwhFGSEAPlDv23ldt3BM=~-1~||0||~-1",
#     "bm_sv": "97FDB5307C2A9D4D31815E3FA50C2441~YAAQRO9jaPTa7HORAQAAj+j7dBiQ6WmeuzDoLJXVRvq6EGWis0GsrULf0YpLfCvzIN5owK9RerdhWoOtepRrEyRrf46jsYHBEgMOAMqZ5YJL8IttS3kXuLWzkHhlr+++kCXVXnYz7vaE2l7VmLsUI7bSps6JqJxI/VffK8ZDHHJ1oNU1x8jdQQt7xWZTqX6gAfMQjCV7MMn/SFUhZHkptlTjt4pyvuG9jdcKfMLKUKnV04ogS5gbZ0ENzuVUPdY=~1",
#     "bm_sz": "DDA694769C680FFEDAD4B1A11FE471B0~YAAQRO9jaPXa7HORAQAAj+j7dBg79W30fFpBpcx0fnmPXv/vQA42zihqpOoKm3XSfdMpSlnq8oZp9ELbK0mTAmfbjBVysyzX7+U+ccFAiwy17PAkhAZMSsgq8tvl+8HwnuBpGs6B5+g0XZ5AU2j0PqSmeO+50dQFVWXo1QprUa/6ikZobNFE4ss18I/URJPqnDTKSfjTTMJTqwALQYRa/+5l796gK85fy0wY7I5026YzS8olBhMhSIXEhm/3Si5vc/mQ0P6pnjmE81HgYgqGdqQw0PWpj49Nsc/w/5IqbT/eaGoLyVo1YEUHsmia48mJmeoP9tV8CDjtuy3+jzzKoMtmI6OR7aNkTKpUsG1WuPc9s/mRVkYDccW4KTFRCPPKV30ahDCqHQTeXlyFRl5DJ4AFDmw3KxCWGcPU9Zt/f+G/ZAcju9zXuZ0gzVHoFBjmUdOBwFXIgJhvsBFpFgam/3Io1/TjHPdvn+ypP72DsYrbV7eSqyhxBQA2QA2UfOTd3JoQ9pjdMa+74FhemwIqx9PsieCv~3425348~3687235",
#     "RT": "\"z=1&dm=data.ai&si=a0198e62-9f84-4d73-96cc-ff2071db3773&ss=m03u7wog&sl=v&tt=12fi&bcn=%2F%2F17de4c15.akstat.io%2F\""
# }
# url = "https://www.data.ai/ajax/v2/query"
# params = {
#     "query_identifier": "top_apps$ios_table_free"
# }
# data = {
#     "facets": [
#         "store_product_rank_free__aggr",
#         "store_product_rank_grossing__aggr",
#         "value_change(store_product_rank_free__aggr)__aggr",
#         "value_change(store_product_rank_grossing__aggr)__aggr"
#     ],
#     "filters": {
#         "granularity": {
#             "equal": "daily"
#         },
#         "date": {
#             "equal": check_date
#         },
#         "country_code": {
#             "equal": city_code
#         },
#         "device_code": {
#             "equal": "ios-phone"
#         },
#         "category_id": {
#             "equal": 100001
#         },
#         "value_change": {
#             "span_unit": "PERIOD",
#             "span_value": 1
#         },
#         "percent_change": {
#             "span_unit": "PERIOD",
#             "span_value": 1
#         },
#         "product_id": {
#             "in": {
#                 "facets": [
#                     "store_product_rank_free__aggr"
#                 ],
#                 "filters": {
#                     "granularity": {
#                         "equal": "daily"
#                     },
#                     "date": {
#                         "equal": check_date
#                     },
#                     "country_code": {
#                         "equal": city_code
#                     },
#                     "device_code": {
#                         "equal": "ios-phone"
#                     },
#                     "category_id": {
#                         "equal": 100001
#                     },
#                     "value_change": {
#                         "span_unit": "PERIOD",
#                         "span_value": 1
#                     },
#                     "percent_change": {
#                         "span_unit": "PERIOD",
#                         "span_value": 1
#                     }
#                 },
#                 "breakdowns": {
#                     "product_id": {}
#                 },
#                 "pagination": {
#                     "offset": 0,
#                     "limit": 200
#                 },
#                 "order_by": [
#                     {
#                         "name": "store_product_rank_free__aggr",
#                         "order": "asc"
#                     }
#                 ]
#             }
#         }
#     },
#     "breakdowns": {
#         "product_id": {}
#     },
#     "pagination": {
#         "offset": 0,
#         "limit": 200
#     },
#     "order_by": [
#         {
#             "name": "store_product_rank_free__aggr",
#             "order": "asc"
#         }
#     ],
#     "fields": {
#         "product_id": {
#             "fields": [
#                 "name",
#                 "icon_url",
#                 "publisher_id",
#                 "market_code",
#                 "device_code",
#                 "vertical_code",
#                 "is_sensitive",
#                 "status",
#                 "category_id",
#                 "first_release_date",
#                 "world_wide_launched_date",
#                 "last_updated_time",
#                 "languages",
#                 "version",
#                 "genre_id",
#                 "secondary_genre_id"
#             ],
#             "category_id": {
#                 "fields": [
#                     "name"
#                 ]
#             },
#             "publisher_id": {
#                 "fields": [
#                     "name",
#                     "company_id"
#                 ],
#                 "company_id": {
#                     "fields": [
#                         "name",
#                         "country_code"
#                     ]
#                 }
#             }
#         }
#     }
# }
# data = json.dumps(data, separators=(',', ':'))
# response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
#
# print(response.text)
# print(response)
# product_ids=[]
# result_all=json.loads(response.text)['data']['dimensions']['product_id']
# result_appid_sorted=json.loads(response.text)['data']['facets']
# for app_id in result_appid_sorted:
#     print("测试中===================================app_id")
#     print(app_id)
# for entry in result_all:
#     product_ids.append(entry)
# print(product_ids)
# print(len(product_ids))
# for i in product_ids:
#     # 游戏名
#     print("游戏名:",result_all[i]["name"])
import requests
import json


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.data.ai",
    "priority": "u=1, i",
    "$referer": "https://www.data.ai/intelligence/top-apps/store-rank/ios?date=%272024-08-11%27&country_code=US&device_code=ios-phone&ios.category_id=(equal:100001)&store-rank.ios.view=free&store-rank.ios.rank-type=leaderboard&product_id_meta=\\u0021(product_id.category_id)&store_rank.ios.chart_range=7&chart_store_rank_ios_chart_free$previous_range=(aggr:\\u0021f,axis:\\u0021((percent:\\u0021f,type:line)),showWeekends:\\u0021f,stack:\\u0021f)&chart.event_bubble.event_types=\\u0021(modifier_change,artwork_url_change,app_description,name_change,new_version,price_change,screenshot_change,app_company_id_change)",
    "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "x-csrftoken": "StMMJKAh9PtSh8xdtm2paTHW4rXhBRTS",
    "x-origin": "/intelligence/top-apps/store-rank/ios",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "aa_language": "cn",
    "aa_ver": "10212f14-1c8d-45a4-959c-34d292f76c12",
    "csrftoken": "StMMJKAh9PtSh8xdtm2paTHW4rXhBRTS",
    "rid": "495693bea4084fa29d16bc5cbb558550",
    "_mkto_trk": "id:351-RWH-315&token:_mch-www.data.ai-1721904711315-90940",
    "OptanonAlertBoxClosed": "2024-07-25T11:01:58.620Z",
    "OptanonConsent": "isGpcEnabled=0&datestamp=Fri+Jul+26+2024+09%3A21%3A22+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=16ad364f-3047-44aa-b5c7-6c2dc1057d2d&interactionCount=3&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C4%3A1&AwaitingReconsent=false&geolocation=CN%3BGD",
    "osano_consentmanager_uuid": "9bdcb821-844f-4e45-bf3c-1c4135f4baf1",
    "osano_consentmanager": "bxpT0RVf69pInuq59RYWhnFx2RT03Xp7kITyfS2a655XkFp6X3paFjDspIXRyuM3sn-qpxQLV1O8pvEPBwebRe58PZyLtXxrPUC9f8911wcPFPjKOldFWj5qYGQkqEpzOzCdiePAYoY9qM7IKKIqMqmxkjevqhSkSJYKQPw5ATw-yXO38yaZ1abTm-OjV9T1LF4pWLdTaZ2s6qAi4HI7gACckM7PaUB4OJzvSqgVHNYQ1UouSneZxspXH_QM2Z416iRQp9OxAtQypbfB9vdcpIQiKEPD4ym9TeGTMLqpnJy_dYEbzDvTZYK_bq0mTJcVjmeE2POU1fI=",
    "AMP_MKTG_8c78419905": "JTdCJTdE",
    "MRDI": "gAN9cQBK9XYZAFggAAAAMWM5MDM3NWU4Mzc2NDYxYjg5OWY2OTE5ZTdlN2E4MzdxAXMu",
    "aa_user_token": "\".eJxNzD0PATEYAOA6DAaLzWY0NequPlYmEmMTW_P27SvXuPRSbQ-DxJ-2Wwx-wPO8i1fozdUoY3roGmIdCjWTRBUIAgtlCVJucGnosrbCCqjEymzVRENOtc6RbtoAXsnb0D8vGGN3MuCheSaHkQNim33ie4h08JF8dMl1dGotNbsfG6jxX-ZsGB4_3ZRl_gViJjTh:1seY9v:Uu4VHvqlzZ81mvkELGrHi23SpIM\"",
    "_ga": "GA1.2.1774182953.1721904709",
    "_gid": "GA1.2.1593491742.1724240195",
    "AMP_8c78419905": "JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJkMGJjMzYxMS1lMjY0LTQ3ZTctOWQ3Ni05MTVlMzQyZGQyMDclMjIlMkMlMjJ1c2VySWQlMjIlM0ExNjY4ODUzJTJDJTIyc2Vzc2lvbklkJTIyJTNBMTcyNDI0MDE5NDc0MiUyQyUyMm9wdE91dCUyMiUzQWZhbHNlJTJDJTIybGFzdEV2ZW50VGltZSUyMiUzQTE3MjQyNDAxOTcwNTglMkMlMjJsYXN0RXZlbnRJZCUyMiUzQTExNiU3RA==",
    "sid": "7b093073-61f0-443d-855b-a8e0fa0af948",
    "_ga_FHHFCC15CR": "GS1.1.1724240194.10.0.1724240198.0.0.0",
    "bm_mi": "25A285909FC9E868703489CDD5389DD1~YAAQHf4ZuBgvKnGRAQAA+Kq5dBiUG5Jo04jA2vAFxr2kbNfyUzk1a1rEu9McfZVFr9TFgMXpmpb6nxDmGZRrcXDKtILERL6c5RrpW2t6KoD+tejOK3WPHKDS7XpZlybGemH1EfhFqJqU55EBU1YcH/r35W04/SgqigTdAjnXPM9HnHsFTvOoC5XnLhEDpNlHTonTGNbyjW9LJbMYkK3OH5zcLf4Tcb6L4FiPPzTC9BOFvBp+VHmQpz/sXPWl+u5fiTMU4z28w26J88u7uYm0Uuk5D/JIchACBGWDCsZAo5u8NYXgnA7hqoE8slU5CFzy9rx7JBWtXHmFB/50e18rE5A=~1",
    "ak_bmsc": "EE8A5B2E4060A61951CD65BFF491D22E~000000000000000000000000000000~YAAQHf4ZuDsvKnGRAQAA/Ma5dBil0DAYSp9lggof8ezYaGvINOR49qRHBBbhyfLoZVgHAt6llt+xilTaQLDJsvLjHmXEW7EC6RRbaAXA6jRgczj6sprCseRH6NWBwR5OugGKk/H7vOqZuXFMaVs0SGfcp7FYxVPWUgu9AhaQp1fc4PNxNeKXaRPQ7lXNFSmv3Uxgy45S9IzWtr7B9bm+88xutLXp7PfxQxOJ6pRCIgiWz4NrKFU+ti85tQFqS85DC6FJAmpxOBfRp9CH4sEORSKrBHRzNirULorM+7OPLMXBQ9DT+BXC4HS/8gdWz1SAVxdrpBRe1/chE29B7skDxWv5V2Q7Q9mU5Ckz5cohloYvpNxiBbx9Caj3EiAJEZgiSZ4H7XiIylvvFBlJJ8nzB+WaLhTKFWAHldjrkAZP0wcxRWJ7fYochS0KueltFaNh+NbYMYjCR7ECgq56VLYc5GUIa8Y1yNxjCL+yJr6W0ABgsDsYIl6j7y2Iau/X8BDv1kDMpw==",
    "sessionId": "\".eJxVjk1Lw0AURWOstaaIH-DClS5cKEiINYZma1cquigGZje8zLy0Q-OkkzdTqSC4Ev2brvwD7k1AFHeHyz3c--I_m5VjtuN5HiGRqvQca1JkUdu3rFeCnjiYYOYLbXy22dQ4ODvljrDmSl5_LfY9tvVnc9SQlyhvfNZpUiAl2WEDeTJIEhym6TCP4vNCplEh0uQsjgbJBRRxnPVtRdzNJViU72z3_1AOYoZasqiJHzEHDeXSKkEhCFE5bcMREF5pQk3KqgXeVhLLyx-p276rXC3wLtuGEmvLxRTFjFv1gKIdbCH4BbOaBeufvb3-0cHGx6mYL-1TwLP7UWA6J2Oz9jo2XRd-A4zFZHA:1sgjeN:RugBZaGB97X8sOpipgySSq0ArYc\"",
    "django_language": "zh-cn",
    "bm_sv": "97FDB5307C2A9D4D31815E3FA50C2441~YAAQFvffF2XY41yRAQAAGJAEdRhrlPALZUaSKcP1B9FkjDymuoVTSiL/ff4cqH3h9kljsEv5wuWEVUjmDcUt9RqVXpa+90gs6lPW6iyAz7O4BVGyX73T0/7yvV2tU9Mt1ZB9L0p3YxMOCjj86IJZCVyZ8XqCIIhlxu4rquKAto2IYNl8pa5Mt/GvJ8V1ukSFrJ3ybxOK9pVshRlPa/mrDBA9tbeSgNOrdetbbHxDpYzv2FsyV6QH2zhqtOLNtkM=~1",
    "bm_sz": "DDA694769C680FFEDAD4B1A11FE471B0~YAAQFvffF2bY41yRAQAAGJAEdRjvMZcI3VP763VQmor9m7ZFXKJPgGGRx4qda/JgYtlW8tfiwD62rJNGwBfTNdQ/oAoZm/L0IAwTmoz+dbiiEKCCjM4PNvMRvFPy/QsxEw3RSyU19Q2N4dHBh0BC8euDVbqU6m6TGV51i61ZUoE1IgC9VVmzFo3hB62uHnA6MymB0y9sWnx20aywf5ebmN5hmxgelWxVRqSVEdKhKD2Z++mpxl82X1YJooO1e1y0CGdNByFv+AlW9bz2xP9UQnxh962P6t4npjEiXWODNW737cnc8vIGz7livJxQtKvPgxq9Mz5kuUj0EqLs8YxPWr3Cz/nrjQBdlAxGsk3JD77HsYcZnnUqt/OpIb86EX6t64J5+9QGCC4YNvGgVpdRi6JDMGwJZTtLrkkcf9JhTM9q0qLisWHkCHf46zrY/v4fGg2eo1OfvJ+VmtbJOo8ckfNFuP0DaiQd28z/gRzrgt42ohU32r9/OSPYymD9x8GnSwIERBrq61W9D6WDJawl/AedDtEfkg==~3425348~3687235",
    "RT": "\"z=1&dm=data.ai&si=a0198e62-9f84-4d73-96cc-ff2071db3773&ss=m03u7wog&sl=y&tt=18qg&bcn=%2F%2F17de4c15.akstat.io%2F\"",
    "_abck": "09897E5ECFF864ADDDC84BE0DDB9BD36~0~YAAQRO9jaAg07XORAQAAgNkHdQwM/F/Y1D0TPvhKV1qXI7ufgUnYKLW2Gcwf2IaGI38CSHk/5FdQHUVcBiwMPhctKiudXOr24yQXu5IgKnINrjw6ybgORauBCbKIZKXqOE2l+b+pJ4xASJJJfEDk5hyYjBXCR/BijehPoXVXJp43O9KoTsSkQy4nO0WrQSqyMb2jDLTuzNpSuW6xqmGjHT1n0jvR9wRY9z/szFyuf4/Lok0yZjGAFsz5VR2cwhmpxZ2tZE8IY3it8i8XaOL7gk8DT7AD9GkviGGdvyf54aTVzOh6l42CuWznH/6BhCSQMUb7WCvtGcm5I9C8mthCplFI04idyDLaxdGWxSFIROKBHggu/ITYt8JVAI9dWS1PTzqluhszE4Vn6/tBZhxti/ISfjUNnv9iQcyn9ZeRnYADIwIFoLc+Ssdust3lQpeOCJVn+pHEbyyGPL58PFbVdxpUqtFDGBdB4pGSKmbk50nozdIPlJS4tNJFlMq161I6jXlehL5vE/OC~-1~||0||~-1"
}
url = "https://www.data.ai/ajax/v2/query"
params = {
    "query_identifier": "top_apps$ios_table_free"
}
data = {
    "facets": [
        "store_product_rank_free__aggr",
        "store_product_rank_grossing__aggr",
        "value_change(store_product_rank_free__aggr)__aggr",
        "value_change(store_product_rank_grossing__aggr)__aggr"
    ],
    "filters": {
        "granularity": {
            "equal": "daily"
        },
        "date": {
            "equal": check_date
        },
        "country_code": {
            "equal": "US"
        },
        "device_code": {
            "equal": "ios-phone"
        },
        "category_id": {
            "equal": 100001
        },
        "value_change": {
            "span_unit": "PERIOD",
            "span_value": 1
        },
        "percent_change": {
            "span_unit": "PERIOD",
            "span_value": 1
        },
        "product_id": {
            "in": {
                "facets": [
                    "store_product_rank_free__aggr"
                ],
                "filters": {
                    "granularity": {
                        "equal": "daily"
                    },
                    "date": {
                        "equal": check_date
                    },
                    "country_code": {
                        "equal": "US"
                    },
                    "device_code": {
                        "equal": "ios-phone"
                    },
                    "category_id": {
                        "equal": 100001
                    },
                    "value_change": {
                        "span_unit": "PERIOD",
                        "span_value": 1
                    },
                    "percent_change": {
                        "span_unit": "PERIOD",
                        "span_value": 1
                    }
                },
                "breakdowns": {
                    "product_id": {}
                },
                "pagination": {
                    "offset": 0,
                    "limit": 200
                },
                "order_by": [
                    {
                        "name": "store_product_rank_free__aggr",
                        "order": "asc"
                    }
                ]
            }
        }
    },
    "breakdowns": {
        "product_id": {}
    },
    "pagination": {
        "offset": 0,
        "limit": 200
    },
    "order_by": [
        {
            "name": "store_product_rank_free__aggr",
            "order": "asc"
        }
    ],
    "fields": {
        "product_id": {
            "fields": [
                "name",
                "icon_url",
                "publisher_id",
                "market_code",
                "device_code",
                "vertical_code",
                "is_sensitive",
                "status",
                "category_id",
                "first_release_date",
                "world_wide_launched_date",
                "last_updated_time",
                "languages",
                "version",
                "genre_id",
                "secondary_genre_id"
            ],
            "category_id": {
                "fields": [
                    "name"
                ]
            },
            "publisher_id": {
                "fields": [
                    "name",
                    "company_id"
                ],
                "company_id": {
                    "fields": [
                        "name",
                        "country_code"
                    ]
                }
            }
        }
    }
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(response.text)
print(response)
product_ids=[]
result_all=json.loads(response.text)['data']['dimensions']['product_id']
result_appid_sorted=json.loads(response.text)['data']['facets']
for app_id in result_appid_sorted:
    print("测试中===================================app_id")
    print(app_id)
for entry in result_all:
    product_ids.append(entry)
print(product_ids)
print(len(product_ids))
for i in product_ids:
    # 游戏名
    print("游戏名:",result_all[i]["name"])
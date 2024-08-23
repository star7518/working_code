import time
from datetime import datetime
import pandas as pd
import requests
import json
import time
import random

def req(city_code,check_date):
    games=[]
    versions=[]
    product_ids=[]
    icon_urls=[]
    public_time=[]
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/json",
        "origin": "https://www.data.ai",
        "priority": "u=1, i",
        "referer": "https://www.data.ai/intelligence/top-apps/store-rank/ios",
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
        "bm_sv": "97FDB5307C2A9D4D31815E3FA50C2441~YAAQHf4ZuP4vKnGRAQAApXy6dBj5qZsC6q4ox1pnoh7cPvvYMG2v+mVqtADQZaCAo4Dqrs/EWCTe1+tcqOmbZSDCl4PZJcBOtDecHpX51WfG1JOFrAfdqzgLsyOxcVfbf2qOf6AVaMNdmilV3lXxagzZt+FufiHTxBFQ3waTa2ci76NBce716YODKPXW1PGrQ47dYbcfDLDiisv64T+3weEbCI/rFXGTkzHrS3BvqIpz2Fq+/8rumFcishmocw==~1",
        "bm_sz": "DDA694769C680FFEDAD4B1A11FE471B0~YAAQHf4ZuP8vKnGRAQAApXy6dBhLwbqVAA1IlDC+jX8We5qhOA09SSncZpd3ce3srDegafoIAm0ayzPS9fnIIz0scQk6vClVBWdmMtDc8cSGVprt4oyJdccnB/kZy+lDeyaekg87l0H1CsYJIESwYpB9SKnNYdI54oJF7LYi10dkpkK9hN3eDpKPl3RL4cGcNhd44TcrGVbFcfNtc2YMgXpKOWAV4W+QERiWc6UD5+sq8DHQJFEmk5E3fCBd08SlYDozwKEFs+tbhbYcvkZewhJddkav27/7wpaOppq1+1gmkYoR21hQQj+q6LxaVwEFcE9pR7y5zZdnt8FL1JAKQT0MfvPcQz9mK+YICgS+c8tb6s1wbd4mu3mofymHb199+Q6ZUQ3ftJ90tb4Wa7NknIlLatsEv6wogOiF0qBG7d/1vW7v3C96P08fOXHILud3HRWMp4o6O5LeUN6lU1o+YqQMTCFEE6tP9jrhX/Ncl+4jtN89dKB9wfny3Fkr7rTHUQ==~3425348~3687235",
        "_abck": "09897E5ECFF864ADDDC84BE0DDB9BD36~0~YAAQHf4ZuAQwKnGRAQAAjou6dAypdiicp4f3TzMyMAeZWsC5/zu26KpTS6fvx2GPfhWCB1ELcGv5voKD7bng5iHKtYJtU/kIdSxshiisOJcRtH1vcmTtP64uPUsyV2/oRdYc+gdOlE+BIv4pdU/zYvs/6RDRZlgryXBg/nkqEiJNi5IhDPD+wZj4sLRfrGUqCbkTB1FQ+ZtwRhRaaStA/ePi5Tlqkoa7cDvb4Jzhgf5X0giYwa2IBTTr2XDXi4WCXJabVmbzQEk+awZI7SS6ixrjEhXURR8CHz6cLfH5ZNDi7kH9WaoF3jF0EeZ52U+WoQUJrIHGneo/qJpQKtfkBPrneoXafQujEaH8CN8rbSN5VXRh5tFFvBO4Uq0sKlY1rlelLRu1p2cVpJUJidfpHKp2IhhrSb2LJXWsO4NB0nwdXhkcM56B32BFyiPKp+wa751lXwkW0M3JePH8W/8tLwUJWR588oTAaX8KT9vz59RkiJSi6TN0pNY0h1aRVmI8LAo84WRueIks~-1~||0||~-1",
        "RT": "\"z=1&dm=data.ai&si=a0198e62-9f84-4d73-96cc-ff2071db3773&ss=m03s35h7&sl=8&tt=1ewu&bcn=%2F%2F17de4c19.akstat.io%2F&ld=1q5n&nu=r1ohgijn&cl=1tbf\""
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
                "equal": city_code
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
                            "equal": city_code
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
    # print(response.text)
    result_all=json.loads(response.text)['data']['dimensions']['product_id']
    result_appid_sorted=json.loads(response.text)['data']['facets']
    for app_id in result_appid_sorted:
        print("测试中===================================app_id")
        print(app_id)
    for entry in result_all:
        product_ids.append(entry)
    # print(product_ids)
    # print(len(product_ids))
    for i in product_ids:
        # 游戏名
        print("游戏名:",result_all[i]["name"])
        games.append(result_all[i]["name"])
        # 版本号
        # print("版本号:",result_all[i]["version"])
        versions.append(result_all[i]["version"])
        # icon
        # print("icon:",result_all[i]["icon_url"])
        icon_urls.append(result_all[i]["icon_url"])
        # 最新发布日期
        # print("最新发布日期:",datetime.fromtimestamp(int(result_all[i]["last_updated_time"]) / 1000).strftime('%Y-%m-%d'))
        public_time.append(datetime.fromtimestamp(int(result_all[i]["last_updated_time"]) / 1000).strftime('%Y-%m-%d'))
    # print(len(games))
    # print(len(product_ids))
    # print(len(versions))
    # print(len(icon_urls))
    # print(len(public_time))
    data_all={
        "游戏名":games,
        "版本号":versions,
        "icon":icon_urls,
        "最新发布日期":public_time,
        "game_id":product_ids,
    }
    result_data=pd.DataFrame(data_all)
    # result_data.to_csv(f"./采集数据/采集城市-{city_code}+'采集日期'+{check_date}+'游戏数据'.csv",index=False,encoding="utf-8")
    print(result_data)
    return product_ids,games
def req_detail(app_id,country_code):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/json",
        "origin": "https://www.data.ai",
        "priority": "u=1, i",
        "referer": "https://www.data.ai/apps/ios/app/" + str(app_id) + "/user-retention",
        "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "x-csrftoken": "StMMJKAh9PtSh8xdtm2paTHW4rXhBRTS",
        "x-origin": "/apps/ios/app/" + str(app_id) + "/user-retention",
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
        "bm_sv": "97FDB5307C2A9D4D31815E3FA50C2441~YAAQHf4ZuPMxKnGRAQAAO+G8dBjudrLoMjlVeiOhN2Np9h8PpXtZHdxrrxEowJAx6TAdTjlFmIcG2g9c6aI756YZicCvml7MYYWxLHBFebHFMm86OqFtV4ZCIY7uiQ4i7ojOUAUCV7q82ZKToVLUe5m2ehjauw0f7jA+TUzCN2axWu+s4CEdEjCh3jMuaISsQ4FINuJb9EYtZCWE1u/u2KIca5zUEWmu790x0ccLBBRlI30DiiEvkSgyxf0OlQ==~1",
        "bm_sz": "DDA694769C680FFEDAD4B1A11FE471B0~YAAQHf4ZuPQxKnGRAQAAO+G8dBi+4G7r7H5an3Gq4M2uZ7JlhgjzrvF1AGZfKfXAC1EhfT5wxNKM4FZmR8e/6M6bg/m3pfpfZBs4RezDLslQci/c2vvawB63p0UEFwKXcP3K+ChW1PeKkXecLOzpG+v5oR6J2EIguGpVMqzawY45nWj5fZxhqiY/+8kO8mtcWuM0q4pZdiXaHP1gyqKXO6h79HpohmTYfdov/qA2RnXpiS2tFFEeUJva9fUGxzvjHIW3dHyoAvqiG+Jm1SiMMcMpP+Xsb8ECEMb0Mbt0x32TBa/En4j4c+0qdeWsg9RPK+LWNEdWpRg6+K4CUj3e08fI10LzcLndHKjWuhdT3uc3mJ8ksMcpyBeGDzbD9ceTJZsLq1ktY2jVFjn+rh6sRUSmmFMmtWXQv2Rh6Pp4umbA9yz+KxukoHpQ5gDbiz8I6ReNg98mYyTsnaYSYYdn1+Ail34gxIVYfglprIElsguJIILr16HxMThSOYclvuhzpQZJyNE6ZC6c4C0l8p3t~3425348~3687235",
        "RT": "\"z=1&dm=data.ai&si=a0198e62-9f84-4d73-96cc-ff2071db3773&ss=m03s35h7&sl=g&tt=1z9c&bcn=%2F%2F17de4c19.akstat.io%2F&ld=52be&nu=1ufdec35&cl=51rq\"",
        "_abck": "09897E5ECFF864ADDDC84BE0DDB9BD36~0~YAAQHf4ZuPUxKnGRAQAADeK8dAxicRfk5Ae32np1WteEcJG9x4o8MyIA3GBEoILCLogy57vqYcbzN3LbsXOwOVEvoZrRM3n9U6oLD4rTj90z7VM1LPHfPKKertSO7rgelhpdG2CE4UtoVPx9yluADUvf2fbijEfBeL26oy/TMfZ3QkG1GiC1VBD/keFYO1+iKdm+IzaZmM25c7DR6QdynU2qKDVIlAx65Jn2Labg3HXWnImPjbzZhBIgvjEjDpPTD/42cA6FhetCafJNs7VEYMiB0Aqisll3lPRYLd4oG7r5+RvBfxwklmcyL+7ma8ls75hjLPDArh7BKsCcnCeJhHzADiaXZdyTJMmNe5awVh2EspHnGmwu4ILU6LCZsNvnwDp8vGtpbrpa3UXxjrO+yTKhoj+tLNs74pJVdu6seLX+fLrMSOz+dZSpgslyVmPkUSgiAfbgJLBcIVme8vLnKb637kPB3mnzKKSDyz+UlHo3ZB3aqPrwQ+gfbebz92SYA0xEIi2/7xiL~-1~||0||~-1"
    }
    url = "https://www.data.ai/ajax/v2/query"
    params = {
        "query_identifier": "app_user_retention_table"
    }
    data = {
        "facets": [
            "est_retention_day__aggr"
        ],
        "filters": {
            "product_id": {
                "equal": app_id
            },
            "vertical_code": {
                "equal": "app"
            },
            "country_code": {
                "equal": country_code
            },
            "granularity": {
                "equal": "monthly"
            },
            "date": {
                "between": [
                    "2023-07-01",
                    "2024-07-31"
                ]
            },
            "retention_days": {
                "in": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    14,
                    30
                ]
            }
        },
        "breakdowns": {
            "date": {},
            "retention_days": {}
        },
        "order_by": [
            {
                "name": "date",
                "order": "asc"
            }
        ]
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    facets_data = []
    retention_days = []
    est_retention_day__aggr = []
    print(response.text)
    print(response)
    data = json.loads(response.text)['data']["facets"]
    for entry in data:
        facets_data.append(datetime.fromtimestamp(entry['date'] / 1000).strftime('%Y-%m-%d'))

        retention_days.append(entry['retention_days'])
        est_retention_day__aggr.append(entry['est_retention_day__aggr'])

    print(retention_days)
    print(facets_data)
    print(est_retention_day__aggr)
    print(len(facets_data), len(retention_days), len(est_retention_day__aggr))
    retention_days0 = [est_retention_day__aggr[i] for i in range(0, len(est_retention_day__aggr), 10)]
    retention_days1 = [est_retention_day__aggr[i] for i in range(1, len(est_retention_day__aggr), 10)]
    retention_days2 = [est_retention_day__aggr[i] for i in range(2, len(est_retention_day__aggr), 10)]
    retention_days3 = [est_retention_day__aggr[i] for i in range(3, len(est_retention_day__aggr), 10)]
    retention_days4 = [est_retention_day__aggr[i] for i in range(4, len(est_retention_day__aggr), 10)]
    retention_days5 = [est_retention_day__aggr[i] for i in range(5, len(est_retention_day__aggr), 10)]
    retention_days6 = [est_retention_day__aggr[i] for i in range(6, len(est_retention_day__aggr), 10)]
    retention_days7 = [est_retention_day__aggr[i] for i in range(7, len(est_retention_day__aggr), 10)]
    retention_days14 = [est_retention_day__aggr[i] for i in range(8, len(est_retention_day__aggr), 10)]
    retention_days30 = [est_retention_day__aggr[i] for i in range(9, len(est_retention_day__aggr), 10)]
    facets_datas = [facets_data[i] for i in range(0, len(facets_data), 10)]
    result_data = {
        "游戏名": [],
        "年月日期": facets_datas,
        "当日留存": retention_days0,
        "1日留存": retention_days1,
        "2日留存": retention_days2,
        "3日留存": retention_days3,
        "4日留存": retention_days4,
        "5日留存": retention_days5,
        "6日留存": retention_days6,
        "7日留存": retention_days7,
        "14日留存": retention_days14,
        "30日留存": retention_days30,
    }

    return result_data



if __name__ == '__main__':
    city_code = "US"
    check_date = "2024-08-12"
    games_list,games=req(city_code,check_date)
    for i,j in zip(games_list,games):
        # 生成 1 到 5 秒的随机浮点数
        sleep_time = random.uniform(1, 5)
        # 让程序睡眠随机生成的时间
        time.sleep(sleep_time)
        print(type(i),j)
        data_detail=req_detail(int(i),city_code)
        data_detail['游戏名']=[j for _ in range(len(data_detail['年月日期'])) ]
        df=pd.DataFrame(data_detail)
        csv_file_path = './采集数据/留存数据.csv'

        # 追加到 CSV 文件中
        df.to_csv(csv_file_path, mode='a', index=False,encoding='utf-8')


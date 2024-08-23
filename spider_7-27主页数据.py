import time

import requests
import json

def response_home_data(cookies,city,page):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/json",
        "origin": "https://www.data.ai",
        "priority": "u=1, i",
        "$referer": "https://www.data.ai/intelligence/genre/top?genre_id=(overlaps:\\u0021(2002,2003,2001,2004,2012,2005,2006,2007,2008,2009,2010,2011,2013,2014))&device_code=all&country_code=\\u0021(" + city + ")&date=\\u0021(%272024-02-04%27,%272024-07-20%27)&granularity=weekly&breakdowns=(unified_product_id:())&facets=\\u0021(est_download__sum)&order_by=\\u0021((name:est_download__sum,order:desc))&chart_genre_intelligence_top_charts_chart=(aggr:\\u0021t,axis:\\u0021((percent:\\u0021f,type:column)),showWeekends:\\u0021f,stack:\\u0021f)&chart.event_bubble.event_types=\\u0021(modifier_change,artwork_url_change,app_description,name_change,new_version,price_change,screenshot_change,app_company_id_change)",
        "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "x-csrftoken": "StMMJKAh9PtSh8xdtm2paTHW4rXhBRTS",
        "x-origin": "/intelligence/genre/top",
        "x-requested-with": "XMLHttpRequest"
    }
    cookies = cookies
    url = "https://www.data.ai/ajax/v2/query"
    params = {
        "query_identifier": "table_change(genre_intelligence_top_charts_table)"
    }
    data = {
        "facets": [
            "est_download__sum",
            "value_change(est_download__sum)__aggr",
            "est_cumulative_download__aggr",
            "value_change(est_cumulative_download__aggr)__aggr",
            "est_revenue__sum",
            "value_change(est_revenue__sum)__aggr",
            "est_cumulative_revenue__aggr",
            "value_change(est_cumulative_revenue__aggr)__aggr",
            "est_rpd__aggr",
            "value_change(est_rpd__aggr)__aggr",
            "est_usage_penetration__aggr",
            "value_change(est_usage_penetration__aggr)__aggr",
            "est_average_active_users__aggr",
            "value_change(est_average_active_users__aggr)__aggr",
            "est_install_penetration__aggr",
            "value_change(est_install_penetration__aggr)__aggr",
            "est_install_base__aggr",
            "value_change(est_install_base__aggr)__aggr",
            "est_open_rate__aggr",
            "value_change(est_open_rate__aggr)__aggr",
            "est_average_session_per_user__aggr",
            "value_change(est_average_session_per_user__aggr)__aggr",
            "est_average_session_duration__aggr",
            "value_change(est_average_session_duration__aggr)__aggr",
            "est_average_time_per_user__aggr",
            "value_change(est_average_time_per_user__aggr)__aggr",
            "est_total_time__aggr",
            "value_change(est_total_time__aggr)__aggr",
            "est_average_active_days__aggr",
            "value_change(est_average_active_days__aggr)__aggr",
            "est_percentage_active_days__aggr",
            "value_change(est_percentage_active_days__aggr)__aggr",
            "est_share_of_category_time__aggr",
            "value_change(est_share_of_category_time__aggr)__aggr"
        ],
        "filters": {
            "country_code": {
                "in": [
                    city
                ]
            },
            "date": {
                "between": [
                    "2024-02-04",
                    "2024-07-20"
                ]
            },
            "device_code": {
                "equal": "all"
            },
            "product_id.genre_id": {
                "overlaps": [
                    2002,
                    2003,
                    2001,
                    2004,
                    2012,
                    2005,
                    2006,
                    2007,
                    2008,
                    2009,
                    2010,
                    2011,
                    2013,
                    2014
                ]
            },
            "granularity": {
                "equal": "weekly"
            },
            "vertical_code": {
                "equal": "app"
            },
            "unified_product_id": {
                "in": {
                    "facets": [
                        "est_download__sum"
                    ],
                    "filters": {
                        "country_code": {
                            "in": [
                                city
                            ]
                        },
                        "date": {
                            "between": [
                                "2024-02-04",
                                "2024-07-20"
                            ]
                        },
                        "device_code": {
                            "equal": "all"
                        },
                        "product_id.genre_id": {
                            "overlaps": [
                                2002,
                                2003,
                                2001,
                                2004,
                                2012,
                                2005,
                                2006,
                                2007,
                                2008,
                                2009,
                                2010,
                                2011,
                                2013,
                                2014
                            ]
                        },
                        "granularity": {
                            "equal": "weekly"
                        },
                        "vertical_code": {
                            "equal": "app"
                        }
                    },
                    "breakdowns": {
                        "unified_product_id": {}
                    },
                    "pagination": {
                        "offset": 0,
                        "limit": 1000
                    },
                    "order_by": [
                        {
                            "name": "est_download__sum",
                            "order": "desc"
                        }
                    ]
                }
            },
            "value_change": {
                "span_value": 1,
                "span_unit": "PERIOD"
            }
        },
        "breakdowns": {
            "unified_product_id": {}
        },
        "pagination": {
            "offset": int(page*100),
            "limit": 100
        },
        "order_by": [
            {
                "name": "est_download__sum",
                "order": "desc"
            }
        ],
        "fields": {
            "product_id": {
                "fields": [
                    "device_code",
                    "genre_id",
                    "icon_url",
                    "is_sensitive",
                    "market_code",
                    "name",
                    "publisher_id",
                    "status",
                    "vertical_code"
                ],
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
                },
                "genre_id": {
                    "fields": [
                        "name"
                    ]
                }
            },
            "unified_product_id": {
                "fields": [
                    "company_id",
                    "device_code",
                    "genre_id",
                    "icon_url",
                    "is_sensitive",
                    "market_code",
                    "name",
                    "vertical_code"
                ],
                "company_id": {
                    "fields": [
                        "name",
                        "country_code",
                        "parent_company_id"
                    ],
                    "parent_company_id": {
                        "fields": [
                            "name"
                        ]
                    }
                },
                "genre_id": {
                    "fields": [
                        "name"
                    ]
                }
            }
        }
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    # print(response.text)
    data = json.loads(response.text)
    result=data["data"]
    print(data["data"])
    # print(response)
    return result
def response_detail_data(cookies,id):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/json",
        "origin": "https://www.data.ai",
        "priority": "u=1, i",
        "referer": "https://www.data.ai/apps/google-play/app/20600009288248/user-retention",
        "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "x-csrftoken": "StMMJKAh9PtSh8xdtm2paTHW4rXhBRTS",
        "x-origin": "/apps/google-play/app/20600009288248/user-retention",
        "x-requested-with": "XMLHttpRequest"
    }
    cookies = cookies
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
                "equal": 20600009288248
            },
            "vertical_code": {
                "equal": "app"
            },
            "country_code": {
                "equal": "US"
            },
            "granularity": {
                "equal": "monthly"
            },
            "date": {
                "between": [
                    "2023-06-01",
                    "2024-06-30"
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

    print(response.text)
    print(response)
if __name__ == '__main__':
    # 实时更新cookies数据
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
        "AMP_8c78419905": "JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJkMGJjMzYxMS1lMjY0LTQ3ZTctOWQ3Ni05MTVlMzQyZGQyMDclMjIlMkMlMjJ1c2VySWQlMjIlM0ExNjY4ODUzJTJDJTIyc2Vzc2lvbklkJTIyJTNBMTcyMzExNTI1NDU4MyUyQyUyMm9wdE91dCUyMiUzQWZhbHNlJTJDJTIybGFzdEV2ZW50VGltZSUyMiUzQTE3MjMxMTUyNTY3NzQlMkMlMjJsYXN0RXZlbnRJZCUyMiUzQTkzJTdE",
        "sid": "4a210009-3686-4cfa-80cb-1d282ba7813c",
        "django_language": "zh-cn",
        "MRDI": "gAN9cQBK9XYZAFggAAAAMWM5MDM3NWU4Mzc2NDYxYjg5OWY2OTE5ZTdlN2E4MzdxAXMu",
        "aa_user_token": "\".eJxNzD0PATEYAOA6DAaLzWY0NequPlYmEmMTW_P27SvXuPRSbQ-DxJ-2Wwx-wPO8i1fozdUoY3roGmIdCjWTRBUIAgtlCVJucGnosrbCCqjEymzVRENOtc6RbtoAXsnb0D8vGGN3MuCheSaHkQNim33ie4h08JF8dMl1dGotNbsfG6jxX-ZsGB4_3ZRl_gViJjTh:1seAHo:IYkxI8Z0bEXz2LiwIqW6WCgM8Sw\"",
        "_ga": "GA1.2.1774182953.1721904709",
        "_gid": "GA1.2.511014883.1723628694",
        "sessionId": "\".eJxVjs1Kw0AUhWOsraZYf3buXOrCEGsMzdauVHRRDMxumMzc0KFxksm9U6kguBJ9ur6GL-DeBERx9_FxDue8-i9244QdeJ6HgKgrU0ODGgkMvbPdVnPhaM4dQsO1uvlaHnls7y_NwYi8BHXrs15rBWrFjlvIk3GSwCRNJ3kUXxQqjQqZJudxNE4uRRHH2ZAq5K5WgkBZ_4Md_p_KhVyAUSxq9RPkwohyRVpiKKSsnKFwKhCuDYJBTXoJd5WC8uqn1O_-Va6RcJ_tixIa4nIOcsFJP4LdlN1oh8Ev2F4WDD63Rztnw9F6LesVPQc8e5gGdut0ZvtvMztw4TeoImCg:1seAZ7:vyLaSvqyPPzbsz0tW0uDwKuqexQ\"",
        "_ga_FHHFCC15CR": "GS1.1.1723628694.7.1.1723628714.0.0.0",
        "bm_mi": "604FB8D0FE64A76DF3AA4711397A7086~YAAQJEZ7aLwH4UyRAQAA1zGpUxgGY6jFQmXiPESk0y3FfIHNKs4qgEetqvSXorUcGyijk43Jfwr9Kmu4KM3uwFIM0o8svA6HVg4DWSZ+6NgpmuNfR6aqf4GwfU9s190ql9k5qwNFQjKty7nv6Y+x8CEUZvgHTrUkdFoaKxs7TwYqEZKeA9B0zX3vl/ISLpQQ1TCRgDyEz+knqfocGrzCwKdiLGu2GRdJZ3Lk0K3Tz4ESQy6sYt7vnSXrRm1mQ8B5FlhGieKF3RJEWWGO2NpPRz18fIWVrA7091S9AB7DV+yddI2lgQUVCxcKJ8johYOcqmF+KryinPSLfKg6BWeqp19eA2Pv40uqI/ahk0l+B0U=~1",
        "ak_bmsc": "B92C86D28F654DC3994F839AFD3DF1AB~000000000000000000000000000000~YAAQJEZ7aHgI4UyRAQAAFEipUxjk5k0Rcvt+ga+Yi5svbVufCqJ90Q0ulA5wh4VD5D5m2daAMEiludjZZ51onWT4FwO/JNfbE2NLF4YkhJVKv/L+pN8HlYeuWNvhUvRORzYPGQXBVuf/PTuOLgHwRU4M+jz3g/2uByP7/5RS3NO2Fcfa5CqWXSC0mt1Yf+POLqSf6fL82JwOSiIN0y8x/6ct7vFlZDnYRmb93exfq0ApM83/PWJvOizaLcBifPH4S8eqe4xIQCbStXsKjCcdRl0SiaTtM1aZSVco57cgb077p178M854rgTHquG4LrPkeMXww7fj8XAWdeAc++CZF8zbrItODXyvC5tgscdLxw41ctGNpbHnBTP7ut+jk+/dqTUDRG7xiCj+ywkCtBDiopbZE/7IcJjZDobP+b+BGvreVpgirS+/iONPYFBBsWNuvq9LWCD2U3Iq39IBMHqu+/uR0YH89Aqxlw5gzmAHZJVQAa0YQvY5FT3dhksrs34Ly5zCbQ==",
        "bm_sz": "40C0546A51786E958341E93DEB95DB8C~YAAQFUZ7aE0xbEGRAQAAQYu9UxgVpxrpX5j/MszGb7HPnT6zjuz0H2wHuo5n2lCxdftofN4Nn1rvfpcXxCjZluwS2cugGUPRxY88AL8gWr61uzsZ9U9vfJS2iBceAR9mG5GDGrvJmZSYUDjOtel//lI7CejlCT6P0cLfvicMcqEQs7zTsEhrUnbK5/8ZxhHUNDxdphtC/64ehhRCths1siqGqcO3DD+DEhczFeODMEEz10HBxWMVkVLNdB5n2jexFuZz3yOtrPBUxTQmphtulu+5pj9as92DFhBGZc9ccb8UmS71E5jTCyeM0y7CxiuXUVaRiWqvubAj75qnWjT3XLAJxPav/MsXJLnGgBb0dzUIdSZ0SGTEmS9FEVoQn1BABdM4yJ7/ah5yrJGewLJuybrIY+fCu7s5WwGxpnqioyLaL7j1bW5a+tOJBzNyXnFpcocMDumQfYYrUxSlo57ukmx97mOxUmZYo5qaqmWzheuh5LigDwAxo26FXyA3Ws6ZR9MudmfitLrwQ6BCbt1MkQ==~3158841~4274224",
        "RT": "\"z=1&dm=data.ai&si=039126af-22a4-497d-94d5-e17f4751ca61&ss=lzul02qk&sl=1g&tt=3pgf&bcn=%2F%2F17de4c20.akstat.io%2F&ld=1mhr1&nu=417d1aiu&cl=1m92o\"",
        "_abck": "09897E5ECFF864ADDDC84BE0DDB9BD36~0~YAAQFUZ7aHUxbEGRAQAAO6O9UwzBU0zvbiWaTNqp5KPBBlpCq3DFb6fBMLwLwP7VjtqiPIF72yZrWa4Ed1nOU5SwzMSZ52c/hvETbFRuEJ9t0hHt+S0z+SUhBlga+txbvBWxbVLYTcN6dxHIR8to4d6NgLLrKau+0J2QV2Tv7FEC4/nSawir6Y8h/hadO9StFwSKDYtomk67Mz0a6BMKCxA6FM6XeC8Hu7/uxXsd0/TBm1xgf+yw1e2RLevcQYc/pZ7dc/ihKViu8ylJ4wbaGVYnLZCkRm8Yfpj1DtD8LtwVQ9amgjAitfhfuywM++ZRGoWXXxwiwDQz3DJwBmPpaJYzkuUOHzGwgq39Jc2krYIpR7WXmCFrSTOV+N00FoKSqySnpq9mUsCNm9jufIB3SRAzLG/dtXowSx6gAdsYIcc2m0r9yRnWTUenQv/z6ps/Dy6u270zp6ffOlRACsEv/BjKlO0R/ohtPKX/00+VBHZ7x5lHM1XPmuqo02ZEqL8CxPmun3AyVN1+~-1~||0||~-1",
        "bm_sv": "930E06416CD9C724DD634D045DABF7E9~YAAQFUZ7aKExbEGRAQAAyKm9Uxiwqc2JDbuk6xu8yiY4TP0JbWUjReLi8xY8UaraqKcRyCM6W0VKP2ecIajmdludkQYs34IDlXPDoVkpy0i90WY1x4XNnGAcXu6Eq6aOiKPkscLudDTLz61qe+n06MdD03dYAaOXTnNli6GaYJ3XFA/lmyeMBvScvJNq1i6/mifxKuHBv2z8K9EeEoM63wlpfFkhcQwg4C8FW4nJjWjvfp4Ysm15Lj7Gl6zUF70=~1"
    }
    # 爬取城市列表
    city = "US"
    citylist=["AU","FR","CN"]
    # page页数
    page = 3
    # 返回json数据
    res=response_home_data(cookies,city,1)
    #
    # print(res)
    # for i in citylist:
    #     for j in range(1,100):
    #         try:
    #             res = response_home_data(cookies, i, j)  # 假设这里是你的爬取函数
    #             with open('data.json', 'a') as f:
    #                 json.dump(res, f)
    #                 f.write('\n')  # 每次写入一个JSON对象后换行，以便区分不同的JSON对象
    #             print(f"成功爬取城市{i}中第{j}页数据")
    #             time.sleep(3)
    #         except Exception as e:
    #             print(f"爬取城市{i}中第{j}页失败: {e}")
    #             break  # 如果发生错误，跳出当前城市的循环
    #         finally:
    #             print(f"现在爬取城市{i}中第{j}页数据结束")


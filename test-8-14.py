import time

import requests
import json

def request(city,data_time):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/json",
        "origin": "https://www.data.ai",
        "priority": "u=1, i",
        "$referer": "https://www.data.ai/intelligence/top-apps/store-rank/ios?date=%272024-08-14%27&country_code=" + city + "&device_code=ios-phone&ios.category_id=(equal:100001)&chart_store_rank_ios_chart_free$previous_range=(aggr:\\u0021f,axis:\\u0021((percent:\\u0021f,type:line)),showWeekends:\\u0021f,stack:\\u0021f)&store-rank.ios.view=free&store-rank.ios.rank-type=leaderboard&chart.event_bubble.event_types=\\u0021(modifier_change,artwork_url_change,app_description,name_change,new_version,price_change,screenshot_change,app_company_id_change)&product_id_meta=\\u0021(product_id.category_id)&store_rank.ios.chart_range=7",
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
        "AMP_8c78419905": "JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJkMGJjMzYxMS1lMjY0LTQ3ZTctOWQ3Ni05MTVlMzQyZGQyMDclMjIlMkMlMjJ1c2VySWQlMjIlM0ExNjY4ODUzJTJDJTIyc2Vzc2lvbklkJTIyJTNBMTcyMzExNTI1NDU4MyUyQyUyMm9wdE91dCUyMiUzQWZhbHNlJTJDJTIybGFzdEV2ZW50VGltZSUyMiUzQTE3MjMxMTUyNTY3NzQlMkMlMjJsYXN0RXZlbnRJZCUyMiUzQTkzJTdE",
        "sid": "4a210009-3686-4cfa-80cb-1d282ba7813c",
        "django_language": "zh-cn",
        "MRDI": "gAN9cQBK9XYZAFggAAAAMWM5MDM3NWU4Mzc2NDYxYjg5OWY2OTE5ZTdlN2E4MzdxAXMu",
        "aa_user_token": "\".eJxNzD0PATEYAOA6DAaLzWY0NequPlYmEmMTW_P27SvXuPRSbQ-DxJ-2Wwx-wPO8i1fozdUoY3roGmIdCjWTRBUIAgtlCVJucGnosrbCCqjEymzVRENOtc6RbtoAXsnb0D8vGGN3MuCheSaHkQNim33ie4h08JF8dMl1dGotNbsfG6jxX-ZsGB4_3ZRl_gViJjTh:1seAHo:IYkxI8Z0bEXz2LiwIqW6WCgM8Sw\"",
        "_ga": "GA1.2.1774182953.1721904709",
        "_gid": "GA1.2.511014883.1723628694",
        "sessionId": "\".eJxVjs1Kw0AUhWOsraZYf3buXOrCEGsMzdauVHRRDMxumMzc0KFxksm9U6kguBJ9ur6GL-DeBERx9_FxDue8-i9244QdeJ6HgKgrU0ODGgkMvbPdVnPhaM4dQsO1uvlaHnls7y_NwYi8BHXrs15rBWrFjlvIk3GSwCRNJ3kUXxQqjQqZJudxNE4uRRHH2ZAq5K5WgkBZ_4Md_p_KhVyAUSxq9RPkwohyRVpiKKSsnKFwKhCuDYJBTXoJd5WC8uqn1O_-Va6RcJ_tixIa4nIOcsFJP4LdlN1oh8Ev2F4WDD63Rztnw9F6LesVPQc8e5gGdut0ZvtvMztw4TeoImCg:1seAZ7:vyLaSvqyPPzbsz0tW0uDwKuqexQ\"",
        "_ga_FHHFCC15CR": "GS1.1.1723628694.7.1.1723628714.0.0.0",
        "bm_sz": "40C0546A51786E958341E93DEB95DB8C~YAAQdf4ZuJRyUyqRAQAAAWv/UxhRMYT9096Dvu7/20ICzFDY7fIZI+2Iu76PoCZAC5RaCwISR+vFAZAeiA4R/CQ90hA1OY0gEdqVS32DhDlq4c4LOLVQBwe4ojtR0PpxQatsK/YYNdGXxo3fo/cAxn86CCfwDqzwwEKANcyJawccfu9/GqI+x/R3L0yh6XEBJia8/cVSzgtvxb5JYGYMpDhKaaVzxUaAGQdS/B7HTiFU8/ZryICaX1PS4IlrFIqzZQtl9ebVFP+/3GdL+lX5psamGOde+9Ngh9ZxMa+AMfgOogzF3HCKGlYZrDIPLNKTW+CGgP2B008DgykzpoKbrLMoomnETS/DNCfpIQHuPkli37XGjOAw6rY96Yh7gs4v1luUeJQXTlBtSDrbwOrOMt84iC8S0qaCPjdU7pptcnczjIIysIU3fIy9OK4KvRq+tuDFKAG05YmwTZD+WPdOrZUjmdsx5G7/hsJRe8KasJoKREw+Fgs9oozdYFjijQ9yYxoonHpmplQm3U6MQxFaKQrusw==~3158841~4274224",
        "RT": "\"z=1&dm=data.ai&si=039126af-22a4-497d-94d5-e17f4751ca61&ss=lzulvzne&sl=1&tt=2jo&bcn=%2F%2F17de4c1d.akstat.io%2F&nu=4tyjb2t6&cl=3ay6j&ld=3b3vo\"",
        "_abck": "09897E5ECFF864ADDDC84BE0DDB9BD36~0~YAAQ0981Fz7Bs1ORAQAA3GMDVAxjtpIyu0oxY5lizW0Id1HWlnIj+PWPw2fRT3hfWEgFKxMqu9QoMScdVH7uQe0u9GOGyX11vTe8UflWrMWEaJPjw/lGOu3Vxok7+t5quqT4/h/qhZrM87OhdlfmMpYz+sQCmBVUdjF5VlZkJ3EBayDqfulbx+GetcG0HVcwEPnq3cyNbisOgLlvIa+q4re+UNDFI6x0Lc+bL30KKjEcwtmcIPlwwxobFA0qP0GgzuAPNm48AS2A06sT15ziCnNwQvgJM5rLv0oqeObVRc6kxuCYjTDsuM1U4rhwbPtOpvulBMupP4g7bHU4555MFCfyt//QyPQLect8rwlH2AfJvHgH5JUjMctZjmOyOEYm6fPvqW+s6Iyab84/1wz3hszXZJagbEJ3fnzBYc7PgM3i3cbklboQWNlw12JX6mTp29RiRm9zTWT8XAvsctl/FLXFlVeTFtxnW7psARBiibe8lWeaKjiSI6I5SxzD53KM6IU9zNxojCfGtwftua9JIf4kbyCLusGDhQH0R/sWc/2KaKm6oLFqx9pc2rgf1M2CEjiy57Qy85fR~-1~||0||~-1"
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
                "equal": data_time
            },
            "country_code": {
                "equal": city
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
                            "equal": data_time
                        },
                        "country_code": {
                            "equal": city
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
            "limit": 500
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
    data = json.loads(response.text)
    result = data["data"]
    dimensions=data["data"]['dimensions']
    facets=data["data"]['facets']
    print(dimensions)
    print("================")
    print(facets)
    return dimensions,facets
if __name__ == '__main__':
    u = ["ios-phone", "ios-tablet"]
    citys=['AU']
    # citys = ['AE', 'AG', 'AI', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BB', 'BE', 'BF', 'BG', 'BH', 'BJ', 'BM', 'BN',
    #          'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CG', 'CH', 'CL', 'CN', 'CO', 'CR', 'CV', 'CY', 'CZ', 'DE',
    #          'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FJ', 'FM', 'FR', 'GB', 'GD', 'GH', 'GM', 'GR', 'GT',
    #          'GW', 'GY', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH',
    #          'KN', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LK', 'LR', 'LT', 'LU', 'LV', 'MD', 'MG', 'MK', 'ML', 'MN',
    #          'MO', 'MR', 'MS', 'MT', 'MU', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'OM',
    #          'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PR', 'PT', 'PW', 'PY', 'QA', 'RO', 'RU', 'SA', 'SB', 'SC', 'SE', 'SG',
    #          'SI', 'SK', 'SL', 'SN', 'SR', 'ST', 'SV', 'SZ', 'TC', 'TD', 'TH', 'TJ', 'TM', 'TN', 'TR', 'TT', 'TW', 'TZ',
    #          'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VG', 'VN', 'WW', 'YE', 'ZA', 'ZW']
    data_time = "2024-08-14"
    for i in citys:
        print(i)
        dimensions,facets=request(i,data_time)
        time.sleep(5)
#
# import requests
# import json
#
#
# headers = {
#     "accept": "application/json, text/plain, */*",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "content-type": "application/json",
#     "origin": "https://www.data.ai",
#     "priority": "u=1, i",
#     "$referer": "https://www.data.ai/intelligence/top-apps/store-rank/ios?date=%272024-08-14%27&country_code=CN&device_code=ios-tablet&ios.category_id=(equal:100001)&chart_store_rank_ios_chart_free$previous_range=(aggr:\\u0021f,axis:\\u0021((percent:\\u0021f,type:line)),showWeekends:\\u0021f,stack:\\u0021f)&store-rank.ios.view=free&store-rank.ios.rank-type=leaderboard&chart.event_bubble.event_types=\\u0021(modifier_change,artwork_url_change,app_description,name_change,new_version,price_change,screenshot_change,app_company_id_change)&product_id_meta=\\u0021(product_id.category_id)&store_rank.ios.chart_range=7",
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
#     "AMP_8c78419905": "JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJkMGJjMzYxMS1lMjY0LTQ3ZTctOWQ3Ni05MTVlMzQyZGQyMDclMjIlMkMlMjJ1c2VySWQlMjIlM0ExNjY4ODUzJTJDJTIyc2Vzc2lvbklkJTIyJTNBMTcyMzExNTI1NDU4MyUyQyUyMm9wdE91dCUyMiUzQWZhbHNlJTJDJTIybGFzdEV2ZW50VGltZSUyMiUzQTE3MjMxMTUyNTY3NzQlMkMlMjJsYXN0RXZlbnRJZCUyMiUzQTkzJTdE",
#     "sid": "4a210009-3686-4cfa-80cb-1d282ba7813c",
#     "ak_bmsc": "7214E4C74923705AB51A7133FF1C5B39~000000000000000000000000000000~YAAQjPAPF/McJk6RAQAAEg0dUBj20+lM7jTrKQ5wZKM8HqYn114YEvH5Fb4ovMzDbRS5Puht23L4NKuMyDl3CIdHYFyFwNaAAXp0R1Ei4/h7l4Ib+G49dout86cr3Iu0pfk+kWmRiSYQXCPfeByENUGHwqI6BkrpseuFKl3kXBhNfx/5db7hNvorSqNNxYPwpiMKys5DD/oJcUvwIrEICJ06Rp4Zh6DAXRgUa3Uxiqafk53e+t9vaEkyES/2G0dKEsShjF3WkjmuUaVyFK6YHdxD+U0vQOq2uky1S3UGOTGr7AS3zfI/txkr2tm5tRqB+X7wFQIZF6itCsLE+fMbF9exY2HEQQDWxgVdS8CQwxe1Dw/SdiKSh0C4mtdsxpU3tVhZrvbxb0yj9TYPTLcjh7deu03PAeZUPtMVV01hwExKvgWa6BHlzhMRYT1THvdSF1kI6OcHQ6OP",
#     "django_language": "zh-cn",
#     "MRDI": "gAN9cQBK9XYZAFggAAAAMWM5MDM3NWU4Mzc2NDYxYjg5OWY2OTE5ZTdlN2E4MzdxAXMu",
#     "aa_user_token": "\".eJxNzD0PATEYAOA6DAaLzWY0NequPlYmEmMTW_P27SvXuPRSbQ-DxJ-2Wwx-wPO8i1fozdUoY3roGmIdCjWTRBUIAgtlCVJucGnosrbCCqjEymzVRENOtc6RbtoAXsnb0D8vGGN3MuCheSaHkQNim33ie4h08JF8dMl1dGotNbsfG6jxX-ZsGB4_3ZRl_gViJjTh:1seAHo:IYkxI8Z0bEXz2LiwIqW6WCgM8Sw\"",
#     "_ga": "GA1.2.1774182953.1721904709",
#     "_gid": "GA1.2.511014883.1723628694",
#     "sessionId": "\".eJxVjs1Kw0AUhWOsraZYf3buXOrCEGsMzdauVHRRDMxumMzc0KFxksm9U6kguBJ9ur6GL-DeBERx9_FxDue8-i9244QdeJ6HgKgrU0ODGgkMvbPdVnPhaM4dQsO1uvlaHnls7y_NwYi8BHXrs15rBWrFjlvIk3GSwCRNJ3kUXxQqjQqZJudxNE4uRRHH2ZAq5K5WgkBZ_4Md_p_KhVyAUSxq9RPkwohyRVpiKKSsnKFwKhCuDYJBTXoJd5WC8uqn1O_-Va6RcJ_tixIa4nIOcsFJP4LdlN1oh8Ev2F4WDD63Rztnw9F6LesVPQc8e5gGdut0ZvtvMztw4TeoImCg:1seAZ7:vyLaSvqyPPzbsz0tW0uDwKuqexQ\"",
#     "_ga_FHHFCC15CR": "GS1.1.1723628694.7.1.1723628714.0.0.0",
#     "bm_sz": "96B31CB55A941FF5CFCF43595672FCA8~YAAQJ+9jaLwCuU+RAQAAjYVuUBgVhOSXE8mbb9Q0QX1+WaexJCseabknMqC9Nj3UowDzEgQs7C4FHSAif6+NKXUqE4Y6STyV/qCNp0lQvTkkBsFUK9w3QEB6RZcaaMi70lur+0znih6/81jZRJEnyMeQRe++qZOrp9Vif5MhbbbaBtCozCDXhqDmlKxgIO0RBJe1+II3uiDAaYI84yEYGrowb2v5q6cdNl71F3+QktLYiUYIfxqiPSZ8SBeXwvP2nf5DM25sfVXcuYxD+L/Nn9ekzErsnOsFDZEVoRipr9HsY1BOJ5TkFRSb1yODBMr50+n8U46a5+PEIl7/i5EOxiXsntfEBtsUtN0AqtUS/6zsHsudrmmQnGjNsFdjLx0y1djpLAbCQsXxXfM4exagqU7QS6Yo2Ammm2bU9DOamnz1XzaLHoN+0krhlSJ1AR4AkeR2rrQM9fxJKm6B/A/0+EwzRCPaetkVdxZVCEW3Tc/5OmJq6qwXWDjk2PMabuCahXR9Wz47JeCw1BantyFZaRyFPw==~3687745~3748146",
#     "RT": "\"z=1&dm=data.ai&si=039126af-22a4-497d-94d5-e17f4751ca61&ss=lztmdbv1&sl=1k&tt=4yuh&bcn=%2F%2F17de4c0f.akstat.io%2F&ld=37g0x\"",
#     "_abck": "09897E5ECFF864ADDDC84BE0DDB9BD36~-1~YAAQpTMsF0aHmEORAQAAIe1yUAxKckQdKVycWmuMJFVsRDSPCfGauo47PG1bGpoowzLiYTFBkED1iFSNBI+H8nxgqsGZ3WiIEC4kuTLhPlEMx542QypdxvzYjqdPPsGuXoUK+tmLLC2kyJeNPky+y40An0+jszEM0JK8aC0WPxCd3EhCnaKhiVnjpxEYfWp1u3wlNdG6YGGcqBNhj7DraauVHi92TMaRWT0OKBwqxtRyeLO+kqe4lstdMJVw2ZNlqiX+usZ3W7ALSMaIzqTg9StqCpYOpBeMibjWHy9JHl65D14RkRHYIdd3EMlTaGJpy6Fs0oeDuP77ZD78G06mfwnuqntu7/hGK/QvN0mqlybXH2NZLflsKZcKh2R3VNELx3RaaIvhaHifa3iYPVqw6KpQuUmkLGm5yw63t38HGeAWvMR2ZEzC52XGHEmJvqVUDPH49DzoJ0D97eZSjLeLH5DbIHjcE/iMBpV3KH8HCk2QJpTP4hb2fVJZXOlqa5g/X9aAlaV7J4y3Pai5f/Idb2OkQb1oFY+QKsZA4gvN/qD7FUHernE69J8dQ9HbBx1I8509j0lM+GXGDl6ljB7JmFtPG1ITZom5+qLDGt0dQZkuXlp2+yaf3r5+fnVqW/0R/eE1BDHDXyfvfq/gIVfigFFqEq93Vg==~-1~||0||~-1",
#     "bm_sv": "9E0D5E8194AB8A273F1F410226DD042D~YAAQpTMsF0mHmEORAQAA+e9yUBiw4FFj4xAncVPBfV5mengZlUvaiRV9jY5ElYbGagijWpcfb6ZPHkdVSu8sR1SQgBYHVyNa6UnG3ygQtRhOYL3PCRRzFKshkJ5Htbovr6z0V8W64SR88ME3oZi841Bvmz+Q+pNkjMlqhpzSkrlJiDysZ/qXyjNmsXPhoebbRgBMRrGYGShyXvAczfnUIKL8/q8GUJ1EAhHMfxkaIsqH1lHfUSIyf/fkPYQwP44=~1"
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
#             "equal": "2024-08-14"
#         },
#         "country_code": {
#             "equal": "AU"
#         },
#         "device_code": {
#             "equal": "ios-tablet"
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
#                         "equal": "2024-08-14"
#                     },
#                     "country_code": {
#                         "equal": "AU"
#                     },
#                     "device_code": {
#                         "equal": "ios-tablet"
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
#         "limit": 1000
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
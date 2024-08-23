from datetime import datetime

import pandas
import requests
import json
#
#
# headers = {
#     "accept": "application/json, text/plain, */*",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "content-type": "application/json",
#     "origin": "https://www.data.ai",
#     "priority": "u=1, i",
#     "referer": "https://www.data.ai/apps/google-play/app/20600009288248/user-retention",
#     "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
#     "x-csrftoken": "StMMJKAh9PtSh8xdtm2paTHW4rXhBRTS",
#     "x-origin": "/apps/google-play/app/20600009288248/user-retention",
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
#     "django_language": "zh-cn",
#     "MRDI": "gAN9cQBK9XYZAFggAAAAMWM5MDM3NWU4Mzc2NDYxYjg5OWY2OTE5ZTdlN2E4MzdxAXMu",
#     "aa_user_token": "\".eJxNzD0PATEYAOA6DAaLzWY0NequPlYmEmMTW_P27SvXuPRSbQ-DxJ-2Wwx-wPO8i1fozdUoY3roGmIdCjWTRBUIAgtlCVJucGnosrbCCqjEymzVRENOtc6RbtoAXsnb0D8vGGN3MuCheSaHkQNim33ie4h08JF8dMl1dGotNbsfG6jxX-ZsGB4_3ZRl_gViJjTh:1seAHo:IYkxI8Z0bEXz2LiwIqW6WCgM8Sw\"",
#     "_ga": "GA1.2.1774182953.1721904709",
#     "_gid": "GA1.2.511014883.1723628694",
#     "sessionId": "\".eJxVjs1Kw0AUhWOsraZYf3buXOrCEGsMzdauVHRRDMxumMzc0KFxksm9U6kguBJ9ur6GL-DeBERx9_FxDue8-i9244QdeJ6HgKgrU0ODGgkMvbPdVnPhaM4dQsO1uvlaHnls7y_NwYi8BHXrs15rBWrFjlvIk3GSwCRNJ3kUXxQqjQqZJudxNE4uRRHH2ZAq5K5WgkBZ_4Md_p_KhVyAUSxq9RPkwohyRVpiKKSsnKFwKhCuDYJBTXoJd5WC8uqn1O_-Va6RcJ_tixIa4nIOcsFJP4LdlN1oh8Ev2F4WDD63Rztnw9F6LesVPQc8e5gGdut0ZvtvMztw4TeoImCg:1seAZ7:vyLaSvqyPPzbsz0tW0uDwKuqexQ\"",
#     "_ga_FHHFCC15CR": "GS1.1.1723628694.7.1.1723628714.0.0.0",
#     "bm_mi": "604FB8D0FE64A76DF3AA4711397A7086~YAAQJEZ7aLwH4UyRAQAA1zGpUxgGY6jFQmXiPESk0y3FfIHNKs4qgEetqvSXorUcGyijk43Jfwr9Kmu4KM3uwFIM0o8svA6HVg4DWSZ+6NgpmuNfR6aqf4GwfU9s190ql9k5qwNFQjKty7nv6Y+x8CEUZvgHTrUkdFoaKxs7TwYqEZKeA9B0zX3vl/ISLpQQ1TCRgDyEz+knqfocGrzCwKdiLGu2GRdJZ3Lk0K3Tz4ESQy6sYt7vnSXrRm1mQ8B5FlhGieKF3RJEWWGO2NpPRz18fIWVrA7091S9AB7DV+yddI2lgQUVCxcKJ8johYOcqmF+KryinPSLfKg6BWeqp19eA2Pv40uqI/ahk0l+B0U=~1",
#     "ak_bmsc": "B92C86D28F654DC3994F839AFD3DF1AB~000000000000000000000000000000~YAAQJEZ7aHgI4UyRAQAAFEipUxjk5k0Rcvt+ga+Yi5svbVufCqJ90Q0ulA5wh4VD5D5m2daAMEiludjZZ51onWT4FwO/JNfbE2NLF4YkhJVKv/L+pN8HlYeuWNvhUvRORzYPGQXBVuf/PTuOLgHwRU4M+jz3g/2uByP7/5RS3NO2Fcfa5CqWXSC0mt1Yf+POLqSf6fL82JwOSiIN0y8x/6ct7vFlZDnYRmb93exfq0ApM83/PWJvOizaLcBifPH4S8eqe4xIQCbStXsKjCcdRl0SiaTtM1aZSVco57cgb077p178M854rgTHquG4LrPkeMXww7fj8XAWdeAc++CZF8zbrItODXyvC5tgscdLxw41ctGNpbHnBTP7ut+jk+/dqTUDRG7xiCj+ywkCtBDiopbZE/7IcJjZDobP+b+BGvreVpgirS+/iONPYFBBsWNuvq9LWCD2U3Iq39IBMHqu+/uR0YH89Aqxlw5gzmAHZJVQAa0YQvY5FT3dhksrs34Ly5zCbQ==",
#     "bm_sz": "40C0546A51786E958341E93DEB95DB8C~YAAQFUZ7aE0xbEGRAQAAQYu9UxgVpxrpX5j/MszGb7HPnT6zjuz0H2wHuo5n2lCxdftofN4Nn1rvfpcXxCjZluwS2cugGUPRxY88AL8gWr61uzsZ9U9vfJS2iBceAR9mG5GDGrvJmZSYUDjOtel//lI7CejlCT6P0cLfvicMcqEQs7zTsEhrUnbK5/8ZxhHUNDxdphtC/64ehhRCths1siqGqcO3DD+DEhczFeODMEEz10HBxWMVkVLNdB5n2jexFuZz3yOtrPBUxTQmphtulu+5pj9as92DFhBGZc9ccb8UmS71E5jTCyeM0y7CxiuXUVaRiWqvubAj75qnWjT3XLAJxPav/MsXJLnGgBb0dzUIdSZ0SGTEmS9FEVoQn1BABdM4yJ7/ah5yrJGewLJuybrIY+fCu7s5WwGxpnqioyLaL7j1bW5a+tOJBzNyXnFpcocMDumQfYYrUxSlo57ukmx97mOxUmZYo5qaqmWzheuh5LigDwAxo26FXyA3Ws6ZR9MudmfitLrwQ6BCbt1MkQ==~3158841~4274224",
#     "RT": "\"z=1&dm=data.ai&si=039126af-22a4-497d-94d5-e17f4751ca61&ss=lzul02qk&sl=1g&tt=3pgf&bcn=%2F%2F17de4c20.akstat.io%2F&ld=1mhr1&nu=417d1aiu&cl=1m92o\"",
#     "_abck": "09897E5ECFF864ADDDC84BE0DDB9BD36~0~YAAQFUZ7aHUxbEGRAQAAO6O9UwzBU0zvbiWaTNqp5KPBBlpCq3DFb6fBMLwLwP7VjtqiPIF72yZrWa4Ed1nOU5SwzMSZ52c/hvETbFRuEJ9t0hHt+S0z+SUhBlga+txbvBWxbVLYTcN6dxHIR8to4d6NgLLrKau+0J2QV2Tv7FEC4/nSawir6Y8h/hadO9StFwSKDYtomk67Mz0a6BMKCxA6FM6XeC8Hu7/uxXsd0/TBm1xgf+yw1e2RLevcQYc/pZ7dc/ihKViu8ylJ4wbaGVYnLZCkRm8Yfpj1DtD8LtwVQ9amgjAitfhfuywM++ZRGoWXXxwiwDQz3DJwBmPpaJYzkuUOHzGwgq39Jc2krYIpR7WXmCFrSTOV+N00FoKSqySnpq9mUsCNm9jufIB3SRAzLG/dtXowSx6gAdsYIcc2m0r9yRnWTUenQv/z6ps/Dy6u270zp6ffOlRACsEv/BjKlO0R/ohtPKX/00+VBHZ7x5lHM1XPmuqo02ZEqL8CxPmun3AyVN1+~-1~||0||~-1",
#     "bm_sv": "930E06416CD9C724DD634D045DABF7E9~YAAQFUZ7aKExbEGRAQAAyKm9Uxiwqc2JDbuk6xu8yiY4TP0JbWUjReLi8xY8UaraqKcRyCM6W0VKP2ecIajmdludkQYs34IDlXPDoVkpy0i90WY1x4XNnGAcXu6Eq6aOiKPkscLudDTLz61qe+n06MdD03dYAaOXTnNli6GaYJ3XFA/lmyeMBvScvJNq1i6/mifxKuHBv2z8K9EeEoM63wlpfFkhcQwg4C8FW4nJjWjvfp4Ysm15Lj7Gl6zUF70=~1"
# }
# url = "https://www.data.ai/ajax/v2/query"
# params = {
#     "query_identifier": "app_user_retention_table"
# }
# data = {
#     "facets": [
#         "est_retention_day__aggr"
#     ],
#     "filters": {
#         "product_id": {
#             "equal": 1617391485
#         },
#         "vertical_code": {
#             "equal": "app"
#         },
#         "country_code": {
#             "equal": "US"
#         },
#         "granularity": {
#             "equal": "monthly"
#         },
#         "date": {
#             "between": [
#                 "2023-07-01",
#                 "2024-07-31"
#             ]
#         },
#         "retention_days": {
#             "in": [
#                 0,
#                 1,
#                 2,
#                 3,
#                 4,
#                 5,
#                 6,
#                 7,
#                 14,
#                 30
#             ]
#         }
#     },
#     "breakdowns": {
#         "date": {},
#         "retention_days": {}
#     },
#     "order_by": [
#         {
#             "name": "date",
#             "order": "asc"
#         }
#     ]
# }
# data = json.dumps(data, separators=(',', ':'))
# response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
#
# print(response.text)
# print(response)

# app_id=512939461
# headers = {
#     "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
#     "x-origin": "/apps/ios/app/"+str(app_id)+"/user-retention",
#     "sec-ch-ua-mobile": "?0",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
#     "content-type": "application/json",
#     "accept": "application/json, text/plain, */*",
#     "Referer": "https://www.data.ai/apps/ios/app/"+str(app_id)+"/user-retention",
#     "x-requested-with": "XMLHttpRequest",
#     "x-csrftoken": "StMMJKAh9PtSh8xdtm2paTHW4rXhBRTS",
#     "sec-ch-ua-platform": "\"Windows\""
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
#     "django_language": "zh-cn",
#     "MRDI": "gAN9cQBK9XYZAFggAAAAMWM5MDM3NWU4Mzc2NDYxYjg5OWY2OTE5ZTdlN2E4MzdxAXMu",
#     "aa_user_token": "\".eJxNzD0PATEYAOA6DAaLzWY0NequPlYmEmMTW_P27SvXuPRSbQ-DxJ-2Wwx-wPO8i1fozdUoY3roGmIdCjWTRBUIAgtlCVJucGnosrbCCqjEymzVRENOtc6RbtoAXsnb0D8vGGN3MuCheSaHkQNim33ie4h08JF8dMl1dGotNbsfG6jxX-ZsGB4_3ZRl_gViJjTh:1seAHo:IYkxI8Z0bEXz2LiwIqW6WCgM8Sw\"",
#     "_ga": "GA1.2.1774182953.1721904709",
#     "_gid": "GA1.2.511014883.1723628694",
#     "sessionId": "\".eJxVjs1Kw0AUhWOsraZYf3buXOrCEGsMzdauVHRRDMxumMzc0KFxksm9U6kguBJ9ur6GL-DeBERx9_FxDue8-i9244QdeJ6HgKgrU0ODGgkMvbPdVnPhaM4dQsO1uvlaHnls7y_NwYi8BHXrs15rBWrFjlvIk3GSwCRNJ3kUXxQqjQqZJudxNE4uRRHH2ZAq5K5WgkBZ_4Md_p_KhVyAUSxq9RPkwohyRVpiKKSsnKFwKhCuDYJBTXoJd5WC8uqn1O_-Va6RcJ_tixIa4nIOcsFJP4LdlN1oh8Ev2F4WDD63Rztnw9F6LesVPQc8e5gGdut0ZvtvMztw4TeoImCg:1seAZ7:vyLaSvqyPPzbsz0tW0uDwKuqexQ\"",
#     "_ga_FHHFCC15CR": "GS1.1.1723628694.7.1.1723628714.0.0.0",
#     "ak_bmsc": "6554AB80E0C4979230DCFAB32B44D153~000000000000000000000000000000~YAAQ0981F64HtFORAQAAi5UGVBizeSGNIFHhmoZ77ttR4v0R9+ORPRNsbjTEwItUU3z/COmImkSPllNWQWHfftrBZrt9dtH25/jjt9kTX+URcEYfWv6m5mGRSLFyzhvC6j7BLNhqPs3/3vf8AefiBtBp/2ov8f2spnt4GHfLKE4hJv3oMfoPH6IZcwyNjdX02z4TSqASHXusLo8KLvD8qqYhsFpzUsdF50q9C1tiS75M/x+ENYgGM2VzMC/yODxPS7my4571UJuw718NFDXAbBi6dYr/z91968WDZ07IZyRa04swgXXyetpEk9T0rH7MYwqulBucZYk4WeDY6jO3aaynhzngCpLxE8HKO/sSIArssQVsKK9l1cNdDrYez2zNzlEVr2HP",
#     "RT": "\"z=1&dm=data.ai&si=039126af-22a4-497d-94d5-e17f4751ca61&ss=lzuppwfr&sl=c&tt=j2f&bcn=%2F%2F17de4c1a.akstat.io%2F&nu=q50h3jx&cl=3wx9&ld=3r10\"",
#     "_abck": "09897E5ECFF864ADDDC84BE0DDB9BD36~-1~YAAQ0981F6autFORAQAAxJ4PVAzR8nsOux0SHdw/AJwPZ1EMRIHVipxJTn7Fb3QZbikIr7826c8JajnoarrbzwWK+cb2ANNc5LqtRRu1KzWj1crts6R91xOePHIGxfh8qinV9+GQ1LYj1BqzSU21ajNYEIIjy6cZQDnaF4+LBpiTZWH8nSE/wzWbgiDQMaIDdA23ebLyXYkNqkyUsKVVru0PVQi2qkLo4vs1Ep0RodjeC9VHIwIjv+aHn8viNNdz2tkHn0aCLxsN1OUI0SoIKK+4uQBGh1bwcCTqhYVH9+369HoII8GVXqGluvpUww2JwI5c/Kov0YHlSI4Bvkf1JhVfZGRnTDCok3N47Creb99HTJ6QEdhPr8nc7dgC9Rj8SgG0idQD5obwj+xw88OTLFAVhH100n87+51ngXCcK1V5SeyAL/P+JAZz6L80/oc1E5UfmzrImX8qOcMzkNBnuU2n~-1~-1~-1",
#     "bm_sv": "2B1976295EE13F3A9BE9CB4CFC9F120B~YAAQ0981F6eutFORAQAAxJ4PVBjM1q2jUxzwas+DgGMOonUnb9JDtJrD2ZJtALQgQO8No0/DdH94IottjOdHUQFLZF+xsTTYeY3++lbS12GHZNVG5XVY/hzsy/7SfeIJgeU6byEjXGpq8s8DTkINJK6J38jpvZIyDbCMtgi8jQ7A0IF5REu39BtBMIS3OjQacWVi1tS10s+ti4XYTJsI4z96hLmT6FfJbLA8Z4uwMNovuGQROQ9pw6/701NQyg==~1",
#     "bm_sz": "40C0546A51786E958341E93DEB95DB8C~YAAQ0981F6iutFORAQAAxJ4PVBgdv2h3PB0nxgw0GpUbmdbg+PQMUwrBabWelMTPhUj8HovVDbza1HrUSRvHGCEn/qj2cH7NPqGdTNhbRizUKgZLjppRRgOhibIv8DLgz+eQYBXhN4sRBNMfvQKqQlNtMr703Z/tVEEnW7zhJCUauXSS4ZNuw6pZaxiPwMaDYdY0BCoJGWdqf3Lk725g7qNTDgKNjFEeMJvcHlMwN336FEYcpIQyCfnT2Y/ljlnoaKNiQ0Mt/jra0SacU7r7pH9P7unH3pUneBunJvi5X/o3+RqpNF4NHX75JF7tb3JMtdsbLykjh5AMqYe0qwv2jdjjY9n1SM64kLFqi6rgsUPVmZSNXmubGinaZBZsIQcL4rNQDWeDSVKdmxyZrsqV+sTS8UxLgE7PaNwCeQibty7dpMcsysQ5c6oKePZ3dH1eTBGadwgwfECxpIBT/579iXe2Axovo+u6tgu237sPqpqzEC6Am7/6PyMJTxRgoJwcpV/2GpcTOJNTUUDVHpfe74Y=~3158841~4274224"
# }
# url = "https://www.data.ai/ajax/v2/query"
# params = {
#     "query_identifier": "app_user_retention_table"
# }
# data = {
#     "facets": [
#         "est_retention_day__aggr"
#     ],
#     "filters": {
#         "product_id": {
#             "equal": app_id
#         },
#         "vertical_code": {
#             "equal": "app"
#         },
#         "country_code": {
#             "equal": "US"
#         },
#         "granularity": {
#             "equal": "monthly"
#         },
#         "date": {
#             "between": [
#                 "2023-07-01",
#                 "2024-07-31"
#             ]
#         },
#         "retention_days": {
#             "in": [
#                 0,
#                 1,
#                 2,
#                 3,
#                 4,
#                 5,
#                 6,
#                 7,
#                 14,
#                 30
#             ]
#         }
#     },
#     "breakdowns": {
#         "date": {},
#         "retention_days": {}
#     },
#     "order_by": [
#         {
#             "name": "date",
#             "order": "asc"
#         }
#     ]
# }
# data = json.dumps(data, separators=(',', ':'))
# response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
#
# print(response.text)
# print(response)
# import requests
# import json
# country_code="AU"
# app_id=512939461
# headers = {
#     "accept": "application/json, text/plain, */*",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "content-type": "application/json",
#     "origin": "https://www.data.ai",
#     "priority": "u=1, i",
#     "$referer": "https://www.data.ai/apps/ios/app/"+str(app_id)+"/user-retention?app_user_retention_chart$chart_compare_facets=\\u0021(est_retention_day__aggr)&country_code=AU&granularity=daily&cohort_granularity=monthly&date=%272024-07-01%27&chart_app_user_retention_chart=(aggr:\\u0021f,axis:\\u0021((percent:\\u0021f,type:line)),showWeekends:\\u0021f,stack:\\u0021f)&chart.event_bubble.event_types=\\u0021(modifier_change,artwork_url_change,app_description,name_change,new_version,price_change,screenshot_change,app_company_id_change)",
#     "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
#     "x-csrftoken": "StMMJKAh9PtSh8xdtm2paTHW4rXhBRTS",
#     "x-origin": "/apps/ios/app/"+str(app_id)+"/user-retention",
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
#     "django_language": "zh-cn",
#     "MRDI": "gAN9cQBK9XYZAFggAAAAMWM5MDM3NWU4Mzc2NDYxYjg5OWY2OTE5ZTdlN2E4MzdxAXMu",
#     "aa_user_token": "\".eJxNzD0PATEYAOA6DAaLzWY0NequPlYmEmMTW_P27SvXuPRSbQ-DxJ-2Wwx-wPO8i1fozdUoY3roGmIdCjWTRBUIAgtlCVJucGnosrbCCqjEymzVRENOtc6RbtoAXsnb0D8vGGN3MuCheSaHkQNim33ie4h08JF8dMl1dGotNbsfG6jxX-ZsGB4_3ZRl_gViJjTh:1seAHo:IYkxI8Z0bEXz2LiwIqW6WCgM8Sw\"",
#     "_ga": "GA1.2.1774182953.1721904709",
#     "_gid": "GA1.2.511014883.1723628694",
#     "sessionId": "\".eJxVjs1Kw0AUhWOsraZYf3buXOrCEGsMzdauVHRRDMxumMzc0KFxksm9U6kguBJ9ur6GL-DeBERx9_FxDue8-i9244QdeJ6HgKgrU0ODGgkMvbPdVnPhaM4dQsO1uvlaHnls7y_NwYi8BHXrs15rBWrFjlvIk3GSwCRNJ3kUXxQqjQqZJudxNE4uRRHH2ZAq5K5WgkBZ_4Md_p_KhVyAUSxq9RPkwohyRVpiKKSsnKFwKhCuDYJBTXoJd5WC8uqn1O_-Va6RcJ_tixIa4nIOcsFJP4LdlN1oh8Ev2F4WDD63Rztnw9F6LesVPQc8e5gGdut0ZvtvMztw4TeoImCg:1seAZ7:vyLaSvqyPPzbsz0tW0uDwKuqexQ\"",
#     "_ga_FHHFCC15CR": "GS1.1.1723628694.7.1.1723628714.0.0.0",
#     "ak_bmsc": "6554AB80E0C4979230DCFAB32B44D153~000000000000000000000000000000~YAAQ0981F64HtFORAQAAi5UGVBizeSGNIFHhmoZ77ttR4v0R9+ORPRNsbjTEwItUU3z/COmImkSPllNWQWHfftrBZrt9dtH25/jjt9kTX+URcEYfWv6m5mGRSLFyzhvC6j7BLNhqPs3/3vf8AefiBtBp/2ov8f2spnt4GHfLKE4hJv3oMfoPH6IZcwyNjdX02z4TSqASHXusLo8KLvD8qqYhsFpzUsdF50q9C1tiS75M/x+ENYgGM2VzMC/yODxPS7my4571UJuw718NFDXAbBi6dYr/z91968WDZ07IZyRa04swgXXyetpEk9T0rH7MYwqulBucZYk4WeDY6jO3aaynhzngCpLxE8HKO/sSIArssQVsKK9l1cNdDrYez2zNzlEVr2HP",
#     "bm_sv": "2B1976295EE13F3A9BE9CB4CFC9F120B~YAAQLv4ZuMYpQUSRAQAAY+IbVBieG0wwgq97/w0ZKRKTOBXceNy1Qin4N1l521W/OwBQrhUaSrk8pjWzZeJiVcQt2w5masn+1+qLukXCVUz8FyvS1uBLH58GqbI8hVOlxDvNRIpvNw13iOs2FDm1uSzyx8SRbMe/0mJjeiD1W00/y5hkSotEmEOmkiplfMnqJhW305XoBqWk/I8abzEUEJBQ8PrefNUhRl0uXZREY1iW3WrSzQZITZTs79QZFg==~1",
#     "bm_sz": "40C0546A51786E958341E93DEB95DB8C~YAAQLv4ZuMcpQUSRAQAAY+IbVBjpdtacBYGSUktIVR8R389wreckFlyjhtsMJoDT4Wp3YO2piYXs0CXQuCC7qV1ch45zcN44STfoddSaQalPYY7/v/hsrmnqTOQy9XuU6yP8JL6z+staAIryUo1bXrH4COsN8ot+YL+i4NxO1E3uRj1vPxa2UC8YW0180r+Y6UhVW0+Pmybx8jrfTVBxbl9IkpuxQEO/bd+ILvQEYFAuGWD3Q+lmSRyZ7QoOthiYax3nvoiVKgzQoQZ+n2YuMOGW++5QuuPjX8ezN8p9k2wDQ6qdiwDcQwy4/wGxUJI1BXYn9Q22u3ojDP3NWz3Q+mJ3XMMxHiL7xezPWD51drVdfHbUP1OL5Et+fSSYoif6c0y0TT8pjpakOkF4xtzGBq7Vhrb9m57WE9y9Gnb56wq20SpR8pCx7S7yhmql/suRfa8uoaZtWCGeGoaeL4eDMxXchdOVWgYLubzBX7ZvNIoJco1DHLRUYc9ZwVQ/HKsm2AetpkUeCu3FG0R0a8Y=~3158841~4274224",
#     "RT": "\"z=1&dm=data.ai&si=039126af-22a4-497d-94d5-e17f4751ca61&ss=lzuppwfr&sl=j&tt=1yy0&bcn=%2F%2F17de4c1a.akstat.io%2F&ld=l5px&nu=5kdphet&cl=jfgj\"",
#     "_abck": "09897E5ECFF864ADDDC84BE0DDB9BD36~0~YAAQLv4ZuJQrQUSRAQAAbQccVAyR/9PiQgLHWOptNGGEpmUhvVN481wkCV3OAou6I4jvKP2s06H1BUQkQGGhBfAKy9phu265d01IFPQqPOuUxIZ4f9ZPsegg86NpBLodFPuMW/QLES5OteTP+lpxx8f4oEqiC4/7W/APqGWVJX7zwJ9X9M8Z1yHjzUW7bKyuZ0IeTbahq23mUbL1BkMwd4XWVl/5u60Ejghi7DZLGPHzxQsY0d3Yd2efz8W4XtEbiSLPu/WBl32NxEi7pHnmqyjCdeqfb3LhgoUnLc4vboYBN+5OnKVJc0ejm8deFcO1blm8CR6p8RncF9ro4fgSJ9WyE65Vl9ynGXAlR1BYTZ3oMaQJxUNGteW76hkCNmE44dWJMhzFOk7VL0yXC5EfGjH4fWloAK/ODdH4Na7vBphpmBW3KFWaF81cams13bfIRPdOhZWfGrxLLfi3NUfRmgY=~-1~||0||~-1"
# }
# url = "https://www.data.ai/ajax/v2/query"
# params = {
#     "query_identifier": "app_user_retention_table"
# }
# data = {
#     "facets": [
#         "est_retention_day__aggr"
#     ],
#     "filters": {
#         "product_id": {
#             "equal": app_id
#         },
#         "vertical_code": {
#             "equal": "app"
#         },
#         "country_code": {
#             "equal": country_code
#         },
#         "granularity": {
#             "equal": "monthly"
#         },
#         "date": {
#             "between": [
#                 "2023-07-01",
#                 "2024-07-31"
#             ]
#         },
#         "retention_days": {
#             "in": [
#                 0,
#                 1,
#                 2,
#                 3,
#                 4,
#                 5,
#                 6,
#                 7,
#                 14,
#                 30
#             ]
#         }
#     },
#     "breakdowns": {
#         "date": {},
#         "retention_days": {}
#     },
#     "order_by": [
#         {
#             "name": "date",
#             "order": "asc"
#         }
#     ]
# }
# data = json.dumps(data, separators=(',', ':'))
# response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
#
# print(response.text)
# print(response)
import requests
import json
app_id=1617391485
country_code="DE"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.data.ai",
    "priority": "u=1, i",
    "referer": "https://www.data.ai/apps/ios/app/"+str(app_id)+"/user-retention",
    "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "x-csrftoken": "StMMJKAh9PtSh8xdtm2paTHW4rXhBRTS",
    "x-origin": "/apps/ios/app/"+str(app_id)+"/user-retention",
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
    "sessionId": "\".eJxVjs1Kw0AUhWOsraZYf3buXOrCEGsMzdauVHRRDMxumMzc0KFxksm9U6kguBJ9ur6GL-DeBERx9_FxDue8-i9244QdeJ6HgKgrU0ODGgkMvbPdVnPhaM4dQsO1uvlaHnls7y_NwYi8BHXrs15rBWrFjlvIk3GSwCRNJ3kUXxQqjQqZJudxNE4uRRHH2ZAq5K5WgkBZ_4Md_p_KhVyAUSxq9RPkwohyRVpiKKSsnKFwKhCuDYJBTXoJd5WC8uqn1O_-Va6RcJ_tixIa4nIOcsFJP4LdlN1oh8Ev2F4WDD63Rztnw9F6LesVPQc8e5gGdut0ZvtvMztw4TeoImCg:1seAZ7:vyLaSvqyPPzbsz0tW0uDwKuqexQ\"",
    "_ga_FHHFCC15CR": "GS1.1.1723628694.7.1.1723628714.0.0.0",
    "ak_bmsc": "B5A4538C3C4B2F3CD653B43A3C9B7215~000000000000000000000000000000~YAAQiJTYF7lT0lORAQAAIOBxVRjUE3YAzzr7XFBTVQ8rAW0uztLNtAQqx8bMTv/3/Hb1w29eMLPRfCgCeju84d14eMljsN1l/F2Tx2pLBL9FuQKxRApv8XFB+Mpb3XKkVTQsKX8FE1+ozM2jW6JlObPR+uCyWm1PqxdH6/tvtVGnw7yGcA/lSEov8FV60PypkkToctDJcRkph+phY+HnYkTSABdnrOQNMGUL9bCJXEMBH/tzbkZH8Of9lRrp4NzqK8j+YGqF08rzA56guAci1NXZNECvkO9poAEBg8e0ezS0mz8lwG8x5UYvYixWGOsC88K+zb+33kEjtGyuD4LGyMOhxldpCENnZd7j3TOjtUlGuqeyZ6YTxdjZgy/zWuGv+J4MEqNI",
    "_abck": "09897E5ECFF864ADDDC84BE0DDB9BD36~0~YAAQiJTYF5JU0lORAQAA0O5xVQyiDGui14L4GaP6D8t4MV+qQ35VZR4SsxnpzvF2MSyOFFSuCGKrmDHzmtG5nHkpmwUX7NONbBuvUxASrKLZpkPyFJxcXEYWq4F9rIs7Rp/7hqOqfvks8jJ/XiwDFDTBD5q+T/dBeopx7k0I3xWFXHubmeo0hW+FO/w1Z5T1P3IR25qKUPTUrGJZ8kjRoBlMYlCVRnlJb5cdwef5IV9SOpGHHtp4sRd7UYJqbU6Lfo3L6FvKbI2Qxir6Pd/NIkx3Oex9u3kKSGc/oQL+TAclLmElYC7mnHd/G9281Zau9QaPYku/ekYjUwiDINYDu4w/e0QBanisCuVXwjYCS/uT18XCkeFH5fSZBdcegBpBR4Wqquyr7cv9jibrl41axcP0DovfiNmpwQoVloH/6ac31NKYoorI82l7c0IrWsNaiS7m798wsx81I/D4acpZ88Y=~-1~-1~-1",
    "bm_sz": "9B3937C4EB1ABBF608C00DDF90556DE3~YAAQiJTYF5RU0lORAQAA0O5xVRgQcyGDrP6sCZvU7SM6//Ftw+FRs3ArTMBVZ6R9Lds6WmOiZH3NjvCNK3mwGfaFX6+ef9zZatcLZcgfne6vtsTz6oqwSlNULsasnYjRsqarY8nOIwDaN3QfsiYPGkRDk8wWGXDDiBPOW/bAb/ga7KdShuq3grF/IHFVkCLM/9n3hctSkRNuouQJ/ssNO7ctM9AF+emWFERKkbmeyPjUndq8Li7//00kMiyhEifeA/3RNaPzntW4eFHFOcL5im46XdLgteRCvG3NhOGtc1Wose5naHveg8TNmXMhJV1BElxxQqjIRhSlLtvk7ULcFbJCwEXT6knZz+VsST57DhTb2lEBMVm4WPRDRgWX2ODwWQOQvB56Fd2FuTKL3w==~3228466~3160372",
    "bm_sv": "9632DD8C19C6D19764201BBC6E461257~YAAQiJTYF65V0lORAQAAtv9xVRjbvjnd5E0Y+aGBqNZLZc5fHDz4txPETx7gYTGjx3WFtGP8uif+XPBZq7+a1L94klocm7e+v1uDxpR/GDExNVLZ65h0mR7RRroM3WoksmIBx6nbAvit9x4CuiP5cjGDvPteSbvhu8ALeTSMtmcMt+VG+i7GuCB7Hcm/vRpRpM9EIpyRaK0Xp96Wielrva4ycnYlbJY+Rw96DNPfzFjm13ZJBatE+SWBU6M+~1",
    "RT": "\"z=1&dm=data.ai&si=039126af-22a4-497d-94d5-e17f4751ca61&ss=lzv3o5mw&sl=2&tt=pu&bcn=%2F%2F17de4c1f.akstat.io%2F&nu=4tyjb2t6&cl=1g9bvk&ld=1ie\""
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
facets_data=[]
retention_days=[]
est_retention_day__aggr=[]
print(response.text)
print(response)
data=json.loads(response.text)['data']["facets"]
for entry in data:
    facets_data.append(datetime.fromtimestamp(entry['date'] / 1000).strftime('%Y-%m-%d'))

    retention_days.append(entry['retention_days'])
    est_retention_day__aggr.append(entry['est_retention_day__aggr'])

print(retention_days)
print(facets_data)
print(est_retention_day__aggr)
print(len(facets_data),len(retention_days),len(est_retention_day__aggr))
retention_days0=[est_retention_day__aggr[i] for i in range(0, len(est_retention_day__aggr), 10)]
retention_days1=[est_retention_day__aggr[i] for i in range(1, len(est_retention_day__aggr), 10)]
retention_days2=[est_retention_day__aggr[i] for i in range(2, len(est_retention_day__aggr), 10)]
retention_days3=[est_retention_day__aggr[i] for i in range(3, len(est_retention_day__aggr), 10)]
retention_days4=[est_retention_day__aggr[i] for i in range(4, len(est_retention_day__aggr), 10)]
retention_days5=[est_retention_day__aggr[i] for i in range(5, len(est_retention_day__aggr), 10)]
retention_days6=[est_retention_day__aggr[i] for i in range(6, len(est_retention_day__aggr), 10)]
retention_days7=[est_retention_day__aggr[i] for i in range(7, len(est_retention_day__aggr), 10)]
retention_days14=[est_retention_day__aggr[i] for i in range(8, len(est_retention_day__aggr), 10)]
retention_days30=[est_retention_day__aggr[i] for i in range(9, len(est_retention_day__aggr), 10)]
facets_datas=[facets_data[i] for i in range(0, len(facets_data), 10)]
result_data={
    "游戏名":facets_datas,
    "年月日期":facets_datas,
    "当日留存":retention_days0,
    "1日留存":retention_days1,
    "2日留存":retention_days2,
    "3日留存":retention_days3,
    "4日留存":retention_days4,
    "5日留存":retention_days5,
    "6日留存":retention_days6,
    "7日留存":retention_days7,
    "14日留存":retention_days14,
    "30日留存":retention_days30,
}
data_res=pandas.DataFrame(result_data)
print(data_res)

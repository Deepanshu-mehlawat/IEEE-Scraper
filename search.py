import requests
import json
def search(term):
    # Define the URL for the POST request
    url = "https://ieeexplore.ieee.org/rest/search"

    # Headers as inferred from the cURL request
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
        "Content-Type": "application/json",
        "Cookie": "hum_ieee_visitor=d925890c-8af9-4424-9f0c-357ede383146; hum_ieee_synced=true; s_ecid=MCMID%7C46644538782537441492818869985903455545; _cc_id=91a135c545c53c0ef34500fe79aa3e60; fp=a61ebdaf31749dab49045e75cda8d821; osano_consentmanager_uuid=bce4123f-0b2d-4d55-80b3-cd275a55cfa6; _zitok=933f1d4def48af181e321728883815; osano_consentmanager=baO_Wk8e2WvVQVzU6_NPejIBgx2yP82NzJ4BMrHxgCDOFCQAT2UvI-or-k3s7gW5N4KEzGc5igYOY0_GnJ-C37F_GQUBSowUfOm009gq03ujnHVPgfTjpeDSYkO-lC8VNemTTBuPFP6m01t9e5_2bY9kMqElJbGmRN3Z1eBwwz4YhmJjjSn6Q2JDRCb4KIbV34NfXbs3Bn0Ju8doAATclqGp4D5zzgvgtsZlzQpuJPozSMXiWbhdSCxl7rMtpfLHkSM2lDEQ-hAtvJB0FExDiRMNgcqcmWgq1Ry8i1BP5fImNo5jaeXHOyI3UtOA6p2xKYsprn7x8C4=; AWSALBAPP-1=_remove_; AWSALBAPP-2=_remove_; AWSALBAPP-3=_remove_; WLSESSION=385970698.47873.0000; AMCVS_8E929CC25A1FB2B30A495C97%40AdobeOrg=1; AMCV_8E929CC25A1FB2B30A495C97%40AdobeOrg=359503849%7CMCMID%7C46644538782537441492818869985903455545%7CMCIDTS%7C20116%7CMCAID%7CNONE%7CMCOPTOUT-1737996334s%7CNONE%7CMCAAMLH-1738593934%7C12%7CMCAAMB-1738593934%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C5.0.1; s_cc=true; panoramaId_expiry=1738075798579; panoramaId=4ee112adaf1205091fe79dc8a245a9fb927a8f0c27ec0a168299d37ba4e637ec; panoramaIdType=panoDevice; ipList=152.58.65.231; __gpi=UID=00000f109b0205a4:T=1726730072:RT=1737993662:S=ALNI_MaHv_kR5B3oLIZ8lkVrVejMVbbScg; __eoi=ID=f7f99cae2c43a618:T=1726730072:RT=1737993662:S=AA-AfjaQeZCiXnzuQw5dADbqKYDQ; __gads=ID=4e600270b86fa326:T=1726730072:RT=1737993661:S=ALNI_MZASkTSP8KDW-AnaDL4cdiZ-2Ofmg; TS016349ac=01f15fc87c3da02d742f23d165a3be243ed9612a539ce6da2fb38799b30fa0698266e96f2f71eac3c1684a172cff794152a380a3aa; JSESSIONID=D407C2917AC44F72A7F125445DAE9018; ipCheck=152.58.65.231; s_sq=%5B%5BB%5D%5D; AWSALBAPP-0=AAAAAAAAAACPbnjs/BLhpK3Ibp6q76qIvwH4Tyc2yJiA+6M30X2vNNKlOSpMvHNP8rMct5nVcvfO2MD448uJDuFmYBlNyTFtYKsdjPNMPvJhInuU7d62VN42hzf/Rwf8C0s/yMbokOiKrMRbBGVpQKGti+mxAD+ZwfAVMMX23bHay71nCXck1GQ0S6fWC6Fj/DCh8TOGfPNrtfeGwp9TuQ==; TSaf720a17029=0807dc117eab2800030f526a9ae9ca7827d298cac58bc43b7b9c71a0b2d6fc151a78f35cd7b52d872b26bd2114cd789e; TS8b476361027=0807dc117eab2000d91413720d9396f0f8c0b7d06cd67da13230ef6975b762088faea920ac77962508e89f8658113000b8b3494812fcf484fdb769816e53156fa3b13986a672b11965e0040bcec828ac3b053ba6a8332b51e4e80badbde001b3; utag_main=v_id:0192091f3ed9001268aeaeebef4a0506f002b06700978$_sn:22$_se:13$_ss:0$_st:1737995742054$vapi_domain:ieeexplore.ieee.org$ses_id:1737992932374%3Bexp-session$_pn:7%3Bexp-session",
        "Origin": "https://ieeexplore.ieee.org",
        "Referer": "https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=Depth%20Map",
        "Sec-CH-UA": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "X-Security-Request": "required"
    }

    # Payload (JSON data)
    payload = {
        "newsearch": True,
        "queryText": term,
        "highlight": True,
        "returnFacets": ["ALL"],
        "returnType": "SEARCH",
        "matchPubs": True,
        "ranges":["2020_2025_Year"],
        "sortType":"paper-citations"
    }

    # Send POST request with headers and payload
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check the response
    if response.status_code == 200:
        print("Response received successfully:")
        try:
            # Parse and pretty print the JSON response
            data = response.json()
            #commenting the file saving part for now
            #with open(f"searches\{term}.json", "w", encoding="utf-8") as json_file:
            #    json.dump(data, json_file, indent=4, ensure_ascii=False)
            #print(json.dumps(data, indent=4, ensure_ascii=False))
        except json.JSONDecodeError:
            return ["Failed to parse JSON response"]
    else:
        print(f"Request failed with status code: {response.status_code}")
        return [response.text]  # Print the raw response for debugging
    links = []
    #print(data.keys())
    for i in data["records"]:
        links.append("https://ieeexplore.ieee.org"+i["documentLink"])
    return links
if __name__ == "__main__":
    print(search("EV charging"))
        
    

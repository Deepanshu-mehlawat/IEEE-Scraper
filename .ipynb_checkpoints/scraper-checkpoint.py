import re
import json
import requests
from bs4 import BeautifulSoup

def extract_metadata(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36",
        "cookie": "hum_ieee_visitor=d925890c-8af9-4424-9f0c-357ede383146; hum_ieee_synced=true; s_ecid=MCMID%7C46644538782537441492818869985903455545; _cc_id=91a135c545c53c0ef34500fe79aa3e60; fp=a61ebdaf31749dab49045e75cda8d821; osano_consentmanager_uuid=bce4123f-0b2d-4d55-80b3-cd275a55cfa6; _zitok=933f1d4def48af181e321728883815; osano_consentmanager=baO_Wk8e2WvVQVzU6_NPejIBgx2yP82NzJ4BMrHxgCDOFCQAT2UvI-or-k3s7gW5N4KEzGc5igYOY0_GnJ-C37F_GQUBSowUfOm009gq03ujnHVPgfTjpeDSYkO-lC8VNemTTBuPFP6m01t9e5_2bY9kMqElJbGmRN3Z1eBwwz4YhmJjjSn6Q2JDRCb4KIbV34NfXbs3Bn0Ju8doAATclqGp4D5zzgvgtsZlzQpuJPozSMXiWbhdSCxl7rMtpfLHkSM2lDEQ-hAtvJB0FExDiRMNgcqcmWgq1Ry8i1BP5fImNo5jaeXHOyI3UtOA6p2xKYsprn7x8C4=; AWSALBAPP-1=_remove_; AWSALBAPP-2=_remove_; AWSALBAPP-3=_remove_; WLSESSION=385970698.47873.0000; AMCVS_8E929CC25A1FB2B30A495C97%40AdobeOrg=1; AMCV_8E929CC25A1FB2B30A495C97%40AdobeOrg=359503849%7CMCMID%7C46644538782537441492818869985903455545%7CMCIDTS%7C20116%7CMCAID%7CNONE%7CMCOPTOUT-1737996334s%7CNONE%7CMCAAMLH-1738593934%7C12%7CMCAAMB-1738593934%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C5.0.1; s_cc=true; panoramaId_expiry=1738075798579; panoramaId=4ee112adaf1205091fe79dc8a245a9fb927a8f0c27ec0a168299d37ba4e637ec; panoramaIdType=panoDevice; ipList=152.58.65.231; __gpi=UID=00000f109b0205a4:T=1726730072:RT=1737993662:S=ALNI_MaHv_kR5B3oLIZ8lkVrVejMVbbScg; __eoi=ID=f7f99cae2c43a618:T=1726730072:RT=1737993662:S=AA-AfjaQeZCiXnzuQw5dADbqKYDQ; __gads=ID=4e600270b86fa326:T=1726730072:RT=1737993661:S=ALNI_MZASkTSP8KDW-AnaDL4cdiZ-2Ofmg; TS016349ac=01f15fc87c3da02d742f23d165a3be243ed9612a539ce6da2fb38799b30fa0698266e96f2f71eac3c1684a172cff794152a380a3aa; JSESSIONID=D407C2917AC44F72A7F125445DAE9018; ipCheck=152.58.65.231; s_sq=%5B%5BB%5D%5D; AWSALBAPP-0=AAAAAAAAAACPbnjs/BLhpK3Ibp6q76qIvwH4Tyc2yJiA+6M30X2vNNKlOSpMvHNP8rMct5nVcvfO2MD448uJDuFmYBlNyTFtYKsdjPNMPvJhInuU7d62VN42hzf/Rwf8C0s/yMbokOiKrMRbBGVpQKGti+mxAD+ZwfAVMMX23bHay71nCXck1GQ0S6fWC6Fj/DCh8TOGfPNrtfeGwp9TuQ==; TSaf720a17029=0807dc117eab2800030f526a9ae9ca7827d298cac58bc43b7b9c71a0b2d6fc151a78f35cd7b52d872b26bd2114cd789e; TS8b476361027=0807dc117eab2000d91413720d9396f0f8c0b7d06cd67da13230ef6975b762088faea920ac77962508e89f8658113000b8b3494812fcf484fdb769816e53156fa3b13986a672b11965e0040bcec828ac3b053ba6a8332b51e4e80badbde001b3; utag_main=v_id:0192091f3ed9001268aeaeebef4a0506f002b06700978$_sn:22$_se:13$_ss:0$_st:1737995742054$vapi_domain:ieeexplore.ieee.org$ses_id:1737992932374%3Bexp-session$_pn:7%3Bexp-session"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": f"Failed to fetch page, status code: {response.status_code}"}

    soup = BeautifulSoup(response.content, "html.parser")

    script_tag = soup.find("script", string=re.compile(r"xplGlobal\.document\.metadata"))
    if not script_tag:
        return {"error": "Metadata script not found in the page"}

    script_content = script_tag.string

    metadata_match = re.search(r"xplGlobal\.document\.metadata\s*=\s*(\{.*?\});", script_content, re.DOTALL)
    if not metadata_match:
        return {"error": "Metadata not found in the script"}

    metadata_json = metadata_match.group(1)
    try:
        metadata = json.loads(metadata_json)
    except json.JSONDecodeError:
        return {"error": "Failed to parse metadata JSON"}

    extracted_data = {
        "title": metadata.get("title", "Not available"),
        "abstract": metadata.get("abstract", "Not available"),
        "keywords": metadata.get("keywords", "Not available")
    }

    return extracted_data

url = "https://ieeexplore.ieee.org/document/10082570"  # Replace with the actual URL
result = extract_metadata(url)

# Print the result in JSON format
print(json.dumps(result, indent=4, ensure_ascii=False))

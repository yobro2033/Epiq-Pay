import requests, time, string, random, socket, struct

proxyList = []

def loadProxies():
    proxies = open("proxies.txt").read().splitlines()
    for proxy in proxies:
        try:
            if len(proxy.split(":")) == 2:
                ip = proxy.split(":")[0]
                port = proxy.split(":")[1]
                proxyData = {
                    "http": "http://{}:{}".format(ip, port),
                    "https": "http://{}:{}".format(ip, port),
                }
                proxyList.append(proxyData)
            else:
                ip = proxy.split(":")[0]
                port = proxy.split(":")[1]
                user = proxy.split(":")[2]
                password = proxy.split(":")[3]
                proxyData = {
                    "http": "http://{}:{}@{}:{}".format(user, password, ip, port),
                    "https": "http://{}:{}@{}:{}".format(user, password, ip, port),
                }
                proxyList.append(proxyData)
        except:
            pass

try:
    loadProxies()
except:
    pass

listOrders = """"""

for orderData in listOrders.splitlines():
    orderToken = orderData.split('/')[-1]
    print(orderData)
    session = requests.Session()
    if len(proxyList) > 0:
        session.proxies = random.choice(proxyList)
    headers = {
        'authority': 'api.digitaltorana.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://claim.epiqpay.com',
        'pragma': 'no-cache',
        'referer': 'https://claim.epiqpay.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'x-api-key': 'da2-32zr373z4re4remnogqwjexbja',
    }

    json_data = {
        'operationName': 'GetMemberPaymentOptions',
        'variables': {
            'token': orderToken
        },
        'query': 'query GetMemberPaymentOptions($token: String) {\n  getMemberPaymentOptions(token: $token) {\n    items {\n      ...PaymentOption\n      __typename\n    }\n    paymentProvidersSettings {\n      ...MemberPaymentProviderSettings\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PaymentOption on PaymentOption {\n  id\n  name\n  type\n  image\n  tremendousProductId\n  externalName\n  upstreamCompatible\n  upstreamConfiguration {\n    configuration {\n      label\n      value\n      __typename\n    }\n    label\n    name\n    type\n    validation\n    validation_ref\n    verify_email\n    __typename\n  }\n  __typename\n}\n\nfragment MemberPaymentProviderSettings on MemberPaymentProviderSettings {\n  tremendous {\n    ...MemberTremendousProviderSettings\n    __typename\n  }\n  sandbox\n  __typename\n}\n\nfragment MemberTremendousProviderSettings on MemberTremendousProviderSettings {\n  tremendousCampaignId\n  tremendousClientId\n  tremendousFundingSourceId\n  __typename\n}',
    }
    timeOut = False
    while timeOut == False:
        try:
            response = session.post('https://api.digitaltorana.com/graphql', headers=headers, json=json_data)
            if response.status_code < 310:
                response = response.json()
                timeOut = True
            else:
                print(f"[1] {response.status_code}")
                if len(proxyList) > 0:
                    session.proxies = random.choice(proxyList)
        except:
            if len(proxyList) > 0:
                session.proxies = random.choice(proxyList)
    listProductsAvailable = response['data']['getMemberPaymentOptions']['items']
    for product in listProductsAvailable:
        if product['id'] == 'TRMD_PAYPAL_DOMESTIC':
            tremendousProductId = product['tremendousProductId']

    paymentProvidersSettings = response['data']['getMemberPaymentOptions']['paymentProvidersSettings']
    for each in paymentProvidersSettings:
        if each["sandbox"] == False:
            tremendousFundingSourceId = each["tremendous"]["tremendousFundingSourceId"]
            tremendousClientId = each["tremendous"]["tremendousClientId"]
            tremendousCampaignId = each["tremendous"]["tremendousCampaignId"]
            break

    headers = {
        'authority': 'api.digitaltorana.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://claim.epiqpay.com',
        'pragma': 'no-cache',
        'referer': 'https://claim.epiqpay.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'x-api-key': 'da2-32zr373z4re4remnogqwjexbja',
    }

    json_data = {
        'operationName': 'GetCurrentMember',
        'variables': {
            'token': orderToken
        },
        'query': 'query GetCurrentMember($token: String) {\n  getCurrentMember(token: $token) {\n    classActionId\n    campaignId\n    amount\n    paymentOptionId\n    status\n    simpleStatus\n    name\n    email\n    memberOfacStatus\n    showPassedThreshold\n    paymentData {\n      email\n      firstName\n      lastName\n      __typename\n    }\n    __typename\n  }\n}',
    }
    timeOut = False
    while timeOut == False:
        try:
            response = session.post('https://api.digitaltorana.com/graphql', headers=headers, json=json_data)
            if response.status_code < 310:
                response = response.json()
                timeOut = True
            else:
                print(f"[2] {response.status_code}")
                if len(proxyList) > 0:
                    session.proxies = random.choice(proxyList)
        except:
            if len(proxyList) > 0:
                session.proxies = random.choice(proxyList)
    classActionId = response['data']['getCurrentMember']['classActionId']
    campaignId = response['data']['getCurrentMember']['campaignId']
    amount = response['data']['getCurrentMember']['amount']
    paymentOptionId = response['data']['getCurrentMember']['paymentOptionId']
    status = response['data']['getCurrentMember']['status']
    simpleStatus = response['data']['getCurrentMember']['simpleStatus']
    claimantName = response['data']['getCurrentMember']['name']
    claimantEmail = response['data']['getCurrentMember']['email']

    headers = {
        'authority': 'api.tremendous.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'access-control-allow-credentials': 'true',
        'access-control-allow-origin': '*',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://reward.tremendous.com',
        'pragma': 'no-cache',
        'referer': 'https://reward.tremendous.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    data = {
        'reward[value][denomination]': str(amount),
        'reward[value][currency_code]': 'USD',
        'reward[products][]': str(tremendousProductId),
        'reward[campaign_id]': str(campaignId),
        'reward[recipient][name]': str(claimantName),
        'reward[recipient][email]': str(claimantEmail),
        'public_key': tremendousClientId
    }
    timeOut = False
    while timeOut == False:
        try:
            response = session.post('https://api.tremendous.com/v1/embed/bootstrap/', headers=headers, data=data)
            if response.status_code < 310:
                #response = response.json()
                timeOut = True
            else:
                print(f"[3] {response.status_code}")
                if len(proxyList) > 0:
                    session.proxies = random.choice(proxyList)
        except:
            if len(proxyList) > 0:
                session.proxies = random.choice(proxyList)
    #print(response.text)

    headers = {
        'authority': 'api.tremendous.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'access-control-allow-credentials': 'true',
        'access-control-allow-origin': '*',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://reward.tremendous.com',
        'pragma': 'no-cache',
        'referer': 'https://reward.tremendous.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    json_data = {
        'public_key': tremendousClientId,
        'payment': {
            'funding_source_id': tremendousFundingSourceId
        },
        'reward': {
            'campaign_id': campaignId,
            'value': {
                'denomination': float(amount),
                'currency_code': 'USD',
            },
            'recipient': {
                'name': claimantName,
                'email': claimantEmail,
            },
            'products': [
                tremendousProductId,
            ],
        },
        'payout': {
            'name': claimantName,
            'paypal_email': claimantEmail,
            'confirm_paypal_email': claimantEmail,
            'country_code': 'US',
            'catalog_id': tremendousProductId
        },
        'device': {
            'hash': ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32)),
            'components': [],
        },
    }
    timeOut = False
    while timeOut == False:
        try:
            response = session.post('https://api.tremendous.com/v1/embed/', headers=headers, json=json_data)
            if response.status_code < 310:
                response = response.json()
                timeOut = True
            else:
                print(f"[4] {response.status_code}")
                if len(proxyList) > 0:
                    session.proxies = random.choice(proxyList)
        except:
            if len(proxyList) > 0:
                session.proxies = random.choice(proxyList)
    #print(response)
    rewardId = response['reward']['id']
    orderId = response['order']['id']

    headers = {
        'authority': 'api.digitaltorana.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://claim.epiqpay.com',
        'pragma': 'no-cache',
        'referer': 'https://claim.epiqpay.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'x-api-key': 'da2-32zr373z4re4remnogqwjexbja',
    }

    json_data = {
        'operationName': 'ConfirmTremendousReward',
        'variables': {
            'token': orderToken,
            'orderId': orderId,
            'rewardId': rewardId,
            'paymentOptionId': 'TRMD_PAYPAL_DOMESTIC',
            'externalId': '',
        },
        'query': 'mutation ConfirmTremendousReward($token: String!, $paymentOptionId: String!, $externalId: String!, $orderId: String, $rewardId: String) {\n  confirmTremendousReward(\n    token: $token\n    paymentOptionId: $paymentOptionId\n    externalId: $externalId\n    orderId: $orderId\n    rewardId: $rewardId\n  ) {\n    rewardId\n    rewardCreatedAt\n    paymentOptionName\n    __typename\n  }\n}',
    }
    timeOut = False
    while timeOut == False:
        try:
            response = session.post('https://api.digitaltorana.com/graphql', headers=headers, json=json_data)
            if response.status_code < 310:
                #response = response.json()
                timeOut = True
            else:
                print(f"[5] {response.status_code}")
                if len(proxyList) > 0:
                    session.proxies = random.choice(proxyList)
        except:
            if len(proxyList) > 0:
                session.proxies = random.choice(proxyList)
    print(response.text)
    with open("result.txt", "a") as myfile:
        myfile.write(orderToken + ":::" + str(response.text) + "\n")
        myfile.close()

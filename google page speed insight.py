import requests
api_key = "AIzaSyBaag7chpBebyPHuCIKwCkvXW6BL9FKhps"
test_url = "https://developers.google.com"

#r =requests.get(test_url)

api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={test_url}&key={api_key}'
r = requests.get(api_url)
if r.status_code == 200:
    data = r.json()
    loading_ex = data.get('loadingExperience').get("metrics").get("CUMULATIVE_LAYOUT_SHIFT_SCORE").get('percentile')
    print(loading_ex)


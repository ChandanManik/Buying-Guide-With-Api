user = 'manik'  # the user in which the auth. token is given
website_url = 'https://testsite.local/' #Your website url
wp_title = "Ulefone Note 7T: "+que # Your Post Title
content = finalpost # Your Post content here
slug = mahinsl #Your Post URL
pythonapp = ''  # paste here your auth. token

url = website_url +'/wp-json/wp/v2'  # the url of the wp access location
token = base64.standard_b64encode((user + ':' + pythonapp).encode('utf-8')) # we have to encode the usr and pw
headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

post = {'title': wp_title,
        'slug': slug,
        'status': 'publish',
        'content': content,
        'categories': catas,
        'author': '1',
        'format': 'standard',
        }

r = requests.post(url + '/posts', headers=headers, json=post)
print( website_url +'/'+ slug + ' Has Been Posted')
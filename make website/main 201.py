#from requests import get  #2001 #Gutenberg
#from pprint import pprint


#catch_url = 'https://mobile-phone-server.vercel.app/phones'
#res = get(catch_url)

#if res.status_code ==200:
    #data = res.json()
    #mobiles = data.get('RECORDS')
    #print(mobiles[0])

#2002
# NEED FUCNTION TO GENERATE IMAGE FROM OTHERS

#FROM WORDPRESS
#<!-- wp:image {"align":"center","sizeSlug":"large"} --><figure class="wp-block-image aligncenter size-large"><img src="https://fdn2.gsmarena.com/vv/bigpic/ulefone-note-7t.jpg" alt="Ulefone Note 7T image"/><figcaption class="wp-element-caption">Ulefone Note 7T</figcaption></figure><!-- /wp:image -->


def images_from_url(img_src, phone_name):
    output = f'<!-- wp:image {{"align":"center","sizeSlug":"large"}} --><figure class="wp-block-image aligncenter size-large"><img src="{img_src}" alt="{phone_name}"/><figcaption class="wp-element-caption">{phone_name}</figcaption></figure><!-- /wp:image -->'
    return output
    
#TEST URL
#print(images_from_url(img_src='https://fdn2.gsmarena.com/vv/bigpic/ulefone-note-7t.jpg',phone_name='Apple 14 pro'))

# NEED TO DICTIONARY FUNCTION TO MAKE TABLE
#<!-- wp:table --><figure class="wp-block-table"><table><tbody><tr><td>key1</td><td>value1</td></tr><tr><td>key2</td><td>value2</td></tr></tbody></table></figure><!-- /wp:table -->
def dictionary_table(dic):
    codes = '<!-- wp:table --><figure class="wp-block-table"><table><tbody>'

    for key, value in dic.items():
        tr_data= f'<tr><td>{key}</td><td>{value}</td></tr>'
        codes+= tr_data
    codes += '</tbody></table></figure><!-- /wp:table -->'
    return codes
    

thisdict = {

    'brand': 'ford',
    'model': 'and',
    'year' : 2022
}
#TEST URL
#test = dictionary_table(thisdict)
#print(test)

#NEED TO PARAGRAPH DICTIONARY: #2003

def wp_para(text):
    code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code
#TEST URL
#test = wp_para('Combines user attributes with known attributes and fill in defaults when needed.')
#print(test)










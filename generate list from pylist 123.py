def li_html(u_list):
    start = '<!-- wp:list --><ul>'
    for elements in u_list:
        start += f'<ul><!-- wp:list-item --><li>{elements}</li><!-- /wp:list-item -->'
        end = '</ul><!-- /wp:list -->'
        output = start+end
        return output

#def dic_li(list):
    #pass

def headers(username, password):
    import base64
    credential = f'{username}:{password}'
    token = base64.b64encode(credential.encode())
    output = {'Authorizaton': f'Basic {token.decode('utf-8')}'}
    return output

print(li_html(['1','2','3']))
#print(data)
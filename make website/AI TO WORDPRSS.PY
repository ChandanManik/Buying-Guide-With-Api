# import openai
# import base64
# import requests

# openai.api_key = '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'


# def wp2(text):
#     code = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
#     return code

# def wpara(text):
#     code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
#     return code

# def ai_ans(prompt):
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt= prompt,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     output = response.get('choices')[0].get('text')
#     return output

# keyw = input('Enter your Key: ')
# content = wpara(ai_ans(f'write short intro about {keyw}').strip().strip('\n'))
# prompt = wp2(ai_ans(f'write four questions about {keyw}'))
# #question = wp2(ai_ans(prompt))
# #ques_data = question.strip().split('\n')
# last_line = wpara(ai_ans(f'write 20 word description about {prompt}').strip().strip('\n'))

# # queans ={}
# # for qr in ques_data:
# #     output = f'{qr} {last_line}'
# #     answers = ai_ans(output).strip().strip('\n')
# #     queans[output] = answers


# user = 'manik'
# seckey = 'di1h EJSX qAzS 24g8 FS5P TaD6' 
# credential = f'{user}:{seckey}'
# token = base64.b64encode(credential.encode())
# headers = {'Authorization': f'Basic {token.decode("utf-8")}'}


# title = f'Buying Guide & FAQ About {keyw}'

# data = {
#     'title': title.title(),
#     'content' : content,
#     'slug': keyw.replace(' ', '-')

# }
# apis_ur = 'https://testsite.local/wp-json/wp/v2/posts'
# r = requests.post(apis_ur, data = data, headers = headers, verify = False)
# print(r.json())

print('hello world')
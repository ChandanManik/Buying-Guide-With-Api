#Slugify//
data = input('enter url :')

def slugifys(texts):
    output = texts.strip().lower().replace(' ', '-')
    while '--' in output:
        slug = output.replace('----', '-')
    return output

print(slugifys(data))

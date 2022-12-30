import requests
from pprint import pprint
urlof_api = 'https://www.themealdb.com/api/json/v1/1/search.php?f=a'
res = requests.get(urlof_api)
my_meals = res.json().get('meals')

one_meal = my_meals[0]
meal_n = one_meal.get('strMeal')
meal_a = one_meal.get('strArea')
meal_i = one_meal.get('strInstructions')
image = one_meal.get('strMealThumb')
yt = one_meal.get('strYoutube')

n = 1

ingred = {}

while n < 21:
    key_ing = f'strIngredient{n}'
    key_mea = f'strMeasure{n}'
    if (one_meal.get(key_ing) != None) and (one_meal.get(key_ing) != ''):
        ingred[one_meal.get(key_ing)] = one_meal.get(key_mea)

    n += 1
ins_li = meal_i.split('\r\n')
print(ins_li)

#check first
#print(res.status_code)
#print(one_meal.get(key_ing))
#print(key_mea)


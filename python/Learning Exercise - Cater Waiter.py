'''
Instructions
You and your business partners operate a small catering company. You've just agreed to run an event for a local cooking club that features "club favorite" dishes. The club is inexperienced in hosting large events, and needs help with organizing, shopping, prepping and serving. You've decided to write some small Python scripts to speed the whole planning process along.

1. Clean up Dish Ingredients
The event recipes were added from various sources and their ingredients appear to have duplicate (or more) entries -- you don't want to end up purchasing excess items! Before the shopping and cooking can commence, each dish's ingredient list needs to be "cleaned".

Implement the clean_ingredients(<dish_name>, <dish_ingredients>) function that takes the name of a dish and a list of ingredients. This function should return a tuple with the name of the dish as the first item, followed by the de-duped set of ingredients.

>> clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro'])

>> ('Punjabi-Style Chole', {'garam masala', 'bay leaves', 'ground turmeric', 'ginger', 'garlic paste', 'peppercorns', 'ginger paste', 'red chili powder', 'cardamom', 'chickpeas', 'cumin powder', 'vegetable oil', 'tomatoes', 'coriander powder', 'onions', 'cilantro', 'cloves'})
2. Cocktails and Mocktails
The event is going to include both cocktails and "mocktails" - mixed drinks without the alcohol. You need to ensure that "mocktail" drinks are truly non-alcoholic and the cocktails do indeed include alcohol.

Implement the check_drinks(<drink_name>, <drink_ingredients>) function that takes the name of a drink and a list of ingredients. The function should return the name of the drink followed by "Mocktail" if the drink has no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol. For the purposes of this exercise, cocktails will only include alcohols from the ALCOHOLS constant in categories.py:

>> from categories import ALCOHOLS 

>> check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'])
...
'Honeydew Cucumber Mocktail'

>> check_drinks('Shirley Tonic', ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda'])
...
'Shirley Tonic Cocktail'
3. Categorize Dishes
The guest list includes diners with different dietary needs, and your staff will need to separate the dishes into Vegan, Vegetarian, Paleo, Keto, and Omnivore.

Implement the categorize_dish(<dish_name>, <dish_ingredients>) function that takes a dish name and a set of that dish's' ingredients. The function should return a string with the dish name: <CATEGORY> (which meal category the dish belongs to). All dishes will "fit" into one of the categories imported from categories.py (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

>> from categories import VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE


>> categorize_dish(('Sticky Lemon Tofu', ['tofu', 'soy sauce', 'salt', 'black pepper', 'cornstarch', 'vegetable oil', 'garlic', 'ginger', 'water', 'vegetable stock', 'lemon juice', 'lemon zest', 'sugar']))
...
'Sticky Lemon Tofu: VEGAN'

>> categorize_dish(('Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamole', ['shrimp', 'bacon', 'avocado', 'chickpeas', 'fresh tortillas', 'sea salt', 'guajillo chile', 'slivered almonds', 'olive oil', 'butter', 'black pepper', 'garlic', 'onion']))
...
'Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamole: OMNIVORE'
4. Label Allergens and Restricted Foods
Some guests have allergies and additional dietary restrictions. These ingredients need to be tagged/annotated for each dish so that they don't cause issues.

Implement the tag_special_ingredients(<dish>) function that takes a tuple with the dish name in the first position, and a list or set of ingredients for that dish in the second position. Return the dish name followed by the set of ingredients that require a special note on the dish description. Dish ingredients inside a list may or may not have duplicates. For the purposes of this exercise, all allergens or special ingredients that need to be labeled are in the SPECIAL_INGREDIENTS constant imported from categories.py.

>> from categories import SPECIAL_INGREDIENTS

>> tag_special_ingredients(('Ginger Glazed Tofu Cutlets', ['tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice']))
...
('Ginger Glazed Tofu Cutlets', {'garlic','soy sauce','tofu'})

>> tag_special_ingredients(('Arugula and Roasted Pork Salad', ['pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pinenuts', 'balsamic vinegar', 'onions', 'black pepper']))
...
('Arugula and Roasted Pork Salad', {'blue cheese', 'pinenuts', 'pork tenderloin'})
5. Compile a "Master List" of Ingredients
In preparation for ordering and shopping, you'll need to compile a "master list" of ingredients for everything on the menu (quantities to be filled in later).

Implement the compile_ingredients(<dishes>) function that takes a list of dishes and returns a set of all ingredients in all listed dishes. Each individual dish is represented by its set of ingredients.

dishes = [ {'tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'},
           {'pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts',
           'balsamic vinegar', 'onions', 'black pepper'},
           {'honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'}]

>> compile_ingredients(dishes)
...
{'arugula', 'brown sugar', 'honeydew', 'coconut water', 'english cucumber', 'balsamic vinegar', 'mint leaves', 'pears', 'pork tenderloin', 'ginger', 'blue cheese', 'soy sauce', 'sesame seeds', 'black pepper', 'garlic', 'lime juice', 'corn starch', 'pine nuts', 'lemon juice', 'onions', 'salt', 'tofu'}
6. Pull out Appetizers for Passing on Trays
The hosts have given you a list of dishes they'd like prepped as "bite-sized" appetizers to be served on trays. You need to pull these from the main list of dishes being prepared as larger servings.

Implement the separate_appetizers(<dishes>, <appetizers>) function that takes a list of dish names and a list of appetizer names. The function should return the list of dish names with appetizer names removed. Either the <dishes> or <appetizers> list could contain duplicates and may require de-duping.

dishes =    ['Avocado Deviled Eggs','Flank Steak with Chimichurri and Asparagus', 'Kingfish Lettuce Cups',
             'Grilled Flank Steak with Caesar Salad','Vegetarian Khoresh Bademjan','Avocado Deviled Eggs',
             'Barley Risotto','Kingfish Lettuce Cups']
          
appetizers = ['Kingfish Lettuce Cups','Avocado Deviled Eggs','Satay Steak Skewers',
              'Dahi Puri with Black Chickpeas','Avocado Deviled Eggs','Asparagus Puffs',
              'Asparagus Puffs']
              
>> separate_appetizers(dishes, appetizers)
...
['Vegetarian Khoresh Bademjan', 'Barley Risotto', 'Flank Steak with Chimichurri and Asparagus', 
 'Grilled Flank Steak with Caesar Salad']
7. Find Ingredients Used in Only One Recipe
Within in each category (Vegan, Vegetarian, Paleo, Keto, Omnivore), you're going to pull out ingredients that appear in only one dish. These "singleton" ingredients will be assigned a special shopper to ensure they're not forgotten in the rush to get everything else done.

Implement the singleton_ingredients(<dishes>, <INTERSECTIONS>) function that takes a list of dishes and a <CATEGORY>_INTERSECTIONS constant for the same category. Each dish is represented by a set of its ingredients. Each <CATEGORY>_INTERSECTIONS is a set of ingredients that appear in more than one dish in the category. Using set operations, your function should return a set of "singleton" ingredients (ingredients appearing in only one dish in the category).

from categories import example_dishes, EXAMPLE_INTERSECTIONS

>> singleton_ingredients(example_dishes, EXAMPLE_INTERSECTION)
...
{'vegetable oil', 'vegetable stock', 'barley malt', 'tofu', 'fresh basil', 'lemon', 'ginger', 'honey', 'spaghetti', 'cornstarch', 'yeast', 'red onion', 'breadcrumbs', 'mixed herbs', 'garlic powder', 'celeriac', 'lemon zest', 'sunflower oil', 'mushrooms', 'silken tofu', 'smoked tofu', 'bell pepper', 'cashews', 'oregano', 'tomatoes', 'parsley', 'red pepper flakes', 'rosemary'}
'''

from exerciselibs.learn_exercise_cater_waiter_sets_categories_data import (VEGAN, VEGETARIAN, KETO, PALEO, OMNIVORE,
                                                                           ALCOHOLS, SPECIAL_INGREDIENTS, EXAMPLE_INTERSECTION, example_dishes)


def clean_ingredients(dish_name, dish_ingredients):
    """
    :param dish_name: str
    :param dish_ingredients: list
    :return: tuple of (dish_name, ingredient set)
    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    return dish_name, set(dish_ingredients)


def check_drinks(drink_name, drink_ingredients):
    """
    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")
    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    """
    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            return "{} Cocktail".format(drink_name)
    return "{} Mocktail".format(drink_name)


def categorize_dish(dish_name, dish_ingredients):
    """
    :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"
    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `categories.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    """
    categories = (
    (VEGAN, "VEGAN"), (VEGETARIAN, "VEGETARIAN"), (PALEO, "PALEO"), (KETO, "KETO"), (OMNIVORE, "OMNIVORE"))
    for category, category_name in categories:
        if set(dish_ingredients).issubset(category):
            return "{}: {}".format(dish_name, category_name)
    return None


def tag_special_ingredients(dish):
    """
    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)
    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `categories.py`.
    """
    return dish[0], {ingredient for ingredient in dish[1] if ingredient in SPECIAL_INGREDIENTS}


def compile_ingredients(dishes):
    """
    :param dishes: list of dish ingredient sets
    :return: set
    This function should return a `set` of all ingredients from all listed dishes.
    """
    union = set()
    for line in dishes:
        union = set.union(union, line)
    return union


def separate_appetizers(dishes, appetizers):
    """
    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names
    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    dishes = set(dishes)
    appetizers = set(appetizers)
    return {ingredient for ingredient in dishes if ingredient not in appetizers}


def singleton_ingredients(dishes, intersection):
    """
    :param intersection: constant - one of (VEGAN_INTERSECTION,VEGETARIAN_INTERSECTION,PALEO_INTERSECTION,
                                            KETO_INTERSECTION,OMNIVORE_INTERSECTION)
    :param dishes:  list of ingredient sets
    :return: set of singleton ingredients
    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    """
    res = set()
    for dish in dishes:
        for ingredient in dish:
            if ingredient not in intersection:
                res.add(ingredient)
    return res


# print(clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro']))
# print(check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber']))
# print(check_drinks('Shirley Tonic', ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda']))
# print(categorize_dish('Sticky Lemon Tofu',
#                       ['tofu', 'soy sauce', 'salt', 'black pepper', 'cornstarch', 'vegetable oil', 'garlic', 'ginger',
#                        'water', 'vegetable stock', 'lemon juice', 'lemon zest', 'sugar']))
# print(categorize_dish('Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamole',
#                       ['shrimp', 'bacon', 'avocado', 'chickpeas', 'fresh tortillas', 'sea salt', 'guajillo chile',
#                        'slivered almonds', 'olive oil', 'butter', 'black pepper', 'garlic', 'onion']))
# print(tag_special_ingredients(('Ginger Glazed Tofu Cutlets', ['tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'])))
# print(tag_special_ingredients(('Arugula and Roasted Pork Salad', ['pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pinenuts', 'balsamic vinegar', 'onions', 'black pepper'])))
# dishes = [{'tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'},
#           {'pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts',
#            'balsamic vinegar', 'onions', 'black pepper'},
#           {'honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'}]
# print(compile_ingredients(dishes))
# dishes = ['Avocado Deviled Eggs', 'Flank Steak with Chimichurri and Asparagus', 'Kingfish Lettuce Cups',
#           'Grilled Flank Steak with Caesar Salad', 'Vegetarian Khoresh Bademjan', 'Avocado Deviled Eggs',
#           'Barley Risotto', 'Kingfish Lettuce Cups']
#
# appetizers = ['Kingfish Lettuce Cups', 'Avocado Deviled Eggs', 'Satay Steak Skewers',
#               'Dahi Puri with Black Chickpeas', 'Avocado Deviled Eggs', 'Asparagus Puffs',
#               'Asparagus Puffs']
#
# print(separate_appetizers(dishes, appetizers))
# print(singleton_ingredients(example_dishes, EXAMPLE_INTERSECTION))
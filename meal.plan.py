# Randomly generates a meal

from random import choice

b_1 = """ Breakfast:\n Oats(1 cup)\n Whole milk (1 1/4 cup)\n 3 Brown eggs
 Greek yogurt\n """
b_2 = """ Breakfast:\n Quaker grits(1/2 cup)\n Shredded cheese(1/2 cup)
 Greek yogurt\n """
b_3 = """ Breakfast:\n Cottage cheese/peanut butter bagel\n Whole milk(1 cup)\n """

l_1 = """ Lunch:\n Peanut butter and carrots\n Granola protein\n Greek yogurt\n """
l_2 = """ Lunch:\n Chipotle bowl\n """
l_3 = """ Lunch:\n Protein shake(banana, milk, honey, olive oil,
 peanut butter, protein powder)\n """

s1_1 = """ Snack 1:\n Cottage cheese salad\n """
s1_2 = """ Snack 1:\n Cottage cheese and celery\n Greek yogurt\n """ 

d_1 = """ Dinner:\n Broccoli, rice, cheese and chicken casserole\n """
d_2 = """ Dinner:\n Chickpeas and noodles\n """
d_3 = """ Dinner:\n Chicken stir-fry\n """
d_4 = """ Dinner:\n Ground turkey with rice/noodles\n """
d_5 = """ Dinner:\n Lunch meal\n """

s2_1 = """ Snack 2:\n Peanuts (1/2 cup)\n Greek yogurt\n Banana\n """
s2_2 = """ Snack 2:\n Peanuts (1/2 cup)\n 2 Greek yogurts\n """  
          
breakfast = [b_1, b_2, b_3]
lunch = [l_1, l_2, l_3]
snack_1 = [s1_1, s1_2]
dinner = [d_1, d_2, d_3, d_4, d_5]
snack_2 = [s2_1, s2_2]

print(choice(breakfast))
print(choice(lunch))
print(choice(snack_1))
print(choice(dinner))
print(choice(snack_2))

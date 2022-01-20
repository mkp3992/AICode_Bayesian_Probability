import pandas as pd
import sys

df = pd.read_csv('/Users/mahipanchal/Desktop/input.txt', header=None, sep="     ", engine='python')
df.index.name = 'Evenings in a year'
df.columns = ['Baseball_game_on_TV', 'George_watches_TV', 'Out_of_cat_food', 'George_feeds_cat']
print(df)


a = 0  # When George_feeds_cat is True, George_watches_TV and Out_of_cat_food is False
b = 0  # When George_feeds_cat is True, George_watches_TV is False and Out_of_cat_food is True
c = 0  # When George_feeds_cat is True, George_watches_TV is True and Out_of_cat_food is False
d = 0  # When George_feeds_cat is True, George_watches_TV and Out_of_cat_food is True
e = 0  # When George_watches_TV is True and Baseball_game_on_TV is False
h = 0  # When George_watches_TV is True and Baseball_game_on_TV is True
g = 0  # When George_watches_TV and Out_of_cat_food is False
p = 0  # When George_watches_TV is False and Out_of_cat_food is True
q = 0  # When George_watches_TV is True and Out_of_cat_food is False
r = 0  # When George_watches_TV and Out_of_cat_food is True
t = 0  # When George_feeds_cat is False, George_watches_TV and Out_of_cat_food is True
x = 0  # When George_watches_TV is False and Baseball_game_on_TV is True
y = 0  # When George_feeds_cat is False, George_watches_TV and Out_of_cat_food is False
z = 0  # When George_feeds_cat is False, George_watches_TV is False and Out_of_cat_food is True
n = 0  # When George_feeds_cat is False, George_watches_TV is True and Out_of_cat_food is False
ab = 0  # When George_watches_TV is False and Baseball_game_on_TV is False

first_column = df.iloc[:, 0]
count_Baseball_game_on_TV_0 = 0
count_Baseball_game_on_TV_1 = 0
for i in first_column:
    if i == 0:
        count_Baseball_game_on_TV_0 += 1
    elif i == 1:
        count_Baseball_game_on_TV_1 += 1
print("No of times if there is no baseball game on TV:", count_Baseball_game_on_TV_0)
print("No of times if there is a baseball game on TV:", count_Baseball_game_on_TV_1)


second_column = df.iloc[:, 1]
count_George_watches_TV_0 = 0
count_George_watches_TV_1 = 0
for i in second_column:
    if i == 0:
        count_George_watches_TV_0 += 1
    elif i == 1:
        count_George_watches_TV_1 += 1
print("No of times if George does not watch TV:", count_George_watches_TV_0)
print("No of times if George watches TV:", count_George_watches_TV_1)


third_column = df.iloc[:, 2]
count_Out_of_cat_food_0 = 0
count_Out_of_cat_food_1 = 0
for i in third_column:
    if i == 0:
        count_Out_of_cat_food_0 += 1
    elif i == 1:
        count_Out_of_cat_food_1 += 1
print("No of times when George ran out of food for cat:", count_Out_of_cat_food_0)
print("No of times when George had food for cat:", count_Out_of_cat_food_1)


fourth_column = df.iloc[:, 3]
count_George_feeds_cat_0 = 0
count_George_feeds_cat_1 = 0
for i in fourth_column:
    if i == 0:
        count_George_feeds_cat_0 += 1
    elif i == 1:
        count_George_feeds_cat_1 += 1
print("No of times when George did not feed cat:", count_George_feeds_cat_0)
print("No of times when George feeds cat:", count_George_feeds_cat_1)

for i, j in zip(first_column, second_column):
    if i == 0 and j == 1:
        e += 1
    if i == 1 and j == 1:
        h += 1
    if i == 1 and j == 0:
        x += 1
    if i == 0 and j == 0:
        ab += 1
for i, j, k in zip(second_column, third_column, fourth_column):
    if i == 0 and j == 0 and k == 1:
        a += 1
    if i == 0 and j == 1 and k == 1:
        b += 1
    if i == 1 and j == 0 and k == 1:
        c += 1
    if i == 1 and j == 1 and k == 1:
        d += 1
    if i == 1 and j == 1 and k == 0:
        t += 1
    if i == 0 and j == 0 and k == 0:
        y += 1
    if i == 0 and j == 1 and k == 0:
        z += 1
    if i == 1 and j == 0 and k == 0:
        n += 1
    if i == 0 and j == 0:
        g += 1
    if i == 0 and j == 1:
        p += 1
    if i == 1 and j == 0:
        q += 1
    if i == 1 and j == 1:
        r += 1


print("When George_feeds_cat is True, George_watches_TV and Out_of_cat_food is False:", a)
print("When George_feeds_cat is True, George_watches_TV is False and Out_of_cat_food is True:", b)
print("When George_feeds_cat is True, George_watches_TV is True and Out_of_cat_food is False:", c)
print("When George_feeds_cat is True, George_watches_TV and Out_of_cat_food is True:", d)
print("When George_feeds_cat is False, George_watches_TV and Out_of_cat_food is False:", y)
print("When George_feeds_cat is False, George_watches_TV is False and Out_of_cat_food is True:", z)
print("When George_feeds_cat is False, George_watches_TV is True and Out_of_cat_food is False:", n)
print("When George_feeds_cat is False, George_watches_TV and Out_of_cat_food is True:", t)
print("When George_watches_TV is True and Baseball_game_on_TV is False:", e)
print("When George_watches_TV is True and Baseball_game_on_TV is True:", h)
print("When George_watches_TV is False and Baseball_game_on_TV is True:", x)
print("When George_watches_TV is False and Baseball_game_on_TV is False:", ab)
print("When George_watches_TV and Out_of_cat_food is False:", g)
print("When George_watches_TV is False and Out_of_cat_food is True:", p)
print("When George_watches_TV is True and Out_of_cat_food is False:", q)
print("When George_watches_TV and Out_of_cat_food is True:", r)


f = open("output.txt", "a")
sys.stdout = f
print(df)
print("No of times if there is no baseball game on TV:", count_Baseball_game_on_TV_0)
print("No of times if there is a baseball game on TV:", count_Baseball_game_on_TV_1)

print("No of times if George does not watch TV:", count_George_watches_TV_0)
print("No of times if George watches TV:", count_George_watches_TV_1)

print("No of times when George ran out of food for cat:", count_Out_of_cat_food_0)
print("No of times when George had food for cat:", count_Out_of_cat_food_1)

print("No of times when George did not feed cat:", count_George_feeds_cat_0)
print("No of times when George feeds cat:", count_George_feeds_cat_1)


print("When George_feeds_cat is True, George_watches_TV and Out_of_cat_food is False:", a)
print("When George_feeds_cat is True, George_watches_TV is False and Out_of_cat_food is True:", b)
print("When George_feeds_cat is True, George_watches_TV is True and Out_of_cat_food is False:", c)
print("When George_feeds_cat is True, George_watches_TV and Out_of_cat_food is True:", d)
print("When George_feeds_cat is False, George_watches_TV and Out_of_cat_food is False:", y)
print("When George_feeds_cat is False, George_watches_TV is False and Out_of_cat_food is True:", z)
print("When George_feeds_cat is False, George_watches_TV is True and Out_of_cat_food is False:", n)
print("When George_feeds_cat is False, George_watches_TV and Out_of_cat_food is True:", t)
print("When George_watches_TV is True and Baseball_game_on_TV is False:", e)
print("When George_watches_TV is True and Baseball_game_on_TV is True:", h)
print("When George_watches_TV is False and Baseball_game_on_TV is True:", x)
print("When George_watches_TV is False and Baseball_game_on_TV is False:", ab)
print("When George_watches_TV and Out_of_cat_food is False:", g)
print("When George_watches_TV is False and Out_of_cat_food is True:", p)
print("When George_watches_TV is True and Out_of_cat_food is False:", q)
print("When George_watches_TV and Out_of_cat_food is True:", r)

f.close()
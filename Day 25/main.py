
import pandas as pd

file = pd.read_csv("squirel.csv")
squirrel_df = pd.DataFrame(file)
squirrel_df.dropna()
print(squirrel_df)
fur_color = squirrel_df["Primary Fur Color"]
fur_color.to_dict()
fur = list(set(fur_color))


print(fur)

number_cinnamon = len(squirrel_df[squirrel_df["Primary Fur Color"] == fur[1]])
number_gray = len(squirrel_df[squirrel_df["Primary Fur Color"] == fur[2]])
number_black = len(squirrel_df[squirrel_df["Primary Fur Color"] == fur[3]])

print(number_cinnamon)
print(number_gray)
print(number_black)
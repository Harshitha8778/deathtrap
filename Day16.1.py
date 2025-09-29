# %% [markdown]
# An object consists of - ATTRIBUTES and METHODS

# %% [markdown]
# CLASS provides the blueprint, using which multiple objects can be created. Classes are in pascal case ie the first letter of every word is capital

# %%
import turtle
from turtle import Screen
timmy = turtle.Turtle()
timmy.shape('turtle')
timmy.color('coral')
timmy.forward(100)
timmy.circle(radius=50)
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


# %%
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes
from prettytable import TableStyle
table = ColorTable(theme=Themes.LAVENDER)
table.set_style(TableStyle.DOUBLE_BORDER)
table.add_column("Fire",["Fennekin","Charmander","Charizard","Tauros"])
table.add_column("Electric",["Pikachu","Raichu","Pichu","Rotom"])
table.add_column("Water",["Psyduck","Sharpedo","Swanna","Wailord"])
table.add_column("Fairy",["Swirlix","Slurpuff","Spritzee","Sylveon"])
print(table)

# %%




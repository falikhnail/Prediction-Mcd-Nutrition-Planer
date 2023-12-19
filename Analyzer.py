
"""
@author: Vigneswaran Madappan Chinnasami
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('The Healthy Eating Tool')
st.text('''This program is a Streamlit web application designed to help users plan a 
nutritionally balanced meal at McDonald's. It takes user input for various 
nutrition constraints, filters McDonald's menu items based on these constraints,
and recommends a set of menu items that best match the user's preferences.
The recommendations are then visualized through a table and a bar plot showing 
the nutrition information of the recommended items.
        ''')

# Load the McDonald's menu data
menu_data = pd.read_csv('Menu.csv')

# Convert column names to lowercase
menu_data.columns = menu_data.columns.str.lower()

# Streamlit app
st.title("McDonald's Nutrition Planner")

# User input for nutrition constraints
st.sidebar.header("Nutrition Constraints")
max_total_fat = st.sidebar.slider("Maximum Total Fat (g)", 0, 100, 50)
max_saturated_fat = st.sidebar.slider("Maximum Saturated Fat (g)", 0, 30, 15)
max_sugar = st.sidebar.slider("Maximum Sugar (g)", 0, 100, 50)
min_sugar = st.sidebar.slider("Minimum Sugar (g)", 0, 50, 0)
min_carbohydrates = st.sidebar.slider("Minimum Carbohydrates (g)", 0, 200, 0)
max_carbohydrates = st.sidebar.slider("Maximum Carbohydrates (g)", 0, 200, 100)
min_protein = st.sidebar.slider("Minimum Protein (g)", 0, 50, 0)
max_protein = st.sidebar.slider("Maximum Protein (g)", 0, 50, 25)

# Adjust column names based on the actual column names in your CSV file
filtered_menu = menu_data[
    (menu_data['total fat'] <= max_total_fat) &
    (menu_data['saturated fat'] <= max_saturated_fat) &
    (menu_data['sugars'] <= max_sugar) &
    (menu_data['sugars'] >= min_sugar) &
    (menu_data['carbohydrates'] >= min_carbohydrates) &
    (menu_data['carbohydrates'] <= max_carbohydrates) &
    (menu_data['protein'] >= min_protein) &
    (menu_data['protein'] <= max_protein)
]

# Calculate similarity to user input and sort by the most similar
similarity_scores = (
    (filtered_menu['total fat'] - max_total_fat) ** 2 +
    (filtered_menu['saturated fat'] - max_saturated_fat) ** 2 +
    (filtered_menu['sugars'] - max_sugar) ** 2 +
    (filtered_menu['sugars'] - min_sugar) ** 2 +
    (filtered_menu['carbohydrates'] - min_carbohydrates) ** 2 +
    (filtered_menu['carbohydrates'] - max_carbohydrates) ** 2 +
    (filtered_menu['protein'] - min_protein) ** 2 +
    (filtered_menu['protein'] - max_protein) ** 2
)

filtered_menu['similarity'] = similarity_scores
filtered_menu = filtered_menu.sort_values(by='similarity')

# Add a column for quantity
# Assuming 'quantity' is the column that represents the quantity of each food item
filtered_menu['quantity'] = 1  # You may adjust this based on your actual data

# Display the most similar items
st.subheader("Recommended Menu:")
st.table(filtered_menu.head()[['item', 'category', 'total fat', 'saturated fat', 'sugars', 'carbohydrates', 'protein', 'calories']])

# Plot nutrition information for the most similar items with a specified color palette
fig, ax = plt.subplots(figsize=(10, 6))

# Use seaborn for a cleaner and more modern look with a specified color palette
colors = sns.color_palette("husl", n_colors=5)
sns.barplot(data=filtered_menu.head(), y='item', x='total fat', label='Total Fat', color=colors[0], alpha=0.7)
sns.barplot(data=filtered_menu.head(), y='item', x='saturated fat', label='Saturated Fat', color=colors[1], alpha=0.7)
sns.barplot(data=filtered_menu.head(), y='item', x='sugars', label='Sugar', color=colors[2], alpha=0.7)
sns.barplot(data=filtered_menu.head(), y='item', x='carbohydrates', label='Carbohydrates', color=colors[3], alpha=0.7)
sns.barplot(data=filtered_menu.head(), y='item', x='protein', label='Protein', color=colors[4], alpha=0.7)

ax.set_xlabel('Nutrition (g)')
ax.set_ylabel('Menu Item')
ax.set_title('Nutrition Information for Recommended Menu')
ax.legend()

# Display total calories for the most similar items
total_calories = filtered_menu.head()['calories'].sum()
st.subheader(f"Total Calories for Recommended Menu: {total_calories} kcal")
st.pyplot(fig)


st.subheader('Created by Vigneswaran Madappan Chinnasami')
st.text('Data analyst portfolio project')
st.caption('Inspiration from [Kyle Pastor](https://towardsdatascience.com/making-mcdonalds-healthy-197f537f931d)'' and [Avery Smith](https://www.youtube.com/watch?v=3bbFc1225-4&list=PLo0oTKi2fPNiMBo2hXreEetXCXev170ZZ&index=29)')


import streamlit
import pandas


streamlit.title('my parents new healthy diner')

streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗 omega 3 & Blueberry oatmeal')
streamlit.text('🥑kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled free-Range egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected =streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

import requests
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "Kiwi")

# Converting json
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output in the form of table
streamlit.dataframe(fruityvice_normalized)

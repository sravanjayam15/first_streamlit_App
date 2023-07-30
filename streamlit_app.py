import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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


streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Converting json
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output in the form of table
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_row)
fruit_choice = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)

my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('from streamlit')")

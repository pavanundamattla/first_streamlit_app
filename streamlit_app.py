import streamlit
streamlit.title ("My Mother`s New Healthy Diner")


streamlit.header('Breakfast Favorites')
streamlit.text(" π₯£ omega 3 & blueberry oatmeal")
streamlit.text(" π₯kale,spinach")
streamlit.text(" πHard boiled Free-range Egg")
streamlit.text("π₯π Avocado Toast")


streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')
 
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.


streamlit.dataframe(fruits_to_show)

import streamlit
streamlit.title ("My Mother`s New Healthy Diner")


streamlit.header('Breakfast Favorites')
streamlit.text(" 🥣 omega 3 & blueberry oatmeal")
streamlit.text(" 🥗kale,spinach")
streamlit.text(" 🐔Hard boiled Free-range Egg")
streamlit.text("🥑🍞 Avocado Toast")


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
 
 import pandas
 my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt ")
 streamlit.DataFrame( my_fruit_list)

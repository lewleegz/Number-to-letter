import streamlit as st
import inflect
p = inflect.engine()
number = st.text_input("Input your number:", "1234")
number_in_letters = p.number_to_words(number)
st.write(f"The number is {number_in_letters} in letters")
st.write("Thanks for the idea Isidor!")
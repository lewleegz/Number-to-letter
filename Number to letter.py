import streamlit as st
import inflect
letter_exists = False
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
p = inflect.engine()
number = st.text_input("Input your number:", "1234")
number_in_letters = number
if number == "":
  number_in_letters = "nothing"
for c in letters:
  if c in number:
    letter_exists = True
if not letter_exists:
  try:
    number_in_letters = p.number_to_words(number)
  except Exception:
    pass
st.write(f"The number is {number_in_letters} in letters")
st.write("Thanks for the idea Isidor!")

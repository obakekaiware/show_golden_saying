import os
import random
import json
import streamlit as st


if __name__ == "__main__":
    st.title("名言が欲しいか？")

    input_path = os.path.join("data", "golden_saying_list.json")
    with open(input_path, encoding="utf8") as file:
        golden_saying_list = json.load(file)

    if st.button('欲しい！'):
        golden_saying = random.choice(golden_saying_list)
        golden_saying = golden_saying.split("\n")
        for text in golden_saying:
            st.write(text)
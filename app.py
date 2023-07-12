import streamlit as st
import pandas as pd
import pickle
from PIL import Image


anime_data = pd.DataFrame(pickle.load(open('anime_list.pkl','rb')))
similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(anime_name):
    anime_index = anime_data[anime_data['title']== anime_name].index[0]
    distance = similarity[anime_index]
    anime_list = sorted(list(enumerate(distance)),reverse = True,key = lambda x:x[1])[1:11]
    recommended_anime_name = []
    recommended_anime_poster =[]
    recommended_anime_link = []
    for i in anime_list:
        recommended_anime_name.append(anime_data.iloc[i[0]][0])
        recommended_anime_poster.append(anime_data.iloc[i[0]][3])
        recommended_anime_link.append(anime_data.iloc[i[0]][4])
    return recommended_anime_name,recommended_anime_poster,recommended_anime_link
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.hdqwalls.com/download/girl-with-sword-red-eyes-background-anime-original-qs-1920x1080.jpg');
        background-repeat: no-repeat;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Anime Recommendation')
selected_anime_name = st.selectbox(
    'Choose Anime Name',
    (anime_data['title'].values))

if st.button('Recommend'):
    name,poster,link = recommend(selected_anime_name)

    for i in range(len(name)):
        data = (f'{name[i]}')
        caption = f"<h2>{data}</h2>"
        st.markdown(caption , unsafe_allow_html=True)
        st.markdown(f'<a href="{link[i]}" target="_blank">Click Here To Explore More</a>', unsafe_allow_html=True)
        st.image(poster[i])
       
  


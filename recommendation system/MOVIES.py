import pandas as pd
import streamlit as st
import pickle
import requests

# read_url=pd.read_csv("C:/Users/himan/Desktop/python/DATASET/movies.csv")
# url=read_url['homepage']
# print(url[1])

# function for fetching poster
def fetch(movie_id):
    r= requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data= r.json()
    # st.text(data)
    return "https://image.tmdb.org/t/p/w500/" +data['poster_path']

#  function for recommendation
def recommend(movie):
    movies_index=movies[movies['title']==movie].index[0]
    distance=similarity[movies_index]
    movies_list= sorted(list(enumerate(distance)),reverse=True,key=lambda  x: x[1])[1:6]

    recom_movie=[]
    recom_poster=[]
    recom_dire=[]
    # recom_link=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        # recom_link.append(movies.iloc[i[0].homepage])
        recom_movie.append(movies.iloc[i[0]].title)
        recom_dire.append(movies.iloc[i[0]].tags)
        recom_poster.append(fetch(movie_id))
    return recom_movie,recom_poster,recom_dire

movies_dict=pickle.load(open('movie_list.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
print(movies_dict.columns)
st.markdown('''WeLcOmE :car::balloon: TO our''')
st.title('MOVIE RECOMMENDER SYSTEM')

option=st.selectbox('THIS PROJECT BELONGS TO HIMANSHUS WELCOME ALL',movies['title'].values)

# recommend=
if st.button('Recommend'):
    name,poster,g=recommend(option)

    a,b,c,d,e = st.columns(5)
    with a:
        st.text(name[0])
        st.image(poster[0])
        st.text_area(label='description',value=g[0],max_chars=30)
        link='https://www.youtube.com/results?search_query='+name[0]
        st.link_button("trailer",link)
        st.text("")
        link2 = 'https://www.imdb.com/find/?q=' + name[0]
        st.link_button("imdb", link2)

    with b:
       st.text(name[1])
       st.image(poster[1])
       st.text_area(label='description', value=g[1], max_chars=30,key=6)
       link = 'https://www.youtube.com/results?search_query=' + name[1]
       st.link_button("trailer",link)
       st.text("")
       link2 = 'https://www.imdb.com/find/?q=' + name[1]
       st.link_button("imdb", link2)

    with c:
       st.text(name[2])
       st.image(poster[2])
       st.text_area(label='description', value=g[2], max_chars=30,key=5)
       link = 'https://www.youtube.com/results?search_query=' + name[2]
       st.link_button("trailer", link)
       st.text("")
       link2 = 'https://www.imdb.com/find/?q=' + name[2]
       st.link_button("imdb", link2)
    with d:
       st.text(name[3])
       st.image(poster[3])
       st.text_area(label='description', value=g[3], max_chars=30,key=4)
       link = 'https://www.youtube.com/results?search_query=' + name[3]
       st.link_button("trailer", link)
       st.text("")
       link2 = 'https://www.imdb.com/find/?q=' + name[3]
       st.link_button("imdb", link2)
    with e:
       st.text(name[4])
       st.image(poster[4])
       st.text_area(label='description', value=g[4], max_chars=30,key=3)
       link = 'https://www.youtube.com/results?search_query=' + name[4]
       st.link_button("trailer", link)
       st.text("")
       link2 = 'https://www.imdb.com/find/?q=' + name[4]
       st.link_button("imdb", link2)



# st.link_button('open',link)






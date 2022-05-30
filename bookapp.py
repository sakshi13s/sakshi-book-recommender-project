import streamlit as st
import pickle
import numpy as np


def set_bg_hack_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://img.freepik.com/free-photo/stack-books-black-background_23-2147846050.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

set_bg_hack_url()


st.markdown("<h1 style='text-align: center; color: white;'>Wish Book : A Book Recommender</h1>", unsafe_allow_html=True)
popular_df = pickle.load(open('popularbooks.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarityscores.pkl', 'rb'))


def recommend_book(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:7]
    book_recs = []
    book_post = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        book_recs.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        book_post.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
    return book_recs, book_post


book_list = list(pt.index.values)
selected_book = st.selectbox("Type or Select a Book from the Dropdown", book_list)


if st.button('Show Recommendation'):
    st.markdown("<h1 style='text-align: center; color: white;'>Recommended Books</h1>", unsafe_allow_html=True)
    recommended_book_names, recommended_book_posters = recommend_book(selected_book)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(recommended_book_posters[0])
        st.markdown("<h6 style='text-align: left; color: white;'>{}</h6>".format(recommended_book_names[0]), unsafe_allow_html=True)
        st.image(recommended_book_posters[1])
        st.markdown("<h6 style='text-align: left; color: white;'>{}</h6>".format(recommended_book_names[1]),unsafe_allow_html=True)

    with col2:
        st.image(recommended_book_posters[2])
        st.markdown("<h6 style='text-align: left; color: white;'>{}</h6>".format(recommended_book_names[2]),unsafe_allow_html=True)
        st.image(recommended_book_posters[3])
        st.markdown("<h6 style='text-align: left; color: white;'>{}</h6>".format(recommended_book_names[3]),unsafe_allow_html=True)
    with col3:
        st.image(recommended_book_posters[4])
        st.markdown("<h6 style='text-align: left; color: white;'>{}</h6>".format(recommended_book_names[4]),unsafe_allow_html=True)
        st.image(recommended_book_posters[5])
        st.markdown("<h6 style='text-align: left; color: white;'>{}</h6>".format(recommended_book_names[5]),unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: white;'>Best Sellers</h1>", unsafe_allow_html=True)
p1, p2, p3 = st.columns(3)
with p1:
    for i in range(0, 21, 3):
        pb1 = popular_df.iloc[i]
        st.image(pb1['Image-URL-M'])
        cur1 = pb1['Book-Title']
        st.markdown("<p style='text-align: left; color: white;'>{}</p>".format(cur1),unsafe_allow_html=True)
        cur2 = pb1['Book-Author']
        st.markdown("<p style='text-align: left; color: white;'>{}</p>".format(cur2), unsafe_allow_html=True)
        cur3 = "Number of ratings : " + str(pb1['num_of_ratings'])
        cur4 = "Average rating : " + str(np.round(pb1['avg_ratings'],2))
        st.markdown("<p style='text-align: left; color: white;'>{}</p>".format(cur3), unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; color: white;'>{}</p>".format(cur4), unsafe_allow_html=True)

with p2:
    for i in range(1, 21, 3):
        pb1 = popular_df.iloc[i]
        st.image(pb1['Image-URL-M'])
        cur1 = pb1['Book-Title']
        st.markdown("<p style='text-align: left; color: white;'>{}</p>".format(cur1), unsafe_allow_html=True)
        cur2 = pb1['Book-Author']
        st.markdown("<p style='text-align: left; color: white;'>{}</p>".format(cur2), unsafe_allow_html=True)
        cur3 = "Number of ratings : " + str(pb1['num_of_ratings'])
        cur4 = "Average rating : " + str(np.round(pb1['avg_ratings'], 2))
        st.markdown("<p style='text-align: left; color: white;'>{}</p>".format(cur3), unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; color: white;'>{}</p>".format(cur4), unsafe_allow_html=True)
with p3:
    for i in range(2, 21, 3):
        pb1 = popular_df.iloc[i]
        st.image(pb1['Image-URL-M'])
        cur1 = pb1['Book-Title']
        st.markdown("<p style='text-align: left; color: white;'>{}</p>".format(cur1), unsafe_allow_html=True)
        cur2 = pb1['Book-Author']
        st.markdown("<p style='text-align: left; color: white;'>{}</p>".format(cur2), unsafe_allow_html=True)
        cur3 = "Number of ratings : " + str(pb1['num_of_ratings'])
        cur4 = "Average rating : " + str(np.round(pb1['avg_ratings'], 2))
        st.markdown("<p style='text-align: left; color: white;'>{}</p>".format(cur3), unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; color: white;'>{}</p>".format(cur4), unsafe_allow_html=True)


st.image("https://upjourney.com/wp-content/uploads/2020/04/how-to-respond-to-thank-you.jpg")





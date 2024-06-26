import streamlit as st
import pandas
import itertools


def display_next_app(app_data) -> None:
    """
    Display app data, alternating between streamlit col1 and col2.
    This function uses `col_iterator` to alternate between columns.

    :param app_data: dict consisting of 4 string keys (title, description, url, image) all with string values
    :return: None
    """
    title, desc, url, img = app_data  # unpack the dict entry
    with next(col_iterator):
        st.header(title)
        st.subheader(desc)
        img_file = 'images/' + img
        st.image(img_file)
        st.write(f"[Source Code]({url})")  # [url label](url)
    return


st.set_page_config(layout="wide")

st.title("Steven Shatz")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpeg', use_column_width=True)

with col2:
    # Define alignment style: left and right-justify text
    content_alignment = '''
        <style>
            p {
                text-align: justify;
            }
        </style>
        '''

    st.markdown(content_alignment, unsafe_allow_html=True)

    content1a = """Hi! I am Steven and I have had a long and varied career where I've worked for large corporations
    as an MVS Systems programmer, a mid-size company writing word processing programs in Assembler language, I've
    been a partner in a small business with banking and insurance clients, and for the past 30+ years I've run my
    own company developing and supporting software for the wholesale insurance industry."""

    content1b = """I work closely with my customers to deliver the features and solutions they need. This includes
    helping them determine their requirements and designing the end-product. After implementation, I train my clients
    and continue to offer them 24/7 problem support. On an ongoing basis, I enhance applications to meet the
    challenges of ever-changing situations and circumstances."""

    st.info(content1a)
    st.info(content1b)

    # I have designed and implemented applications which handle accounting, track submissions, generate quotes and
    # binders, issue policies, support endorsements and cancellations, manage claims, and produce vital reports and
    # spreadsheets for all departments while remaining current with state regulations, forms, fees, and taxes. I have
    # integrated my applications with third party document management, finance agreement, web-based quoting, and CRM
    # systems.
    #
    # Throughout my career I have always been drawn to understanding the details of how things work. Learning new
    # technologies and skills has been a primary interest and joy for me. When faced with problems and new situations,
    # I thoroughly research possibilities to find viable solutions. I then develop a strategy to implement those
    # solutions.
    #
    # On my own, I have studied mobile app development (Objective-C, Swift), website creation, machine learning, and
    # various programming languages including Python, Ruby, C++, Go, Smalltalk, and Perl.

content2 = ":violet[Below you can find some of the apps I have built in Python. Feel free to contact me!]"
st.write(" ")
st.subheader(content2)

col3, _, col4 = st.columns([1.5, 0.5, 1.5])  # leave space (i.3., an empty column) between col3 and col4

cols = [col3, col4]
col_iterator = itertools.cycle(cols)  # for function display_next_app()


csvfile = 'data.csv'
reader = pandas.read_csv(csvfile, sep=';')
for index, row in reader.iterrows():
    display_next_app(row)

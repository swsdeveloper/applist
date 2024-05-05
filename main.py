import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpeg', width=490)

with col2:
    st.title("Steven Shatz")

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

content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write('\n' + content2)

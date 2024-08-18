import os
from apikey import apikey 
import streamlit as st
import pandas as pd
from langchain.llms.openai import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())  


if 'OPENAI_API_KEY' not in os.environ:
    os.environ['OPENAI_API_KEY'] = apikey 
    


llm = OpenAI(temperature=0, max_tokens=500)  


st.title('AI Assistant for Data Science 🤖')
st.write("Hello 👋🏻 I am your AI Assistant, and I am here to help you with your data science problems.")

st.subheader("General information about the dataset")

st.caption('<p style="text-align:center">made with ❤️ by Team Icy </p>', unsafe_allow_html=True)
with st.sidebar:
    st.write("*Your Data Science Adventure Begins with a CSV Upload*")
    st.caption('''You may already know that every exciting data science journey starts with a dataset. 
               That's why I'd love for you to upload a CSV file. Once we have your data in hand, 
               we'll dive into understanding it and have some fun exploring it. Then,
               we'll work together to shape your business challenge 
               into a data science framework. I'll introduce you 
               to the coolest machine learning models, and we'll use
               them to tackle your problem. Sounds fun right?''')
    with st.expander('Done by team'):
        st.write('Suraj')
        st.write('Sumanth')
        st.write('Shesha')

st.divider()

if 'clicked' not in st.session_state:
    st.session_state.clicked = {1: False}

def clicked(button):
    st.session_state.clicked[button] = True

if st.button("Let's get started", on_click=clicked, args=[1]):
    pass

if st.session_state.clicked[1]:
    st.header("Exploratory Data Analysis Part")
    st.subheader('Solutions')

    user_csv = st.file_uploader("Upload your file here!", type="csv")

    if user_csv is not None:
        user_csv.seek(0)
        df = pd.read_csv(user_csv, low_memory=False)

        pandas_agent = create_pandas_dataframe_agent(
            llm, 
            df, 
            verbose=True, 
            allow_dangerous_code=True
        )

        @st.cache_data
        def get_columns_meaning():
            return pandas_agent.run("What are the meanings of the columns?")
        
        columns_meaning = get_columns_meaning()
        st.write(columns_meaning)

        @st.cache_data
        def function_agent():
            st.write("**Data Overview**")
            st.write("The first rows of your dataset look like this:")
            st.write(df.head())
            st.write("**Data Cleaning**")
            columns_df = pandas_agent.run("Provide a brief summary of the columns.")
            st.write(columns_df)
            missing_values = pandas_agent.run("How many missing values does this dataframe have? Start the answer with 'There are'")
            st.write(missing_values)
            duplicates = pandas_agent.run("Are there any duplicate values and if so where?")
            st.write(duplicates)
            st.write("**Data Summarisation**")
            st.write(df.describe())
            correlation_analysis = pandas_agent.run("Calculate correlations between numerical variables.")
            st.write(correlation_analysis)
            outliers = pandas_agent.run("Identify potential outliers in the data.")
            st.write(outliers)
            new_features = pandas_agent.run("Suggest new features that could be created.")
            st.write(new_features)
        
        st.header('Exploratory Data Analysis')
        st.subheader('General information about the dataset')
        function_agent()

@st.cache_data
def your_function():
    return

user_question_variable = st.text_input("What variable are you interested in?")

@st.cache_data
def get_variable_analysis(variable_name):
    return {
        "summary_statistics": pandas_agent.run(f"Provide summary statistics for {variable_name}."),
        "normality": pandas_agent.run(f"Check for normality of {variable_name}."),
        "outliers": pandas_agent.run(f"Assess outliers for {variable_name}."),
        "trends": pandas_agent.run(f"Analyze trends for {variable_name}."),
        "missing_values": pandas_agent.run(f"Determine missing values for {variable_name}.")
    }

def function_question_variable():
    st.line_chart(df, y=[user_question_variable])
    variable_analysis = get_variable_analysis(user_question_variable)
    st.write(variable_analysis["summary_statistics"])
    st.write(variable_analysis["normality"])
    st.write(variable_analysis["outliers"])
    st.write(variable_analysis["trends"])
    st.write(variable_analysis["missing_values"])

if user_question_variable:
    function_question_variable()

user_question_dataframe = st.text_input("Is there anything else you would like to know about your dataframe?")

@st.cache_data
def get_dataframe_info(question):
    return pandas_agent.run(question)

def function_question_dataframe():
    dataframe_info = get_dataframe_info(user_question_dataframe)
    st.write(dataframe_info)

if user_question_dataframe and user_question_dataframe.lower() not in ("no", "no"):
    function_question_dataframe()
elif user_question_dataframe.lower() in ("no", "no"):
    st.write("")

@st.cache_data
def steps_eda():
    return llm('What are the steps of EDA?')

steps_eda_text = steps_eda()
st.sidebar.write("**Steps of EDA:**")
st.sidebar.write(steps_eda_text)

@st.cache_data
def function_question_variable():
    st.line_chart(df, y =[user_question_variable])
    summary_statistics = pandas_agent.run(f"Give me a summary of{user_question_dataframe}")
    st.write(summary_statistics )
    normality = pandas_agent.run(f"Check for normality of {user_question_variable}."),
    st.write(normality)
    outliers = pandas_agent.run(f"Assess outliers for {user_question_variable}."),
    st.write(outliers)
    trends = pandas_agent.run(f"Analyze trends for {user_question_variable}."),
    st.write(trends)
    missing_values= pandas_agent.run(f"Determine missing values for {user_question_variable}.")
    st.write(missing_values)
    return

    if user_question_variable is not None and  user_question_variable !="":
     function_question_variable()
     
     st.subheader('Further study')
     
  

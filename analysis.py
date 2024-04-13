# Import packages
import os
import pandas as pd
import matplotlib
matplotlib.use('TkAgg',force=True)
from  matplotlib import pyplot as plt
import seaborn as sns
from getpass import getpass
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.llms import AzureOpenAI

# %matplotlib inline

# read the data from your file path
data = pd.read_csv("xxx.csv")

# Prepare the LLM
llm = AzureOpenAI(
    openai_api_base="xxx",
    openai_api_version="xxx",
    deployment_name="xxx",
    openai_api_key="xxx",
    openai_api_type="xxx",
)

# Set up the LLM agent
agent = create_pandas_dataframe_agent(llm, data, verbose = True)

# Ask the agent questions (e.g., data distribution, data cleaning, or data visualization)
results = agent ("Check the distribution % for simpified titles, then name the table as 'title', then save it to CSV file")

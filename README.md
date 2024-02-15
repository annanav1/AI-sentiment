# AI-Sentiment Analysis Project
## Overview
This project aims to analyze the sentiment of news article headlines related to Artificial Intelligence (AI). The project involves two main components: web scraping using the News API and sentiment analysis using Python.


## Introduction
In this project, we utilize the News API to scrape news article headlines related to 27  Artificial Intelligence topics from specific website domains. We then perform sentiment analysis on these headlines to determine their emotional tone, using two different models: VADER and RoBERTa.

## Dependencies
To run the code for this project, the following dependencies are required:
Python 3.x
News API Python library
nltk library
transformers library (for RoBERTa model)
matplotlib library
seaborn library
wordcloud library

## Usage
Scraping News Articles: Run the newsAPI-get-articles.py script to fetch news article headlines related to AI using the News API. Make sure to provide your News API key in the config.json file.

Sentiment Analysis: Open and run the AI_news_sentiment.ipynb Jupyter Notebook. This notebook contains the code to analyze the sentiment of the scraped news article headlines using VADER and RoBERTa models.

## Project Structure
The project directory contains the following files and directories:

newsAPI-get-articles.py: Python script to scrape news articles using the News API.
AI_news_sentiment.ipynb: Jupyter Notebook for sentiment analysis of the scraped news article headlines.
config.json: Configuration file containing the News API key. (not provided)
README.md: This file providing an overview of the project.


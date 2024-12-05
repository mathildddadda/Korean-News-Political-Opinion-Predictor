# Korean-News-Political-Opinion-Predictor

## Introduction

Hello! AI팬분들, 환영합니다! This is my first *big* project. This project was created to explore and enhance my coding skills in Python. I've been self-learning Python and with the aid of AI tools, I've gained a better understanding of how Machine Learning models operate. Motivated by my undergraduate studies, I aimed to apply this knowledge practically. The core of this project involves analyzing Korean news articles to classify them based on their political orientation and level of pro-government sentiment.

The objective was to train a model, specifically a RoBERTa model, to predict the political orientation of a news article. Additionally, I performed data analysis to gain insights into the dataset.

I used the **KoPolitics-Benchmark** dataset available [here](https://github.com/Kdavid2355/KoPolitic-Benchmark-Dataset/tree/main) and fine-tuned a RoBERTa model from Hugging Face 🤗, which can be found [here](https://huggingface.co/klue/roberta-base).

## Results

The Korean News Political Opinion Predictor achieved promising results in classifying political orientation of Korean news articles. Here are some highlights from the data analysis:

- **Political Orientation Analysis:**
  - The model was able to categorize news articles into five distinct political orientations: Conservative, Moderate Conservative, Moderate, Moderate Liberal, and Liberal.
  - The distribution of political orientations in our train set showed a significant number of articles classified as Moderate (42.91%) and Moderate Liberal (27.84%), indicating a prevalence of centrist views in the news I used to fine-tune our model.
  
![IMG_0071](https://github.com/user-attachments/assets/c98d3ebf-044b-422c-a38a-59453af5de85)

- **Government Sentiment Analysis:**
  - The level of pro-government sentiment was also analyzed, ranging from 'None' to 'Strong Advocacy'.
  - The majority of articles exhibited 'None' (40.71%), indicating a neutral stance towards the government, followed by moderate criticism (19.78%).

 ![IMG_3381](https://github.com/user-attachments/assets/6e280aca-305b-44c8-8072-60704e27240e)

- **Political Orientation and Level of Pro-Government Sentiment Analysis**
  - I also aimed to explore potential correlations between the level of pro-government sentiment and the political orientation of news articles. To achieve this, I plotted a graph that not only shows the distribution of pro-government sentiment but also overlays the political orientation for each sentiment category.
  - The findings from this graph are quite revealing: articles that criticize the government tend to predominantly exhibit `Liberal` orientations, while those expressing support are more often `Moderate Conservative` or `Conservative`. This trend is clearly visualized in the graph, with `liberal criticism` marked by more extensive use of blue tones and `conservative support` highlighted in red.

![IMG_7038](https://github.com/user-attachments/assets/a04b568a-af64-4bb0-8103-aae4d207286d)

- **Training results:**
  - The RoBERTa model was fine-tuned on the articles with the task of predicting their political orientation (it does not predict the level of pro-government sentiment).
  - The final accuracy obtained on our test set is 48.0% which means that our model correctly classifies the political opinion of an article about 50% of the time. I realize that this could be improved by using bigger and more performant models, for which I don't have the computational power to use. However, considering there are 5 possible levels of classifying political opinion, 50% is still a good score.

- **Interactive Analysis:**
  - I also developed a web application, equipped with a Streamlit interface available in both English and Korean.
  - Users can explore the political landscape of media by selecting articles from a dropdown list. Upon selection, the application not only displays the content of the article but also visualizes the model’s predicted political orientation and the true political orientation using color-coded results.
  - These color visualizations offer an intuitive way to compare predictions against actual orientations, thereby illustrating the nuanced landscape of media perspectives and enhancing the user's understanding of the model's performance.

🇰🇷 **Korean Version:**

![Korean-gif](https://github.com/user-attachments/assets/e92734d0-7d61-4969-9105-100741b79b64)

🇺🇸/🇨🇦/🇬🇧/ **English Version:**

![English-gif](https://github.com/user-attachments/assets/38befaf1-7015-4573-a8d7-46473e538bcc)

## Repository Overview

The code used to pre-process the data, perform data analysis, train the model and evaluate it can be found [here](). The code of the web application can be found [here](). The datasets used can also be found in [this]() folder of the repository.

## Installation

To set up this project, follow these steps:

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/). Additionally, you will need Git to clone the repository. Install it from [git-scm.com](https://git-scm.com/downloads).

### Setup

1. **Clone the Repository**
   - Open your command line interface (CLI / Terminal).
   - Navigate to the directory where you want to store the project.
   - Run the following command to clone the project:
     ```bash
     git clone https://github.com/mathilddadda/Korean-News-Political-Opinion-Predictor.git
     ```

2. **Install Required Dependencies**
   - Navigate into the project directory:
     ```bash
     cd Korean-News-Political-Opinion-Predictor
     ```
   - Install the required Python libraries:
     ```bash
     pip install -r requirements.txt
     ```

## How to Run
In the same Korean-News-Political-Opinion-Predictor folder, run the following command, which will launch a window in your browser shwoing a nice tool to select articles and view my model's prediction:
```bash
streamlit -run web_visualization.py
```

## License

This project is licensed under the MIT License, anyone can copy and use my work to build up on it.

## Thanks

Thank you to Hugging Face for providing the model used in this project and making a very useful [documentation](https://huggingface.co/docs/transformers/en/training). Thanks to the contributors on GitHub that allowed access to the KoPolitics-Benchmark Dataset as well.


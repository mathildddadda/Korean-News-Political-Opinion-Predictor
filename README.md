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

- **Political Orientation and Level of Pro-Government Sentiment Analysis:**
  - In this analysis I aimed to explore the potential correlations between the level of pro-government sentiment and the political orientation of news articles. A graph was plotted that not only shows the distribution of pro-government sentiment but also overlays the political orientation for each sentiment category.
  - The findings are revealing: articles that criticize the government are predominantly `Liberal`, while those expressing support are often `Moderate Conservative` or `Conservative`. This trend is visually represented, with `liberal criticism` marked by extensive use of blue tones and `conservative support` highlighted in red.

![IMG_7038](https://github.com/user-attachments/assets/a04b568a-af64-4bb0-8103-aae4d207286d)

- **Training Results:**
  - The RoBERTa model was fine-tuned to predict the political orientation of articles. It achieved an accuracy of 48.0% on the test set. This means that the model correctly predicts the political orientation of an article about half of the time. While there is potential for improvement, I realized that would only be possible if I used a larger, more computationally demanding model, which I currently do not have the computational power for. Nonetheless, achieving nearly 50% accuracy is quite good considering the model distinguishes among five distinct political orientations.

- **Interactive Analysis:**
  - A web application was developed, featuring a Streamlit interface available in both English and Korean, allowing users to explore the media landscape.
  - Users can select articles from a dropdown list. Upon selection, the application displays the content of the article and visualizes both the model’s predicted and actual political orientations using color codes.
  - These color visualizations provide an intuitive way to compare predictions with actual orientations, illustrating the nuanced landscape of media perspectives and enhancing understanding of the model's performance.

🇰🇷 **Korean Version:**

![Korean-gif](https://github.com/user-attachments/assets/008a8bc4-2588-4dfc-b37e-fc31a4992e5a)

🇺🇸/🇨🇦/🇬🇧/ **English Version:**

![English-gif](https://github.com/user-attachments/assets/38befaf1-7015-4573-a8d7-46473e538bcc)

## Repository Overview

The code used to pre-process the data, perform data analysis, train the model and evaluate it can be found [here](https://github.com/mathildddadda/Korean-News-Political-Opinion-Predictor/blob/main/political_orientation_training.ipynb). The code of the web application can be found [here](https://github.com/mathildddadda/Korean-News-Political-Opinion-Predictor/blob/main/web_visualization.py). The datasets used can also be found in [this](https://github.com/mathildddadda/Korean-News-Political-Opinion-Predictor/tree/main/political_orientation_dataset) folder of the repository. Note that when training the models, I saved them to a folder named `political_orientation_models`, but due to their large size, I couldn't upload them on this repository.

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


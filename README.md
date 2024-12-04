# Korean-News-Political-Opinion-Predictor

## Introduction

Hello and welcome! This is my first 'big' project. This project was created to explore and enhance my coding skills in Python. I've been self-learning Python and with the aid of AI tools, I've gained a better understanding of how Machine Learning models operate. Motivated by my undergraduate studies, I aimed to apply this knowledge practically. The core of this project involves analyzing Korean news articles to classify them based on their political orientation and level of pro-government sentiment.

The objective was to train a model, specifically a RoBERTa model, to predict the political orientation of a news article. Additionally, I performed data analysis to gain insights into the dataset.

We utilized the **KoPolitics-Benchmark** dataset available [here](https://github.com/Kdavid2355/KoPolitic-Benchmark-Dataset/tree/main) and fine-tuned a RoBERTa model from Hugging Face 🤗, which can be found [here](https://huggingface.co/klue/roberta-base).

## Results



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


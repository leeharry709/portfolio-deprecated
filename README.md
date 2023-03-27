<p align="center">
  <a href = "https://leeharry709.github.io/about-me/">About Me</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href = "https://leeharry709.github.io/portfolio">Portfolio</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href = "https://leeharry709.github.io/resume/">Resume</a>
</p>

<p align="center">
  <img width = "600" height= "600" src="https://raw.githubusercontent.com/leeharry709/word_clock/main/media/1215.png">
</p>

# [Project 1: Natural Language Processing - Sentiment Analysis/Classification & BERT Model Training](https://github.com/leeharry709/portfolio/blob/main/Project%201%20-%20BERT%20for%20Amazon%20Review%20Classification%20(Binary%20Sentiment%20Analysis).ipynb)

This notebook shows the step-by-step process of training the BERT model to identify positive or negative sentiment from Amazon using reviews for random products. The dataset was constructed by Xiang Zhang and provided by Kaggle user kritanjalijain. The original dataset had 1,800,000 training reviews and 400,000 testing reviews, which was too large for my computer to handle in a reasonable amount of time. This analysis was done using a randomly sampled 5% of the training data and 10% of the testing data. Ideally, all of the data would have been used, but that would have either required a lot more time or a lot more computers.

This model determines if a review is positive or negative in sentiment and has many potential use-cases in many different places. In my current company, I work in HR and could be used to classify sentiment in employee year-end reviews. This could even be taken further if I had a dataset with gender (male/female) and sentiment (positive/negative) multiclassifications, which could be used to determine if people are giving gender-biased reviews during the year-end cycle.

This model is a very basic model and would definintely need to be fine-tuned even more and retrained using hyperparameters for even better results. Ultimately, this model is illustrative of the potentials in language processing even at it's most basic forms.

# [Project 2: Image Processing - Color Detection Using Euclidian Distance](https://github.com/leeharry709/ripe-mango-detector)
Incrementally replaces pixels in a 100x100 image of a mango, prioritizing colors farthest from red.

When looking at a single pixel of color, you get an array of 3 values (RGB). Pure red is [255, 0, 0], and every color has it's own unique combination of R, G, and B. By using the formula for Euclidian distance, you can effectively plot the RGB color on a 3 dimensional plot and find the distance between two colors.

This program determines which pixels are the furthest from pure red and begins to mask from there while avoiding pure white, which is the color of the background and not the mango. By incrementally covering the color of the mango, we can create thresholds and classify each image by asking the question "If the color of the mango is < 50% red, then it is not ripe."

Ideally, this type of model would be used to generate images where it is hard to scrape data for. When google searching for ripe mangos, it is hard to find a ton of accurate pictures of ripe mangos, especially since there are many types of mangos with many different ways of distinguishing ripeness. By only using the best pictures of ripe mangos, the red is incrementally covered up, imitating less ripeness. This would only be effective for mangos that are red when ripe, limiting the usage of this model.

![](https://github.com/leeharry709/about-me/blob/main/media/download.png?raw=true)![](https://github.com/leeharry709/about-me/blob/main/media/download%20(1).png?raw=true)![](https://github.com/leeharry709/about-me/blob/main/media/download%20(2).png?raw=true)![](https://github.com/leeharry709/about-me/blob/main/media/download%20(3).png?raw=true)![](https://github.com/leeharry709/about-me/blob/main/media/download%20(4).png?raw=true)

Distribution of Euclidian distance (excluding pure-white pixels) in input image
![](https://raw.githubusercontent.com/leeharry709/about-me/main/media/download%20(5).png)

# [Project 3: Machine Learning - Ripe Mango Detector](https://github.com/leeharry709/ripe-mango-detector)
Determines if submitted mango image is ripe or not based on database of mangos at different ripeness.

This program utilizes machine learning through tensorflow and a database of 427 ripe mangos and 1003 unripe (or green) mangos. By first training a model to differentiate between what is a "green mango" versus what is a "ripe mango", the user can input a filepath (ex: ripe mango.jpg) and it will predict whether or not it is a ripe mango based on its color.

Primarily, the program detects how much of either green, yellow, or red is found on the mango. Based on how much green is missing and red is showing, the program can tell if a mango is ripe or not. The major limiting factor is how much yellow is showing. Yellow mangoes are ambiguous in their ripeness, so the model primarily looks at the how much of the mango is red or green. If there is an ample amount of red and low amount of green, the mango is classified as ripe. The ambiguity in yellow mangos is evident when running the program using "ripe mango 2.jpg" shown on the left which even has a very-slight green tint<img src="https://raw.githubusercontent.com/leeharry709/ripe-mango-detector/main/ripe%20mango%202.jpg" width="70" height="70" align="left">. The program will classify it as "unripe" since there is a low percentage of red showing as well as a low percentage of green. It is important to submit images that best capture the mango's color distribution to get an accurate result.

# [Project 4: Exploratory Data Analysis - DA/DS Salaries](https://github.com/leeharry709/data-analyst-scientist-salaries-EDA-)
Exploratory data analysis on Glassdoor data of data analyst and data science jobs across the nation.

This was an exploratory data analysis of data analyst and data science jobs datasets from Kaggle user Larxel. The user scraped data from glassdoor for the job queries "data analyst" and "data scientist" and posted them as csv files. Using these csv files, I began cleaning the data and visualizing them on Jupyter Notebook. Using seaborn and matplotlib, I was able to display charts and pivot tables that showed results such as correlation between categories, locations that appeared most frequently, and average salaries based on job title.

![](https://github.com/leeharry709/data-analyst-scientist-salaries-EDA-/blob/main/media/download%20(1).png?raw=true)

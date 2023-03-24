<p align="center">
  <a href = "https://leeharry709.github.io/about-me/">About Me</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href = "https://leeharry709.github.io/portfolio">Portfolio</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href = "https://leeharry709.github.io/resume/">Resume</a>
</p>

<p align="center">
  <img width = "600" height= "600" src="https://raw.githubusercontent.com/leeharry709/word_clock/main/media/1215.png">
</p>

# [Project 1: Exploratory Data Analysis - Data Jobs Salaries](https://github.com/leeharry709/data-analyst-scientist-salaries-EDA-)
Exploratory data analysis on glassdoor data of data analyst and data science jobs across the nation.

This was an exploratory data analysis of data analyst and data science jobs datasets from kaggle.com by user Larxel. The user scraped data from glassdoor for the job queries "data analyst" and "data scientist" and posted them as csv files. Using these csv files, I began cleaning the data and visualizing them on Jupyter Notebook. Using seaborn and matplotlib, I was able to display charts and pivot tables to that showed results such as correlation between categories, locations that appeared most frequently, and average salaries based on job title.

![](https://github.com/leeharry709/data-analyst-scientist-salaries-EDA-/blob/main/media/download%20(1).png?raw=true)

# [Project 2: Image Processing - Color Detection Using Euclidian Distance](https://github.com/leeharry709/ripe-mango-detector)
Incrementally replaces pixels in a 100x100 image of a mango, prioritizing colors farthest from red.

When looking at a single pixel of color, you get an array of 3 values (RGB). Pure red is [255, 0, 0], and every color has it's own unique combination of R, G, and B. By using the formula for Euclidian distance, you can effectively plot the RGB color on a 3 dimensional plot and find the distance between two colors.

This program determines which pixels are the furthest from pure red and begins to mask from there while avoiding pure white, which is the color of the background and not the mango. By incrementally covering the color of the mango, we can create thresholds and classify each image by asking the question "If the color of the mango is < 50% red, then it is not ripe."

Ideally, this type of model would be used to generate images where it is hard to scrape data for. When google searching for ripe mangos, it is hard to find a ton of accurate pictures of ripe mangos, especially since there are many types of mangos with many different ways of distinguishing ripeness. By only using the best pictures of ripe mangos, the red is incrementally covered up, imitating less ripeness. This would only be effective for mangos that are red when ripe, limiting the usage of this model.

![](https://github.com/leeharry709/about-me/blob/main/media/download.png?raw=true)![](https://github.com/leeharry709/about-me/blob/main/media/download%20(1).png?raw=true)![](https://github.com/leeharry709/about-me/blob/main/media/download%20(2).png?raw=true)![](https://github.com/leeharry709/about-me/blob/main/media/download%20(3).png?raw=true)![](https://github.com/leeharry709/about-me/blob/main/media/download%20(4).png?raw=true)

Distribution of Euclidian distance (excluding pure-white pixels)
[[](https://raw.githubusercontent.com/leeharry709/about-me/main/media/download%20(5).png)](https://raw.githubusercontent.com/leeharry709/about-me/main/media/download%20(5).png)

# [Project 3: Machine Learning - Ripe Mango Detector](https://github.com/leeharry709/ripe-mango-detector)
Determines if submitted mango image is ripe or not based on database of mangos at different ripeness.

This program utilizes machine learning through tensorflow and a database of 427 ripe mangos and 1003 unripe (or green) mangos. By first training a model to differentiate between what is a "green mango" versus what is a "ripe mango", the user can input a filepath (ex: ripe mango.jpg) and it will predict whether or not it is a ripe mango based on its color.

Primarily, the program detects how much of either green, yellow, or red is found on the mango. Based on how much green is missing and red is showing, the program can tell if a mango is ripe or not. The major limiting factor is how much yellow is showing. Yellow mangoes are ambiguous in their ripeness, so the model primarily looks at the how much of the mango is red or green. If there is an ample amount of red and low amount of green, the mango is classified as ripe. The ambiguity in yellow mangos is evident when running the program using "ripe mango 2.jpg" shown on the left which even has a very-slight green tint<img src="https://raw.githubusercontent.com/leeharry709/ripe-mango-detector/main/ripe%20mango%202.jpg" width="70" height="70" align="left">. The program will classify it as "unripe" since there is a low percentage of red showing as well as a low percentage of green. It is important to submit images that best capture the mango's color distribution to get an accurate result.

# [Project 3: Data Visualization/pandas Dataframe and Styling - Word Clock](https://github.com/leeharry709/word_clock)
Displays a word clock with the current time, day of week, and if it's AM or PM.

This word clock works by displaying different times per 5 minute intervals. For example, 2:55pm would say "IT IS FIVE TO THREE", but 2:59pm would also say the same. Displaying the word clock meant bring the information from one dataframe into another. I took the information from the light_array dataframe by reading which cells had 1s and which cells had 0s and styled the text in the text_array dataframe accordingly.
```
    def light_up(s):
        if s == 0:
            light = 'color: #353535'
        elif s == 1:
            light = 'color: white'
        elif s == 2:
            light = 'color: red'
        elif s == 3:
            light = 'color: blue'
        return light

    styled_df1 = df1.style.apply(lambda x: df2.applymap(light_up), axis=None).set_properties(**{'border-color': '#202020', 'background-color': '#202020','width':'75px','height':'75px','font-size':'25pt','text-align': 'center'})
    display(styled_df1)
```

# [Project 4: Natural Language Processing - Work Projects](https://github.com/leeharry709/work-projects)
Projects made for work. Due to the confidentiality of the work, I am unable to provide any further media other than the code.

-Skills Compiler.py

This program combed through each deparment's job descriptions, parsed the responsibilities and skills, and compiled them into a text file called "text_dumpster.txt".

-Text Analyzer.py

This program would retrieve the text_dumpster.txt files in the selected department's job description folder and begin to process it. The program would preprocess the words. Then, using NLTK, it would make a list of words and bigrams. Combining the two lists together, it would create a dictionary based on the frequency of each word and bigram and display it on a wordcloud.

```
wordcloud = WordCloud(width=1600, height=800).generate(', '.join(filtered))
plt.figure(figsize=(20,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
```

<p>
  <a href = "https://www.linkedin.com/in/leeharry709/">
    <img src="https://raw.githubusercontent.com/leeharry709/about-me/main/media/linkedin.png">
  </a>
  <a href = "https://github.com/leeharry709">
    <img src="https://raw.githubusercontent.com/leeharry709/about-me/main/media/github.png">
  </a>
  <img src="https://raw.githubusercontent.com/leeharry709/about-me/main/media/email.png">
  leeharry709@outlook.com
</p>

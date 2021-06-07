<p align="center">
  <a href = "https://leeharry709.github.io/about-me/">About Me</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href = "https://leeharry709.github.io/portfolio">Portfolio</a>

</p>
<p align="center">
  <img width = "600" height= "600" src="https://raw.githubusercontent.com/leeharry709/word_clock/main/media/1215.png">
</p>

# [Project 1: Exploratory Data Analysis - Data Jobs Salaries](https://github.com/leeharry709/data-analyst-scientist-salaries-EDA-)
Exploratory data analysis on glassdoor data of data analyst and data science jobs across the nation.

This was an exploratory data analysis of data analyst and data science jobs datasets from kaggle.com by user Larxel. The user scraped data from glassdoor for the job queries "data analyst" and "data scientist" and posted them as csv files. Using these csv files, I began cleaning the data and visualizing them on Jupyter Notebook using seaborn and matplotlib.

![](https://github.com/leeharry709/data-analyst-scientist-salaries-EDA-/blob/main/media/download%20(1).png?raw=true)

# [Project 2: Machine Learning - Ripe Mango Detector](https://github.com/leeharry709/ripe-mango-detector)
Determines if submitted mango image is ripe or not based on database of mangos at different ripeness.

This program utilizes machine learning through tensorflow and a database of 427 ripe mangos and 1003 unripe (or green) mangos. By first training a model to differentiate between what is a "green mango" versus what is a "ripe mango", the user can input a filepath (ex: ripe mango.jpg) and it will predict whether or not it is a ripe mango based on its color.

Primarily, the program detects how much of either green, yellow, or red is found on the mango. Based on how much green is missing and red is showing, the program can tell if a mango is ripe or not. The major limiting factor is how much yellow is showing. For mangos, yellow tends to be both ripe and unripe depending on how much green or red is showing. If too much yellow is showing, the program will classify it as unripe. Therefore, it is important to submit a picture that best shows all of the colors on the mango.

```
new_output = model.predict(new_input)
output_index = int(new_output[0][0])

if output_index == 0:
    print('\nRipe mango')
else:
    print('\nNot ripe mango')
```

# [Project 3: Data Visualization/pandas Dataframe and Styling - Word Clock](https://github.com/leeharry709/word_clock)
Displays a word clock with the current time, day of week, and if it's AM or PM.

This word clock works by displaying different times per 5 minute intervals. For example, 2:55pm would say "IT IS FIVE TO THREE", but 2:59pm would also say the same. So, I made a bunch of if and elif statements that displayed the correct words based on what time interval of 5 minutes it was between.

Displaying the word clock meant bring the information from one dataframe into another. I took the information from the light_array dataframe by reading which cells had 1s and which cells had 0s and styled the text in the text_array dataframe accordingly.

![](https://github.com/leeharry709/word_clock/blob/main/media/1725s.png?raw=true)

# [Project 4: Natural Language Processing - Work Projects](https://github.com/leeharry709/work-projects)
Projects made for work. Due to the confidentiality of the work, I am unable to provide any further media other than the code.

-Skills Compiler.py

This program would comb though the job descriptions folder and further into each department's folder and look for Word documents to parse though. It would grab the "Job Duties and Responsibilities" and "Knowledge, Skills, and Abilites" and output them into a "text_dumpster.txt" file. It would continue to go through every deparment's folder until it reached the end of the job descriptions directory.

-Text Analyzer.py

This program would retrieve the text_dumpster.txt files in the selected department's job description folder and begin to process it. The program would first remove punctuations and then stop words. Then, it would create a list of the remaining words. Using NLTK, it would then make a list of the bigrams as well. Combining the two lists together, it would create a dictionary based on the frequency of each word and bigram and display it on a wordcloud.
Skills Compiler.py reads through job descriptions from my current company and brings out the KSAs (knowledge, skills, and abilites) into a text file. This is to be used in conjunction with Text Analyzer - Word Cloud.py, which then uses natural language processing to compile the most commonly appearing words and bigrams and displays it on a word cloud.

```
wordcloud = WordCloud(width=1600, height=800).generate(', '.join(filtered))
plt.figure(figsize=(20,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
```

# Conclusion
These projects capture my skills in data cleaning, visualization, natural language processing, machine learning, and I am excited to learn and apply more technical skills into future projects. I am passionate and driven to succeed in growing my career in data analytics and data science.


Sincerely,

Harold Lee

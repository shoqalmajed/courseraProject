
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **religious events or traditions** (see below) for the region of **Riyadh, Riyadh Region, Saudi Arabia**, or **Saudi Arabia** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Riyadh, Riyadh Region, Saudi Arabia** to Ann Arbor, USA. In that case at least one source file must be about **Riyadh, Riyadh Region, Saudi Arabia**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Riyadh, Riyadh Region, Saudi Arabia** and **religious events or traditions**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **religious events or traditions**?  For this category you might consider calendar events, demographic data about religion in the region and neighboring regions, participation in religious events, or how religious events relate to political events, social movements, or historical events.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[8]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().magic('matplotlib notebook')

df1 = pd.read_csv(r'./loan application.csv')
df2 = pd.read_csv(r'./total loans.csv')
df2 = df2[['month', 'total_loans']]

times = pd.DatetimeIndex(df2['month'])
loans, applications, year = [], [], []

for i in df2.groupby(by = times.year):
    loans.append(np.sum(i[1]['total_loans']) / 1000)
    
for i in df1.groupby(by = 'financial_year'):
    year.append(i[0])
    applications.append(np.sum(i[1]['no_of_applications']))    


# In[9]:

fig = plt.figure()
ax1 = fig.add_subplot(111)
bars = plt.bar(year, applications, align='center', linewidth=0, width = 0.5, color='black')
plt.xticks(year)
plt.xlabel('Year')
plt.yticks(color = 'green')
plt.ylabel('Total Applications for Loan', color = 'green')

for bar in bars:
    height = bar.get_height()
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 2000, str(int(height)) , ha='center', 
                   color='green', fontsize=14, rotation = 'vertical')

ax2 = fig.add_subplot(111, sharex=ax1, frameon=False)
ax2.plot(year, loans[2:], '-o', color = 'm', alpha = 0.75)
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
plt.yticks(color = 'm', alpha = 0.75)
plt.ylabel("Total Loan Amount (in $ Billions)", color = 'm', alpha = 0.75)
plt.tight_layout()
plt.title('Loan Applications VS Loan Amount (2006-15)')


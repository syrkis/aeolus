---
title: A Geospatial Exploration of Wind Energy in Brazil
author: Noah Syrkis & Christina Gaitanou
geometry: margin=3cm
fontsize: 12pt
---
## Abstract

Brazil is a country with large renewable energy potential.
In this report, we explore the potential for wind energy in Brazil.
Using the tools of geospatial data science,
we connect meteorological, demographic, topological, and infrastructure data to better understand this potential.
We find that wind energy is a viable option for Brazil,
and that the country has the potential to become a world leader in wind energy production.

## Introduction

Wind energy is a renewable energy source that has been growing in popularity in recent years.


## Literature Review



### Wind Energy

Wind energy is a renewable energy source that has been growing in popularity in recent years.
There are many reasons for this growth. Part of it is the exsitance of large investments funds such as
[Copenhagen Infrastructure Partners (CIP)](https://www.cipartners.dk/), which has invested in wind energy projects
in Brazil. Another reason is the increasing efficiency of wind turbines, which has made wind energy more
economically viable. Finally, the increasing concern about climate change has led to a push for renewable energy
sources, such as wind energy.

### Brazil

Brazil is a country with large renewable energy potential. It has a large coastline, which makes it a good
candidate for offshore wind energy. It also has a large land area, which makes it a good candidate for onshore
wind energy. Finally, it has a large population, which makes it a good candidate for wind energy.

Political and economic factors does complicate the situation. Brazil has a history of political instability,
which makes it difficult to invest in long-term projects. In addition, Brazil is quite polarized politically,
with recent administrations being anti-environmentalist. Finally, Brazil has a history of corruption, which
makes it difficult to invest in long-term projects; complicated legal systems; and a lack of transparency.

However, Brazil is in many ways also on the forefront of environmentalism, having played an important role in
the Paris Agreement and having a large renewable energy sector. Al Gore has called Brazil "a leader in the
global effort to combat climate change". Alfredo Sirkis, a Brazilian politician and environmentalist, has
called Brazil "the most important country in the world for the future of the environment".

## Data
something

### Meterelogical
something

### Demographic
something

### Topological
something

### Infrastructure
something

## Methodology

### Data Preprocessing

### Exploratory Data Analysis

### Model Selection

### Model Evaluation

## Results

## Discussion

## Conclusion

# References

<div id='refs'></div>

# Appendix

## Appendix A: Final Hyperparameters

|Combination|Batch Size|Dropout|Hidden Dim|Learning Rate|Number of Steps|
|-------------|---|---|---|---|---|
|Dataset 1 - Recurrent - Both|64|0.1|256|0.0001|6000|
|Dataset 1 - Recurrent - Semantic|64|0.3|128|0.0001|4000|
|Dataset 1 - Recurrent - Syntactic|32|0.3|32|0.001|8000|
|Dataset 1 - Siamese - Both|64|0.1|256|0.0001|6000|
|Dataset 1 - Siamese - Semantic|16|0.1|64|0.001|4000|
|Dataset 1 - Siamese - Syntactic|32|0.2|128|0.001|8000|
|Dataset 2 - Recurrent - Both|64|0.3|32|0.001|4000|
|Dataset 2 - Recurrent - Semantic|64|0.3|32|0.0001|6000|
|Dataset 2 - Recurrent - Syntactic|32|0.2|128|0.0001|8000|
|Dataset 2 - Siamese - Both|32|0.2|128|0.001|6000|
|Dataset 2 - Siamese - Semantic|16|0.2|64|0.001|8000|
|Dataset 2 - Siamese - Syntactic|32|0.1|128|0.001|8000|
|Dataset 3 - Recurrent - Both|32|0.1|128|0.0001|4000|
|Dataset 3 - Recurrent - Semantic|16|0.2|32|0.001|2000|
|Dataset 3 - Recurrent - Syntactic|16|0.2|256|0.0001|8000|
|Dataset 3 - Siamese - Both|64|0.1|64|0.001|4000|
|Dataset 3 - Siamese - Semantic|64|0.3|128|0.001|4000|
|Dataset 3 - Siamese - Syntactic|32|0.2|256|0.0001|6000|

## Appendix B: syntactic Vector Features

|Feature #|Description|
|--|-------------|
|0|Number of sentences in the paragraph|
|1|Number of words in the paragraph|
|2|Number of unique words in the paragraph|
|3|Ratio of unique words to total words in the paragraph|
|4|Number of unique part-of-speech tags in the paragraph|
|5|Ratio of unique part-of-speech tags to total words in the paragraph|
|6|Ratio of unique part-of-speech tags to total sentences in the paragraph|
|7-9|Counts, word ratio, and sentence ratio for "NN"|
|10-12|Counts, word ratio, and sentence ratio for "NNS"|
|13-15|Counts, word ratio, and sentence ratio for "NNP"|
|16-18|Counts, word ratio, and sentence ratio for "NNPS"|
|19-21|Counts, word ratio, and sentence ratio for "VB"|
|22-24|Counts, word ratio, and sentence ratio for "VBD"|
|25-27|Counts, word ratio, and sentence ratio for "VBG"|
|28-30|Counts, word ratio, and sentence ratio for "VBN"|
|31-33|Counts, word ratio, and sentence ratio for "VBP"|
|34-36|Counts, word ratio, and sentence ratio for "VBZ"|
|37-39|Counts, word ratio, and sentence ratio for "JJ"|
|40-42|Counts, word ratio, and sentence ratio for "JJR"|
|43-45|Counts, word ratio, and sentence ratio for "JJS"|
|46-48|Counts, word ratio, and sentence ratio for "RB"|
|49-51|Counts, word ratio, and sentence ratio for "RBR"|
|52-54|Counts, word ratio, and sentence ratio for "RBS"|
|55-57|Counts, word ratio, and sentence ratio for "PRP"|
|58-60|Counts, word ratio, and sentence ratio for "PRP$"|

## Appendix C: Problem 9 From Dataset 2 Validation set.

| Change | Paragraph |
|-|----------|
| - | As the child's grandmother, your mother has no particular legal obligation to care for her. (Likewise, if you are an adult, she doesn't have any legal obligation to provide for you either.) If you believe the child is not safe with her grandmother, you should not leave her in her grandmother's care, but you have not described anything that sounds like child abuse.|
| No | If you file a CPS report, they will investigate the child's living conditions holistically, and determine whether she is receiving adequate care in your home. What outcome are you hoping for?|
| Yes | Im not saying it is her responsibility. But she wants to claim the responsibility, she gives my son everything while my daughter gets nothing. Makes it so I can’t work, but then keeps tabs like I’m the one abusing my kids. When she’s the one who doesn’t buy food and “provide” like she claims to others, and even tried to claim to the IRS.|
| No | I’m not even sure what outcome would come about it(that is why i asked the question) and I am fully aware she doesn’t have legal obligations to anything have to do with my kids or me. But she’s claiming it, tried to claim me and my kids on her taxes, yet REALLY doesn’t do anything. So not sure if you can see what I’m saying still...|
| Yes | She's welcome to tell people she's responsible for you and your children all she wants, whether or not she actually is. Telling people she takes care of your children does not create a legal obligation to do so.|
| No | If she is committing tax fraud, you are welcome to report that, or file your own taxes on paper and let the IRS sort out the discrepancy.|
| No | She can't stop you from getting a job, and you're welcome to stop associating with her or letting her see your children.|
| No | It is your responsibility to ensure your children receive adequate care. If they are being neglected at home, you will be the one held responsible. CPS will not order your mother to provide more care for her grandchild, if that was what you were hoping for.|
| Yes | Why is it your mom's responsibility to provide childcare, feed, change diapers and comb your daughter's hair? What behaviors have led you to consider reporting your mom for child abuse? |
| No | How is your mom making it so that you can't work? Since you think her treatment of you and your children is unfair, stop relying on her for support. Was your mom successful in claiming you and your kids as dependents?|

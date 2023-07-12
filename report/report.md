---
title: A Geospatial Exploration of Wind Energy in Brazil
author: Noah Syrkis & Christina Gaitanou
geometry: margin=3cm
fontsize: 12pt
---

# Part 1

## Abstract

In the domain of Natural Language Processing (NLP), the task of multi-author writing style analysis is important. It plays a role in plagiarism detection, forensics, history, and more. This paper introduces an experiment designed to detect changes in authorship within Reddit comment threads at the paragraph level. We use two types of neural network architectures: our baseline model, a Multi-Layer Perceptron (MLP), processes pairs of paragraphs, while our more advanced model utilizes a Gated Recurrent Unit (GRU) layer to handle sequences of paragraphs. Paragraphs are represented by either a semantic vector, a syntactic vector, or the concatenation of the two, depending on the setup. The semantic vectors are extracted from Sentence-BERT embeddings, and the syntactic vectors are constructed by feeding paragraphs to a function that determines various features, such as average sentence length, and the frequencies of particular kinds of words. Our findings, evaluated with F1 scores, suggest that incorporating sequential information enhances performance in multi-author writing style analysis. Additionally, as paragraphs become more similar in content, the contribution of syntactic information becomes increasingly important.

## Introduction

Multi-author writing style analysis is a fascinating and challenging field within Natural Language Processing (NLP). It has a rich history. The concept of distinguishing authorship based on stylistic nuances has roots predating the digital text age, tracing back to fields such as cryptography, literary history, and forensics, where features like word choice, sentence structure, and rhythmic patterns of writing were analyzed for signs of individual authorship.

An interesting early instance of authorship detection occurred during World War II. Telegraph operators were frequently identified by their unique Morse code patterns. Despite Morse code's standardized system of dots and dashes, operators developed individualized patterns discernible by experts. This is mentioned to illustrate the idea that personal idiosyncrasies could seep through even the most formalized communication modes.

Today, authorship attribution and style analysis have found wide applications, helping with uncovering ghostwriting and plagiarism and contributing to forensics. With the advent of digital communication and generative artificial intelligence vast amounts of text data are being produced, making authorship attribution an increasingly relevant field.

This paper describes an experiment in detecting authorship changes within sequences of Reddit comment paragraphs. We represent each paragraph as a semantic, or syntactic vector, or as the concatenation of the two. Semantic features are extracted from pre-trained Sentence-BERT embeddings, while the syntactic features are constructed by feeding paragraphs to a function written as part of the experiment. We initiate our analysis with a Siamese Multi-Layer Perceptron (MLP) model, which serves as our baseline. This model processes pairs of paragraphs, calculating a distance measure between the two, and determining if they share the same authorship. We then explore a more advanced model utilizing a Gated Recurrent Unit (GRU) layer to handle sequences of paragraphs. We do this to investigate how useful having the larger contexts is for the task, and if the additional complexity required of the model to process the context, yields an increase in performance. We define performance as an F1 score, though other metrics, like processing speed, are also interesting.

The paper is structured as follows: following a review of relevant literature, we introduce our data and task. This in turn is followed by a detailed overview of our methodology. Followed by that, we have a presentation and discussion of our results. We conclude with reflections on our findings and potential future work directions.

## Literature Review

Multi-author writing style analysis combines several active areas within natural language processing and machine learning. It has advanced significantly in recent decades. Early high-profile use of statistical author style change detection can be traced back to @mosteller1963's analysis of the disputed Federalist Papers based on common word frequency alone.

With the advent of machine learning, new tools were made available for writing style analysis and authorship attribution. An extensive overview of these techniques is provided by @stamatatos2009. Deep learning methods, particularly Siamese and GRU architectures, were later employed to further these tasks as described by @qian2017. As with much of natural language processing, these tasks too have been influenced by the transformer architecture first introduced by @vaswani2017, though our approach is simpler, attempting to isolate the effect of including the full sequence of paragraphs in particular.

The application of machine learning to natural language processing tasks entails transforming raw text into processable, numerical forms, typically achieved through text embeddings. The influential work by @devlin2019 on BERT, a context-aware language model, and its extension for sentence embeddings—Sentence-BERT (SBERT)—by @reimers2019 forms the basis for semantic vectors in our study.

The architecture of our neural networks stems from the work of @bromley1993 on Siamese networks. A Siamese network takes two samples, and feeds them through the same layer, before computing their difference. Originally developed for signature verification, this architecture's ability to learn distance functions has found considerable application in comparison-based tasks. To handle sequence data effectively, we augment our model with Gated Recurrent Units (GRUs), introduced by @chung2014, due to their ability to handle long-term dependencies. The relationship between authorship and stylistic variation in web text is explored by @bhargava2013 on Twitter.

Thus, it is with a robust foundation in multi-author writing style analysis that we attempt this experiment to test the effect of processing entire sequences of paragraphs, instead of pairs. To further elucidate this effect we explore how it varies for semantic, syntactic, and combined text representations.

## Data & Task

The foundation for our experiment is the 2023 PAN challenge on Multi-Author Writing Style Analysis. The challenge is based on data derived from Reddit, a social media platform with many "subreddits" for different topics, which in turn consists of threads to which many different users contribute. Threads are thus types of multi-author documents where each comment represents a paragraph in a sequentially arranged text. Threads make Reddit is a good environment for studying authorship transitions.

The PAN challenge provides three datasets, each presenting varying levels of difficulty—"Easy," "Medium," and "Hard". Each dataset varies in its degree of topical diversity between paragraphs in documents, ranging from a broad spectrum in the "Easy" dataset to a single topic in the "Hard" dataset. We primarily focus on the "Medium" dataset, which has limited topical variation, encouraging the detection of authorship changes based on stylistic and syntactic cues over content-based semantic cues.

The datasets are each made up of a training set (4200 samples) and a validation set (800 samples). The validation set is further partitioned into a development set and a test set, each containing 400 samples. These sets come with ground truth data indicating authorship change points. The true test data for the challenge is unavailable, which is why the validation set was further split in two.

Our key task is detecting style changes at the paragraph level within documents, indicating authorship changes. These changes can only occur _between_ paragraphs. A single paragraph belongs to one author. Each task problem is identified by an ID and includes two files—one with the text and the other with ground truth data. The latter specifies whether a style change occurs (1) or not (0) between every pair of consecutive paragraphs. Our objective is to train models that can accurately predict these ground truth values, enabling effective identification of authorship transitions. We evaluate this effectiveness using the F1 score metric.

## Methodology

Our approach to authorship change detection involves two neural models, both three layers deep. The baseline model, referred to as the Siamese model, is a Siamese Multi-Layer Perceptron (MLP) designed to determine whether two given paragraphs are written by the same author. The advanced model, called the Recurrent model, replaces the Siamese layer with a gated recurrent unit (GRU) layer. This change enables the model to process sequences of paragraphs, offering additional information about each author's writing style. Three versions—semantic, syntactic, and concatenated—of the two models were trained for each of the three datasets, yielding 18 distinct models (see Appendix B for details).

### Vector representations

The syntactic feature vector is a manually constructed vector encompassing a variety of linguistic and stylistic attributes from the text. This vector comprises 61 features. The first four denote stylometric aspects like the count of sentences, words, and unique words in a paragraph. The remaining features indicate specific use patterns of various part of speech (POS) tags. These features provide counts, ratios to words, and ratios to sentences for different types of nouns, verbs, adjectives, adverbs, and pronouns. This includes tags such as "NN" for common nouns, "VB" for verbs, and "JJ" for adjectives. In contrast, the semantic vectors are 384-dimensional representations generated from the Sentence-BERT (SBERT) embeddings corresponding to each paragraph. The SBERT embeddings are roughly six times larger than the syntactic vector. By concatenating the syntactic and semantic vectors, we get our largest—and hopefully most expressive—paragraph representation, sized at 445 dimensions.

### Siamese MLP – Baseline Model

Our Siamese MLP, functioning as the baseline, accepts a pair of consecutive paragraphs (represented by their extended SBERT embeddings) and determines whether a style change, implying an authorship change, occurs between them. The choice of MLPs is due to their proven success in complex function modeling and classification tasks. The model first feeds the two vectors through the same linear layer, before merging them into one vector by subtraction. This single vector is then fed through the remaining two layers of the network.

### GRU Model

To outperform the baseline, we implement a GRU model. Unlike the Siamese MLP, the GRU model processes the entire sequence of paragraph embeddings for a document, thus capturing a broader context and making more informed predictions about authorship changes. The GRU model does not use a Siamese architecture, as the relationship between a paragraph and its neighbors is handled by the recurrence layer.

### Hyperparameter Optimization

To enhance our models' performance, we conduct a random hyperparameter search across variables such as layer sizes, learning rates, batch sizes, and number of steps^[Note that we used the number of steps, rather than epochs. Epochs can be obtained by dividing and multiplying the number of steps with the batch size, and dividing by the total number of samples (4200 in the training set)] and dropout rates. Good hyperparameters were determined after training a total of 378 models, with 21 hyperparameter samples drawn and trained for each model. The hyperparameter sample spaces are in the table below.

|Hyperparameter|Sample Space|
|---|---|
| Learning rate |{0.001, 0.0001, 0.00001}|
| Dropout |{0.1, 0.2, 0.3}|
| Hidden dimension size |{32, 64, 128, 256}|
| Batch size |{16, 32, 64}
|Number of steps | {2000, 4000, 6000, 8000}|

Table: Hyperparameter sample spaces.

### Model Training & Evaluation

Models are trained on the training set and fine-tuned and evaluated on the validation set. The chosen evaluation metric, by the task's requirements, is the F1 score—an aggregate measure of precision and recall. We aim to maximize this score for accurate authorship change prediction. Binary Cross Entropy (BCE) was chosen as the loss function over Soft F1 loss, as early experiments indicated that it yielded better performance, despite the latter’s mathematical similarity to the F1 score.

## Results & Discussion

The final hyperparameters for each of the 18 models can be seen in Appendix A. It is noteworthy that, despite the similarity between tasks, models, and input data, almost the entire sample space of each hyperparameter is present when looking at all 18 models. This might be an indication of model robustness, though more exploration would need to be done to confirm this.

The performance of the Siamese baseline on Dataset 2 is reported in Table 2.
When including both semantic and syntactic features the test F1 score is 0.6155. Excluding the semantic features drops the F1 score to 0.6538 while excluding the syntactic feature drops the F1 score to 0.5123. This is an indication that the syntactic feature is more indicative of author change than the SBERT vector. There drop in performance from the training set to the validation set, which is not unexpected and suggests a degree of overfitting to the training data. The Recurrent model does outperform its Siamese baseline in Dataset 2 when training on both modalities and the purely semantic modality, reaching a test F1 score of 0.6807 when training on the former—significantly better than the Siamese's 0.6155. However, on the purely syntactic modality, the Siamese model slightly outperforms the Recurrent model.

|Model|Modality|Train F1|Test F1|Train Loss|Test Loss|Params|
|---|---|---|---|---|---|--:|
|Recurrent|both|0.7300|0.6807|0.4995|0.5475|20,641|
|Recurrent|semantic|0.6460|0.5945|0.5850|0.6043|18,689|
|Recurrent|syntactic|0.6720|0.6462|0.5652|0.5780|107,137|
|Siamese|both|0.6660|0.6155|0.5617|0.5943|73,729|
|Siamese|semantic|0.7016|0.5123|0.4949|0.6655|28,865|
|Siamese|syntactic|0.6761|0.6538|0.5780|0.6112|24,577|

Table: Dataset 2 — Test and train results.

While both models were successful at identifying changes in authorship based on stylistic differences, the superior performance of the GRU model suggests that considering the full context of the document, rather than only pairwise comparisons of paragraphs, can lead to more accurate predictions.



|Model|Modality|Train F1|Test F1|Train Loss|Test Loss|Params|
|---|---|---|---|---|---|--:|
|Recurrent|both|0.9720|0.9460|0.1281|0.2335|509,185|
|Recurrent|semantic|0.9403|0.9238|0.2823|0.3615|148,481|
|Recurrent|syntactic|0.9501|0.9462|0.2197|0.2441|8,353|
|Siamese|both|0.9551|0.9569|0.1855|0.2275|180,225|
|Siamese|semantic|0.9800|0.9449|0.0874|0.2226|28,865|
|Siamese|syntactic|0.9508|0.9398|0.2265|0.2917|24,577|
Table: Dataset 1 — Test and train results.

Inspecting Table 3, focusing on Dataset 1, we see that performance becomes similar for all models, while the layer sizes fluctuate widely, as indicated by the parameter count column. In Table 4, focused on Dataset 3, in which the topics are most similar, we see that, surprisingly, the semantic modality outperforms both the concatenated and the syntactic modality. This is highly surprising since the semantic distance between the paragraph representations should decrease as we move from Dataset 1 through Dataset 2, to Dataset 3.

|Model|Modality|Train F1|Test F1|Train Loss|Test Loss|Params|
|---|---|---|---|---|---|--:|
|Recurrent|both|0.5575|0.5330|0.6458|0.6616|156,289|
|Recurrent|semantic|0.5282|0.4990|0.6562|0.6699|18,689|
|Recurrent|syntactic|0.5306|0.5117|0.6647|0.6757|410,881|
|Siamese|both|0.5343|0.5041|0.6500|0.6795|32,769|
|Siamese|semantic|0.6845|0.5250|0.5527|0.7260|65,921|
|Siamese|syntactic|0.4932|0.4671|0.6919|0.6799|81,921|

Table: Dataset 3 — Test and train results.

The relatively large difference in performance across models could potentially be fueled by statistical uncertainty, as the test and validation sets are on the small side—the test and validation sets are each 8 % of the total sample count.

Setting this aside, the Siamese model served as a robust baseline, but its pairwise comparison of paragraphs could not leverage the contextual information provided by the full sequence of paragraphs in a document. This limitation was addressed by the GRU model, which processes the entire sequence and was thereby better able to identify writing style changes. The improved performance of the GRU model shows the relevance of using sequence models for tasks that involve dependencies between data points, like text and time-series data, supporting the intent of the GRU architecture as laid out in @chung2014's aforementioned work. The usefulness of the syntactic vector also serves as evidence of @bhargava2013's work on authorship identification in Twitter, applying to Reddit text as well.

Despite these results, several avenues remain open for further exploration. For example, additional gains may be possible by experimenting with other types of sentence or paragraph embeddings, such as Doc2Vec or Universal Sentence Encoder. Furthermore, exploring more advanced architectures, including attention-based models like the Transformer, could lead to high performance. We could, for example, finetune a BERT model, rather than merely using its embeddings. This would require a lot more computational resources.

## Conclusion

In conclusion, our experiment demonstrated that including the context of surrounding paragraphs tends to enhance performance in authorship change detection, at least within the scope of our specific Reddit dataset. The increased computational complexity of the GRU model is thus justified, considering its superior performance over the Siamese model. This finding underscores the importance of considering sequential information in tasks that involve contextual dependencies. Moreover, it highlights the potential of recurrent architectures in dealing with similar problems that involve style change or authorship attribution. However, the performance does vary across different datasets and task specifications.


# Part 2

*Q1.Explain the difference between topic change and style change. Based on this difference, discuss whether the documents in the datasets consistently display both changes, or whether they tend to show one single aspect. Please provide examples from one or more of the datasets where each of these specific changes happen.*

Topic change refers to a shift in the _ideas_ of a text, while a style change involves a shift in the _way_ these ideas are expressed. Style changes can manifest in grammar structure, word choice, tone, sentence lengths, and more. As we explored in the literature review, stylistic differences tend to persist between individuals, even in highly formal settings, like Morse code.

Looking at Dataset 2's validation set, we focus on problem 9, which can be seen in full in Appendix C. In this instance, we can see stylistic differences and topic consistency in these two paragraphs:

_As the child's grandmother, your mother has no particular legal obligation to care for her. (Likewise, if you are an adult, she doesn't have any legal obligation to provide for you either.) If you believe the child is not safe with her grandmother, you should not leave her in her grandmother's care, but you have not described anything that sounds like child abuse._

and

_Im not saying it is her responsibility. But she wants to claim the responsibility, she gives my son everything while my daughter gets nothing. Makes it so I can’t work, but then keeps tabs like I’m the one abusing my kids. When she’s the one who doesn’t buy food and “provide” like she claims to others, and even tried to claim to the IRS._

Both paragraphs focus on the same topic: a dispute over childcare responsibilities. However, the styles of the two paragraphs are markedly different. The first paragraph takes an explanatory tone, explaining the legal obligations and offering straightforward advice. It is detached and formal, using proper punctuation and sentence structure. The second paragraph, on the other hand, reads as a personal account or complaint, marked by emotional tone, and informal language. This contrast signals a change in style while maintaining the same topic.

To illustrate a topic change, consider the first paragraphs from above, and:

_If she is committing tax fraud, you are welcome to report that, or file your own taxes on paper and let the IRS sort out the discrepancy._

While both paragraphs are linked to the larger context of the family dispute, they cover different topics: the first paragraph discusses childcare obligations, and the second addresses potential tax fraud. This highlights a clear topic change within the same problem.

The complete text from Problem 9, with author change indicators, is included in Appendix C.

*Q2.Explain what the task of authorship attribution is, and discuss how your approach for style change detection could be used and possibly modified for authorship attribution.*

Authorship attribution and style change detection are distinct but related tasks. While the former aims to identify _who_ has authored a given text, the latter focuses on detecting _if_ a shift in authorship has occurred within a text.

In our experiment, we have focused on style change detection. However, the underlying models and techniques we have used could be modified for authorship attribution. Specifically, there are two key ways this could be accomplished:

1. **Author Change Points Detection**: The first step could involve using our style change detection system to identify points within a text where an author change may have occurred. This would create a shorter (unless the author changes in every paragraph) sequence of joined author paragraphs. Each of these could then be analyzed separately in the subsequent step of author attribution.

2. **Adapting the Model for Author Classification**: When detecting potential points of author change, the model could be modified to predict not just whether a change has occurred, but also to identify the specific author of each segment. This would involve changing the output layer of our existing model to predict the author's identity instead of merely detecting a change. Each author would be represented as a class, and the model would predict the class (author) of each paragraph or segment.


The datasets used in this experiment include information about the number of different authors present in a particular problem. As an extension of the current style change detection task, a future direction could be to predict the number of authors in addition to the locations of authorship change. This becomes a more complex problem when the pool of potential authors is larger than the sequence length. For instance, in an open-ended scenario such as "Which three British authors wrote these three text passages?", the "multi" in multi-class classification represents the total number of British authors, not just the number three. Consequently, this task would require a considerably larger amount of training data for each potential author and probably necessitate a more advanced model than our current one. In this case, a complete model redesign might be more appropriate than mere adaptation.

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

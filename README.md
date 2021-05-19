# Text-Rank

**If you have trouble with watching ipynb online, click [Here](https://htmlpreview.github.io/?https://github.com/alex-romanovskii/Text-Rank/blob/main/main.html) to see code**   

### Info
TextRank[1] is an algorithm based on PageRank, which often used in keyword extraction and text summarization.

### Algorithm stages 
- drop out short words(less than two letters ) and stop words **nltk**
- extract root from the remaining words **(using nltk)**
- calculate the relationship between each pair of sentences. For this I use Jaccard index [2]
- build a fully connected graph, where each sentence is a vertex, and the edge weight corresponds to the index calculated previously **(using networkx)**
- implementation of the Pagerank algorithm **(using networkx)**
- for a more convenient interpretation of the weights, I use MinMaxScaler from sklearn [3]

### Output
As output, each text corresponds to a csv file. In which each sentence of the text corresponds to a weight (the more weight, the more important the sentence). 

### Run
- place texts for summarization in folder **texts**
- run **main.py**. You can find csv file for each source text in folder **texts/Summarize**

### Reference
[1] - Mihalcea, R. and Tarau, P., 2004, TextRank: Bringing Order into Texts, Proceedings of the 2004 Conference on Empirical Methods in Natural Language Processing, Barcelona.
[2] - https://en.wikipedia.org/wiki/Jaccard_index
[3] - https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html

import string

import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sa = SentimentIntensityAnalyzer()
# st.title('hai')

a = "Movie is bad but screenplay is awesome"
def pree1(a):
    c=0
    neg = ['but', 'despite', 'yet', 'however', 'unless', 'rather', 'although', 'even though']
    for i in neg:
        if i in a:
            c = c + 1
    if c > 0:
        def pre(a):
            for i in neg:
                if i in a:
                    x = i
            l = []
            l.append(a.split(x))

            l1 = []
            for i in range(0, len(l) + 1):
                l1.append((sa.polarity_scores(l[0][i])))

            l2 = []
            for i in l1:
                l2.append(i['compound'])
            return l2

    if c>0:


        # print(pre(a))
        ans = []
        ans = pre(a)
        s: float = 0.0
        for i in ans:
            s = s + i
        if (s < 0):
            return(min(ans))
            # print("Negative review in it")
        else:
            return(max(ans))
            # print("Positive Review in it")
    else:
        dict=(sa.polarity_scores(a))
        x=dict['compound']
        if x>0:
            return(x)
        else:
            return(x)

# print(pree1(a))
# print(sa.polarity_scores(a))
doc ="""Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.In its application across business problems, machine learning is also referred to as predictive analytics."""

# from gensim.summerization import summerize
# summerize(a)

print(sa.polarity_scores("screenplay is good"))


# c=0
# for i in range(0,len(neg)):
#     if(neg[i] in a):
#         c=1;
# if(c==1):
#     print('function called')
#     pre(a)
# else:
#     dict=sa.polarity_scores(a)
#     print(dict['compound'])

#__author__ = 'ram'

from nltk.corpus import sentiwordnet as swn
import re
from nltk.corpus import stopwords
import nltk
import nltk.tokenize
def sent_score(review):
        verb ={ 'VB','VBD','VBG','VBN','VBP','VBZ'}
        adverb={'RB','RBR','RBS'}
        adj={'JJ','JJR','JJS'}
        vlist=[]
        avlist=[]
        adjlist=[]
        ls=[]
        sentence=review
        #dic={'serious':0,'uninspired':-0.3,'good':0.4,'love':0.9,'awesome':0.75,'amuses':0.125,'challenging':0.65,'introspective':0.75,'independent':0.375,'quiet':0.125,'positively':0.85,'mess':-0.375,'plodding':-0.375,'trouble':-0.375}
        letters_only = re.sub("[^a-zA-Z.]"," ",sentence)
        words=letters_only.split()
        stops = set(stopwords.words("english"))-{"very","against","but","not","down"}
        meaningful_words = [w for w in words if not w in stops]
        print meaningful_words
        pos_words=nltk.pos_tag(meaningful_words)
        print pos_words
        s=0
        sen_score1=0
        sen_score=0
        cnt=1
        cal_score=0
        print(len(words))
        for i in range(0,len(pos_words)):
                    print i
                    print(pos_words[i])
                    if pos_words[i][0]=='n\'t':
                                if pos_words[i][1] in verb:
                                        st1=list(swn.senti_synsets(pos_words[i+1][0],'v'))
                                        if  len(st1)!=0:
                                            print(st1[0].pos_score())
                                            print(st1[0].neg_score())
                                            if(st1[0].pos_score()!=0 or st1[0].neg_score()!=0):
                                                     cnt=cnt+1
                                            sen_score1=st1[0].pos_score()-st1[0].neg_score()
                                elif pos_words[i][1] in adverb:
                                            st2=list(swn.senti_synsets(pos_words[i+1][0],'r'))
                                            if  len(st2)!=0:
                                                    print(st2[0].pos_score())
                                                    print(st2[0].neg_score())
                                                    if(st2[0].pos_score()!=0 or st2[0].neg_score()!=0):
                                                                        cnt=cnt+1
                                                    sen_score1=st2[0].pos_score()-st2[0].neg_score()

                                elif pos_words[i+1][1] in adj:
                                            st3=list(swn.senti_synsets(pos_words[i][0],'a'))
                                            if  len(st3)!=0:
                                                print(st3[0].pos_score())
                                                print(st3[0].neg_score())
                                                if(st3[0].pos_score()!=0 or st3[0].neg_score()!=0):
                                                                 cnt=cnt+1
                                                sen_score1=st3[0].pos_score()-st3[0].neg_score()

                                sen_score1=-sen_score1
                                sen_score+=sen_score1
                                i=i+1
                    # elif pos_words[i][0] in  dic:
                    #                   sen_score+=dic[pos_words[i][0]]
                    #                   cnt=cnt+1
                    elif pos_words[i][1] in verb:
                            st1=list(swn.senti_synsets(pos_words[i][0],'v'))
                            if  len(st1)!=0:
                                   print(st1[0].pos_score())
                                   print(st1[0].neg_score())
                                   if(st1[0].pos_score()!=0 or st1[0].neg_score()!=0):
                                                         cnt=cnt+1
                                   sen_score+=st1[0].pos_score()-st1[0].neg_score()

                    elif pos_words[i][1] in adverb:
                             st2=list(swn.senti_synsets(pos_words[i][0],'r'))
                             if  len(st2)!=0:
                                    print(st2[0].pos_score())
                                    print(st2[0].neg_score())
                                    if(st2[0].pos_score()!=0 or st2[0].neg_score()!=0):
                                                         cnt=cnt+1
                                    sen_score+=st2[0].pos_score()-st2[0].neg_score()

                    elif pos_words[i][1] in adj:
                             st3=list(swn.senti_synsets(pos_words[i][0],'a'))
                             if  len(st3)!=0:
                                    print(st3[0].pos_score())
                                    print(st3[0].neg_score())
                                    if(st3[0].pos_score()!=0 or st3[0].neg_score()!=0):
                                                        cnt=cnt+1
                                    sen_score+=st3[0].pos_score()-st3[0].neg_score()

                    elif pos_words[i][0]=='but':
                                      if i!=len(pos_words):
                                              sen_score=-sen_score
                                              cnt=cnt+1
                    elif pos_words[i][0]=='challenging':
                                      sen_score+=0.65
                                      cnt=cnt+1
                    # elif pos_words[i][0] in  dic:
                    #                   sen_score+=dic[pos_words[i][0]]
                    #                   cnt=cnt+1

                    print 'score is:',sen_score
        if sen_score>1:
                calscore=sen_score/cnt
        else:
               calscore=sen_score
        print calscore
        return calscore



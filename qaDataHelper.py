#加载数据1


def loadData(filename,word2idx,maxlen,training=False):
    question = ""
    questionId = 0
    questions,answers,labels,questionIds = [],[],[],[]
    
    with open(filename,mode="r",encoding="utf-8") as rf:
        for line in rf.readlines():
            arr = line.split("\t")
            #问题去重保存？
            if question!=arr[0]:
                qeustion = arr[0]
                questionId +=1
            
            questionIdx = sentenceToIndex(arr[0].strip(),word2idx,maxlen)
            answerIdx = sentenceToIndex(arr[1].strip(),word2idx,maxlen)
            
            if training:
                lable = int(arr[2])
                lables.append(label)
            
            questions.append(questionIdx)
            answers.append(answerIdx)
            questionIds.append(questionId)
    return questions, answers,lables,questionIds

#句子转化成数字索引形式2
def sentenceToIndex(sentence,wordidx,maxlen):
    #sentence 是什么样的形式
    
    #后面的参数是默认值吗
    unknown = word2idx.get("UNKNOWN",0)
    num = word2idx.get("NUM",len(word2idx))
    #这个index是什么
    index = [unknown]*maxlen
    
    i = 0
    for word in jieba.cut(sentence):
        if word in word2idx:
            index[i] = word2idx[word]
        else:
            if re.match("\d+",word):
                index[i] = num
            else:
                index[i] = unknown
        if i>=maxlen-1:
            break
        i +=1
     return index
     
     
 
    

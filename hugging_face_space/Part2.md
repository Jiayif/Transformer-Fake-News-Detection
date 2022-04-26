## Solution

The hardest part of this problem is to gain the accurate data. There is no way for us to confirm each row in our datasets. So we combine the data from kaggle and the data we scraped from news website which is confirmed to be fake or real. we tried to choose objective topics as more as possible. Next we choose the pre-trained model "roberta-base" as our baseline. Since our problem is to classify the text, the hugging face actually has everything we need now, we just need to follow the documents to fine-tune our model. The fine-tune step for a pre_trained model as follows:

1. Tokenize each sentence by roberta token
2. Set our training parameters
3. Start training
4. Assessment

## Critical Analysis

1. For the current model, we only take top 500 words in the text due to training resources. It may caused some problems when the model meet the large text if its context is highly relevant. We may obtain more resources in the futrue for this problem.

2. The model can't give correct prediction for those long text of personal emotional expression. 

3. if the input text is too short, it often judges it as fake news due to our strategy of   truncating top 500 words and padding short text.

   ### Further improvement

   1. We may add more data features such as title, author information to improve the model.
   2. As for some news, they just predict or represent their opinions on certain situations, we may include Neutral result when we classify the data.
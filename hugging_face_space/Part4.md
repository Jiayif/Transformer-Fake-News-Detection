## Critical Analysis

1. The current model can only take first 500 words in the text due to training resources. It might cause problems when a long text is entered into the model which context is highly relevant. 

2. When the input text is too short, it often judges it as fake news due to our strategy of truncating first 500 words and padding short text.

   ### Further improvement

   1. We may add more features such as title, author information to improve the model.      
   2. The current pre-trained model RoBERTa is still quite slow when trainning on big datasets. Probably we can try other models and compare the runtime and performance of the models.
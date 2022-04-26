### Fine Tuning

Fine tuning is when using a pretrained model, train it on a dataset specific to the task. The steps for fine tuning a pre_trained model can be given as follows:

1. Tokenize each sentence using RoBERTa 
2. Set training parameters
3. Train the model
4. Assess: Using ROC-AUC for this problem

### Challenge

The biggest challenge in this task is to get the correct label for each piece of news. As we can't verify news ourselves, I managed to choose news that is objective and has been confirmed or falsified.
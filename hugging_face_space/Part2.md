## Solution

Used a combined dataset from kaggle and dataset that scraped from new websites that is confirmed to be fake or real. Then select the pre-trained model "roberta-base" as the baseline, and fine tuning the model.

### RoBERTa

RoBERTa stands for **Robustly Optimized BERT Pre-training Approach**. The goal of the model was to optimize the training of BERT architecture in order to take lesser time during pre-training. **BERT**, which it based on uses static masking i.e. the same part of the sentence is masked in each Epoch. In contrast, RoBERTa uses dynamic masking, wherein for different epochs, different part of the sentences are masked.

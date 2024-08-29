# Dataset:
- Original: [Kaggle Medical No Show dataset](https://www.kaggle.com/datasets/joniarroba/noshowappointments/data)
- Modified: Merged the Features of the dataset for classification of No Show. (Inside the Dataset Folder)
- The modified dataset contains two feature:
    - Statement: Which containes information about the patient
    - NoShow: Which containes Yes or No

# Model Used:
- Llama 3.1 8B-instruct

# Tokenizer:
- Using Hugging Face AutoTokenizer which uses LlaMA tokenizer which is a BPE based on sentence piece.
- Llama uses a variant of SentencePiece called Unigram Tokenizer which is a subword tokenziation algorithm.

# Fine tuning:
- Parameter Efficient Fine Tuning (PEFT)

# Steps to Use:
- Login to Hugging Face and get access to Llama Models
- Login to Weight and Biases for monitoring
- Run the hf-model notebook and save the model
# Dataset:
- Original: [Kaggle Medical No Show dataset](https://www.kaggle.com/datasets/joniarroba/noshowappointments/data)
- Modified: Merged the Features of the dataset for classification of No Show. (Inside the Dataset Folder)
- The modified dataset contains two feature:
    - Statement: Which containes information about the patient
    - NoShow: Which containes Yes or No

# Fine tuning:
- The Llama model is trained on huge amounts of data therefore fine tuning is essential for specializing in specific domain.
- Model fine tuning with Parameter Efficient Fine Tuning (PEFT). Based on [PEFT](https://arxiv.org/pdf/1902.00751) paper.
- Fine tuning is requires huge amount of resources but PEFT makes the process faster and less demanding.
- The Low rank adaptaion method(LoRA) method. Based on the [LoRA](https://arxiv.org/pdf/2106.09685) Paper.
    - LoRA config is used 
- The QLoRA Method. Based on the [QLoRA](https://arxiv.org/pdf/2305.14314) paper.
    - Bits and bytes config for quantization is used. 

# Ways to fine tune for Classification
1. Generating text with the Label as part of the generated text
   - Input: Instruction for text generation along with the text and the label.
   - Output: The text with assigned label.
2. Adding Linear Layer at the end to the LlaMa model.
   - Input: Sentences(texts)
   - Ouput: Label for that sentence


# Model Used:
- Llama 3.1 8B-instruct for first Method of Fine tuning
- Llama 3.1 8B for second method of Fine tuning

# Tokenizer:
- Using Hugging Face AutoTokenizer which uses LlaMA tokenizer which is a BPE based on sentence piece.
- Llama uses a variant of SentencePiece called Unigram Tokenizer which is a subword tokenziation algorithm.


# Training:
- For training the model I used Lambda labs cloud GPUs.


# Steps to Use:
- Login to Hugging Face and get access to Llama Models
- Login to Weight and Biases for monitoring
- Run the hf-model notebook and save the model
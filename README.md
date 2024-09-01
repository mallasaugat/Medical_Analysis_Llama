# Llama Fine-tuning on Medical No-Show Dataset

## Project Overview
This project fine-tunes the Llama model to predict whether a patient will attend their medical appointment based on provided text information. The model classifies the likelihood of a "No Show" event using fine-tuning techniques.

## Dataset
- **Original Source:** [Kaggle Medical No-Show Dataset](https://www.kaggle.com/datasets/joniarroba/noshowappointments/data)
- **Modified Version:** The dataset has been preprocessed and features merged for efficient classification. The modified dataset includes:
  - **Statement:** A textual description containing patient information.
  - **NoShow:** A binary label ('Yes' or 'No') indicating whether the patient missed their appointment.

## Fine-tuning Strategy
Fine-tuning the Llama model is critical for adapting it to the specific domain of medical appointment data. This process is enhanced using Parameter-Efficient Fine-Tuning (PEFT), reducing resource demands and accelerating adaptation.

- **PEFT Method:** Based on the [PEFT](https://arxiv.org/pdf/1902.00751) framework, which allows for efficient fine-tuning.
- **LoRA (Low-Rank Adaptation):** Applied as described in the [LoRA](https://arxiv.org/pdf/2106.09685) paper. Configurations for LoRA are utilized to adjust the model effectively.
- **QLoRA (Quantized Low-Rank Adaptation):** Further optimization is achieved through quantization techniques as detailed in the [QLoRA](https://arxiv.org/pdf/2305.14314) paper. Bits-and-bytes configurations are used for this purpose.

## Fine-tuning Approaches for Classification
1. **Text Generation with Label Integration:**
   - **Input:** Instructions for text generation, including the text and corresponding label.
   - **Output:** The generated text includes the label.
  
2. **Linear Layer Addition:**
   - **Input:** Sentences (texts) are processed through the model.
   - **Output:** The model outputs the label corresponding to the input text.

## Model Used
- **Llama 3.1 8B-Instruct:** Used for the first method of fine-tuning.
- **Llama 3.1 8B:** Used for the second method of fine-tuning.

## Tokenizer
- **Tokenizer:** Hugging Face AutoTokenizer is used, employing Llama's BPE-based tokenizer built on SentencePiece.
- **Unigram Tokenizer:** Llama uses a variant of SentencePiece known as the Unigram Tokenizer, which is a subword tokenization algorithm.

## Training
- **Platform:** The model was trained using Lambda Labs cloud GPUs.

## Steps to Use
1. **Hugging Face Access:** Login to Hugging Face to access Llama models.
2. **Weights & Biases:** Login to Weights & Biases for monitoring training progress.
3. **Running the Model:** Execute the `hf-model` notebook and save the trained model.



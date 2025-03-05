import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def synthesize_speech(text, model_name="facebook/fastspeech2-en-ljspeech"):
    # Load pre-trained model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt")
    
    # Generate speech
    with torch.no_grad():
        generated_ids = model.generate(inputs["input_ids"])
    
    return generated_ids

if __name__ == "__main__":
    text = "Hello, this is a test."
    generated_speech = synthesize_speech(text)
    print(f"Generated Speech: {generated_speech}")

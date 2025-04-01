from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time

start_time = time.time()  # Record start time
# Your code here



# device = "mps" if torch.backends.mps.is_available() else "cpu"

# local_path = "Llama-2-7b-chat-hf" 

# model_name = "meta-llama/Llama-2-7b-chat-hf"  # Choose 7B, 13B, or 65B
# tokenizer = AutoTokenizer.from_pretrained(local_path)
# model = AutoModelForCausalLM.from_pretrained(local_path)



# from transformers import pipeline

# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]
# pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1", trust_remote_code=True, device='cpu')
# pipe(messages)

# from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
# import torch

# # Set device to MPS if available
device = "mps" if torch.backends.mps.is_available() else "cpu"

# # Load the model and tokenizer
model_name = "EleutherAI/pythia-70m"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map=device)

end_time = time.time()  # Record end time

print(f"Execution Time: {end_time - start_time:.4f} seconds")
print("Model loaded successfully!")

tokenizer.pad_token = tokenizer.eos_token

# Run inference
inputs = tokenizer("What is AI?", return_tensors="pt",padding=True, truncation=True)
# inputs = inputs.to(device)
outputs = model.generate(**inputs.to(device))
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

end_time2 = time.time()  # Record end time

print(f"Execution Time: {end_time2 - end_time:.4f} seconds")
print("Model loaded successfully!")


# # Create the pipeline
# pipe = pipeline("text-generation", model=model, trust_remote_code=True, tokenizer=tokenizer, device=device)

# # Example input
# messages = [{"role": "user", "content": "Who are you?"}]
# output = pipe(messages)
# print(output)

model.generate()
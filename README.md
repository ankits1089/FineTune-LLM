## Train a small LLM model to finetune of a document

### Dataset
Model should be finetuned to give response in QA format from the document "Good_and_Bad_Communication.pdf"
For training a set of question answer has been created from the above document.
Also, a set of questions are added to the above which does not relate to document. The answer to these question has been created as "Please let's keep our discussion related to good or bad communication."

### Finetune all the models parameters
Model : EleutherAI/pythia-70m
The above small parameter was trained on the QA.txt so that model can respond as per the doc.

The model was able to do a good job for questions not related to topic. For questions related to topic, the response were better than the base model. Below are a few examples

Q : "What is the larget lake?"  
**Finetuned model response**: "Please let's keep our discussion related to good or bad communication."
Base model response: "The answer is that the larget lake is a lake.  It"

Q: "How does defensiveness block productive conversation?"

Finetuned model response: "It creates a sense of empathy and empathy that can be shared with others. Does defensiveness block communication"
Base model response: "I think you're right.  I think you're right.  I"
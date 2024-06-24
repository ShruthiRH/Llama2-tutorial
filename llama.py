
from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/o8k5m0bfc8dj/Llama2Tutorial/workflows/workflow-e029c0"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="88b79d5c8c5d4768827c981fda72bad5"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)
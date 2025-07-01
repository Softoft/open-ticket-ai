---
description: Review the API for pipe implementations. See
  the developer guide's "How to Add a Custom Pipe" section for
  step-by-step instructions on creating your own pipe classes.
---
# Documentation for `**/ce/run/pipe_implementations/*.py`

## Module: `open_ticket_ai\src\ce\run\pipe_implementations\ai_text_model_input.py`


### <span style='text-info'>class</span> `TextAIModelInput`

Context for the input to the Hugging Face inference service.
This class is used to encapsulate the input data and any additional parameters
required for the inference request.

**Parameters:**

- **`ai_model_input`** (`str`) - The input text provided to the AI model for processing.
Represents the primary data payload for the inference request.


---

## Module: `open_ticket_ai\src\ce\run\pipe_implementations\empty_data_model.py`


### <span style='text-info'>class</span> `EmptyDataModel`

Empty Pydantic model without any fields.
This model serves as a placeholder for scenarios requiring a Pydantic-compatible
object but without any data fields. It can be used as a base class or type hint
when no specific data structure is needed.


---

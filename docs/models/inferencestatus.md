# InferenceStatus

## Example Usage

```python
from flypix.models import InferenceStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: InferenceStatus = "CREATED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"CREATED"`
- `"STARTED"`
- `"FAILED"`
- `"PROCESSED"`
- `"FINISHED"`

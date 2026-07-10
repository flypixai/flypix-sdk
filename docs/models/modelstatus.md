# ModelStatus

## Example Usage

```python
from flypix.models import ModelStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ModelStatus = "CREATED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"CREATED"`
- `"TRAINING"`
- `"TRAINED"`

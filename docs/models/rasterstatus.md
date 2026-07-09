# RasterStatus

## Example Usage

```python
from flypix.models import RasterStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RasterStatus = "CREATED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"CREATED"`
- `"PROCESSING"`
- `"FAILED"`
- `"PROCESSED"`

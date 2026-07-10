# FileType

## Example Usage

```python
from flypix.models import FileType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: FileType = "IMAGE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"IMAGE"`
- `"RASTER"`
- `"GEOTIFF"`
- `"UNSUPPORTED"`
- `"UNKNOWN"`

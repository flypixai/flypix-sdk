# Reason

## Example Usage

```python
from flypix.models import Reason

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Reason = "EMPTY_PLAN_ACTIVATION"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"EMPTY_PLAN_ACTIVATION"`
- `"FREE_PLAN_ACTIVATION"`
- `"CREDIT_PURCHASE"`
- `"SUBSCRIPTION_ACTIVATION"`
- `"BONUS_CREDITS"`
- `"MODEL_TRAINING"`
- `"INFERENCE"`
- `"SPECIAL_OFFER"`
- `"REFUND"`

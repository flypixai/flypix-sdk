# GetInferencesForProjectRequest


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `filter_`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Comma-separated field:operator:value clauses, e.g. status:eq:FAILED |
| `sort`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Comma-separated field:asc\|desc clauses, e.g. created_at:desc       |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
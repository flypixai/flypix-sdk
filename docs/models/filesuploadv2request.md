# FilesUploadV2Request


## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `tenant_id`                          | *str*                                | :heavy_check_mark:                   | N/A                                  |
| `project_id`                         | *str*                                | :heavy_check_mark:                   | N/A                                  |
| `folder_id`                          | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  |
| `filename`                           | *str*                                | :heavy_check_mark:                   | N/A                                  |
| `content_length`                     | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  |
| `body`                               | *Union[bytes, IO[bytes], io.IOBase]* | :heavy_check_mark:                   | N/A                                  |
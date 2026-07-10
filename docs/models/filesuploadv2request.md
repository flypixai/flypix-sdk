# FilesUploadV2Request


## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `tenant_id`                          | *UUID*                               | :heavy_check_mark:                   | N/A                                  |
| `project_id`                         | *UUID*                               | :heavy_check_mark:                   | N/A                                  |
| `folder_id`                          | *OptionalNullable[UUID]*             | :heavy_minus_sign:                   | N/A                                  |
| `filename`                           | *str*                                | :heavy_check_mark:                   | N/A                                  |
| `body`                               | *Union[bytes, IO[bytes], io.IOBase]* | :heavy_check_mark:                   | N/A                                  |
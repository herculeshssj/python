# Send files to MinIO

**Command**

```sh
python manage.py send-to-minio --config <config_file> --file <file_to_send> --keep <n>
```

**Parameters**

`--config` : path to MinIO config file
`--file` : filename to send to MinIO
`--keep` : keep `n` files on bucket, 0 do not remove any file
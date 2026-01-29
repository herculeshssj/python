The database dump is in Nextcloud, in the n8n folder.

Restore database after downloaded:

```sh
docker run --rm --net=host -e PGPASSWORD='py@pr0j3cts' -v "$PWD":/backup postgres:17 pg_restore -U pyprojects -h 127.0.0.1 -W -v -c --if-exists -O -d db_ric /backup/dbstage-ric.backup
```
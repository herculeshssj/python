### Installation

Install dependencies:

```
python -m pip install -r requirements.txt
```

### Configuration

Create or configure the Oracle Cloud credentials file at `~/.oci/config`. Example:

```
[DEFAULT]
user=ocid1.user.oc1...
fingerprint=xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx
key_file=~/.oci/oci_api_key.pem
tenancy=ocid1.tenancy.oc1...
region=us-phoenix-1
```

### Environment Variables

Set the following environment variables:

```
export OCI_CONFIG_FILE=~/.oci/config
export OCI_CONFIG_PROFILE=DEFAULT
export OCI_NAMESPACE=your-namespace
export OCI_BUCKET=your-bucket-name
```

Or use the provided `envfile`:

```
OCI_CONFIG_FILE=~/.oci/config
OCI_CONFIG_PROFILE=DEFAULT
OCI_NAMESPACE=your-namespace
OCI_BUCKET=your-bucket-name
```

### Docker build:

```
docker build -t send-backup-oracle:latest .
```

### Docker run:

```
docker run --rm --env-file=envfile -v "$PWD":/data -v ~/.oci:/root/.oci send-backup-oracle:latest python send-backup-to-oracle.py teste.txt --keep
```

Parameters:
- --keep - keep the oldest file in the bucket
- --nokeep - delete the oldest file from the bucket

### Warning

If your environment has more than one Docker network created, build the image with the --network=host parameter.

```
docker build --network=host -t send-backup-oracle:latest .
```
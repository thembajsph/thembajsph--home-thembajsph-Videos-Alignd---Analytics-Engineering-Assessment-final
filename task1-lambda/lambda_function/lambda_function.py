
import boto3
import pyarrow.parquet as pq
import pandas as pd
import io
import os

s3 = boto3.client('s3')


def lambda_handler(event, context):
    # Get the bucket and key from the S3 event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Only process .parquet files
    if not key.endswith('.parquet'):
        return {
            'statusCode': 400,
            'body': 'Not a Parquet file'
        }

    # Download the Parquet file to Lambda tmp directory
    local_file = '/tmp/temp.parquet'
    s3.download_file(source_bucket, key, local_file)

    # Read Parquet file
    table = pq.read_table(local_file)
    df = table.to_pandas()

    # Convert to CSV
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)

    # Upload to destination bucket
    destination_bucket = 'processed-bucket-analytics'
    destination_key = os.path.splitext(key)[0] + '.csv'

    s3.put_object(
        Bucket=destination_bucket,
        Key=destination_key,
        Body=csv_buffer.getvalue()
    )

    return {
        'statusCode': 200,
        'body': f'Successfully converted {key} to CSV'
    }

# processed-bucket-analytics

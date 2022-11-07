import boto3
import creds
ACCESS_KEY = creds.Access_Key
SECRET_KEY = creds.Secret_Key
session = boto3.Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
dynamoDB = session.resource('dynamodb', region_name='ap-south-1')


def create_table():
    """create the Table."""
    table = dynamoDB.create_table(
        TableName='employee',
        KeySchema=[
            {
                'AttributeName': 'empId',
                'KeyType': 'HASH'  # partition key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'empId',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        },
    )
    print('Table Status', table.table_status)


def delete_table():
    """Delete the Table."""
    table = dynamoDB.Table('employee')
    table.delete()


def main():
    create_table()
    delete_table()


if __name__ == '__main__':
    main()

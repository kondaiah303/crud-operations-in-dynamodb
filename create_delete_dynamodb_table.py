import boto3
ACCESS_KEY = 'AKIAQ7JFMHWTDI6YWU4G'
SECRET_KEY = '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'
session = boto3.Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
dynamoDB = session.resource('dynamodb', region_name='ap-south-1')


""""create the Table"""


def create_table():
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


""""Delete the Table"""


def delete_table():
    table = dynamoDB.Table('employee')
    table.delete()


def main():
    create_table()
    delete_table()


if __name__ == '__main__':
    main()
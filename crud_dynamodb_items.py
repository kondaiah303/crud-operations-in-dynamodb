import boto3
dynamoDB = boto3.resource('dynamodb', region_name='ap-south-1')


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

import boto3
dynamoDB = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamoDB.Table('student')


def get_data():
    """Read the Items."""
    print('Retrieving the data')
    student_id = int(input('enter the id number: '))
    try:
        res = table.get_item(
            Key={
                'SID': student_id
            }
        )
        print(res['Item'])
    except KeyError:
        print('Give a proper key value')


def put_data():
    """Insert the Items."""
    print('inserting the data')
    student_id = int(input('enter the id: '))
    student_name = input('enter the name: ')
    student_age = int(input('enter the age: '))
    student_address = input('enter the student address: ')
    table.put_item(
        Item={
            'SID': student_id,
            'SNAME': student_name,
            'SAGE': student_age,
            'SADDRESS': student_address
        }
    )


def update_data():
    """update the Items."""
    print('updating the data')
    student_id = int(input('enter the id number: '))
    student_name = input('enter the name: ')
    student_age = int(input('enter the age: '))
    res = table.update_item(
        Key={
            'SID': student_id
        },
        UpdateExpression="SET SNAME= :S, SAGE= :S1",
        ExpressionAttributeValues={
            ':S': student_name,
            ':S1': student_age
        },
        ReturnValues='UPDATED_NEW'
    )

    print(res['Attributes'])


def delete_data():
    """Delete the Items."""
    print('deleting the data')
    student_id = int(input('enter the id number: '))
    table.delete_item(
        Key={
            'SID': student_id
        }
    )


def main():
    get_data()
    put_data()
    update_data()
    delete_data()


if __name__ == '__main__':
    main()

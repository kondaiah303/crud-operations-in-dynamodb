import boto3
ACCESS_KEY = 'AKIAQ7JFMHWTDI6YWU4G'
SECRET_KEY = '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'
session = boto3.Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
dynamoDB = session.resource('dynamodb', region_name='ap-south-1')
table = dynamoDB.Table('student')


""""Read the Items"""


def get_data():
    res = table.get_item(
        Key={
            'SID': 101
        }
    )
    return res['Item']


""""Insert the Items"""


def put_data():
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


""""update the Items"""


def update_data():
    student_name = input('enter the name: ')
    student_age = int(input('enter the age: '))
    res = table.update_item(
        Key={
            'SID': 101
        },
        UpdateExpression="SET SNAME= :S, SAGE= :S1",
        ExpressionAttributeValues={
            ':S': student_name,
            ':S1': student_age
        },
        ReturnValues='UPDATED_NEW'
    )
    return res['Attributes']


""""Delete the Items """


def delete_data():
    table.delete_item(
        Key={
            'SID': 102
        }
    )


def main():
    print(get_data())
    put_data()
    print(update_data())
    delete_data()


if __name__ == '__main__':
    main()

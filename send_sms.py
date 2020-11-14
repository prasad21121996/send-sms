from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hi This is test msg",
                     from_='',
                     to=''
                 )

print(message.sid)
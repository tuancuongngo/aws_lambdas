import json
import boto3
from datetime import datetime

# cron = cron (30 12 1,6,19,21 * ? *) Runs at 8:30am on those days monthly
# aws lambda name: dequincey-reminder

current_datetime = datetime.now()
curr_date = current_datetime.day
curr_month = current_datetime.strftime("%B")

#print(f'Date is {curr_date} and month: {curr_month}')

def get_subject():
    if curr_date == 1:
            return f'First day of {curr_month}. Check utilities!'
    elif curr_date == 6:
        return f'New month: {curr_month}. Have you checked utilities?'
    elif curr_date == 19:
        return f'Arij rent reminder {curr_month} {curr_date} [{current_datetime}]'
    elif curr_date == 21:
        return f'Haemoon rent reminder {curr_month} {curr_date} [{current_datetime}]'
    else:
        return f'New month: {curr_month}. Have you checked utilities?'

def get_message():
    intro = ''
    
    if curr_date == 1:
        intro = "New month. Let's be PRODUCTIVE and crush your GOALS"
    elif curr_date == 6:
        intro = "Stay on track brother. It will be worth it. WORK HARD"
    else:
        intro = "Let's finish off the month STRONG. Work HARD"
        
    message = f'''
        {intro}
        
        Electricity monthly (add $1.65): https://login.dominionenergy.com/CommonLogin?SelectedAppName=Electric
        
        Water on Jan, April, July, October (add $4.25): https://fwcustomer.org/
        
        Waste on 1st of Feb, May, August, November: https://myaccount.wcicustomer.com/district/6319
        
        Note: Water uses vt email. Electricity and waste use regular email. LETS HAVE A PRODUCTIVE MONTH!
        
        From: Past Cuong on Sunday 06/09/2024.
        
        P.s I hope your current self is doing good, and making progress with your goals. Keep working HARD and your future self will thank you
        
        [AWS acount created on 06/09/2024. Ends in 1 year time]
    '''
    
    if curr_date == 19:
        message = f'''
            Remind Arij for rent.
        '''
    elif curr_date == 21:
        message = f'''
            Remind Haemoon for rent.
        '''
    return message


def lambda_handler(event, context):
    sns = boto3.client('sns');
    topic_arn = 'arn:aws:sns:us-east-2:381491982658:Utilities-Dequincey'
    subject = get_subject()
    message = get_message()
    
    #print(subject)
    #print(message)
    
    response = sns.publish(
        TopicArn=topic_arn,
        Subject=subject,
        Message=message
    )
    
    print(f'Response: {response}')
    
    return response


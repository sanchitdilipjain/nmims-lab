from __future__ import division
import json

def lambda_handler(event, context):
   
   print(event)
   if 'Records' in event:
      message = json.loads(event['Records'][0]['body'])
      number1 = message['Number1']
      number2 = message['Number2']
   elif 'body' in event:
      message = json.loads(event['body'])
      number1 = message['Number1']
      number2 = message['Number2']
   else:
      number1 = event['Number1']
      number2 = event['Number2']
   
   sum = number1 + number2
   product = number1 * number2
   difference = abs(number1 - number2)
   quotient = number1 / number2
   return {
       "statusCode": 200,
       "Number1": number1,
       "Number2": number2,
       "Sum": sum,
       "Product": product,
       "Difference": difference,
       "Quotient": quotient
   }

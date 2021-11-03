import requests
import random
import time

'''
1. Gather User Information
    channel_list
    create list of User() objects
        tokens
    delay
    message count
2. Using a for loop iterate through the message_count
      for object in object_list 
         object.send_messages()
'''
def use_bot():
  message_list = ['hello', 'herro']
  class User():
      def __init__(self, token):
          self.token = token

      def send_message(self, channel_id, message):
          url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
          data = {"content": message}
          header = {"authorization": self.token}

          r = requests.post(url, data=data, headers=header)
          print(r.status_code)

      def send_messages(self):
          for channel in channel_list:
              self.send_message(channel, random.choice(message_list))

  channel_list = []
  object_list = []

  for i in range(int(input("How many channels do you want to send to? :"))):
      channel_list.append(int(input("Input Channel_{}_id :".format(i + 1))))

  for i in range(1, int(input("How many discord accounts do you have? :")) + 1):
      token = input("What is the discords token? :")
      object_list.append(User(token))

  delay = int(input("What is the higher channel cooldown? : "))
  message_count = int(input("How many messages do you want to send? : "))

  for message in range(message_count):
      for object in object_list:
          object.send_messages()
      time.sleep(delay)
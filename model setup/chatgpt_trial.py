import os
from openai import OpenAI

client = OpenAI(api_key="API KEY HERE")

# client.files.create( 
#   file=open("testdata.jsonl", "rb"),
#   purpose="fine-tune"
# )

# client.fine_tuning.jobs.create(
#   training_file="file-tq8t0d9GCu9j8GUTA5aWNe7c", 
#   model="gpt-3.5-turbo"
# )

# print(client.fine_tuning.jobs.retrieve("ftjob-mLrhfv81l3vNczT1HdPcdCr4"))

# ft_file = client.files.retrieve("file-FfRnylEKSB5OYyUK10rYRboa")
# for line in ft_file:
#     print(line)

def assistant():
  message_list = [{"role": "system", "content": "You are a medical learning assistant, skilled in explaining complex medical concepts to teach medical students."}]
  
  while True:
      message = input("User:")
      message_list.append({"role": "user", "content": message})


      completion = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:seniorprojectrd::9ZDqFLbU",
        messages=message_list
      )
      response = completion.choices[0].message.content
      message_list.append({"role": "assistant", "content": response})

      print("ChatGPT:", response)


assistant()
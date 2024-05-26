from openai import OpenAI
from Prompts import prompt_content
from datetime import datetime

client = OpenAI()

LANGUAGE = "Simplified Chinese"

# conversation = [
#     {"role": "system", "content": f"You are to converse like a human and reply me in {LANGUAGE} language," +
#     " Do not speak more than 2 sentences long." + 
#     "There are times where I may use a mixture of english and chinese in my input, please interpret it accordingly." +
#     "Make sure to keep the conversation flowing." + 
#     "This means always ending in a question or a statement that invites a response."},
# ]


def llm_run(input):
    conversation = [
        {"role": "system", "content": f"{prompt_content}"},
    ]
    current_convo = update_conversation(input)
    conversation = conversation + current_convo
    gpt_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=200
    )
    gpt_output = gpt_response.choices[0].message.content
    print(gpt_output)
    return gpt_output


def update_conversation(latestMessages):
    current_convo = []
    sortedMessages = sorted(latestMessages, key=lambda x: datetime.strptime(x['createdAt'], "%Y-%m-%dT%H:%M:%S.%fZ"))
    for message in sortedMessages:
        if (message['user']['_id'] == 0):
            combined_string = '\n'.join([message['text'], message['romanization'], message['translation']])
            current_convo.append({"role": "system", "content": combined_string})
        else:
            current_convo.append({"role": "user", "content": message['text']})
    return current_convo
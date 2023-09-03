import open_ai_api as gpt

#step 1: Give a Topic
user_topic = input("Please give your video topic: ")
user_minutes = input("Please enter your video length (in minutes): ")
user_context = input("Please type in the speech:")


video_title_gprompt = """Please act as a viral short video title creator. 
Come up with 5 titles about {topic} that are short, concise, fun, and attention-grabbing. 
"""

titles_prompt = video_title_gprompt.format(topic=user_topic)
titles = gpt.basic_generation(titles_prompt)
print("Titles: ")
print(titles)

video_script_prompt = """Act as a professional short video script writer. 
Read the speech: [{speech}].
Create an engaging script with a timeline for a {minutes} minute video on the topic [{topic}]. 
Use a narrative format. Be engaging, honest, and capative for people to watch and share.
"""
script_prompt = video_script_prompt.format(minutes=user_minutes,topic=user_topic, speech=user_context)
script = gpt.basic_generation(script_prompt)
print("Script: ")
print(script)

tweet_prompt = """Act as a social media expert. 
Create a 5 tweet thread based on the follwing script : {transcript}. 
The thread should be optimised for virality and contain hashtag consistent through the thread"""

tweet_prompt = tweet_prompt.format(transcript=script)
tweet = gpt.basic_generation(tweet_prompt)
print("Twitters: ")
print(tweet)

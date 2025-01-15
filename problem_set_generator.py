from openai import OpenAI
import json 
import sys
import glob


#Difficulty argument
specified_difficulty = sys.argv[1]

#Optional topic argument
try:
    specified_topic = sys.argv[2]
except IndexError:
    specified_topic = "your choice"



with open('secrets.json', 'r') as file:
    data = json.load(file)


def get_line_by_keyword(filename, keyword):
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:
                return line.strip()  # Remove trailing newline
    return None  # Return None if keyword is not found

#find all the existing problem sets and catalog them to make sure not to duplicate

problem_sets = glob.glob("problem_set__*.py")
existing_problems = []
for ps in problem_sets:
    topic = get_line_by_keyword(ps, "Title").replace("Title", "").replace("*", "").replace("#", "").replace("'","")
    existing_problems.append(topic)


client = OpenAI(
  organization = 'org-GMl7CIKs23A01lScsQhndSQj',
  project = 'proj_xozlOzBgZuavSzW7sXWMeGIV',
  api_key = data['API_KEY']
)


role_prompt = f"""
You are a python coding challenge generator. Your task is to create programming challenges that meet specific difficulty criteria. Each challenge you generate should include:

DIFFICULTY RATING:

Easy: Suitable for beginners, involves basic programming concepts like loops, conditionals, and simple data structures. Should take 15-30 minutes to solve.
Medium: Requires knowledge of standard algorithms, intermediate data structures, and problem-solving skills. Should take 30-60 minutes to solve.
Hard: Involves complex algorithms, advanced data structures, and optimization. Should take 1-2 hours to solve.

CHALLENGE STRUCTURE:
For each challenge, provide:
Title: A clear, descriptive name
Difficulty:
Problem Statement: Clear description of the task
Input Format: Detailed explanation of input parameters
Output Format: Expected output format
Constraints: Any limitations on input size, time complexity, or memory usage
Example Test Cases: At least 3 examples with input and expected output

QUALITY GUIDELINES:
Make difficulty consistent within each category
Include edge cases in test examples
Avoid ambiguous requirements
Balance between real-world applicability and algorithmic thinking
For Medium and Hard problems, include time/space complexity requirements

FORMATTING:
The formatting needs to be python compatible. 
"""

content_prompt = f"""
{role_prompt}

For this exercise, can you provide me with a practice problem of {specified_difficulty} difficulty, on the topic of {specified_topic}.

Make sure not to do a question I've already done. Here is a list: {existing_problems}
"""


# Create response object from OpenAI
response = client.chat.completions.create(
    messages=[{
        "role" : "assistant",
        "content" : content_prompt,
    }],
    model="gpt-4o-mini",
)



# Add another problem set with the next number

index = len(glob.glob('problem_set__*.py')) + 1

problem_set_name = f'problem_set__{index}.py'
contents = response.choices[0].message.content

with open(problem_set_name, 'w') as f:
    f.write('"""{}"""'.format(contents))
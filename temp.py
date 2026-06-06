# temp_generator.py

from generator import generate_answer

context = """
Metadata is data about data.
It is stored in the data dictionary.
"""

question = "What is metadata?"

print(generate_answer(context, question))
from django.shortcuts import render
import openai
import os
import json
#$env:OPENAI_API_KEY="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"

# OPENAI_API_KEY = "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"
#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

openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)
def generate_response(prompt):
    
    messages = [
        {"text": prompt, "user": "user"},
        {"text": "", "user": "AI"}
    ]
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=json.dumps(messages),
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def book_summary(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        prompt = f"Summarize the book '{book_name}' in 500 words or less."
        summary = generate_response(prompt)
        return render(request, 'book_summary.html', {'summary': summary})
    else:
        return render(request, 'book_summary.html')

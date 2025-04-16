from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import requests

TOGETHER_API_KEY = "cbd3961a8bd64ecfe9e7b6dc7532aaecd64bf220273c9308a6ea611a3e210d1e"  # Replace with your key
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"  # You can also try Mixtral etc.

@csrf_exempt
def chat(request):
    response = ""
    if request.method == "POST":
        user_input = request.POST.get("user_input")

        if user_input:
            headers = {
                "Authorization": f"Bearer {TOGETHER_API_KEY}",
                "Content-Type": "application/json"
            }

            data = {
                "model": MODEL_NAME,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful personal finance assistant. Answer user questions with smart, practical financial advice."
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 512
            }

            try:
                res = requests.post(TOGETHER_API_URL, headers=headers, json=data)
                res_data = res.json()

                if res.status_code == 200:
                    response = res_data["choices"][0]["message"]["content"].strip()
                else:
                    response = f"Error: {res_data.get('error', 'Something went wrong')}"
            except Exception as e:
                response = f"Error: {str(e)}"

    # return redirect('chat')
    return render(request, "chatbot/chat.html", {"response": response})

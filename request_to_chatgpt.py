import os

import openai

# APIキーの設定
openai.api_key = os.environ["OPENAI_API_KEY"]


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "UnityとChatGPTを組み合わせて、アプリを作りたいです。Twitterでバズりそうなアプリを５個考えて、概要案を100文字程度で教えて。その後に、それぞれの概要案に関して理由とマネタイズ方法を箇条書きでそれぞれ3個ずつ書いてください",
        },
    ],
)
print(response.choices[0]["message"]["content"].strip())

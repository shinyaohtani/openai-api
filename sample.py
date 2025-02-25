from openai import OpenAI

order = """
短歌を読んでください。短歌は季語が必要なのできちんと季語を入れてください。

明日2月26日は妻と交際を開始した交際記念日です。29回目です。
短歌は29回目であることを引用してください。
'二十九年'は日本語では7音節です。5-7-5-7-7の形にしてください。
それぞれのブロックの右側に音節数を記載してください。
'二十九年'は日本語では7音節です。絶対に間違えないでください。
歳は私が48才、妻が49歳です。他に聞きたいことはありますか。
"""
msgs = [
    {
        "role": "system",
        "content": "あなたは非常に短くスマートな回答するコンシェルジュです",
    },
    {
        "role": "user",
        "content": order,
    },
]
print(order)

client = OpenAI()
completion = client.chat.completions.create(model="gpt-4o", messages=msgs)
message_content = completion.choices[0].message.content
formatted_message = message_content.replace("\\u3000", " ").replace("\\n", "\n")
print(f"短歌:\n{formatted_message}")

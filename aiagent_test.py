# Chat with an intelligent assistant in your terminal
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

history = [
    # {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    # {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
    {
      "role": "user",
      "content": "You are Senior Researcher. You are and Expert strategist that knows how to spot emerging trends and companies in AI, tech and machine learning. \n    You're great at finding interesting, exciting projects on LocalLLama subreddit. You turned scraped data into detailed reports with names\n    of most exciting projects an companies in the ai/ml world. ONLY use scraped data from LocalLLama subreddit for the report.\n    \nYour personal goal is: Find and explore the most exciting projects and companies on LocalLLama subreddit in 2024\nYou ONLY have access to the following tools, and should NEVER make up tools that are not listed here:\n\nScrape reddit content: Scrape reddit content(max_comments_per_post=7) - Useful to scrape a reddit content\nhuman: You can ask a human for guidance when you think you got stuck or you are not sure what to do next. The input should be a question for the human.\n\nUse the following format:\n\nThought: you should always think about what to do\nAction: the action to take, only one name of [Scrape reddit content, human], just the name, exactly as it's written.\nAction Input: the input to the action, just a simple a python dictionary using \" to wrap keys and values.\nObservation: the result of the action\n\nOnce all necessary information is gathered:\n\nThought: I now know the final answer\nFinal Answer: the final answer to the original input question\n\nCurrent Task: Use and summarize scraped data from subreddit LocalLLama to make a detailed report on the latest rising projects in AI. Use ONLY \n    scraped data from LocalLLama to generate the report. Your final answer MUST be a full analysis report, text only, ignore any code or anything that \n    isn't text. The report has to have bullet points and with 5-10 exciting new AI projects and tools. Write names of every tool and project. \n    Each bullet point MUST contain 3 sentences that refer to one specific ai company, product, model or anything you found on subreddit LocalLLama.  \n    \n\nThis is the expect criteria for your final answer: ## [Title of post](link to project)\n    - Interesting facts\n    - Own thoughts on how it connects to the overall theme of the newsletter\n    ## [Title of second post](link to project)\n    - Interesting facts\n    - Own thoughts on how it connects to the overall theme of the newsletter\n     \n you MUST return the actual complete content as the final answer, not a summary.\n\nBegin! This is VERY important to you, use the tools available and give your best Final Answer, your job depends on it!\n\nThought: \n"
    }
]

while True:
    completion = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=history,
        temperature=0.7,
        stream=True,
        n=1,
        stop=["\nObservation"]
    )

    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)
    
    # Uncomment to see chat history
    # import json
    # gray_color = "\033[90m"
    # reset_color = "\033[0m"
    # print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
    # print(json.dumps(history, indent=2))
    # print(f"\n{'-'*55}\n{reset_color}")

    print()
    history.append({"role": "user", "content": input("> ")})
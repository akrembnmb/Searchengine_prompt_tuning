from openai import OpenAI
# Set your OpenAI API key
client = OpenAI(api_key="env_key")


def evaluate_results(data):
    evaluations = []
    
    for item in data:
        question = item["question"]
        prompt_tuning_result = item["prompt_tuning_result"]
        prompt_engineering_result = item["prompt_engineering_result"]
        
        prompt = (
            f"You are a judge model that evaluates the performance of two techniques: 'prompt tuning' and 'prompt engineering'.\n"
            f"Question: {question}\n"
            f"Prompt Tuning Result: {prompt_tuning_result}\n"
            f"Prompt Engineering Result: {prompt_engineering_result}\n"
            f"Which result is better? Provide the label 1 if the prompt engineering is better and -1 if not."
        )
        
        response = client.chat.completions.create(
            model="gpt-4o",
            prompt=prompt,
            max_tokens=1
        )
        
        evaluation = response.choices[0].text
        evaluations.append(evaluation)
        
    return evaluations

results = evaluate_results("test\eval_sample.json")

print(results)

print("prompt_engineering",results.count("1"))
print("prompt_tuning",results.count("-1"))

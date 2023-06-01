import openai

openai.api_key = "API KEY" #Open AI API Key to make requests 

def generate_response(email, optionalInformation=None):
    prompt = f"Your email: {email}"
    if optionalInformation:
        prompt += f"\nOptional information to put in email: {optionalInformation}"\
        
    prompt += "\nOpenAI's response:"
    
    model = "text-davinci-003"
    
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
       max_tokens=1000, #Max email length 
        n=1, #Will generate one email responce
        stop=None, #Parameter specifies no stop sequence
        temperature=0.7, #Tempature of 0.7 chosen to prevent text from sounding robotic, but also remaining professional
    )
    
    return response.choices[0].text.strip()

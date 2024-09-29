#from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser

application_prompt = """Given the following topic description
              write 3 attention-grabbing headlines for an article.
                Reply only with the titles, one on each line, with no additional text.
                DESCRIPTION: {user_input}"""
user_input = "The Importance of the Earthworm"

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="no-needed",
    model="local-model",
    max_tokens=64,
    temperature=0.8,
)

prompt = PromptTemplate(
    input_variables=["user_input"],
    template=application_prompt
)

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"user_input": user_input})

print(result, end="\n------------\n")
print(prompt.output_schema, end="\n------------\n")
print(llm.input_schema)

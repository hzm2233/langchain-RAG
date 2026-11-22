from langchain_core.prompts import ChatPromptTemplate

FRIENDLY_ASSISTANT = ChatPromptTemplate.from_messages([
      ("system", " 你是一个友好的助手 "),
      ("user", "{input}")
])

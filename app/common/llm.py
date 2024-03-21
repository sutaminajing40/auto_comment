from langchain_community.llms.bedrock import Bedrock
from langchain_openai import ChatOpenAI

# # Bedrockのインスタンスを作成し、Claude3モデルを指定
# claude_llm = Bedrock(
#     credentials_profile_name="bedrock-admin",  # AWSの認証情報プロファイル名
#     model_id="amazon.claude3"  # Claude3モデルのID
# )

# モデルを指定してインスタンスを作成
openai_chat = ChatOpenAI(model="gpt-3.5-turbo")

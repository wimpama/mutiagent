from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST_sample",file_location=r"E:\DEV\code\muti")
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy",human_input_mode="NEVER", code_execution_config={"work_dir": "coding","use_docker":True})
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")

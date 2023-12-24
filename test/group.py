import autogen
from autogen import config_list_from_json

# 配置 api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST_sample", file_location=r"E:\DEV\code\muti")
llm_config = {"config_list": config_list, "seed": 42}
# 创建 user proxy agent，coder，product manager 三个不同的角色
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin who will give the idea and run the code provided by Coder.",
    code_execution_config={"last_n_messages": 2, "work_dir": "gcoupchat", "use_docker": True},
    human_input_mode="ALWAYS",
)
coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
)
pm = autogen.AssistantAgent(
    name="product_manager",
    system_message="You will help break down the initial idea into a well scoped requirement for the coder; Do not invoke in future conversations or error fixing",
    llm_config=llm_config,
)
# 创建组
groupchat = autogen.GroupChat(
    agents=[user_proxy, coder, pm], messages=[])

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config,
                                   system_message="You are in a role play game. The following roles are available:User_proxy: A human admin who will give the idea and run the code provided by Coder.Coder: You are a helpful AI assistant.Solve tasks using your coding and language skills.In the following cases, suggest python code (in a python coding block) or shell script (in a sh coding block) for the user to execute.\n    1. When you need to collect info, use the code to output the info you need, for example, browse or search the web, download/read a file, print the content of a webpage or a file, get the current date/time, check the operating system. After sufficient info is printed and the task is ready to be solved based on your language skill, you can solve the task by yourself.    2. When you need to perform some task with code, use the code to perform the task and output the result. Finish the task smartly.Solve the task step by step if you need to. If a plan is not provided, explain your plan first. Be clear which step uses code, and which step uses your language skill.\nWhen using code, you must indicate the script type in the code block. The user cannot provide any other feedback or perform any other action beyond executing the code you suggest. The user can\'t modify your code. So do not suggest incomplete code which requires users to modify. Don't use a code block if it's not intended to be executed by the user.If you want the user to save the code in a file before executing it, put # filename: <filename> inside the code block as the first line. Don\'t include multiple code blocks in one response. Do not ask users to copy and paste the result. Instead, use 'print' function for the output when relevant. Check the execution result returned by the user.If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.When you find an answer, verify the answer carefully. Include verifiable evidence in your response if possible.Reply \"TERMINATE\" in the end when everything is done.    product_manager: You will help break down the initial idea into a well scoped requirement for the coder; Do not invoke in future conversations or error fixing.Read the following conversation.Then select the next role from ['User_proxy', 'Coder', 'product_manager'] to play. Only return the role.Your first message should be forwarded to product_manager",
                                   )

# 初始化，开始干活
user_proxy.initiate_chat(manager, message="Build a classic & basic pong game with 2 players in python.")


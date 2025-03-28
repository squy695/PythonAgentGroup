from agent_network.base import BaseAgent
from agent_network.exceptions import ReportError
import os
import agent_network.graph.context as ctx


# python代码生成
class python_agent(BaseAgent):
    def __init__(self, graph, config, logger):
        super().__init__(graph, config, logger)

    def forward(self, messages, **kwargs):
        python_generate_request = kwargs.get("task")
        if not python_generate_request:
            raise ReportError("python generate request is not provided", "python_agent")
        
        from openai import OpenAI
        
        api_key, base_url, model = "sk-ca3583e3026949299186dcbf3fc34f8c", "https://api.deepseek.com", "deepseek-chat"
        
        client = OpenAI(api_key=api_key, base_url=base_url)        
        response = client.chat.completions.create(
            model = model,
            messages = [
                {"role": "system", "content": "你是一个Python编程的专家，请用简洁的语言回答用户的问题。"},
                {"role": "user", "content": "现有如下请求，请编写python代码解决。\n" + python_generate_request},
            ],
            stream = False
        )
        
        python_generate_result = response.choices[0].message.content        
        self.log("assistant", python_generate_result)
        result = {
            "result": response.choices[0].message.content
        }
        return result
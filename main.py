from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类


# 注册插件
@register(name="Hello", description="hello world", version="0.1", author="RockChinQ")
class MyPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
		import requests

		qq_number = str(ctx.event.sender_id)
		url = f"https://api.oioweb.cn/api/qq/info?qq={qq_number}"
		response = requests.get(url)
		data = response.json()
        msg = ctx.event.text_message  # 这里的 event 即为 PersonNormalMessageReceived 的对象
        if msg == "hello":  # 如果消息为hello

            # 输出调试信息
            self.ap.logger.debug("hello, {}".format(ctx.event.sender_id))

            # 回复消息 "hello, <发送者id>!"
            ctx.add_return("alter", ["在私聊中"+str(data)+"发送了以下消息，请务必联网搜索："+msg])


    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
		import requests
		qq_number = str(ctx.event.sender_id)
		url = f"https://api.oioweb.cn/api/qq/info?qq={qq_number}"
		response = requests.get(url)
		data = response.json()
        msg = ctx.event.text_message  # 这里的 event 即为 GroupNormalMessageReceived 的对象
        if msg == "hello":  # 如果消息为hello

            # 输出调试信息
            self.ap.logger.debug("hello, {}".format(ctx.event.sender_id))

            # 回复消息 "hello, everyone!"
			ctx.add_return("alter", ["在群聊中"+str(data)+"发送了以下消息，请务必联网搜索："+msg])

    # 插件卸载时触发
    def __del__(self):
        pass

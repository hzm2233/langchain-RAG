# main.py
# 直接从这个文件夹导入，这是因为有 __init__.py 文件
from templates.common import FRIENDLY_ASSISTANT
import pprint

print("--- 测试翻译模板 ---")
# 填入参数
prompt_value = FRIENDLY_ASSISTANT.invoke({"input": "英语",

})
pprint.pp(prompt_value)

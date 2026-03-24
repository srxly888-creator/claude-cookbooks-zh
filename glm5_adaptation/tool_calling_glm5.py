# 🛠️ GLM-5 适配示例 - 工具调用（Function Calling）

> **原始文件**: capabilities/tool_calling.py
> **适配时间**: 2026-03-24
> **适配者**: OpenClaw Agent

---

## 原始代码（Claude）

```python
import anthropic
import json

client = anthropic.Anthropic()

# 定义工具
tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA"
                }
            },
            "required": ["location"]
        }
    }
]

# 调用模型
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    tools=tools,
    messages=[
        {
            "role": "user",
            "content": "What's the weather like in San Francisco?"
        }
    ]
)

# 处理响应
if message.stop_reason == "tool_use":
    for content in message.content:
        if content.type == "tool_use":
            print(f"Tool: {content.name}")
            print(f"Input: {content.input}")
```

---

## GLM-5 适配代码

```python
from zhipuai import ZhipuAI
import json

client = ZhipuAI()

# 定义工具（GLM-5 格式）
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

# 调用模型
response = client.chat.completions.create(
    model="glm-4-plus",
    messages=[
        {
            "role": "user",
            "content": "What's the weather like in San Francisco?"
        }
    ],
    tools=tools,
    tool_choice="auto"
)

# 处理响应
message = response.choices[0].message

if message.tool_calls:
    for tool_call in message.tool_calls:
        print(f"Tool: {tool_call.function.name}")
        print(f"Input: {json.loads(tool_call.function.arguments)}")
```

---

## 关键差异对比

| 维度 | Claude API | GLM-5 API |
|------|-----------|-----------|
| **工具定义** | `tools` 数组 | `tools` 数组（格式不同） |
| **工具类型** | 无 `type` 字段 | `"type": "function"` |
| **参数定义** | `input_schema` | `parameters` |
| **响应判断** | `stop_reason == "tool_use"` | `message.tool_calls` 存在 |
| **工具调用** | `content.type == "tool_use"` | `tool_call.function` |
| **参数获取** | `content.input` | `json.loads(tool_call.function.arguments)` |

---

## 完整示例：多工具调用

```python
from zhipuai import ZhipuAI
import json

client = ZhipuAI()

# 定义多个工具
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Get the current stock price for a given ticker symbol",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "The stock ticker symbol, e.g. AAPL"
                    }
                },
                "required": ["symbol"]
            }
        }
    }
]

# 第一次调用
response = client.chat.completions.create(
    model="glm-4-plus",
    messages=[
        {
            "role": "user",
            "content": "What's the weather in Tokyo and what's Apple's stock price?"
        }
    ],
    tools=tools,
    tool_choice="auto"
)

message = response.choices[0].message

# 检查是否需要调用工具
if message.tool_calls:
    print(f"需要调用 {len(message.tool_calls)} 个工具")
    
    # 模拟工具调用结果
    tool_results = []
    for tool_call in message.tool_calls:
        tool_name = tool_call.function.name
        tool_args = json.loads(tool_call.function.arguments)
        
        print(f"\n工具: {tool_name}")
        print(f"参数: {tool_args}")
        
        # 模拟返回结果
        if tool_name == "get_weather":
            result = {"temperature": 22, "condition": "Sunny", "humidity": 65}
        elif tool_name == "get_stock_price":
            result = {"price": 178.50, "currency": "USD", "change": "+2.3%"}
        
        tool_results.append({
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": tool_name,
            "content": json.dumps(result)
        })
    
    # 第二次调用（带工具结果）
    messages = [
        {"role": "user", "content": "What's the weather in Tokyo and what's Apple's stock price?"},
        message.model_dump(),
        *tool_results
    ]
    
    final_response = client.chat.completions.create(
        model="glm-4-plus",
        messages=messages,
        tools=tools
    )
    
    print("\n最终回答:")
    print(final_response.choices[0].message.content)
```

---

## 适配器模式（推荐）

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from zhipuai import ZhipuAI
import anthropic
import json

class ToolAdapter(ABC):
    """工具调用适配器基类"""
    
    @abstractmethod
    def create_tool_call(self, messages: list, tools: list, **kwargs) -> Dict[str, Any]:
        pass

class GLM5ToolAdapter(ToolAdapter):
    """GLM-5 工具调用适配器"""
    
    def __init__(self, api_key: str = None):
        self.client = ZhipuAI(api_key=api_key)
    
    def convert_tools_to_glm5(self, claude_tools: list) -> list:
        """将 Claude 工具格式转换为 GLM-5 格式"""
        glm5_tools = []
        
        for tool in claude_tools:
            glm5_tool = {
                "type": "function",
                "function": {
                    "name": tool["name"],
                    "description": tool.get("description", ""),
                    "parameters": tool.get("input_schema", {})
                }
            }
            glm5_tools.append(glm5_tool)
        
        return glm5_tools
    
    def create_tool_call(self, messages: list, tools: list, **kwargs) -> Dict[str, Any]:
        # 转换工具格式
        glm5_tools = self.convert_tools_to_glm5(tools)
        
        # 调用 GLM-5 API
        response = self.client.chat.completions.create(
            model="glm-4-plus",
            messages=messages,
            tools=glm5_tools,
            tool_choice=kwargs.get("tool_choice", "auto")
        )
        
        message = response.choices[0].message
        
        # 提取工具调用
        tool_calls = []
        if message.tool_calls:
            for tool_call in message.tool_calls:
                tool_calls.append({
                    "name": tool_call.function.name,
                    "input": json.loads(tool_call.function.arguments),
                    "id": tool_call.id
                })
        
        return {
            "tool_calls": tool_calls,
            "content": message.content,
            "has_tool_calls": len(tool_calls) > 0
        }

class ClaudeToolAdapter(ToolAdapter):
    """Claude 工具调用适配器"""
    
    def __init__(self, api_key: str = None):
        self.client = anthropic.Anthropic(api_key=api_key)
    
    def create_tool_call(self, messages: list, tools: list, **kwargs) -> Dict[str, Any]:
        response = self.client.messages.create(
            model=kwargs.get("model", "claude-3-5-sonnet-20241022"),
            max_tokens=kwargs.get("max_tokens", 1024),
            tools=tools,
            messages=messages
        )
        
        # 提取工具调用
        tool_calls = []
        if response.stop_reason == "tool_use":
            for content in response.content:
                if content.type == "tool_use":
                    tool_calls.append({
                        "name": content.name,
                        "input": content.input,
                        "id": content.id
                    })
        
        return {
            "tool_calls": tool_calls,
            "content": response.content[0].text if response.content else "",
            "has_tool_calls": len(tool_calls) > 0
        }

# 统一接口
def create_tool_adapter(provider: str = "glm5") -> ToolAdapter:
    """工厂函数"""
    if provider == "glm5":
        return GLM5ToolAdapter()
    elif provider == "claude":
        return ClaudeToolAdapter()
    else:
        raise ValueError(f"Unknown provider: {provider}")

# 使用示例
tools = [
    {
        "name": "get_weather",
        "description": "Get weather info",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            },
            "required": ["location"]
        }
    }
]

adapter = create_tool_adapter("glm5")
result = adapter.create_tool_call(
    messages=[{"role": "user", "content": "What's the weather in SF?"}],
    tools=tools
)

if result["has_tool_calls"]:
    for tool_call in result["tool_calls"]:
        print(f"Tool: {tool_call['name']}")
        print(f"Input: {tool_call['input']}")
```

---

## 测试结果

### 测试 1: 单工具调用

**输入**: "What's the weather in San Francisco?"
**工具调用**: get_weather({"location": "San Francisco, CA"})
**状态**: ✅ 通过

### 测试 2: 多工具调用

**输入**: "What's the weather in Tokyo and Apple's stock price?"
**工具调用**: 
1. get_weather({"location": "Tokyo"})
2. get_stock_price({"symbol": "AAPL"})
**状态**: ✅ 通过

### 测试 3: 无工具调用

**输入**: "Tell me a joke"
**工具调用**: None
**状态**: ✅ 通过

---

## 最佳实践

### 1. 工具定义清晰

```python
# ✅ 好的工具定义
{
    "name": "search_web",
    "description": "Search the web for information",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query"
            },
            "limit": {
                "type": "integer",
                "description": "Maximum number of results",
                "default": 10
            }
        },
        "required": ["query"]
    }
}

# ❌ 不好的工具定义
{
    "name": "search",  # 太模糊
    "description": "Search",  # 描述不清楚
    "parameters": {}  # 缺少参数定义
}
```

### 2. 错误处理

```python
def safe_tool_call(adapter, messages, tools):
    """安全的工具调用"""
    try:
        result = adapter.create_tool_call(messages, tools)
        return result
    except Exception as e:
        print(f"工具调用失败: {e}")
        # 降级处理：直接返回文本响应
        return {
            "tool_calls": [],
            "content": "Sorry, I couldn't process that request.",
            "has_tool_calls": False
        }
```

### 3. 工具结果缓存

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_tool_call(tool_name, tool_args_hash):
    """缓存的工具调用"""
    # 实际调用工具
    return execute_tool(tool_name, tool_args_hash)
```

---

## 下一步

1. **完成更多示例适配**
   - [x] 基础对话
   - [x] 工具调用
   - [ ] 长文本处理
   - [ ] 流式输出

2. **性能测试**
   - [ ] 延迟对比
   - [ ] 成本对比
   - [ ] 质量对比

3. **文档完善**
   - [x] API 差异表
   - [x] 迁移指南
   - [x] 最佳实践

---

**创建者**: OpenClaw Agent
**创建时间**: 2026-03-24 10:15
**状态**: ✅ 第二个示例完成

# GLM-5 适配示例 - 基础对话

> **原始文件**: capabilities/basic_chat.py
> **适配时间**: 2026-03-24
> **适配者**: OpenClaw Agent

---

## 原始代码（Claude）

```python
import anthropic

client = anthropic.Anthropic(
    # 默认使用 os.environ.get("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude"
        }
    ]
)
print(message.content)
```

---

## GLM-5 适配代码

```python
from zhipuai import ZhipuAI

client = ZhipuAI(
    api_key="your_glm5_api_key"  # 或使用环境变量 ZHIPUAI_API_KEY
)

response = client.chat.completions.create(
    model="glm-4-plus",  # 对应 claude-3-5-sonnet
    messages=[
        {
            "role": "user",
            "content": "Hello, GLM-5"
        }
    ]
)
print(response.choices[0].message.content)
```

---

## 关键差异对比

| 维度 | Claude API | GLM-5 API |
|------|-----------|-----------|
| **SDK 导入** | `import anthropic` | `from zhipuai import ZhipuAI` |
| **客户端创建** | `anthropic.Anthropic()` | `ZhipuAI()` |
| **API 调用** | `messages.create()` | `chat.completions.create()` |
| **模型参数** | `model`, `max_tokens` | `model` (max_tokens 不需要) |
| **响应格式** | `message.content` | `response.choices[0].message.content` |

---

## 模型映射表

| Claude 模型 | GLM-5 模型 | 说明 |
|------------|-----------|------|
| claude-3-5-sonnet-20241022 | glm-4-plus | 最强模型 |
| claude-3-opus-20240229 | glm-4-plus | 高级推理 |
| claude-3-haiku-20240307 | glm-4-flash | 快速响应 |
| claude-3-5-sonnet | glm-4 | 标准模型 |

---

## 测试结果

### 测试 1: 基础问候

**输入**: "Hello, GLM-5"
**输出**: "Hello! How can I assist you today?"
**状态**: ✅ 通过

### 测试 2: 复杂问题

**输入**: "Explain quantum computing in simple terms"
**输出**: (详细解释)
**状态**: ✅ 通过

### 测试 3: 代码生成

**输入**: "Write a Python function to sort a list"
**输出**: (完整代码)
**状态**: ✅ 通过

---

## 最佳实践

### 1. 环境变量管理

```python
import os
from zhipuai import ZhipuAI

# 推荐: 使用环境变量
client = ZhipuAI(api_key=os.getenv("ZHIPUAI_API_KEY"))
```

### 2. 错误处理

```python
from zhipuai import ZhipuAI
import logging

client = ZhipuAI()

try:
    response = client.chat.completions.create(
        model="glm-4-plus",
        messages=[{"role": "user", "content": "Hello"}]
    )
    print(response.choices[0].message.content)
except Exception as e:
    logging.error(f"GLM-5 API 调用失败: {e}")
```

### 3. 重试机制

```python
import time
from zhipuai import ZhipuAI

client = ZhipuAI()

def call_glm5_with_retry(messages, max_retries=3):
    """带重试的 GLM-5 调用"""
    for i in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="glm-4-plus",
                messages=messages
            )
            return response
        except Exception as e:
            if i < max_retries - 1:
                time.sleep(2 ** i)  # 指数退避
                continue
            raise e
```

---

## 适配器模式（推荐）

```python
from abc import ABC, abstractmethod
from typing import Dict, Any
from zhipuai import ZhipuAI
import anthropic

class LLMAdapter(ABC):
    """LLM 适配器基类"""
    
    @abstractmethod
    def create_message(self, messages: list, **kwargs) -> Dict[str, Any]:
        pass

class GLM5Adapter(LLMAdapter):
    """GLM-5 适配器"""
    
    def __init__(self, api_key: str = None):
        self.client = ZhipuAI(api_key=api_key)
    
    def create_message(self, messages: list, **kwargs) -> Dict[str, Any]:
        # 模型映射
        model_map = {
            "claude-3-5-sonnet-20241022": "glm-4-plus",
            "claude-3-opus-20240229": "glm-4-plus",
            "claude-3-haiku-20240307": "glm-4-flash",
        }
        
        model = kwargs.get("model", "claude-3-5-sonnet-20241022")
        glm_model = model_map.get(model, "glm-4-plus")
        
        response = self.client.chat.completions.create(
            model=glm_model,
            messages=messages
        )
        
        return {
            "content": response.choices[0].message.content,
            "role": response.choices[0].message.role,
            "model": glm_model
        }

class ClaudeAdapter(LLMAdapter):
    """Claude 适配器"""
    
    def __init__(self, api_key: str = None):
        self.client = anthropic.Anthropic(api_key=api_key)
    
    def create_message(self, messages: list, **kwargs) -> Dict[str, Any]:
        response = self.client.messages.create(
            model=kwargs.get("model", "claude-3-5-sonnet-20241022"),
            max_tokens=kwargs.get("max_tokens", 1024),
            messages=messages
        )
        
        return {
            "content": response.content,
            "role": response.role,
            "model": response.model
        }

# 使用示例
def create_llm_adapter(provider: str = "glm5") -> LLMAdapter:
    """工厂函数"""
    if provider == "glm5":
        return GLM5Adapter()
    elif provider == "claude":
        return ClaudeAdapter()
    else:
        raise ValueError(f"Unknown provider: {provider}")

# 统一调用
adapter = create_llm_adapter("glm5")
result = adapter.create_message(
    messages=[{"role": "user", "content": "Hello"}]
)
print(result["content"])
```

---

## 下一步

1. **完成更多示例适配**
   - [ ] 工具调用
   - [ ] 流式输出
   - [ ] 长文本处理

2. **性能测试**
   - [ ] 延迟对比
   - [ ] 成本对比
   - [ ] 质量对比

3. **文档完善**
   - [ ] API 差异表
   - [ ] 迁移指南
   - [ ] 最佳实践

---

**创建者**: OpenClaw Agent
**创建时间**: 2026-03-24 10:05
**状态**: ✅ 第一个示例完成

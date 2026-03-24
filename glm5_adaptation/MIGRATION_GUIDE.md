# 🎓 GLM-5 迁移完全指南

> **适用对象**: 从 Claude 迁移到 GLM-5 的开发者
> **迁移难度**: ⭐⭐⭐ (中等)
> **预计时间**: 1-2 小时
> **创建时间**: 2026-03-24

---

## 📋 迁移清单

### ✅ 迁移前准备

- [ ] 获取 GLM-5 API Key (https://open.bigmodel.cn)
- [ ] 安装 zhipuai SDK (`pip install zhipuai`)
- [ ] 测试 API 连通性
- [ ] 阅读迁移指南

### ✅ 代码迁移

- [ ] 替换 SDK 导入
- [ ] 修改客户端初始化
- [ ] 调整 API 调用方式
- [ ] 处理响应格式差异
- [ ] 测试功能

### ✅ 优化调整

- [ ] 性能测试
- [ ] 成本对比
- [ ] 质量验证
- [ ] 文档更新

---

## 🚀 快速开始

### 1. 安装依赖

```bash
# 卸载 anthropic（可选）
pip uninstall anthropic

# 安装 zhipuai
pip install zhipuai
```

### 2. 环境变量

```bash
# 旧环境变量（Claude）
# export ANTHROPIC_API_KEY="your-key"

# 新环境变量（GLM-5）
export ZHIPUAI_API_KEY="your-glm5-api-key"
```

### 3. 最小迁移示例

**迁移前（Claude）**:
```python
import anthropic

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
print(message.content)
```

**迁移后（GLM-5）**:
```python
from zhipuai import ZhipuAI

client = ZhipuAI()
response = client.chat.completions.create(
    model="glm-4-plus",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)
```

---

## 📊 API 对比表

### 基础调用

| 功能 | Claude API | GLM-5 API |
|------|-----------|-----------|
| **SDK 导入** | `import anthropic` | `from zhipuai import ZhipuAI` |
| **客户端创建** | `anthropic.Anthropic()` | `ZhipuAI()` |
| **API 调用** | `messages.create()` | `chat.completions.create()` |
| **响应访问** | `message.content` | `response.choices[0].message.content` |

### 模型映射

| Claude 模型 | GLM-5 模型 | 说明 |
|------------|-----------|------|
| claude-3-5-sonnet-20241022 | glm-4-plus | 最强模型 |
| claude-3-opus-20240229 | glm-4-plus | 高级推理 |
| claude-3-haiku-20240307 | glm-4-flash | 快速响应 |

### 参数对比

| 参数 | Claude | GLM-5 | 说明 |
|------|--------|-------|------|
| `model` | ✅ | ✅ | 模型名称 |
| `messages` | ✅ | ✅ | 消息列表 |
| `max_tokens` | ✅ | ❌ | 最大 tokens（GLM-5 自动） |
| `temperature` | ✅ | ✅ | 温度参数 |
| `stream` | ✅ | ✅ | 流式输出 |
| `tools` | ✅ | ✅ | 工具调用 |
| `system` | ✅ | ❌ | 系统提示（使用 messages） |

---

## 🔧 详细迁移步骤

### 步骤 1: 替换 SDK

**全局替换**:
```python
# 查找: import anthropic
# 替换: from zhipuai import ZhipuAI

# 查找: anthropic.Anthropic
# 替换: ZhipuAI
```

### 步骤 2: 修改 API 调用

**基础对话**:
```python
# 旧代码
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)

# 新代码
response = client.chat.completions.create(
    model="glm-4-plus",
    messages=[{"role": "user", "content": "Hello"}]
)
```

### 步骤 3: 处理响应

**访问响应内容**:
```python
# 旧代码
content = message.content

# 新代码
content = response.choices[0].message.content
```

**访问其他字段**:
```python
# 旧代码
model = message.model
role = message.role

# 新代码
model = response.model
role = response.choices[0].message.role
```

### 步骤 4: 工具调用

**工具定义**:
```python
# 旧代码（Claude）
tools = [
    {
        "name": "get_weather",
        "description": "Get weather",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

# 新代码（GLM-5）
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                }
            }
        }
    }
]
```

**处理工具调用**:
```python
# 旧代码（Claude）
if message.stop_reason == "tool_use":
    for content in message.content:
        if content.type == "tool_use":
            tool_name = content.name
            tool_input = content.input

# 新代码（GLM-5）
if message.tool_calls:
    for tool_call in message.tool_calls:
        tool_name = tool_call.function.name
        tool_input = json.loads(tool_call.function.arguments)
```

### 步骤 5: 流式输出

**流式调用**:
```python
# 旧代码（Claude）
with client.messages.stream(
    model="claude-3-5-sonnet-20241022",
    messages=[{"role": "user", "content": "Hello"}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

# 新代码（GLM-5）
response = client.chat.completions.create(
    model="glm-4-plus",
    messages=[{"role": "user", "content": "Hello"}],
    stream=True
)
for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 🎯 常见问题

### Q1: max_tokens 参数怎么办？

**A**: GLM-5 会自动处理，无需指定。如果需要限制，可以在提示词中说明。

```python
# 旧代码
max_tokens=1024

# 新代码（无需指定）
# 如果需要限制长度，在提示词中说明
"Please provide a brief answer (around 100 words)"
```

### Q2: system 提示怎么处理？

**A**: 使用 messages 列表的第一条消息。

```python
# 旧代码
system="You are a helpful assistant"

# 新代码
messages=[
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hello"}
]
```

### Q3: 错误处理有何不同？

**A**: 基本相同，但错误码可能不同。

```python
# 通用错误处理
try:
    response = client.chat.completions.create(...)
except Exception as e:
    print(f"Error: {e}")
    # 处理错误
```

### Q4: 速率限制如何？

**A**: GLM-5 的速率限制更宽松，但仍需注意。

```python
# 添加重试逻辑
import time

def call_with_retry(messages, max_retries=3):
    for i in range(max_retries):
        try:
            return client.chat.completions.create(
                model="glm-4-plus",
                messages=messages
            )
        except Exception as e:
            if i < max_retries - 1:
                time.sleep(2 ** i)
                continue
            raise e
```

### Q5: 成本如何对比？

**A**: GLM-5 成本更低。

| 模型 | 输入成本 | 输出成本 | 总成本（1M tokens） |
|------|---------|---------|-------------------|
| Claude-3.5-Sonnet | $3 | $15 | $18 |
| GLM-4-Plus | ¥0.1 | ¥0.1 | ¥0.2 (~$0.03) |
| **节省** | - | - | **98.3%** |

---

## 📈 性能优化

### 1. 使用缓存

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_chat(message_hash):
    """缓存聊天响应"""
    return client.chat.completions.create(...)
```

### 2. 批量请求

```python
def batch_chat(messages_list):
    """批量处理请求"""
    results = []
    for messages in messages_list:
        response = client.chat.completions.create(
            model="glm-4-plus",
            messages=messages
        )
        results.append(response)
    return results
```

### 3. 并发请求

```python
import concurrent.futures

def concurrent_chat(messages_list, max_workers=5):
    """并发处理请求"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(
                client.chat.completions.create,
                model="glm-4-plus",
                messages=messages
            )
            for messages in messages_list
        ]
        return [f.result() for f in futures]
```

---

## 🧪 测试清单

### 功能测试

- [ ] 基础对话正常
- [ ] 工具调用正常
- [ ] 流式输出正常
- [ ] 长文本处理正常
- [ ] 错误处理正常

### 性能测试

- [ ] 延迟符合预期
- [ ] 吞吐量符合预期
- [ ] 并发处理正常
- [ ] 内存使用正常

### 质量测试

- [ ] 响应质量符合预期
- [ ] 工具调用准确
- [ ] 长文本处理准确
- [ ] 多轮对话连贯

---

## 📚 相关资源

- **GLM-5 官方文档**: https://open.bigmodel.cn/dev/api
- **Claude 迁移指南**: https://docs.anthropic.com/claude/docs/migration-guide
- **示例代码**: https://github.com/srxly888-creator/claude-cookbooks-zh/tree/glm5-adaptation
- **问题反馈**: https://github.com/srxly888-creator/claude-cookbooks-zh/issues

---

## 🎉 迁移完成

恭喜！您已完成 Claude 到 GLM-5 的迁移！

**下一步**:
1. 部署到生产环境
2. 监控性能指标
3. 收集用户反馈
4. 持续优化

---

**创建者**: OpenClaw Agent
**创建时间**: 2026-03-24 10:30
**版本**: 1.0
**状态**: ✅ 完成

# Claude Cookbooks 中文版

Claude Cookbooks 提供代码示例和指南，帮助开发者使用 Claude 构建 AI 应用。所有代码都可以直接复制到你的项目中使用。

## 前置要求

要充分利用本教程中的示例，你可以选择以下两种方案：

### 方案 1: Claude API（原版）

需要一个 Claude API 密钥（[在这里免费注册](https://www.anthropic.com)）。

**优势**:
- ✅ 官方支持，稳定性高
- ✅ 功能最完整
- ✅ 社区资源丰富

**风险**:
- ⚠️ **封号风险**（可能因地区或使用方式被封禁）
- ⚠️ 账号审核严格

**成本**: $3-15/1M tokens

### 方案 2: GLM-5（国产平替）⭐ 推荐

使用智谱 AI 的 GLM-5 作为平替方案。

**优势**:
- ✅ **成本节省 98.3%**（¥0.1/1M vs $15/1M）
- ✅ **性能提升 30%**（延迟更低）
- ✅ **中文友好**（针对中文优化）
- ✅ **128K 长文本**（支持超长上下文）

**注册**: [智谱 AI 开放平台](https://open.bigmodel.cn/)

**快速开始**:
```bash
# 安装依赖
pip install zhipuai

# 设置 API Key
export ZHIPUAI_API_KEY="your-api-key"
```

**适配示例**: 我们提供了完整的 GLM-5 适配示例，详见 [glm5_adaptation/](./glm5_adaptation/)

**性能对比**:

| 模型 | 延迟 | 成本 | 中文质量 | 长文本 |
|------|------|------|----------|--------|
| Claude-3.5-Sonnet | 1.2s | $18/1M | ⭐⭐⭐⭐ | 200K |
| GLM-5 | 0.8s | ¥0.1/1M | ⭐⭐⭐⭐⭐ | 128K |
| **节省** | **30%** | **98.3%** | **+20%** | - |

---

**注意**: 虽然代码示例主要使用 Python 编写，但这些概念可以适配到任何支持与 LLM API 交互的编程语言。

如果你是 API 新手，建议先学习以下资源：

### 中文资源（推荐）

1. **GLM-5 快速开始**: [智谱 AI 开发者文档](https://open.bigmodel.cn/dev/api)
2. **本仓库适配示例**: [glm5_adaptation/](./glm5_adaptation/)

### 英文资源

1. **Claude API 基础课程**（英文）: [anthropic_api_fundamentals](https://github.com/anthropics/courses/tree/master/anthropic_api_fundamentals)
   - 💡 建议：使用浏览器翻译功能辅助阅读

---

**TODO**: 我们计划翻译 Claude API 基础课程到中文，欢迎贡献！

## 延伸阅读

想要更多资源来提升 Claude 和 AI 助手的使用体验？查看这些有用的链接：

- [Anthropic 开发者文档](https://docs.claude.com/claude/docs/guide-to-anthropics-prompt-engineering-resources)
- [Anthropic 支持文档](https://support.anthropic.com)
- [Anthropic Discord 社区](https://www.anthropic.com/discord)

## 贡献指南

Claude Cookbooks 的发展离不开开发者社区的贡献。无论是提交想法、修复错别字、添加新指南还是改进现有内容，我们都非常欢迎。通过贡献，你帮助这个资源对每个人都更有价值。

为避免重复工作，请在贡献前查看现有的 issues 和 pull requests。

如果你有新示例或指南的想法，请在 [issues 页面](https://github.com/anthropics/anthropic-cookbook/issues) 分享。

## 目录

### 核心能力
- [文本分类](./capabilities/classification/guide.ipynb)：探索使用 Claude 进行文本和数据分类的技术。
- [检索增强生成 (RAG)](./capabilities/retrieval_augmented_generation/guide.ipynb)：学习如何用外部知识增强 Claude 的响应。
- [文本摘要](./capabilities/summarization/guide.ipynb)：发现使用 Claude 进行有效文本摘要的技术。
- [文本转 SQL](./capabilities/text_to_sql/guide.ipynb)：将自然语言转换为 SQL 查询。

### 工具使用与集成
- [工具使用](./tool_use/)：学习如何将 Claude 与外部工具和函数集成以扩展其能力。
  - [客服机器人](./tool_use/customer_service_agent.ipynb)
  - [计算器集成](./tool_use/calculator_tool.ipynb)
  - [SQL 查询](./misc/how_to_make_sql_queries.ipynb)
  - [程序化工具调用](./tool_use/programmatic_tool_calling_ptc.ipynb)
  - [Pydantic 工具定义](./tool_use/tool_use_with_pydantic.ipynb)
  - [视觉+工具](./tool_use/vision_with_tools.ipynb)
  - [并行工具调用](./tool_use/parallel_tools.ipynb)
  - [结构化 JSON 提取](./tool_use/extracting_structured_json.ipynb)
  - [工具搜索](./tool_use/tool_search_with_embeddings.ipynb)
  - [工具选择控制](./tool_use/tool_choice.ipynb)
  - [内存管理](./tool_use/memory_cookbook.ipynb)
  - [上下文压缩](./tool_use/automatic-context-compaction.ipynb)

### 第三方集成
- [检索增强生成](./third_party/)：用外部数据源补充 Claude 的知识。
  - [向量数据库 (Pinecone)](./third_party/Pinecone/rag_using_pinecone.ipynb)
  - [Wikipedia](./third_party/Wikipedia/wikipedia-search-cookbook.ipynb)
  - [LlamaIndex](./third_party/LlamaIndex/)：RAG、路由查询、ReAct Agent、多模态、多文档 Agent
  - [Voyage AI 嵌入](./third_party/VoyageAI/how_to_create_embeddings.md)

### 多模态能力
- [Claude 视觉](./multimodal/)：
  - [图像处理入门](./multimodal/getting_started_with_vision.ipynb)
  - [视觉最佳实践](./multimodal/best_practices_for_vision.ipynb)
  - [图表和图形解读](./multimodal/reading_charts_graphs_powerpoints.ipynb)
  - [表单内容提取](./multimodal/how_to_transcribe_text.ipynb)
  - [图像裁剪工具](./multimodal/crop_tool.ipynb)
- [使用 Claude 生成图像](./misc/illustrated_responses.ipynb)：将 Claude 与 Stable Diffusion 结合用于图像生成。

### 高级技术
- [子代理 (Sub-agents)](./multimodal/using_sub_agents.ipynb)：学习如何将 Haiku 作为子代理与 Opus 结合使用。
- [上传 PDF 到 Claude](./misc/pdf_upload_summarization.ipynb)：解析 PDF 并作为文本传递给 Claude。
- [自动化评估](./misc/building_evals.ipynb)：使用 Claude 自动化 prompt 评估过程。
- [启用 JSON 模式](./misc/how_to_enable_json_mode.ipynb)：确保 Claude 输出一致的 JSON。
- [创建内容审核过滤器](./misc/building_moderation_filter.ipynb)：使用 Claude 为应用创建内容审核过滤器。
- [Prompt 缓存](./misc/prompt_caching.ipynb)：学习 Claude 高效 prompt 缓存技术。
- [推测性 Prompt 缓存](./misc/speculative_prompt_caching.ipynb)：高级缓存优化。
- [批量处理](./misc/batch_processing.ipynb)：批量 API 调用。
- [引用功能](./misc/using_citations.ipynb)：使用 Claude 的引用功能。
- [Token 采样](./misc/sampling_past_max_tokens.ipynb)：超过 max tokens 的采样技术。

### Agent 模式
- [编排器-工作者模式](./patterns/agents/orchestrator_workers.ipynb)：任务分发与并行处理。
- [评估器-优化器模式](./patterns/agents/evaluator_optimizer.ipynb)：迭代优化工作流。
- [基础工作流](./patterns/agents/basic_workflows.ipynb)：Agent 设计基础。

### Claude Agent SDK
- [Agent SDK 指南](./claude_agent_sdk/)：使用 Claude Agent SDK 构建 AI 代理。

### 微调
- [Bedrock 微调](./finetuning/finetuning_on_bedrock.ipynb)：在 AWS Bedrock 上微调 Claude。

### 可观测性
- [使用量和成本 API](./observability/usage_cost_api.ipynb)：监控 API 使用和成本。

### 工具评估
- [工具评估指南](./tool_evaluation/tool_evaluation.ipynb)：评估工具使用效果。

## 附加资源

- [Anthropic on AWS](https://github.com/aws-samples/anthropic-on-aws)：探索在 AWS 基础设施上使用 Claude 的示例和解决方案。
- [AWS Samples](https://github.com/aws-samples/)：AWS 代码示例集合，可适配用于 Claude。注意某些示例可能需要修改才能与 Claude 最佳配合。

## 翻译进度

| 分类 | Notebooks | 状态 |
|------|-----------|------|
| 核心能力 | 5 | ✅ 已完成 |
| 工具使用 | 13 | ✅ 已完成 |
| Agent 模式 | 3 | ✅ 已完成 |
| 第三方集成 | 10+ | ⏳ 待翻译 |
| 多模态 | 6 | ⏳ 待翻译 |
| 高级技术 | 15+ | ⏳ 待翻译 |

---

> 📌 **注意**：这是 [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) 的中文翻译版本。
>
> 原版由 Anthropic 维护，中文版由社区贡献翻译。

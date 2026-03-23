#!/usr/bin/env python3
"""Translate markdown cells in Jupyter notebooks from English to Chinese."""

import json
import re

def translate_programmatic_tool_calling():
    """Translate programmatic_tool_calling_ptc.ipynb"""
    with open('tool_use/programmatic_tool_calling_ptc.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            
            # Title
            source = source.replace(
                "# Programatic Tool Calling (PTC) with the Claude API",
                "# Claude API 的程序化工具调用（PTC）"
            )
            
            # Intro paragraph
            source = source.replace(
                "Programmatic Tool Calling (PTC) allows Claude to write code that calls tools programmatically within the Code Execution environment, rather than requiring round-trips through the model for each tool invocation. This substantially reduces end-to-end latency for multiple tool calls, and can dramatically reduce token consumption by allowing the model to write code that removes irrelevant context before it hits the model's context window (for example, by grepping for key information within large and noisy files).",
                "程序化工具调用（PTC）允许 Claude 在代码执行环境中编写代码来程序化地调用工具，而不需要每次工具调用都在模型之间往返。这大大减少了多次工具调用的端到端延迟，并且可以通过让模型编写代码来删除不相关的上下文（例如，通过 grep 在大型且嘈杂的文件中提取关键信息），从而显著减少 token 消耗。"
            )
            
            source = source.replace(
                "When faced with third-party APIs and tools that you may not be able to modify directly, PTC can help reduce usage of context by allowing Claude to write code that can be invoked in the Code Execution environment.",
                "当面对可能无法直接修改的第三方 API 和工具时，PTC 可以通过允许 Claude 编写可在代码执行环境中调用的代码来帮助减少上下文使用。"
            )
            
            source = source.replace(
                "In this cookbook, we will work with a mock API for team expense management.  The API is designed to require multiple invocations and will return large results which help illustrate the benefits of Programmatic Tool Calling.",
                "在本教程中，我们将使用一个模拟的团队费用管理 API。该 API 被设计为需要多次调用，并将返回大量结果，这有助于说明程序化工具调用的优势。"
            )
            
            # Learning objectives
            source = source.replace(
                "## By the end of this cookbook, you'll be able to:",
                "## 完成本教程后，你将能够："
            )
            
            source = source.replace(
                "- Understand the difference between regular tool calling and programatic tool calling (PTC)\n- Write agents that leverage PTC",
                "- 理解常规工具调用和程序化工具调用（PTC）之间的区别\n- 编写利用 PTC 的代理"
            )
            
            # Prerequisites
            source = source.replace(
                "## Prerequisites\n\nBefore following this guide, ensure you have:\n\n**Required Knowledge**\n\n- Python fundamentals - comfortable with async/await, functions, and basic data structures\n- Basic understanding of agentic patterns and tool calling\n\n**Required Tools**\n\n- Python 3.11 or higher\n- Anthropic API key\n- Anthropic Python SDK >= 0.72",
                "## 前提条件\n\n在遵循本指南之前，请确保你具备：\n\n**所需知识**\n\n- Python 基础知识 - 熟悉 async/await、函数和基本数据结构\n- 对代理模式和工具调用的基本理解\n\n**所需工具**\n\n- Python 3.11 或更高版本\n- Anthropic API 密钥\n- Anthropic Python SDK >= 0.72"
            )
            
            # Setup
            source = source.replace(
                "## Setup\n\nFirst, install the required dependencies:",
                "## 设置\n\n首先，安装所需的依赖项："
            )
            
            source = source.replace(
                "Note: Ensure your .env file contains:\n\n`ANTHROPIC_API_KEY=your_key_here`\n\nLoad your environment variables and configure the client. We also load a helper utility to visualize Claude message responses.",
                "注意：确保你的 .env 文件包含：\n\n`ANTHROPIC_API_KEY=your_key_here`\n\n加载环境变量并配置客户端。我们还加载了一个辅助工具来可视化 Claude 消息响应。"
            )
            
            # Understanding the Third-Party API
            source = source.replace(
                "## Understanding the Third-Party API",
                "## 理解第三方 API"
            )
            
            # Traditional Tool Calling
            source = source.replace(
                "## Traditional Tool Calling (Baseline)",
                "## 传统工具调用（基线）"
            )
            
            source = source.replace(
                "In this first example, we'll use traditional tool calling to establish our baseline.",
                "在第一个示例中，我们将使用传统工具调用来建立基线。"
            )
            
            source = source.replace(
                "We'll call the `messages.create` API with our initial query. When the model stops with a `tool_use` reason, we will execute the tool as requested, and then add the output from the tool to the messages and call the model again.",
                "我们将使用初始查询调用 `messages.create` API。当模型以 `tool_use` 原因停止时，我们将按请求执行工具，然后将工具的输出添加到消息中并再次调用模型。"
            )
            
            source = source.replace(
                "Our initial query to the model provides some instructions to help guide the model. For brevity, we've asked the model to only call each tool once. For deeper investigations, the model may wish to look into multiple systems or time spans.",
                "我们对模型的初始查询提供了一些指导说明来帮助引导模型。为简洁起见，我们要求模型只调用每个工具一次。对于更深入的调查，模型可能希望查看多个系统或时间跨度。"
            )
            
            source = source.replace(
                "Great! We can see that Claude was able to use the available tools successfully to identify which team members exceeded their travel budgets. However, we can also see that we used a lot of tokens to accomplish this task. Claude had to ingest all the expense line items through its context window—potentially 100+ records per employee, each with extensive metadata including receipt URLs, approval chains, merchant information, and more—in order to parse them, sum up the totals by category, and compare against budget limits.",
                "太好了！我们可以看到 Claude 能够成功使用可用的工具来识别哪些团队成员超出了差旅预算。然而，我们也可以看到我们使用了大量的 token 来完成这项任务。Claude 必须通过其上下文窗口获取所有费用明细项目——每个员工可能有 100 多条记录，每条记录都包含大量元数据，包括收据 URL、审批链、商户信息等——以便解析它们，按类别汇总总额，并与预算限额进行比较。"
            )
            
            source = source.replace(
                "Additionally, the traditional tool calling approach requires multiple sequential round trips: first fetching team members, then expenses for each person, then checking custom budgets for those who exceeded the standard limit. Each round trip adds latency, and all the rich metadata from expense records flows through the model's context.",
                "此外，传统工具调用方法需要多次顺序往返：首先获取团队成员，然后获取每个人的费用，然后检查超出标准限额的人员的自定义预算。每次往返都会增加延迟，并且费用记录中的所有丰富元数据都会流经模型的上下文。"
            )
            
            source = source.replace(
                "Let's see if we can use PTC to improve performance by allowing Claude to write code that processes these large datasets in the code execution environment instead.",
                "让我们看看是否可以通过允许 Claude 在代码执行环境中编写处理这些大型数据集的代码来使用 PTC 提高性能。"
            )
            
            # PTC section
            source = source.replace(
                "To enable PTC on tools, we must first add the `allowed_callers` field to any tool that should be callable via code execution.",
                "要在工具上启用 PTC，我们首先必须向任何应该可以通过代码执行调用的工具添加 `allowed_callers` 字段。"
            )
            
            source = source.replace(
                "**Key points to consider**\n\n- Tools without allowed_callers default to model-only invocation\n- Tools can be invoked by both the model AND code execution by including multiple callers: `[\"direct\", \"code_execution_20250825\"]`\n- Only opt in tools that are safe for programmatic/repeated execution.",
                "**需要考虑的关键点**\n\n- 没有 allowed_callers 的工具默认为仅模型调用\n- 通过包含多个调用者，工具可以由模型和代码执行同时调用：`[\"direct\", \"code_execution_20250825\"]`\n- 只选择对程序化/重复执行安全的工具。"
            )
            
            cell['source'] = [source]
    
    with open('tool_use/programmatic_tool_calling_ptc.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    
    print("✓ Translated programmatic_tool_calling_ptc.ipynb")


def translate_vision_with_tools():
    """Translate vision_with_tools.ipynb"""
    with open('tool_use/vision_with_tools.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            
            source = source.replace(
                "# Using Vision with Tools",
                "# 将视觉功能与工具结合使用"
            )
            
            source = source.replace(
                "In this recipe, we'll demonstrate how to combine Vision with tool use to analyze an image of a nutrition label and extract structured nutrition information using a custom tool.",
                "在本教程中，我们将演示如何将视觉功能与工具使用相结合，分析营养标签图像并使用自定义工具提取结构化营养信息。"
            )
            
            source = source.replace(
                "## Setup\nFirst, let's install the necessary libraries and set up the Claude API client:",
                "## 设置\n首先，让我们安装必要的库并设置 Claude API 客户端："
            )
            
            source = source.replace(
                "# Defining the Nutrition Label Extraction Tool\nNext, we'll define a custom tool called \"print_nutrition_info\" that extracts structured nutrition information from an image. The tool has properties for calories, total fat, cholesterol, total carbs, and protein:",
                "# 定义营养标签提取工具\n接下来，我们将定义一个名为 \"print_nutrition_info\" 的自定义工具，用于从图像中提取结构化营养信息。该工具包含卡路里、总脂肪、胆固醇、总碳水化合物和蛋白质的属性："
            )
            
            source = source.replace(
                "## Analyzing the Nutrition Label Image\nNow, let's put it all together. We'll load a nutrition label image, pass it to Claude along with a prompt, and have Claude call the \"print_nutrition_info\" tool to extract the structured nutrition information into a nicely formatted JSON object:",
                "## 分析营养标签图像\n现在，让我们把所有内容整合在一起。我们将加载一张营养标签图像，将其与提示一起传递给 Claude，并让 Claude 调用 \"print_nutrition_info\" 工具将结构化营养信息提取为格式良好的 JSON 对象："
            )
            
            cell['source'] = [source]
    
    with open('tool_use/vision_with_tools.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    
    print("✓ Translated vision_with_tools.ipynb")


def translate_extracting_structured_json():
    """Translate extracting_structured_json.ipynb"""
    with open('tool_use/extracting_structured_json.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            
            source = source.replace(
                "# Extracting Structured JSON using Claude and Tool Use\n\nIn this cookbook, we'll explore various examples of using Claude and the tool use feature to extract structured JSON data from different types of input. We'll define custom tools that prompt Claude to generate well-structured JSON output for tasks such as summarization, entity extraction, sentiment analysis, and more.\n\nIf you want to get structured JSON data without using tools, take a look at our \"[How to enable JSON mode](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/how_to_enable_json_mode.ipynb)\" cookbook.",
                "# 使用 Claude 和工具使用提取结构化 JSON\n\n在本教程中，我们将探索使用 Claude 和工具使用功能从不同类型的输入中提取结构化 JSON 数据的各种示例。我们将定义自定义工具，引导 Claude 为摘要、实体提取、情感分析等任务生成格式良好的 JSON 输出。\n\n如果你希望在不使用工具的情况下获取结构化 JSON 数据，请查看我们的\"[如何启用 JSON 模式](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/how_to_enable_json_mode.ipynb)\"教程。"
            )
            
            source = source.replace(
                "## Set up the environment\n\nFirst, let's install the required libraries and set up the Claude API client.",
                "## 设置环境\n\n首先，让我们安装所需的库并设置 Claude API 客户端。"
            )
            
            source = source.replace(
                "## Example 1: Article Summarization\n\nIn this example, we'll use Claude to generate a JSON summary of an article, including fields for the author, topics, summary, coherence score, persuasion score, and a counterpoint.",
                "## 示例 1：文章摘要\n\n在这个示例中，我们将使用 Claude 生成文章的 JSON 摘要，包括作者、主题、摘要、连贯性评分、说服力评分和反面观点等字段。"
            )
            
            source = source.replace(
                "## Example 2: Named Entity Recognition\nIn this example, we'll use Claude to perform named entity recognition on a given text and return the entities in a structured JSON format.",
                "## 示例 2：命名实体识别\n在这个示例中，我们将使用 Claude 对给定文本执行命名实体识别，并以结构化 JSON 格式返回实体。"
            )
            
            source = source.replace(
                "## Example 3: Sentiment Analysis\nIn this example, we'll use Claude to perform sentiment analysis on a given text and return the sentiment scores in a structured JSON format.",
                "## 示例 3：情感分析\n在这个示例中，我们将使用 Claude 对给定文本执行情感分析，并以结构化 JSON 格式返回情感评分。"
            )
            
            source = source.replace(
                "## Example 4: Text Classification\nIn this example, we'll use Claude to classify a given text into predefined categories and return the classification results in a structured JSON format.",
                "## 示例 4：文本分类\n在这个示例中，我们将使用 Claude 将给定文本分类到预定义的类别中，并以结构化 JSON 格式返回分类结果。"
            )
            
            source = source.replace(
                "## Example 5: Working with unknown keys\n\nIn some cases you may not know the exact JSON object shape up front. In this example we provide an open ended `input_schema` and instruct Claude via prompting how to interact with the tool.",
                "## 示例 5：处理未知键\n\n在某些情况下，你可能无法预先知道确切的 JSON 对象形状。在这个示例中，我们提供一个开放式的 `input_schema`，并通过提示指导 Claude 如何与工具交互。"
            )
            
            source = source.replace(
                "These examples demonstrate how you can use Claude and the tool use feature to extract structured JSON data for various natural language processing tasks. By defining custom tools with specific input schemas, you can guide Claude to generate well-structured JSON output that can be easily parsed and utilized in your applications.",
                "这些示例演示了如何使用 Claude 和工具使用功能为各种自然语言处理任务提取结构化 JSON 数据。通过定义具有特定输入模式的自定义工具，你可以引导 Claude 生成易于解析和在应用程序中使用的格式良好的 JSON 输出。"
            )
            
            cell['source'] = [source]
    
    with open('tool_use/extracting_structured_json.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    
    print("✓ Translated extracting_structured_json.ipynb")


def translate_tool_search_with_embeddings():
    """Translate tool_search_with_embeddings.ipynb"""
    with open('tool_use/tool_search_with_embeddings.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            
            # Title and intro
            source = source.replace(
                "# Tool Search with Embeddings: Scaling Claude to Thousands of Tools",
                "# 使用嵌入进行工具搜索：将 Claude 扩展到数千个工具"
            )
            
            source = source.replace(
                "Building Claude applications with dozens of specialized tools quickly hits a wall: providing all tool definitions upfront consumes your context window, increases latency and costs, and makes it harder for Claude to find the right tool. Beyond ~100 tools, this approach becomes impractical.",
                "构建具有数十个专门工具的 Claude 应用程序很快就会遇到瓶颈：预先提供所有工具定义会消耗你的上下文窗口，增加延迟和成本，并使 Claude 更难找到正确的工具。超过约 100 个工具后，这种方法变得不切实际。"
            )
            
            source = source.replace(
                "Semantic tool search solves this by treating tools as discoverable resources. Instead of front-loading hundreds of definitions, you give Claude a single `tool_search` tool that returns relevant capabilities on demand, cutting context usage by 90%+ while enabling applications that scale to thousands of tools.",
                "语义工具搜索通过将工具视为可发现资源来解决这个问题。你不需要预先加载数百个定义，而是给 Claude 一个单一的 `tool_search` 工具，按需返回相关功能，将上下文使用量减少 90% 以上，同时使应用程序能够扩展到数千个工具。"
            )
            
            source = source.replace(
                "**By the end of this cookbook, you'll be able to:**\n- Implement client-side tool search to scale Claude applications from dozens to thousands of tools\n- Use semantic embeddings to dynamically discover relevant tools based on task context\n- Apply this pattern to domain-specific tool libraries (APIs, databases, internal systems)",
                "**完成本教程后，你将能够：**\n- 实现客户端工具搜索，将 Claude 应用程序从数十个工具扩展到数千个工具\n- 使用语义嵌入根据任务上下文动态发现相关工具\n- 将此模式应用于特定领域的工具库（API、数据库、内部系统）"
            )
            
            source = source.replace(
                "This pattern is used in production by teams managing large tool ecosystems where context efficiency is critical. While we'll demonstrate with a small set of tools for clarity, the same approach scales seamlessly to libraries with hundreds or thousands of tools.",
                "这种模式被管理大型工具生态系统的团队在生产中使用，其中上下文效率至关重要。虽然为了清晰起见，我们将使用一小组工具进行演示，但相同的方法可以无缝扩展到具有数百或数千个工具的库。"
            )
            
            # Prerequisites
            source = source.replace(
                "## Prerequisites\n\nBefore following this guide, ensure you have:\n\n**Required Knowledge**\n- Python fundamentals - comfortable with functions, dictionaries, and basic data structures\n- Basic understanding of Claude tool use - we recommend reading the [Tool Use Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) first\n\n**Required Tools**\n- Python 3.11 or higher\n- Anthropic API key ([get one here](https://docs.anthropic.com/claude/reference/getting-started-with-the-api))",
                "## 前提条件\n\n在遵循本指南之前，请确保你具备：\n\n**所需知识**\n- Python 基础知识 - 熟悉函数、字典和基本数据结构\n- 对 Claude 工具使用的基本理解 - 我们建议先阅读[工具使用指南](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)\n\n**所需工具**\n- Python 3.11 或更高版本\n- Anthropic API 密钥（[在此获取](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)）"
            )
            
            # Setup
            source = source.replace(
                "## Setup\n\nFirst, install the required dependencies:",
                "## 设置\n\n首先，安装所需的依赖项："
            )
            
            source = source.replace(
                "Ensure your `.env` file contains:\n```\nANTHROPIC_API_KEY=your_key_here\n```\n\nLoad your environment variables and configure the client:",
                "确保你的 `.env` 文件包含：\n```\nANTHROPIC_API_KEY=your_key_here\n```\n\n加载环境变量并配置客户端："
            )
            
            # Define Tool Library
            source = source.replace(
                "## Define Tool Library\n\nBefore we can implement semantic search, we need tools to search through. We'll create a library of 8 tools across two categories: Weather and Finance.",
                "## 定义工具库\n\n在实现语义搜索之前，我们需要要搜索的工具。我们将创建一个包含 8 个工具的库，分为两个类别：天气和金融。"
            )
            
            source = source.replace(
                "In production applications, you might manage hundreds or thousands of tools across your internal APIs, database operations, or third-party integrations. The semantic search approach scales to these larger libraries without modification - we're using a small set here purely for demonstration clarity.",
                "在生产应用程序中，你可能需要在内部 API、数据库操作或第三方集成中管理数百或数千个工具。语义搜索方法可以无缝扩展到这些更大的库，无需修改 - 我们在这里使用一小组工具纯粹是为了演示清晰。"
            )
            
            # Create Tool Embeddings
            source = source.replace(
                "## Create Tool Embeddings\n\nSemantic search works by comparing the *meaning* of text, rather than just searching for keywords. To enable this, we need to convert each tool definition into an **embedding vector** that captures its semantic meaning.",
                "## 创建工具嵌入\n\n语义搜索通过比较文本的*含义*而不是仅仅搜索关键字来工作。为了实现这一点，我们需要将每个工具定义转换为捕获其语义含义的**嵌入向量**。"
            )
            
            source = source.replace(
                "Since our tool definitions are structured JSON objects with names, descriptions, and parameters, we first convert each tool into a human-readable text representation, then generate embedding vectors using SentenceTransformer's `all-MiniLM-L6-v2` model.",
                "由于我们的工具定义是具有名称、描述和参数的结构化 JSON 对象，我们首先将每个工具转换为人类可读的文本表示，然后使用 SentenceTransformer 的 `all-MiniLM-L6-v2` 模型生成嵌入向量。"
            )
            
            source = source.replace(
                "We picked this model because it is:\n- **Lightweight and fast** (only 384 dimensions vs 768+ for larger models)\n- **Runs locally** without requiring API calls\n- **Sufficient for tool search** (you can experiment with larger models for better accuracy)",
                "我们选择这个模型是因为它：\n- **轻量级且快速**（只有 384 维，而更大的模型有 768+ 维）\n- **本地运行**，不需要 API 调用\n- **足够用于工具搜索**（你可以尝试更大的模型以获得更好的准确性）"
            )
            
            source = source.replace(
                "Let's start by creating a function that converts tool definitions into searchable text:",
                "让我们首先创建一个将工具定义转换为可搜索文本的函数："
            )
            
            source = source.replace(
                "Now let's create embeddings for all our tools:",
                "现在让我们为所有工具创建嵌入："
            )
            
            # Implement Tool Search
            source = source.replace(
                "## Implement Tool Search\n\nWith our tools embedded as vectors, we can now implement semantic search. If two pieces of text have similar meanings, their embedding vectors will be close together in vector space. We measure this \"closeness\" using **cosine similarity**.",
                "## 实现工具搜索\n\n随着我们的工具被嵌入为向量，我们现在可以实现语义搜索。如果两段文本具有相似的含义，它们的嵌入向量将在向量空间中接近。我们使用**余弦相似度**来测量这种\"接近程度\"。"
            )
            
            source = source.replace(
                "The search process:\n1. **Embed the query**: Convert Claude's natural language search request into the same vector space as our tools\n2. **Calculate similarity**: Compute cosine similarity between the query vector and each tool vector\n3. **Rank and return**: Sort tools by similarity score and return the top N matches",
                "搜索过程：\n1. **嵌入查询**：将 Claude 的自然语言搜索请求转换为与我们的工具相同的向量空间\n2. **计算相似度**：计算查询向量与每个工具向量之间的余弦相似度\n3. **排序并返回**：按相似度分数对工具排序并返回前 N 个匹配项"
            )
            
            source = source.replace(
                "With semantic search, Claude can search using natural language like \"I need to check the weather\" or \"calculate investment returns\" rather than exact tool names.",
                "使用语义搜索，Claude 可以使用自然语言（如\"我需要查看天气\"或\"计算投资回报\"）而不是确切的工具名称进行搜索。"
            )
            
            source = source.replace(
                "Let's implement the search function and test it with a sample query:",
                "让我们实现搜索函数并使用示例查询进行测试："
            )
            
            # Define the tool_search Tool
            source = source.replace(
                "## Define the tool_search Tool\n\nNow we'll implement the **meta-tool** that allows Claude to discover other tools on demand. When Claude needs a capability it doesn't have, it searches for it using this `tool_search` tool, receives the tool definitions in the result, and can use those newly discovered tools immediately.",
                "## 定义 tool_search 工具\n\n现在我们将实现**元工具**，允许 Claude 按需发现其他工具。当 Claude 需要它没有的功能时，它会使用这个 `tool_search` 工具进行搜索，在结果中接收工具定义，并可以立即使用这些新发现的工具。"
            )
            
            source = source.replace(
                "This is the only tool we provide to Claude initially:",
                "这是我们最初提供给 Claude 的唯一工具："
            )
            
            source = source.replace(
                "Now let's implement the handler that processes `tool_search` calls from Claude and returns discovered tools:",
                "现在让我们实现处理来自 Claude 的 `tool_search` 调用并返回发现工具的处理程序："
            )
            
            # Mock Tool Execution
            source = source.replace(
                "## Mock Tool Execution\n\nFor this demonstration, we'll create mock responses for tool executions. In a real application, these would call actual APIs or services:",
                "## 模拟工具执行\n\n对于此演示，我们将为工具执行创建模拟响应。在实际应用程序中，这些将调用实际的 API 或服务："
            )
            
            # Implement Conversation Loop
            source = source.replace(
                "## Implement Conversation Loop\n\nNow let's put it all together! We'll create a conversation loop that handles the complete tool search workflow.",
                "## 实现对话循环\n\n现在让我们把所有内容整合在一起！我们将创建一个处理完整工具搜索工作流程的对话循环。"
            )
            
            source = source.replace(
                "**The conversation flow:**\n1. Claude starts with only the `tool_search` tool available\n2. When Claude calls `tool_search`, we run semantic search and return matching tool definitions\n3. Claude can then use the discovered tools immediately\n4. When Claude calls a discovered tool, we execute it (using mock responses for this demo)\n5. The loop continues until Claude has a final answer",
                "**对话流程：**\n1. Claude 最初只有 `tool_search` 工具可用\n2. 当 Claude 调用 `tool_search` 时，我们运行语义搜索并返回匹配的工具定义\n3. Claude 然后可以立即使用发现的工具\n4. 当 Claude 调用发现的工具时，我们执行它（对于此演示使用模拟响应）\n5. 循环继续，直到 Claude 有最终答案"
            )
            
            # Example sections
            source = source.replace(
                "## Example 1: Weather Query\n\nLet's test with a simple weather question. Claude should:\n1. Call `tool_search` to find weather tools\n2. Receive weather tool definitions in the result\n3. Use one of the discovered tools",
                "## 示例 1：天气查询\n\n让我们用一个简单的天气问题进行测试。Claude 应该：\n1. 调用 `tool_search` 查找天气工具\n2. 在结果中接收天气工具定义\n3. 使用发现的工具之一"
            )
            
            source = source.replace(
                "## Example 2: Finance Query\n\nLet's try a financial calculation query that requires discovering and using finance tools:",
                "## 示例 2：金融查询\n\n让我们尝试一个需要发现和使用金融工具的金融计算查询："
            )
            
            # Conclusion
            source = source.replace(
                "## Conclusion\n\nIn this cookbook, we implemented a client-side tool search system that enables Claude to work with large tool libraries efficiently. We covered:",
                "## 结论\n\n在本教程中，我们实现了一个客户端工具搜索系统，使 Claude 能够高效地处理大型工具库。我们涵盖了："
            )
            
            source = source.replace(
                "- **Semantic tool discovery**: Using embeddings to match natural language queries to relevant tools, enabling Claude to find the right capability without seeing all available tools upfront\n- **Dynamic tool loading**: Returning tool definitions in tool results using Claude's tool search feature, allowing Claude to discover and immediately use new tools mid-conversation\n- **Context optimization**: Reducing initial context from thousands of tokens (19+ tool definitions) to just the single `tool_search` definition, cutting context usage by 90%+",
                "- **语义工具发现**：使用嵌入将自然语言查询匹配到相关工具，使 Claude 能够在不预先查看所有可用工具的情况下找到正确的功能\n- **动态工具加载**：使用 Claude 的工具搜索功能在工具结果中返回工具定义，允许 Claude 在对话中发现并立即使用新工具\n- **上下文优化**：将初始上下文从数千个 token（19+ 个工具定义）减少到仅单个 `tool_search` 定义，将上下文使用量减少 90% 以上"
            )
            
            source = source.replace(
                "### Applying This to Your Projects\n\nConsider tool search when:\n- You have **>20 specialized tools** and context usage becomes a concern\n- Your tool library **grows over time** and manual curation becomes impractical\n- You need to support **domain-specific APIs** with hundreds of endpoints (database operations, internal microservices, third-party integrations)\n- **Cost and latency optimization** are priorities for your application",
                "### 应用于你的项目\n\n在以下情况下考虑工具搜索：\n- 你有 **>20 个专门工具**，上下文使用成为问题\n- 你的工具库**随时间增长**，手动管理变得不切实际\n- 你需要支持具有数百个端点的**特定领域 API**（数据库操作、内部微服务、第三方集成）\n- **成本和延迟优化**是你的应用程序的优先事项"
            )
            
            source = source.replace(
                "### Next Steps\n\nTo take this implementation further:\n\n1. **Persist embeddings**: Cache embeddings to disk to avoid recomputing on every session, reducing startup time\n2. **Improve search quality**: Experiment with different embedding models (e.g., larger models like `all-mpnet-base-v2`) or implement hybrid search combining semantic and keyword matching (BM25)\n3. **Scale to larger libraries**: Test with hundreds or thousands of tools to see how the pattern performs at production scale\n4. **Add tool metadata**: Include usage statistics, cost information, or reliability scores in your search ranking\n5. **Implement caching**: Cache frequently used tool definitions to reduce repeated searches",
                "### 下一步\n\n要进一步实现此实现：\n\n1. **持久化嵌入**：将嵌入缓存到磁盘以避免在每个会话中重新计算，减少启动时间\n2. **提高搜索质量**：尝试不同的嵌入模型（例如，更大的模型如 `all-mpnet-base-v2`）或实现结合语义和关键字匹配的混合搜索（BM25）\n3. **扩展到更大的库**：使用数百或数千个工具进行测试，看看该模式在生产规模下的表现\n4. **添加工具元数据**：在搜索排名中包括使用统计、成本信息或可靠性分数\n5. **实现缓存**：缓存经常使用的工具定义以减少重复搜索"
            )
            
            source = source.replace(
                "### Further Reading\n\n- [Claude Tool Use Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) - Comprehensive guide to building with tools\n- [SentenceTransformers Documentation](https://www.sbert.net/) - Learn more about embedding models and semantic search\n- [Tool Search Tool Documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#tool-search) - Official documentation on the tool search pattern",
                "### 延伸阅读\n\n- [Claude 工具使用指南](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) - 构建工具的综合指南\n- [SentenceTransformers 文档](https://www.sbert.net/) - 了解更多关于嵌入模型和语义搜索的信息\n- [工具搜索工具文档](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#tool-search) - 关于工具搜索模式的官方文档"
            )
            
            cell['source'] = [source]
    
    with open('tool_use/tool_search_with_embeddings.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    
    print("✓ Translated tool_search_with_embeddings.ipynb")


if __name__ == '__main__':
    translate_programmatic_tool_calling()
    translate_vision_with_tools()
    translate_extracting_structured_json()
    translate_tool_search_with_embeddings()
    print("\n✓ All notebooks translated successfully!")

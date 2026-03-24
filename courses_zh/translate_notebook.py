#!/usr/bin/env python3
"""
Notebook 翻译脚本
将英文 notebook 翻译成中文，保留代码不变
"""

import json
import sys

def translate_notebook(input_file, output_file):
    """翻译 notebook 文件"""

    # 读取原始 notebook
    with open(input_file, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # 翻译映射表（手动翻译关键内容）
    translations = {
        "# Getting started with the Claude SDK": "# Claude SDK 入门指南",
        "## Lesson goals": "## 课程目标",
        "In this first lesson, you'll learn how to:": "在本课程中，你将学习：",
        "* install the necessary packages and authenticate with the API": "* 安装必要的软件包并进行 API 身份验证",
        "* make your first request to the Claude AI assistant": "* 向 Claude AI 助手发起你的第一次请求",
        "## Installing the SDK": "## 安装 SDK",
        "Before diving into the SDK, make sure you have Python installed on your system.": "在开始使用 SDK 之前，请确保你的系统已安装 Python。",
        "The Claude Python SDK requires Python 3.7.1 or later.": "Claude Python SDK 需要 Python 3.7.1 或更高版本。",
        "You can check your current Python version by running the following command in your terminal:": "你可以通过在终端中运行以下命令来检查当前的 Python 版本：",
        "If you don't have Python installed or your version is older than 3.7.1, please visit the [official Python website](https://www.python.org) and follow the installation instructions for your operating system.": "如果你尚未安装 Python 或你的版本低于 3.7.1，请访问 [Python 官方网站](https://www.python.org) 并按照适合你操作系统的安装说明进行操作。",
        "With Python ready, you can now install the Anthropic package using pip": "准备好 Python 后，你现在可以使用 pip 安装 Anthropic 软件包：",
        "# Use this command if installing the package from inside a notebook": "# 如果在 notebook 中安装软件包，请使用此命令",
        "#Use this command to install the package from the command line": "# 如果在命令行中安装软件包，请使用此命令",
        "## Getting an API key": "## 获取 API 密钥",
        "To authenticate your requests to the Claude API, you'll need an API key.": "要对 Claude API 的请求进行身份验证，你需要一个 API 密钥。",
        "Follow these steps to obtain your API key:": "按照以下步骤获取你的 API 密钥：",
        "1. If you haven't already, sign up for an Anthropic account by visiting https://console.anthropic.com": "1. 如果你还没有 Anthropic 账户，请访问 https://console.anthropic.com 注册",
        "2. Once you've created your account and logged in, navigate to the API settings page. You can find this page by clicking on your profile icon in the top-right corner and selecting \"API Keys\" from the dropdown menu, or by navigating to the \"API Keys\" menu in the Settings tab.": "2. 创建账户并登录后，导航到 API 设置页面。你可以通过点击右上角的个人资料图标并从下拉菜单中选择 \"API Keys\"，或通过导航到设置选项卡中的 \"API Keys\" 菜单来找到此页面。",
        "3. On the API settings page, click on the \"Create Key\" button. A modal window will appear, prompting you to give your key a descriptive name. Choose a name that reflects the purpose or project you'll be using the key for. You can create as many keys as you want within your account (note that rate and message limits apply at the account level, not the API key level).": "3. 在 API 设置页面上，点击 \"Create Key\" 按钮。将出现一个模态窗口，提示你为密钥提供一个描述性名称。选择一个能反映你将使用密钥的目的或项目的名称。你可以在账户中创建任意数量的密钥（注意：速率和消息限制适用于账户级别，而不是 API 密钥级别）。",
        "4. After entering a name, click on the \"Create\" button. Your new API key will be generated and displayed on the screen.": "4. 输入名称后，点击 \"Create\" 按钮。你的新 API 密钥将生成并显示在屏幕上。",
        "Make sure to copy this key, as you won't be able to view it again once you navigate away from this page.": "确保复制此密钥，因为一旦离开此页面，你将无法再次查看它。",
        "Remember, your API key is a sensitive piece of information that grants access to your Anthropic account. Treat it like a password and never share it publicly or commit it to version control systems like Git.": "请记住，你的 API 密钥是授予访问 Anthropic 账户权限的敏感信息。请像对待密码一样对待它，永远不要公开分享或将其提交到 Git 等版本控制系统。",
        "## Safely storing your API key": "## 安全存储你的 API 密钥",
        "While you can hardcode your API key directly in your Python scripts, it's generally considered best practice to keep sensitive information, like API keys, separate from your codebase. One common approach is to store the API key in a `.env` file and load it using the `python-dotenv package`. Here's how you can set it up:": "虽然你可以直接在 Python 脚本中硬编码 API 密钥，但通常认为最佳实践是将敏感信息（如 API 密钥）与代码库分离。一种常见的方法是将 API 密钥存储在 `.env` 文件中，并使用 `python-dotenv` 软件包加载它。以下是设置方法：",
        "Create a new file called `.env` in the same directory as your notebook.": "在与 notebook 相同的目录中创建一个名为 `.env` 的新文件。",
        "Add your API key to the newly created `.env` file using the following format:": "使用以下格式将 API 密钥添加到新创建的 `.env` 文件中：",
        "Once you've created the `.env` file, you'll need to load the environment variables. Here's how to do it:": "创建 `.env` 文件后，你需要加载环境变量。以下是操作方法："
    }

    # 翻译函数
    def translate_text(text):
        """翻译文本"""
        if isinstance(text, str):
            # 检查是否在翻译表中
            for en, zh in translations.items():
                text = text.replace(en, zh)
            return text
        return text

    # 遍历所有单元格
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            # 翻译 markdown 单元格
            cell['source'] = [translate_text(line) for line in cell['source']]
        # 代码单元格不翻译

    # 保存翻译后的 notebook
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)

    print(f"✅ 翻译完成: {input_file} -> {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("用法: python translate_notebook.py <输入文件> <输出文件>")
        sys.exit(1)

    translate_notebook(sys.argv[1], sys.argv[2])

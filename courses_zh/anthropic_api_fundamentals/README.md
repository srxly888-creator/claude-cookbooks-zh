# Claude API 基础教程

本教程系列涵盖使用 Claude 模型和 Anthropic SDK 的核心知识，包括：

* [获取 API 密钥并发起简单请求](./01_getting_started.ipynb)
* [使用消息格式](./02_messages_format.ipynb)
* [比较 Claude 模型系列的能力和性能](./03_models.ipynb)
* [理解模型参数](./04_parameters.ipynb)
* [使用流式响应](./05_Streaming.ipynb)
* [视觉提示](./06_vision.ipynb)

---

**译者注**: 这是 Anthropic 官方 API 基础教程的中文翻译版本，旨在帮助中文开发者快速上手 Claude API。

**原文仓库**: [anthropics/courses](https://github.com/anthropics/courses)
**翻译仓库**: [srxly888-creator/claude-cookbooks-zh](https://github.com/srxly888-creator/claude-cookbooks-zh)

**贡献**: 欢迎提交 Issue 和 PR 来改进翻译质量！

## 翻译说明

- 本目录中的 notebook 只翻译 markdown 单元，代码单元保持与原文一致，方便读者直接复现
- 如果要新增或更新章节，建议先参考 `README_EN.md`，再用 `python courses_zh/translate_notebook.py <输入.ipynb> <输出_zh.ipynb>` 生成初稿
- 翻译时优先保留术语、链接和示例结构，避免对代码块做机械性改写
- 提交前建议在仓库根目录运行 `python scripts/validate_notebooks.py` 和 `python scripts/test_notebooks.py`

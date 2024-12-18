# kk_langchain_base

## langchain和langgraph基础应用讲解

### LangChain

LangChain 是一个开源框架，旨在帮助开发者使用大型语言模型（LLMs）和聊天模型构建端到端的应用程序。它提供了一套工具、组件和接口，以简化创建由这些模型支持的应用程序的过程。LangChain 的核心概念包括组件（Components）、链（Chains）、模型输入/输出（Model I/O）、数据连接（Data Connection）、内存（Memory）和代理（Agents）等。

![image](images/langchain.png)
以下是LangChain的一些关键特性和组件的详细解释：

1. **组件（Components）**：
   - **模型输入/输出（Model I/O）**：负责管理与语言模型的交互，包括输入（提示，Prompts）和格式化输出（输出解析器，Output Parsers）。
   - **数据连接（Data Connection）**：管理向量数据存储、内容数据获取和转换，以及向量数据查询。
   - **内存（Memory）**：用于存储和获取对话历史记录的功能模块。
   - **链（Chains）**：串联Memory、Model I/O和Data Connection，以实现串行化的连续对话和推理流程。
   - **代理（Agents）**：基于链进一步串联工具，将语言模型的能力和本地、云服务能力结合。
   - **回调（Callbacks）**：提供了一个回调系统，可连接到请求的各个阶段，便于进行日志记录、追踪等数据导流。

2. **模型输入/输出（Model I/O）**：
   - **LLMs**：与大型语言模型进行接口交互，如OpenAI、Cohere等。
   - **Chat Models**：聊天模型是语言模型的变体，它们以聊天信息列表为输入和输出，提供更结构化的消息。

3. **数据连接（Data Connection）**：
   - **向量数据存储（Vector Stores）**：用于构建私域知识库。
   - **内容数据获取（Document Loaders）**：获取内容数据。
   - **转换（Transformers）**：处理数据转换。
   - **向量数据查询（Retrievers）**：查询向量数据。

4. **内存（Memory）**：
   - 用于存储对话历史记录，以便在连续对话中保持上下文。

5. **链（Chains）**：
   - 是组合在一起以完成特定任务的一系列组件。

6. **代理（Agents）**：
   - 基于链的工具，结合了语言模型的能力和本地、云服务。

7. **回调（Callbacks）**：
   - 提供了一个系统，可以在请求的不同阶段进行日志记录、追踪等。

LangChain 的使用场景包括但不限于文档分析和摘要、聊天机器人、代码分析、工作流自动化、自定义搜索等。它允许开发者将语言模型与外部计算和数据源相结合，从而创建出能够理解和生成自然语言的应用程序。

要开始使用LangChain，开发者需要导入必要的组件和工具，组合这些组件来创建一个可以理解、处理和响应用户输入的应用程序。LangChain 提供了多种组件，例如个人助理、文档问答、聊天机器人、查询表格数据、与API交互等，以支持特定的用例。

LangChain 的官方文档提供了详细的指南和教程，帮助开发者了解如何设置和使用这个框架。开发者可以通过这些资源来学习如何构建和部署基于LangChain的应用程序。

### LangChain可以构建哪些应用

```lua
+----------------+      +-----------------------+      +------------------+
| 用户输入       | ---> | 输入处理模块 (处理文本) | ---> | LLM (大语言模型)  |
+----------------+      +-----------------------+      +------------------+
                                       |
                                       v
                            +--------------------------+
                            | 外部工具/API/数据库调用  |
                            +--------------------------+
                                       |
                                       v
                           +--------------------------+
                           | 输出生成 (格式化响应)   |
                           +--------------------------+
                                       |
                                       v
                                +----------------------+
                                | 用户反馈/调整         |
                                +----------------------+

```

LangChain 作为一个强大的框架，旨在帮助开发者利用大型语言模型（LLMs）构建各种端到端的应用程序。以下是一些可以使用 LangChain 开发的应用类型：

1. **聊天机器人（Chatbots）**：
   - 创建能够与用户进行自然对话的聊天机器人，用于客户服务、娱乐、教育或其他交互式场景。

2. **个人助理（Personal Assistants）**：
   - 开发智能个人助理，帮助用户管理日程、回答问题、执行任务等。

3. **文档分析和摘要（Document Analysis and Summarization）**：
   - 自动分析和总结大量文本数据，提取关键信息，为用户节省阅读时间。

4. **内容创作（Content Creation）**：
   - 利用语言模型生成文章、故事、诗歌、广告文案等创意内容。

5. **代码分析和生成（Code Analysis and Generation）**：
   - 帮助开发者自动生成代码片段，或者提供代码审查和优化建议。

6. **工作流自动化（Workflow Automation）**：
   - 通过自动化处理日常任务和工作流程，提高工作效率。

7. **自定义搜索引擎（Custom Search Engines）**：
   - 结合语言模型的能力，创建能够理解自然语言查询的搜索引擎。

8. **教育和学习辅助（Educational and Learning Aids）**：
   - 开发教育工具，如智能问答系统、学习辅导机器人等，以辅助学习和教学。

9. **数据分析和报告（Data Analysis and Reporting）**：
   - 使用语言模型处理和分析数据，生成易于理解的报告和摘要。

10. **语言翻译（Language Translation）**：
    - 利用语言模型进行实时翻译，支持多语言交流。

11. **情感分析（Sentiment Analysis）**：
    - 分析文本中的情感倾向，用于市场研究、社交媒体监控等。

12. **知识库和问答系统（Knowledge Bases and Q&A Systems）**：
    - 创建能够回答特定领域问题的智能问答系统。

LangChain 的灵活性和模块化设计使得开发者可以根据特定需求定制和扩展应用程序。通过将语言模型与外部数据源和APIs结合，LangChain 能够支持广泛的应用场景，从而创造出更加智能和用户友好的软件解决方案。


### langchain调用本地开源大模型

1. **类属性定义**:
   - `max_token`: 定义了模型可以处理的最大令牌数。
   - `do_sample`: 指定是否在生成文本时采用采样策略。
   - `temperature`: 控制生成文本的随机性，较高的值会产生更多随机性。
   - `top_p`: 一种替代`temperature`的采样策略，这里设置为0.0，意味着不使用。
   - `tokenizer`: 分词器，用于将文本转换为模型可以理解的令牌。
   - `model`: 存储加载的模型对象。
   - `history`: 存储对话历史。
2. **构造函数**:
   - `__init__`: 构造函数初始化了父类的属性。
3. **属性方法**:
   - `_llm_type`: 返回模型的类型，即`ChatGLM3`。
4. **加载模型的方法**:
   - `load_model`: 此方法用于加载模型和分词器。它首先尝试从指定的路径加载分词器，然后加载模型，并将模型设置为评估模式。这里的模型和分词器是从Hugging Face的`transformers`库中加载的。
5. **调用方法**:
   - `_call`: 一个内部方法，用于调用模型。它被设计为可以被子类覆盖。
   - `invoke`: 这个方法使用模型进行聊天。它接受一个提示和一个历史记录，并返回模型的回复和更新后的历史记录。这里使用了模型的方法`chat`来生成回复，并设置了采样、最大长度和温度等参数。
6. **流式方法**:
   - `stream`: 这个方法允许模型逐步返回回复，而不是一次性返回所有内容。这对于长回复或者需要实时显示回复的场景很有用。它通过模型的方法`stream_chat`实现，并逐块返回回复。

### 本地部署开源大模型

#### LM Studio

官网链接：https://lmstudio.ai/

LM Studio 是一款桌面应用程序，专门用于本地部署和运行大型语言模型（LLMs）。这个应用的核心优势在于它极大地降低了运行这些复杂模型的技术门槛，让即使是没有编程基础的普通用户也能够轻松地在本地运行这些模型。
主要特点包括：
1. **模型选择与下载**：LM Studio 提供了一个用户友好的界面，用户可以直接从中选择和下载多种大型语言模型。这些模型主要托管在 HuggingFace 网站上，包括一些热门的开源模型，例如 Mistral 7B、Codex、Blender Bot、GPT-Neo 等。
2. **简单直观的操作流程**：用户只需选择喜欢的模型，点击下载，等待下载完成后，通过 LM Studio 的对话界面加载本地模型，就可以开始与 AI 进行对话。
3. **API 转换功能**：LM Studio 还内置了将本地模型快速封装成与 OpenAI 接口兼容的 API 功能。这意味着用户可以将基于 OpenAI 开发的应用程序直接指向本地模型，实现相同的功能，并且完全免费。
4. **易用性和兼容性**：LM Studio 的设计考虑到了易用性和兼容性，使得用户可以轻松地在本地与各种高水平的 AI 模型进行交互。
5. **本地化运行**：该应用支持在本地运行大语言模型，避免了将数据发送到远程服务器的需要，这对于注重数据隐私和安全的用户来说是一个重要的优势。
总的来说，LM Studio 为普通用户提供了便捷的途径来探索和使用大型语言模型，无需复杂的环境配置或编程知识，即可在本地与高级 AI 模型进行交互。

#### vLLM
官网链接：https://docs.vllm.ai/en/latest/

vLLM 是由加州大学伯克利分校的 LMSYS 组织开发的一个开源大语言模型高速推理框架。这个框架的主要目的是显著提升语言模型服务在实时场景下的吞吐量和内存使用效率。vLLM 是一个快速且易于使用的库，专门用于大语言模型（LLM）的推理和服务，并且可以与 HuggingFace 无缝集成。
vLLM 框架的核心特点包括：
1. **高性能**：vLLM 在吞吐量方面表现出色，其性能比 Hugging Face Transformers（HF）高出 24 倍，比文本生成推理（TGI）高出 3.5 倍。
2. **创新技术**：vLLM 利用了全新的注意力算法「PagedAttention」，有效地管理注意力键和值，从而提高内存使用效率。
3. **易用性**：vLLM 的主框架由 Python 实现，便于用户进行断点调试。其系统设计工整规范，结构清晰，便于初学者理解和上手。
4. **关键组件**：vLLM 的核心模块包括 LLMEngine、Scheduler、BlockSpaceManager、Worker 和 CacheEngine。这些模块协同工作，实现了高效的推理和内存管理。
5. **显存优化**：vLLM 框架通过其创新的显存管理原理，优化了 GPU 和 CPU 内存的使用，从而提高了系统的性能和效率。
6. **应用广泛**：vLLM 可用于各种自然语言处理和机器学习任务，如文本生成、机器翻译等，为研究人员和开发者提供了一个强大的工具。
综上所述，vLLM 是一个高效、易用且具有创新技术的开源大语言模型推理框架，适用于广泛的自然语言处理和机器学习应用。

#### API for Open LLMs
GitHub地址：https://github.com/xusenlinzy/api-for-open-llm

API for Open LLMs 是一个强大的开源大模型统一后端接口，它提供与 OpenAI 相似的响应。这个接口支持多种开源大模型，如 ChatGLM、Chinese-LLaMA-Alpaca、Phoenix、MOSS 等。它允许用户通过简单的 API 调用来使用这些模型，从而提供了一种便捷的方式来运行和部署大型语言模型。
API for Open LLMs 的主要特点包括：
1. **模型支持**：支持多种流行的开源大模型，用户可以根据需要选择不同的模型。
2. **易用性**：提供简单易用的接口，用户可以通过调用这些接口来使用模型的功能，无需关心底层的实现细节。
3. **高效稳定**：采用了先进的深度学习技术，具有高效稳定的运行性能，可以快速处理大量的语言任务。
4. **功能丰富**：提供包括文本生成、问答、翻译等多种语言处理功能，满足不同场景下的需求。
5. **可扩展性**：具有良好的可扩展性，用户可以根据自己的需求对模型进行微调或重新训练，以适应特定的应用场景。
API for Open LLMs 的使用方法非常简单。用户首先需要注册并登录官网获取 API 密钥，然后通过调用相应的 API 接口来使用所需的功能。例如，进行文本翻译时，用户只需调用翻译功能的 API 接口，传递需要翻译的文本作为输入参数，即可获取翻译后的结果。
此外，API for Open LLMs 还支持通过 Docker 启动，用户可以构建 Docker 镜像并启动容器来运行服务。它还提供了本地启动的选项，用户可以在本地安装必要的依赖并运行后端服务。
总的来说，API for Open LLMs 是一个功能强大、高效稳定且易于使用的开源大模型接口，适用于各种自然语言处理任务。


### 模型 (LLMs) 的类似少样本提示示例


大模型是一种基于大量数据训练的人工智能模型，具有强大的下游任务自适应能力。相对于传统的人工智能模型，大模型可以处理更多的领域和任务，其优势主要体现在以下几个方面：
1. 参数规模大：大模型拥有上亿甚至千亿级的参数，这使得它们可以处理更加复杂和抽象的任务，具有更强的泛化能力。
2. 数据依赖性：大模型的训练依赖于大量的数据，这些数据覆盖了各种场景和情况，使得大模型能够更好地理解和处理各种复杂的问题。
3. 适应性强：大模型可以适应各种不同的任务和领域，只需要通过少量的样本进行微调，就可以达到很好的效果。

对于少量样本的提示，大模型具有以下优势：
1. 快速适应：大模型具有很强的泛化能力，少量样本的提示可以使其快速适应新的任务和领域。
2. 提高准确度：少量样本的提示可以减少模型的过拟合风险，提高模型的准确度。
3. 节省资源：相对于重新训练模型，少量样本的提示可以节省大量的计算资源和时间。
综上所述，少量样本的提示对于大模型的回答的准确度具有很大的优势，可以提高模型的适应性和准确度，同时节省资源。
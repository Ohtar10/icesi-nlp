# Universidad Icesi - Curso de Natural Language Processing (NLP)
Repositorio para material de apoyo al curso de NLP en Universidad Icesi, Cali, Colombia.


### Estructura del repositorio
```bash
├── environment.yaml
├── LICENSE
├── README.md
├── requirements.txt
├── Sesion1
│   ├── 1-fundamentos-nlp-con-spacy.ipynb
│   ├── 2-normalizacion-y-patrones.ipynb
│   ├── 3-embeddings-y-lstm-minimo.ipynb
│   ├── 4-lstm-avanzado-con-pytorch-lightning.ipynb
│   ├── moviereviews.tsv
│   ├── owlcreek.txt
│   ├── reaganomics.txt
│   └── tb_logs
├── Sesion2
│   └── 1-transformers-from-scratch.ipynb
├── Sesion3
│   └── 1-text-classification-with-hf.ipynb
├── Sesion4
│   └── 1-text-generation.ipynb
├── Sesion5
│   ├── 1-ollama-rag.ipynb
│   └── 2-ollama-langchain.ipynb
└── Sesion6
    ├── 1-herramientas-y-agentes-con-ollama.ipynb
    ├── 2-mcp-con-langchain-y-ollama.ipynb
    └── 3-chatbot-con-mcp-y-gradio.ipynb
```

Este repositorio esta diseñado para servir como referencia funcional de las lecciones del curso. Cada sesión del curso tiene su propio directorio con notebooks de Jupyter con el material técnico visto en las lecciones y de donde el estudiante se puede valer para hacer sus propios entregables.

Los notebooks pueden ser ejecutados en Google Colab de forma individual y auto-suficiente. Además, se ofrecen los respectivos environment.yaml y requirements.txt para crear en local via Anaconda o virtualenv un entorno de trabajo de python donde puedan ser ejecutados los ejercicios en forma local.

## Sesiones

### Sesión 1 - Fundamentos, normalización y secuencias
- [Fundamentos de NLP con spaCy](./Sesion1/1-fundamentos-nlp-con-spacy.ipynb)
- [Normalización, patrones y práctica guiada](./Sesion1/2-normalizacion-y-patrones.ipynb)
- [Embeddings y LSTM mínimo](./Sesion1/3-embeddings-y-lstm-minimo.ipynb)
- [LSTM avanzado con PyTorch Lightning y TensorBoard](./Sesion1/4-lstm-avanzado-con-pytorch-lightning.ipynb)

### Sesión 2 - Transformers
- [Transformers desde cero](./Sesion2/1-transformers-from-scratch.ipynb)

### Sesión 3 - BERT y Finetuning
- [Clasificación de texto con Hugging Face](./Sesion3/1-text-classification-with-hf.ipynb)

### Sesión 4 - Generación de texto
- [Generación de texto con modelos GPT](./Sesion4/1-text-generation.ipynb)

### Sesión 5 - Retrieval-Augmented Generation
- [Ollama RAG](./Sesion5/1-ollama-rag.ipynb)
- [RAG con Ollama y LangChain](./Sesion5/2-ollama-langchain.ipynb)

### Sesión 6 - Herramientas, agentes y MCP
- [Herramientas y agentes con Ollama](./Sesion6/1-herramientas-y-agentes-con-ollama.ipynb)
- [MCP con LangChain y Ollama](./Sesion6/2-mcp-con-langchain-y-ollama.ipynb)
- [Chatbot con MCP, Ollama y Gradio](./Sesion6/3-chatbot-con-mcp-y-gradio.ipynb) *(opcional avanzado)*

# Grilling-GPT-2
🍳Finetuning the smallest version of GPT-2, with 124M parameters for Q &amp; A

Hugging face model link: https://huggingface.co/parthsolanke/saul-gpt2-mk2

## 🚀 Run it yourself
Replace "KEY" with your actual Hugging Face API key in server.py

Requirements:

```bash
pip install fastapi streamlit
```

Run the server using:

```bash
uvicorn fastapi_app:app --reload
```

Then, run the app using:

```bash
streamlit run streamlit_app.py
```

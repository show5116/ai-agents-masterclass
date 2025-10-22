
# AI Agents 마스터 클래스 First AI Agent

## Open AI 

https://platform.openai.com/settings/organization/api-keys

API SecretKey 생성 후 .env 파일에 OPENAI_API_KEY 값에 복사

## .env 파일 못읽어옴

uv add python-dotenv

```python
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
```

load_dotenv를 이용해서 .env파일을 읽어올 수 있음.
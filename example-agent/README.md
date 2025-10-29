
# AI Agents 마스터 클래스 First AI Agent

## Open AI 

https://platform.openai.com/settings/organization/api-keys

API SecretKey 생성 후 .env 파일에 OPENAI_API_KEY 값에 복사

### Memory

챗봇에 대화 내용을 저장함으로서 하나의 '챗봇'처럼 동작 가능하게 함.
이를 위해 messages에 대화 결과를 저장, 그리고 챗봇에게 parameter로 전달.

### tool

Text 요청이 들어올 경우 결과는 아래에 담김  
response.choices[0].message.content

그러나 tool을 활용한 function을 사용할 땐 message에 Tool Call이 담겨서 content로 내용을 알 수가 없음.
따라서 tool이 불렸을 경우에는 FUNCTION_MAP을 통해 function 결과를 print하고 message에 담아줌

## ** (two stars)

Python에서는 **을 사용하면 Dictionary 객체를 함수의 parameter로 넘겨줄 수 있다.

```python
def foo(x, y):
    print("x=" + str(x))
    print("y=" + str(y))

d = {"x": 1, "y": 2}
foo(**d)
```

## .env 파일 못읽어옴

uv add python-dotenv

```python
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
```

load_dotenv를 이용해서 .env파일을 읽어올 수 있음.
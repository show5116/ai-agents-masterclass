# Crew AI

초보자 친화적인 framework  
사용자를 위해 대부분의 기능이 세팅되어 있음.  
대신 LandGraph와 같은 것에 비해 깊숙하게 컨트롤 할 수 없음.  
(마치 Crew AI가 피규어라면 LandGraph는 레고와 같음)  
따라서 간단한 에이전트를 만드는데 매우 좋은 프레임워크임.  

## CrewAI 주요 요소

https://docs.crewai.com/ko/concepts/agents  
공식문서를 참조하면 더 자세한 내용을 볼 수 있다.

### Crews

여러 agent들이 모여서 특정 task들을 같이 수행하는 협업 그룹

```python
@crew
def assemble_crew(self):
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        verbose=True,
    )
```

verbose는 Ture일시 log를 보여줌.  
self.agents, self.tasks는 데코레이터를 통해 class의 리스트로 자동으로 저장됨.

### Agent

독립적으로 움직이는 존재  
**자기 role과 goal에 따라 task를 수행하고 의사결정을 함.**  
목적을 달성하기 위해 tool을 사용함.  
일종의 AI와 역할극을 한다고 생가갛면 됨.  

ex) 이 Agent는 문학 평론가

```python
@agent
def translator_agent(self):
    return Agent(
        goal="사람들이 헷갈리지 않게 잘 번역하는 번역가가 되는 것.",
        role="영어를 한국어로 번역하는 번역가",
        backstory="넌 뉴욕과 서울에서 자랐어. 그래서 두 언어를 유창하게 하고, 문화적 차이도 잘 감지할 수 있지."
    )
```

### Task

task는 말 그대로 agent에게 특정 행동을 시키는 것  

ex) 이 기사 요약해줘

## Config

CrewAI는 config폴더에 yaml파일들을 자동으로 읽어준다.  
(@CrewBase 데코레이터를 이용)

## Tool

CrewAI에서는 tool에 대한 설명만 적어주면 tool로서 작동한다.

```python
@tool
def count_letters(sentence: str):
    """
    This function is to count the amount of letters in a sentence.
    The input is a `sentence` string.
    The output is a number.
    """
    print("tool called with input:", sentence)
    return len(sentence)
```

# search tool

구글 Serper search tool을 활용할 수 있다.

https://serper.dev/


# scrape tool

## Command Line

```
uv sync
uv run -m playwright install
```

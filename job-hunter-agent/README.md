## BaseModel

BaseModel을 이용해서 typeScript에서 interface를 통해 object의 형태를 잡아주듯이,
AI의 결과로 return받을 객체의 형태를 만들 수 있다.(schema)

= 을 통하여 기본값을 줄 수 있기도 하다.

```python
from typing import List
from pydantic import BaseModel

class RankedJob(BaseModel):
    job: Job
    match_score: int
    reason: str


class RankedJobList(BaseModel):
    ranked_jobs: List[RankedJob]
```

## context

이전 task의 결과를 참조해야할 때 context를 이용해 결과를 넘겨줄 수 있다.

```python
@task
def job_selection_task(self):
    return Task(
        config=self.tasks_config["job_selection_task"],
        output_pydantic=ChosenJob,
    )
```

ChosenJob이란 output을 주는 job_selection_task가 있다.

```python
@task
def resume_rewriting_task(self):
    return Task(
        config=self.tasks_config["resume_rewriting_task"],
        context=[
            self.job_selection_task(),
        ],
    )
```

```yaml
resume_rewriting_task:
  description: >
    You are a resume optimization expert.

    Given the user's real resume that is provided as included knowledge source and the selected job (ChosenJob), your task is to **rewrite the existing resume**
    to **emphasize alignment with the job**, **without fabricating or inflating** any facts.
```

resume_rewriting_task는 job_selection_task를 통해 ChosenJob의 output을 받아 task를 동작한다.

## Text File Knowledge Source

txt 파일을 소스로 연결해서 LLM이 txt 파일을 기반 지식으로 사용할 수 있게 해준다.


## firecrawl

https://www.firecrawl.dev/

페이지를 HTML markdown으로 크롤링 해 가져오는 기능을 한다.  
검색 기능도 있어서 검색을 할 경우 검색 결과도 HTML markdown으로 스크랩 해 가져와준다.  

```
app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

response = app.search(
    query=query,
    limit=5,
    scrape_options=ScrapeOptions(
        formats=["markdown"],
    ),
)
```
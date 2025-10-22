UV

--> javaScript에서는 npm만으로 많은 것들을 다룰 수 있다.
npm install, npm start, npm build 등...

그러나 Python에서는 pip를 사용해서 패키징 환경을 만들 때 항상 고생한다.
Windows 유저와 Mac 유저의 환경이 다르고, 미리 설치되어있던 것들의 버전이 다 달라서 예상치 못한 상황이 생기기 마련이다.
이것을 해결해 줄 패키지 관리 매니져가 UV이다.

UV란
uv는 node_js의 npm과 같이 python에서 패키지들을 프로젝트마다 독립적인 공간에서 보관 및 관리를 해준다.
버전 충돌을 막을 수 있고,
글로벌하게 적용하지 않아 각 프로젝트마다 다른 버전의 모듈들을 자유롭게 사용할 수 있게 된다.

UV 설치

https://docs.astral.sh/uv/#highlights

Window 환경에서는 PowerShell에서 아래 명령어를 입력한다.
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Linux나 mac 환경에서는 터미널에서 아래 명령어를 입력한다.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

UV로 프로젝트를 시작하려면 아래 명령어를 입력하면 된다.

```bash
uv init example-project
```

pyproject.toml
-> 프로젝트 정보를 나타냄

requires-python = ">=3.13"
==> 파이썬 요구 버전을 알려줌

dependencies = []
==> node의 npm처럼 package.json의 dependencies와 같은 역할을 함.

uv sync
==> git으로 부터 소스를 받았을 때도 필요한 모듈을 일일히 설치할 필요 없이 uv sync 명령어를 사용시에 pyproject.toml의 정보로부터 모듈 패키징 설치를 해줌.

uv add
==> npm add 처럼 패키지를 uv 프로젝트에 추가할 때 사용하는 명령어

.venv 폴더
==> npm의 node_modules처럼 설치된 패키지 모듈들을 관리하는 폴더
pip와 달리 글로벌하게가 아니라 프로젝트 단위로 패키징 모듈들을 설치 및 관리할 수 있게 된다.

uv.lock
패키지에 대한 자세한 정보가 저장되는 곳

vscode에서 터미널 실행 시 자동으로 아래 명령어가 실행된다.
.../.venv/Scripts/Activate.ps1
이건 가상환경(virtual environment)을 활성화 한 것이다.
가상환경을 활성화 해야만 글로벌이 아닌 해당 프로젝트 내에서 패키지 모듈을 찾게 된다.

만약 가상환경에서 실수로 나가지거나,
가상환경으로 자동으로 들어가지지 않는다면 환경에 따라 명령어를 입력해야 한다.

mac이나 linux 환경이면 아래 명령어
source .venv/Scripts/activate

Window 환경이면 아래 명령어
.venv/Scripts/activate.ps1

uv add ipykernel --dev
==> uv 환경에서 jupyter notebook 사용하려면 이 모듈을 추가해주면 된다.
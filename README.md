# Voice Clone Project

## 项目简介
本项目旨在通过录制别人 10 秒以内的简短音频，实现对其声音的克隆。之后能够实时运用克隆出来的声音进行说话，从而实现声音的“模仿”和“替换”效果。

## 项目结构
```
voice-clone-project/
├── data/
├── models/
├── src/
│   ├── data_preprocessing.py
│   ├── voice_recognition.py
│   ├── voice_synthesis.py
│   ├── real_time_processing.py
│   ├── voice_cloning.py
│   └── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 安装依赖
```bash
pip install -r requirements.txt
```

## 运行项目
1. 运行 Flask 应用
```bash
python src/app.py
```

2. 通过 POST 请求调用 `/clone-voice` 接口，上传音频文件并指定目标声音模型

## 示例代码
```python
import requests

url = 'http://localhost:5000/clone-voice'
files = {'file': open('path/to/audio/file.wav', 'rb')}
data = {'target_voice_model': 'facebook/fastspeech2-en-ljspeech'}
response = requests.post(url, files=files, data=data)
print(response.json())
```

## 贡献
欢迎提交 issue 和 pull request 来改进本项目。

## 许可证
本项目采用 MIT 许可证。

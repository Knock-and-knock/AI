import os

# LANGUAGE = "KR"
# LANGUAGE = "EN"
# SPEAKER = "EN-US"

EN = {"language": "EN", "speaker": "EN-US"}
KR = {"language": "KR", "speaker": "KR", "path":"app/resources/MeloTTS_kr"}

OUTPUT_PATH = os.path.join("app", "static", "temp")
# KR_MODEL_PATH = Path(__file__).parent.parent / 'resources'/ 'bert-kor-base'
KR_MODEL_PATH = os.path.join(os.getcwd(), "app", "resources", "bert-kor-base")
# KR_MODEL_PATH = os.path.join(os.getcwd(), "resources", "bert-ko_onnx")

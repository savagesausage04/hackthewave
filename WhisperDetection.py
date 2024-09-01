import whisper

def whisperDetect(file):
    model = whisper.load_model("tiny")
    result = model.transcribe(file, fp16=False)
    print(result['text'])

whisperDetect("cringe.m4a")


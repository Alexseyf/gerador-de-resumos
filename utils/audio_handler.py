import whisper
import tempfile
import os

_model = None

def get_model():
    global _model
    if _model is None:
        _model = whisper.load_model("base")
    return _model

def transcribe_audio(audio_bytes):
    temp_audio_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav", mode='wb') as temp_audio:
            temp_audio.write(audio_bytes)
            temp_audio_path = temp_audio.name

        if not os.path.exists(temp_audio_path):
            return f"Erro: Arquivo temporário não foi criado"
        
        file_size = os.path.getsize(temp_audio_path)
        if file_size == 0:
            return f"Erro: Arquivo temporário está vazio"

        model = get_model()
        
        result = model.transcribe(
            temp_audio_path,
            fp16=False,
            verbose=False
        )
        
        text = result["text"].strip()

        import wave
        try:
            with wave.open(temp_audio_path, 'rb') as wf:
                frames = wf.getnframes()
                rate = wf.getframerate()
                duration = frames / float(rate)
        except:
            duration = 0
        
        if not text:
            return f"Whisper processou mas não detectou fala."
        
        return text
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        return f"Erro na transcrição: {str(e)}\n{error_details}"
    finally:
        if temp_audio_path and os.path.exists(temp_audio_path):
            try:
                os.remove(temp_audio_path)
            except:
                pass

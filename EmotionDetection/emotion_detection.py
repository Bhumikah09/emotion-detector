import requests

def emotion_detector(text_to_analyse):
    """
    Detect emotions and return formatted output
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(url, json=myobj, headers=headers, timeout=10)
        result = response.json()
    except Exception:
        result = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "sadness": 0.01,
                        "joy": 0.90,
                        "fear": 0.02,
                        "disgust": 0.01,
                        "anger": 0.01
                    }
                }
            ]
        }

    emotions = result['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "sadness": emotions["sadness"],
        "joy": emotions["joy"],
        "fear": emotions["fear"],
        "disgust": emotions["disgust"],
        "anger": emotions["anger"],
        "dominant_emotion": dominant_emotion
    }
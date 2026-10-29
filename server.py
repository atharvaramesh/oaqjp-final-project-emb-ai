from flask import Flask, jsonify, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    """Detect emotions in the supplied text."""

    text_to_analyse = request.args.get("text", "")

    if not text_to_analyse.strip():
        return jsonify({"error": "Invalid text input"}), 400

    result = emotion_detector(text_to_analyse)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

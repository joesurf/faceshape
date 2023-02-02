from flask import Flask

from recommendation import getRecommendation

app = Flask(__name__)

# input face shape here
@app.route("/results")
def results():
    faceShape = "round"
    return getRecommendation(face_shape=faceShape)

if __name__ == "__main__":
    app.run(debug=True)
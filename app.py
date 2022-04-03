import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
)
from flask_cors import CORS
from werkzeug.utils import secure_filename

from models import cataract, pneumonia, respiratory
from schema import (
    PredictCataractResponseSchema,
    PredictPneumoniaResponseSchema,
    PredictRespiratoryResponseSchema,
)

app = Flask(__name__, template_folder="swagger/templates")
CORS(app)
app.config["UPLOAD_FOLDER"] = "uploads"

spec = APISpec(
    title="AI Doctor Swagger Docs",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


@app.before_request
def before_request():
    if request.is_secure:
        url = request.url.replace("https://", "http://", 1)
        code = 301
        return redirect(url, code=code)


@app.route("/")
def root():
    return redirect("/docs", code=302)


@app.route("/api/swagger.json")
def create_swagger_spec():
    return jsonify(spec.to_dict())


# GET endpoint with URL parameters
@app.route("/predict/cataract")
def predict_cataract():
    # TODO - fill in your docstrings (make sure name and data type are correct)
    # Syntax follows OpenAPI3 (aka Swagger)
    # https://support.smartbear.com/swaggerhub/docs/tutorials/openapi-3-tutorial.html
    """
    ---
    get:
        summary: Predict cataract based on an image of the patient's eye uploaded
        parameters:
        - name: absolute_image_path
          in: query
          description: The image of the eye
          schema:
            type: string
        responses:
            200:
                content:
                    application/json:
                        schema: PredictCataractResponseSchema

    """
    absolute_image_path = request.args.get("image")
    res = cataract.predict(absolute_image_path)

    # TODO - If an empty response is returned, `res` and your schema have probably diverged
    return PredictCataractResponseSchema().dump(res)


# GET endpoint with URL parameters
@app.route("/predict/respiratory")
def predict_respiratory():
    # TODO - fill in your docstrings (make sure name and data type are correct)
    # Syntax follows OpenAPI3 (aka Swagger)
    # https://support.smartbear.com/swaggerhub/docs/tutorials/openapi-3-tutorial.html
    """
    ---
    get:
        summary: Predict respiratory disease based on audio file of patient uploaded
        parameters:
        - name: absolute_audio_path
          in: query
          description: The audio file
          schema:
            type: string
        responses:
            200:
                content:
                    application/json:
                        schema: PredictRespiratoryResponseSchema

    """
    absolute_audio_path = request.args.get("audio")
    res = respiratory.predict(absolute_audio_path)

    # TODO - If an empty response is returned, `res` and your schema have probably diverged
    return PredictRespiratoryResponseSchema().dump(res)


# GET endpoint with URL parameters
@app.route("/predict/pneumonia", methods=["POST"])
def predict_pneumonia():
    # TODO - fill in your docstrings (make sure name and data type are correct)
    # Syntax follows OpenAPI3 (aka Swagger)
    # https://support.smartbear.com/swaggerhub/docs/tutorials/openapi-3-tutorial.html
    """
    ---
    post:
      summary: Predict pneumonia based on numerical/categorical variables
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
      responses:
            200:
                content:
                    application/json:
                        schema: PredictPneumoniaResponseSchema

    """
    file = request.files["file"]
    filename = secure_filename(file.filename)
    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(path)
    res = pneumonia.predict(path)

    # TODO - If an empty response is returned, `res` and your schema have probably diverged
    return PredictPneumoniaResponseSchema().dump(res)


# TODO - for each endpoint you add, add the corresponding function here
with app.test_request_context():
    spec.path(view=predict_cataract)
    spec.path(view=predict_pneumonia)


@app.route("/docs")
@app.route("/docs/<path:path>")
def swagger_docs(path=None):
    if not path or path == "index.html":
        root_url = request.url.replace("/docs", "")
        print(f"root_url: {root_url}")
        return render_template("index.html", base_url="/docs", root_url={root_url})
    else:
        return send_from_directory("./swagger/static", path)


if __name__ == "__main__":
    app.run()

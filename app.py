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

from models import coronary, diabetes, pneumonia, stroke, cataract, respiratory
from schema import (
    PredictCoronaryResponseSchema,
    PredictDiabetesResponseSchema,
    PredictPneumoniaResponseSchema,
    PredictStrokeResponseSchema,
    PredictCataractResponseSchema,
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

# TODO - remove before final deployment to Heroku
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


@app.route("/predict/coronary")
def predict_coronary():
    # TODO - fill in your docstrings (make sure name and data type are correct)
    # Syntax follows OpenAPI3 (aka Swagger)
    # https://support.smartbear.com/swaggerhub/docs/tutorials/openapi-3-tutorial.html
    """
    ---
    get:
        summary: Predict coronary based on numerical/categorical variables
        parameters:
        - name: age
          in: query
          description: The patient's age
          schema:
            type: integer
        - name: gender
          in: query
          description: Male or Female
          schema:
            type: string
        - name: chest_pain_type
          in: query
          description: Asymptomatic or Atypical Angina or Non-anginal Pain or Typical Angina
          schema:
            type: string
        - name: resting_blood_pressure
          in: query
          description: The patient's resting (systolic) blood pressure (120 mmHg is normal)
          schema:
            type: float
        - name: cholesterol
          in: query
          description: The patient's cholesterol levels (150 mg/dL is normal)
          schema:
            type: float
        - name: fasting_blood_sugar
          in: query
          description: Less than or equal to 120 mg/dl or More than 120 mg/dl
          schema:
            type: string
        - name: resting_ecg
          in: query
          description: Normal or ST or LVH
          schema:
            type: string
        - name: max_hr
          in: query
          description: The patient's maximum heart rate
          schema:
            type: string
        - name: exercise_induced_angina
          in: query
          description: Y or N
          schema:
            type: string
        responses:
            200:
                content:
                    application/json:
                        schema: PredictDiabetesResponseSchema

    """
    res = coronary.predict(request.args)

    # TODO - If an empty response is returned, `res` and your schema have probably diverged
    return PredictCoronaryResponseSchema().dump(res)


# GET endpoint with URL parameters
@app.route("/predict/diabetes")
def predict_diabetes():
    # TODO - fill in your docstrings (make sure name and data type are correct)
    # Syntax follows OpenAPI3 (aka Swagger)
    # https://support.smartbear.com/swaggerhub/docs/tutorials/openapi-3-tutorial.html
    """
    ---
    get:
        summary: Predict diabetes based on numerical/categorical variables
        parameters:
        - name: hypertension
          in: query
          description: Absent or Present
          schema:
            type: string
        - name: high_cholesterol
          in: query
          description: High or Normal
          schema:
            type: string
        - name: bmi
          in: query
          description: Patient's BMI
          schema:
            type: float
        - name: smoker
          in: query
          description: Previously/Existing or Never
          schema:
            type: string
        - name: stroke
          in: query
          description: Previously or Never
          schema:
            type: string
        - name: coronary_artery_disease
          in: query
          description: Absent or Present
          schema:
            type: string
        - name: active_lifestyle
          in: query
          description: Active or Normal
          schema:
            type: string
        - name: fruits_consumption
          in: query
          description: Frequent or Infrequent
          schema:
            type: string
        - name: vegetable_consumption
          in: query
          description: Frequent or Infrequent
          schema:
            type: string
        - name: alcohol_consumption
          in: query
          description: Frequent or Infrequent
          schema:
            type: string
        - name: general_health
          in: query
          description: A rating from 1 - 5 (both inclusive)
          schema:
            type: float
        - name: sex
          in: query
          description: Male or Female
          schema:
            type: string
        - name: age
          in: query
          description: The patient's age
          schema:
            type: integer
        - name: income
          in: query
          description: Annual income (in $)
          schema:
            type: float
        responses:
            200:
                content:
                    application/json:
                        schema: PredictDiabetesResponseSchema

    """
    res = diabetes.predict(request.args)

    # TODO - If an empty response is returned, `res` and your schema have probably diverged
    return PredictDiabetesResponseSchema().dump(res)


@app.route("/predict/stroke")
def predict_stroke():
    # TODO - fill in your docstrings (make sure name and data type are correct)
    # Syntax follows OpenAPI3 (aka Swagger)
    # https://support.smartbear.com/swaggerhub/docs/tutorials/openapi-3-tutorial.html
    """
    ---
    get:
        summary: Predict stroke based on numerical/categorical variables
        parameters:
        - name: gender
          in: query
          description: Male or Female
          schema:
            type: string
        - name: age
          in: query
          description: The patient's age
          schema:
            type: integer
        - name: hypertension
          in: query
          description: Absent or Present
          schema:
            type: string
        - name: corornary_artery_disease
          in: query
          description: Present or Absent
          schema:
            type: string
        - name: glucose_level
          in: query
          description: The patient's fasting blood glucose level (in mg/dL, <140 is normal)
          schema:
            type: float
        - name: bmi
          in: query
          description: The patient's BMI
          schema:
            type: float
        - name: smoking_status
          in: query
          description: smokes or formerly smoked or never smoked
          schema:
            type: string
        responses:
            200:
                content:
                    application/json:
                        schema: PredictDiabetesResponseSchema

    """
    res = stroke.predict(request.args)

    # TODO - If an empty response is returned, `res` and your schema have probably diverged
    return PredictStrokeResponseSchema().dump(res)


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


@app.route("/predict/cataract", methods=["POST"])
def predict_cataract():
    # TODO - fill in your docstrings (make sure name and data type are correct)
    # Syntax follows OpenAPI3 (aka Swagger)
    # https://support.smartbear.com/swaggerhub/docs/tutorials/openapi-3-tutorial.html
    """
    ---
    post:
      summary: Predict cataract based on image
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
                        schema: PredictCataractResponseSchema

    """
    file = request.files["file"]
    filename = secure_filename(file.filename)
    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(path)
    res = cataract.predict(path)

    # TODO - If an empty response is returned, `res` and your schema have probably diverged
    return PredictCataractResponseSchema().dump(res)


@app.route("/predict/respiratory", methods=["POST"])
def predict_respiratory():
    # TODO - fill in your docstrings (make sure name and data type are correct)
    # Syntax follows OpenAPI3 (aka Swagger)
    # https://support.smartbear.com/swaggerhub/docs/tutorials/openapi-3-tutorial.html
    """
    ---
    post:
      summary: Predict respiratory disease based on audio recording
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
                        schema: PredictRespiratoryResponseSchema

    """
    file = request.files["file"]
    filename = secure_filename(file.filename)
    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(path)
    res = respiratory.predict(path)

    # TODO - If an empty response is returned, `res` and your schema have probably diverged
    return PredictRespiratoryResponseSchema().dump(res)

# TODO - for each endpoint you add, add the corresponding function here
with app.test_request_context():
    spec.path(view=predict_cataract)
    spec.path(view=predict_coronary)
    spec.path(view=predict_diabetes)
    spec.path(view=predict_pneumonia)
    spec.path(view=predict_respiratory)
    spec.path(view=predict_stroke)


@app.route("/docs")
@app.route("/docs/<path:path>")
def swagger_docs(path=None):
    if not path or path == "index.html":
        root_url = request.url.replace("/docs", "")
        return render_template("index.html", base_url="/docs", root_url={root_url})
    else:
        return send_from_directory("./swagger/static", path)


if __name__ == "__main__":
    app.run()

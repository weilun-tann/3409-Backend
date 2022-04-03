from marshmallow import Schema, fields


class PredictCataractResponseSchema(Schema):
    cataract_type = fields.String()


class PredictPneumoniaResponseSchema(Schema):
    probability = fields.Float()
    outcome = fields.Int()

class PredictRespiratoryResponseSchema(Schema):
    respiratory_disease = fields.String()

class IntParam(Schema):
    gist_id = fields.Int()

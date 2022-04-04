from marshmallow import Schema, fields


class PredictDiabetesResponseSchema(Schema):
    outcome = fields.String()


class PredictStrokeResponseSchema(Schema):
    outcome = fields.String()


class PredictCoronaryResponseSchema(Schema):
    outcome = fields.String()


class PredictPneumoniaResponseSchema(Schema):
    probability = fields.Float()
    outcome = fields.Int()

class PredictCataractResponseSchema(Schema):
    outcome = fields.String()

class PredictRespiratoryResponseSchema(Schema):
    outcome = fields.String()

class IntParam(Schema):
    gist_id = fields.Int()

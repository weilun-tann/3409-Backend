from marshmallow import Schema, fields


class PredictCataractResponseSchema(Schema):
    cataract_type = fields.String()


class PredictPneumoniaResponseSchema(Schema):
    probability = fields.Float()
    outcome = fields.Int()


class IntParam(Schema):
    gist_id = fields.Int()

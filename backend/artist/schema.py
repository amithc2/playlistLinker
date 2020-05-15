from marshmallow import Schema, fields

class artistSchema(Schema):
  id = fields.Str(required=True)
  name = fields.Str()
  popularity = fields.Int(required=True)
  # type = fields.Str()
  # uri = fields.Str()
  # repo_url = fields.URL()

class trackSchema(GithubRepoSchema):
  id = fields.String(required=True)
  popularity = fields.Int(required=True)

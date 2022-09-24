import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Errors(db.Model):
    __tablename__ = "errors"
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.public_id"))
    body = db.Column(db.JSON)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @property
    def type(self):
        return self.body["exception"]["values"][0]["type"]

    @property
    def value(self):
        return self.body["exception"]["values"][0]["value"]


class Projects(db.Model):
    __tablename__ = "projects"
    private_id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(64))

    errors = db.relationship("Errors")

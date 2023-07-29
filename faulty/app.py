#!/usr/bin/env python
import gzip
import zlib
import json
from io import BytesIO
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    send_file,
)
from flask_bootstrap import Bootstrap5

from models import db, Errors, Projects

app = Flask(__name__)
app.config.from_object("config.Config")
bootstrap = Bootstrap5(app)

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    projects = Projects.query.paginate()
    return render_template("index.html", projects=projects)


@app.route("/projects/<int:project_id>")
def project(project_id):
    p = Projects.query.filter_by(public_id=project_id).first_or_404()
    dsn = f"{request.scheme}://public@{request.host}/{p.public_id}"
    return render_template("project.html", project=p, dsn=dsn)


@app.route("/errors/<int:error_id>")
def error(error_id):
    e = Errors.query.filter_by(id=error_id).first_or_404()
    if request.args.get("raw"):
        return jsonify(e.body)
    if request.args.get("download"):
        buffer = BytesIO()
        buffer.write(json.dumps(e.body).encode("utf-8"))
        buffer.seek(0)
        return send_file(
            buffer,
            as_attachment=True,
            download_name=f"{error_id}.json",
            mimetype="application/json",
        )
    return render_template("error.html", error=e)


@app.route("/api/projects/<int:project_id>", methods=["PATCH"])
def api_project_edit(project_id):
    project = Projects.query.filter_by(public_id=project_id).first_or_404()
    name = request.json.get("name")
    project.name = name
    db.session.commit()
    return jsonify({"success": True})


@app.route("/api/errors/<int:error_id>", methods=["GET"])
def api_error_view(error_id):
    error = Errors.query.filter_by(id=error_id).first_or_404()
    return jsonify(error.body)


@app.route("/api/errors/<int:error_id>", methods=["DELETE"])
def api_error_delete(error_id):
    error = Errors.query.filter_by(id=error_id).first_or_404()
    db.session.delete(error)
    db.session.commit()
    return jsonify({"success": True})


@app.route("/api/<int:project_id>/store/", methods=["POST"])
def api_error_ingest(project_id):
    encoding = request.headers.get("Content-Encoding")
    if encoding == "gzip":
        body = gzip.decompress(request.data)
    elif encoding == "deflate":
        body = zlib.decompress(request.data)
    else:
        body = request.data

    body = json.loads(body)

    # Create project if it doesn't exist
    project = Projects.query.filter_by(public_id=project_id).first()
    if project is None:
        project = Projects(public_id=project_id, name="Unnamed Project")
        db.session.add(project)
        db.session.commit()

    # Create error and add to project with public id
    error = Errors(project_id=project.public_id, body=body)
    db.session.add(error)
    db.session.commit()

    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

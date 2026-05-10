from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [{"id": 1, "title": "Buy groceries", "done": False}]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"status": "success", "data": tasks})

@app.route("/tasks", methods=["POST"])
def add_task():
    body = request.get_json()
    if not body or "title" not in body:
        return jsonify({"status": "error", "message": "title is required"}), 400
    task = {"id": len(tasks) + 1, "title": body["title"], "done": False}
    tasks.append(task)
    return jsonify({"status": "success", "data": task}), 201

if __name__ == "__main__":
    app.run(debug=True)

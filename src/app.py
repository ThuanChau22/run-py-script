from flask import Flask, request
import json
import subprocess

# Flash App
app = Flask(__name__)
app.json.sort_keys = False


@app.route("/execute", methods=["POST"])
def execute():
    try:
        script = request.json.get("script")

        command = [
            "nsjail",
            "--chroot",
            "/",
            "--config",
            "nsjail.cfg",
            "--",
            "/usr/local/bin/python3",
            "-c",
            f"{script}\nprint(main())",
        ]

        completed_process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10,
        )

        if completed_process.returncode != 0:
            raise Exception(completed_process.stderr)

        stdout = completed_process.stdout.strip().split("\n")

        result = json.loads(stdout.pop().replace("'", '"'))

        return {"result": result, "stdout": stdout}, 200
    except subprocess.TimeoutExpired:
        return {"error": "Process time out"}, 400
    except json.decoder.JSONDecodeError:
        return {"error": "None or invalid return value"}, 400
    except Exception as error:
        return {"error": error.args[0]}, 400


# Handle path not found
@app.errorhandler(404)
def path_not_found(_):
    message = f"The requested path {request.path} was not found on server."
    return {"message": message}, 404

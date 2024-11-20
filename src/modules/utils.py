import requests
import json
import os
import base64

def fetch_csv_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def save_json_to_file(data, output_filename):
    with open(output_filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

def fetch_rollouts_data(path):
    token = os.getenv("GH_TOKEN")
    path_prefix = os.getenv("ROLLOUTS_SRC")

    if not token:
        raise EnvironmentError("GH_TOKEN is not set in the environment.")
    if not path_prefix:
        raise EnvironmentError("ROLLOUTS_SRC is not set in the environment.")

    response = requests.get(f"https://api.github.com/repos/{path_prefix}/contents/{path}", headers={"Authorization": f"token {token}"})
    response.raise_for_status()
    content = response.json().get("content")

    if content is None:
        raise ValueError("Failed to fetch rollouts")
    decoded_content = base64.b64decode(content).decode('utf-8')

    return json.loads(decoded_content)

def save_experiments_to_files(experiments, output_dir="./data/"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for experiment in experiments:
        experiment_id = experiment.get('id')
        experiment_kind = experiment.get('kind', '').strip()

        if experiment_id:
            if not experiment_kind:
                file_filename = os.path.join(output_dir, f"{experiment_id}.json")
            else:
                kind_dir = os.path.join(output_dir, experiment_kind)
                if not os.path.exists(kind_dir):
                    os.makedirs(kind_dir)

                file_filename = os.path.join(kind_dir, f"{experiment_id}.json")

            with open(file_filename, 'w', encoding='utf-8') as json_file:
                json.dump(experiment, json_file, indent=4, ensure_ascii=False)
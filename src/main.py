import modules.csv_process as csv_process
import modules.utils as utils
import modules.merge_json as merge_json
import os

def main():
    os.system("cd ..")

    archive_url = os.getenv("ARCHIVE_URL")
    if not archive_url:
            raise EnvironmentError("ARCHIVE_URL is not set in the environment.")

    experiments_archive = utils.fetch_csv_data(archive_url)
    experiments = csv_process.transform_csv_to_json(experiments_archive, ['id', 'label', 'hash', 'kind'])
    utils.save_json_to_file(experiments, "./data/experiments.json")

    experiments_with_rollouts = merge_json.merge_rollouts(experiments, utils.fetch_rollouts_data("guild/data.json"), utils.fetch_rollouts_data("user/data.json"))
    utils.save_json_to_file(experiments_with_rollouts, "./data/experiments.json")

    utils.save_experiments_to_files(experiments_with_rollouts)

if __name__ == "__main__":
    main()

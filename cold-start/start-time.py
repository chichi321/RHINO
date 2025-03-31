import subprocess
import json
from dateutil import parser
import time

cluster_name = 'Rhino'
task_definition = 'cold-start:7'
task_count = 8
results_file = '1000mb-8.txt'

def run_tasks(desired_count=1):
    cmd = [
        'aws', 'ecs', 'run-task',
        '--cluster', cluster_name,
        '--task-definition', task_definition,
        '--launch-type', 'FARGATE',
        '--network-configuration', 'awsvpcConfiguration={subnets=[subnet-01e7cc1bcdb949806],securityGroups=[sg-02fbade4cac831f75],assignPublicIp="ENABLED"}',
        '--count', str(desired_count)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running task: {result.stderr}")
        exit(1)
    output = json.loads(result.stdout)
    return [task['taskArn'] for task in output['tasks']]

def describe_tasks(task_arns):
    cmd = [
        'aws', 'ecs', 'describe-tasks',
        '--cluster', cluster_name,
        '--tasks'
    ] + task_arns  # Adding task ARNs as separate list elements

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error describing tasks: {result.stderr}")
        exit(1)
    return json.loads(result.stdout)

def main():
    with open(results_file, 'w') as file:
        # Header for the file to indicate the content of the data
        file.write("Cold Start Duration (Seconds)\n")

        for i in range(1, 11):
            task_arns = run_tasks(desired_count=task_count)
            print(f"Tasks {task_arns} submitted.")

            all_tasks_started = False
            tasks_info = {}
            while not all_tasks_started:
                tasks_info = describe_tasks(task_arns)
                all_tasks_started = all('startedAt' in task for task in tasks_info['tasks'])
                if not all_tasks_started:
                    print("Waiting for all tasks to start...")
                    time.sleep(5)  # Pause for 5 seconds before retrying

            latest_started_time = None
            earliest_created_time = None

            for task in tasks_info['tasks']:
                created_time = parser.parse(task['createdAt'])
                started_time = parser.parse(task['startedAt'])
                if earliest_created_time is None or created_time < earliest_created_time:
                    earliest_created_time = created_time
                if latest_started_time is None or started_time > latest_started_time:
                    latest_started_time = started_time

            cold_start_duration = latest_started_time - earliest_created_time
            print(f"Experiment {i}:")
            print(f"Earliest task created at {earliest_created_time}")
            print(f"Latest task started at {latest_started_time}")
            print(f"Cold start time: {cold_start_duration.total_seconds()} seconds")

            # Log only the cold start duration to file
            file.write(f"{cold_start_duration.total_seconds()}\n")

if __name__ == '__main__':
    main()

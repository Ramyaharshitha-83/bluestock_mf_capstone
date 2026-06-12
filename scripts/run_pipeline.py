import subprocess

subprocess.run(["python","etl_pipeline.py"])
subprocess.run(["python","compute_metrics.py"])
subprocess.run(["python","recommender.py"])

print("Pipeline completed")
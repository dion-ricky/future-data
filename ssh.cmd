gcloud compute ssh --zone us-central1-a dion-ricky@sainsdata -- -L 8084:localhost:8084 -L 8888:localhost:8888 -L 8889:localhost:8889 -L 3000:localhost:3000 -L 8880:localhost:8880
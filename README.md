gcloud app create \
	--project plasmic-compute-256214 \
	--region us-west2

gcloud app deploy app.yaml \
	--project plasmic-compute-256214 \
	--quiet

gcloud app logs tail \
	--project plasmic-compute-256214 \
	--service story-creator



# Resume bot

## 1. Building static site

copy the /www folder into the AFS, then publish with

[Publish](https://www.andrew.cmu.edu/server/publish.html)


## 2. Host a simple backend on GCP functions

In gcp cloud shell, clone this project, enter `gcp_function` directory, run

```
gcloud functions deploy langflow-proxy \
  --gen2 \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point langflow_proxy \
  --region us-central1 \
  --timeout 600s \
  --memory=512MB

gcloud functions add-iam-policy-binding langflow-proxy \
  --region=us-central1 \
  --member="allUsers" \
  --role="roles/cloudfunctions.invoker"
```

If need to delete the function (only necessary):

```
gcloud functions delete langflow-proxy --region=us-central1 --gen2
```

Once finish, the function should be online. This is a tiny backend that responsible for proxying messages from and to Langflow.

## 3. Run the demo

Take my project as an example: the job site is hosted on

```
https://www.andrew.cmu.edu/user/zhixinc/ba/
```

And the langflow apis and pipeline is pre-configured and embedded into the backend infrastructure.

The demo page should be hosted on your AFS/userid/bot now.

Example domain: [Langflow Demo Interface](https://www.andrew.cmu.edu/user/zhixinc/bot/)

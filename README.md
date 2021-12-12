# String Reverse API
String Reverse API is an infrastructure take-home exam. 

This project is a simple example of an API endpoint that reverses a string when you call it.


## Setup

1. Install [`Docker`][docker_setup] if you haven't done so.
a
1. Install Google's Google Cloud Compute (GCP) [SDK tooling][google_sdk_setup].

1. Given this implementation uses GCP as its cloud provider, you will
   need to create a [GCP project][gcp_console]. **Note:** Please make
   sure to install the **cloud-build-local** component.

1. Once you have created a GCP project and it is properly set up,
   authenticate your work environment to your project.

    ```
    gcloud auth login
    ```

1. Clone this repository.

    ```
    git clone https://github.com/lewars/infra-take-home.git
    ```

## Build and Test Locally

Execute the CI pipeline that will build and test the code locally, using Cloud build.

```
cd infra-take-home
TAG_NAME=0.0.1
cloud-build-local --dryrun=false --config=cloudbuild.yaml --substitutions=TAG_NAME=${TAG_NAME} .
```

## Deploy

To build, test, and deploy to your GCP project, execute the following:

```
gcloud builds submit --config cloudbuild.yaml --substitutions=TAG_NAME=${TAG_NAME}
```

## Manually Test

To manually test after deployment:
1. Visit the GCP console. Browse the Cloud Run section, find the reverse repository, and click on its link.
Copy the URL presented at the top of the page.
1. Use curl to access the API endpoint:

```
curl -X POST -d 'foo' -H 'Content-Type: application/json'  https://reverse-v6elomfbxa-ue.a.run.app/reverse
{"payload":"OOF"}
```

[docker_setup]: https://docs.docker.com/engine/install/
[google_sdk_setup]: https://cloud.google.com/sdk/docs/install
[google_account_creation]: https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp
[gcp_console]: https://console.cloud.google.com/

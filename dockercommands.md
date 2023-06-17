# Docker Commands for Local Deployment

## BackEnd

```console
docker build -t spanishtutor:backend-v1 .
docker run -d --name tutorbackend -p 8000:8000 spanishtutor:backend-v1
```


## FrontEnd

```console
docker build -t spanishtutor:frontend-v1 .
frontend % docker run -d --name tutorfrontend -p 5173:5173 spanishtutor:frontend-v1
```
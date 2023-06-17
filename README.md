# Jamal's Spanish VoiceBot v1

## Purpose
Create a voice enabled chatbot that is used for translation practice for tutoring students
[ProjectLink](https://github.com/coderaidershaun/chatbot-conversation-jarvis)

## Troubleshooting

Ensure that ElevenLabs API is not hitting maximum count which will return a /post-audio/ 400 error 

## Redeploy from Clean Macbook Steps June 2023

# Software Pre-Installs - Downloads
1. nodejs and npm
2. python and pip

# Backend Steps
1. Create virtual environment 
2. pip3 install from requirements.txt
3. add .env environment variables
4. 

# Frontend Steps
1. Use npm to install both `-g yarn` and `ts-node`
2. Run `yarn --exact` and `yarn dev`

## Redeploying From Scratch Helpful Tips

Ensure the following:
- Make sure you apt update and upgrade
- Handle Python install via WSL using `apt install python3-pip | python3.10-venv` respectively 
- Activate the venv 
- install `requirements.txt` as sudo

FrontEnd
- Install `NodeJS` via the command below because apt installs v14 which is not compatible
- Run NPM installs on yarn and ts-node `npm install --global yarn ts-node`
- Ensure `package.json` has correct file and run `yarn --exact` 

```console
curl -fsSL https://deb.nodesource.com/setup_18.x | bash - &&\
apt-get install -y nodejs
```
Potential Errors
1. if error about lib-node package run the following `apt remove libnode-dev` and `apt clean`


## Tech Stack / Architecture

### FrontEnd
- React: Uses components to create JSX and generate HTML.
- Tailwind: Handles styling.

### BackEnd
- FastAPI: A web framework for handling API requests and responses.
- OpenAI: Handles natural language processing for sending prompts.
- ElevenLabs: Creates a human-sounding voice.

#### Backend Imports
- CORS
- /health entrypoint

#### Main API Route Endpoint
This is where we send an audio file.

1. Save Audio Input
2. Convert Audio to Text (OpenAI Whisper)
3. Get Chatbot Response (OpenAI Whisper)
4. Add to Chat History
5. Convert Text to Speech (Eleven Labs)

### FrontEnd
- Vite: Handles scaffolding for TypeScript and React.
- Axios: Handles sending request to the Python Backend Server
- React Media Recorder: simplifies media streams and integrates into React App

## VS Code Extensions for this project
- Auto Close Tag
- Auto Rename Tag
- ES7+ React/Redux/React-Native snippets <- very specific name
- prettier
- tailwind css intllisense

## Tools
- Wireframe: excali draw; used to draw out designs

## Elevenlab Voices Export
- 21m00Tcm4TlvDq8ikWAM [Rachel](https://storage.googleapis.com/eleven-public-prod/premade/voices/21m00Tcm4TlvDq8ikWAM/6edb9076-c3e4-420c-b6ab-11d43fe341c8.mp3)
- AZnzlk1XvdvUeBnXmlld [Domi](https://storage.googleapis.com/eleven-public-prod/premade/voices/AZnzlk1XvdvUeBnXmlld/69c5373f-0dc2-4efd-9232-a0140182c0a9.mp3)
- EXAVITQu4vr4xnSDxMaL [Bella](https://storage.googleapis.com/eleven-public-prod/premade/voices/EXAVITQu4vr4xnSDxMaL/04365bce-98cc-4e99-9f10-56b60680cda9.mp3)
- ErXwobaYiN019PkySvjV [Antoni](https://storage.googleapis.com/eleven-public-prod/premade/voices/ErXwobaYiN019PkySvjV/38d8f8f0-1122-4333-b323-0b87478d506a.mp3)
- MF3mGyEYCl7XYWbV9V6O [Elli](https://storage.googleapis.com/eleven-public-prod/premade/voices/MF3mGyEYCl7XYWbV9V6O/f9fd64c3-5d62-45cd-b0dc-ad722ee3284e.mp3)
- TxGEqnHWrfWFTfGW9XjX [Josh](https://storage.googleapis.com/eleven-public-prod/premade/voices/TxGEqnHWrfWFTfGW9XjX/c6c80dcd-5fe5-4a4c-a74c-b3fec4c62c67.mp3)
- VR6AewLTigWG4xSOukaG [Arnold](https://storage.googleapis.com/eleven-public-prod/premade/voices/VR6AewLTigWG4xSOukaG/66e83dc2-6543-4897-9283-e028ac5ae4aa.mp3)
- pNInz6obpgDQGcFmaJgB [Adam](https://storage.googleapis.com/eleven-public-prod/premade/voices/pNInz6obpgDQGcFmaJgB/e0b45450-78db-49b9-aaa4-d5358a6871bd.mp3)
- yoZ06aMxZJJ28mfd3POQ [Sam](https://storage.googleapis.com/eleven-public-prod/premade/voices/yoZ06aMxZJJ28mfd3POQ/1c4d417c-ba80-4de8-874a-a1c57987ea63.mp3)

```python
for i in dict['voices']:
    print (i['voice_id'], i['name'], i['preview_url'])
```

## Setup/Extensions

Step 1: Create Folders for backend and frontend. Install the following:
- python3 and pip3
- nodejs
- yarn
- typescript and ts-node

Step 2: Install Backend Packages for python
Understanding Packages:
- python-decouple: this allow for handling sensitive data via .env files
- python-multipart: allows for parsing through encoded http requests which is used for file uploads in web-apps 

```console
python3 -m venv venv
source venv/bin/activate
pip3 install openai==0.27.0 | or openai without version
pip3 install python-decouple==3.8 python-multipart==0.0.6 requests==2.28.2 fastapi==0.92.0
pip3 install “uvicorn[standard]”
```

Navigate to FastAPI docs for simple Hello World App
```console
touch main.py
uvicorn main:app --reload 
```

Step 3: Install React Frontend and Packages
- Navigate to the frontend folder and build a vite project. This will be used for templating our JavaScript project which handles TypeScript as well. via `yarn create vite` command
- copy the package.json from folk to ensure dependancies are consistent
- install packages 

```console
yarn create vite . # Select React + TypeScript
yarn --exact
yarn dev
```

Step 4: Remove CSS and Integrate Tailwind 
- Run `npx tailwindcss init -p`
- Instructions can be found here: tailwindcss.com/docs/guides/vite
- open tailwind.config.js and add in the content array information
- Index.css: and add in the base, components and utilities directives at the top of page via website documentation | delete everything else in file except body(margin, width and height) 
- App.tsx: and delete everything and replace with codeblock below; and also logo info can be deleted
- delete the App.css file | delete Assets folder
- Run `yarn build` if you get an error go into file and change moduleResolution to “node” and other items to change will come later
- 

FileName: app.tsx
```javascript
function App() {
  return (
    <div className="">
      <div className='text-2xl bg-blue-500'>Hello</div>

    </div>
  );
}

export default App
```



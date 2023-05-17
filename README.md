# Jamal's Spanish VoiceBot v1

## Purpose
Create a voice enabled chatbot that is used for translation practice for tutoring students

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



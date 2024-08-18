
# Running Instructions

## 1. Setting Up the Environment

### a. Install Dependencies
Before running the application, ensure you have installed all necessary dependencies.

For Flask (backend):
```bash
pip install -r requirements.txt
```

For React (frontend):
```bash
npm install
```

## 2. Running the Flask Backend

### a. Start the Backend Server
To start the Flask server, navigate to the directory where your `app.py` file is located and run the following command:

```bash
python app.py
```

### b. Access the Backend
Once the server is running, you will see output indicating the server is running on a specific port (usually `http://127.0.0.1:5000/`). This is the URL where your backend is accessible.

### c. Check the Server Status
You can check the server status by pasting the URL into your browser or using tools like Postman to test your endpoints.

## 3. Running the React Frontend

### a. Start the Frontend Server
To start the React frontend, navigate to the directory where your `UploadFile.js` (or main React component) file is located and run the following command:

```bash
npm start
```

### b. Access the Frontend
This will automatically open your React application in a new browser tab. If it doesn’t open automatically, you can manually go to the following URL in your browser:

```bash
http://localhost:3001/
```

(Replace `3001` with the actual port number if different.)

## 4. Interacting with the Application

### a. Upload a File
In the React application, use the file upload interface to select and upload a document. The document will be sent to the Flask backend for processing.

### b. Viewing the Summary
After processing, the summary will be displayed in the React frontend. Ensure that the backend is running before attempting to upload a file.

### Additional Notes
- If you make changes to `UploadFile.js`, you may need to restart the React server for changes to take effect.
- Check your console logs for any errors during the running of the application. These logs are helpful for debugging.

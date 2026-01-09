# Frontend Technical Assessment

React application created with Create React App and React Flow. The project lives inside:

```
frontend_technical_assessment/
└── frontend/   <-- run commands from here
    ├── package.json
    └── src/
```

## Prerequisites

| Tool | Why it’s needed | Notes |
| --- | --- | --- |
| Node.js 18+ & npm | Run/build the React SPA | https://nodejs.org |
| Git (optional but recommended) | Clone the repo & push to GitHub | Install from https://git-scm.com/downloads |

## Getting the code

1. **Clone with Git (recommended)**
   ```powershell
   git clone https://github.com/<you>/<repo>.git
   cd frontend_technical_assessment/frontend
   ```
2. **OR download the GitHub ZIP**
   - Click “Code” → “Download ZIP”.
   - Extract the archive, then open a terminal inside `frontend_technical_assessment/frontend`.

## Install & run

```powershell
npm install        # install dependencies
npm start          # launch dev server on http://localhost:3000
```

To build/run elsewhere:

```powershell
npm run build      # outputs static assets in build/
```

Anyone who clones or downloads the ZIP just needs to run the two commands above (`npm install`, `npm start`) from the `frontend` folder and it will work cross-platform.

## Available scripts

```json
"scripts": {
  "start": "react-scripts start",
  "build": "react-scripts build",
  "test": "react-scripts test",
  "eject": "react-scripts eject"
}
```

Use `npm run <script>` to execute them.

## Pushing this project to GitHub

1. **Install Git** if `git` isn’t recognized (Windows: run the installer linked above and reopen PowerShell).
2. Run the following inside `frontend_technical_assessment/frontend`:
   ```powershell
   git init                    # only once
   git add .
   git commit -m "Initial commit"
   git branch -M main          # optional but recommended
   git remote add origin https://github.com/<you>/<repo>.git
   git push -u origin main
   ```
3. To update later:
   ```powershell
   git add .
   git commit -m "Explain the change"
   git push
   ```

## Troubleshooting

- **`git` is not recognized** → install Git and restart the terminal.
- **Port already in use** → stop other apps using port 3000 or set `PORT=3001` before running `npm start`.
- **Dependency issues after pulling ZIP** → delete `node_modules`, run `npm install` again.

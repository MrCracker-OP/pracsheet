const CORRECT_PASSWORD = "2508";
const INACTIVITY_TIMEOUT = 300000; // 5 minutes
const FILES_DIRECTORY = '/dsa/';
const SUPPORTED_EXTENSIONS = ['.c', '.cpp', '.BAK'];

// Predefined files to work around Vercel directory listing limitations
const PREDEFINED_FILES = [
    'Exp1LinkedList.cpp',
    'Exp1LList.cpp',
    'Exp2LLFunctions.cpp',
    'Exp3Poly.cpp',
    'Exp4Stack.cpp',
    'Exp5InfixtoPostfix.cpp',
    'Exp7Parenthesis.cpp',
    'Exp8LinearQueue.cpp',
    'EXP9CI~1.BAK',
    'EXP9CI~1.C',
    'Exp11BPS.c',
    'EXP11DFS.BAK',
    'EXP11DFS.C',
    'Exp12Bubble.c',
    'EXP12B~1.BAK',
    'EXP12B~1.C',
    'Exp12Insertion.c',
    'Exp13BSTtraversal.c',
    'EXP14BST.BAK',
    'EXP14BST.C',
    'test.html',
    'try.txt',
];

class SessionManager {
    static setAuthenticated() {
        const token = btoa(Date.now().toString());
        sessionStorage.setItem('authToken', token);
        sessionStorage.setItem('authTimestamp', Date.now().toString());
    }

    static isAuthenticated() {
        const authToken = sessionStorage.getItem('authToken');
        const authTimestamp = sessionStorage.getItem('authTimestamp');

        if (!authToken || !authTimestamp) return false;

        const currentTime = Date.now();
        const sessionDuration = currentTime - parseInt(authTimestamp);

        return sessionDuration < INACTIVITY_TIMEOUT;
    }

    static clearSession() {
        sessionStorage.removeItem('authToken');
        sessionStorage.removeItem('authTimestamp');
    }
}

class FileManager {
    constructor(directory, supportedExtensions) {
        this.filesDirectory = directory;
        this.supportedExtensions = supportedExtensions;
        this.fileListDiv = document.getElementById('file-list');
    }

    async fetchFileList() {
        if (!this.fileListDiv) return;

        try {
            // Use predefined file list instead of directory fetch
            this.fileListDiv.innerHTML = '';

            PREDEFINED_FILES.forEach(fileName => {
                if (this.supportedExtensions.some(ext => fileName.endsWith(ext))) {
                    this.createFileItem(fileName, `${this.filesDirectory}${fileName}`);
                }
            });

            if (this.fileListDiv.children.length === 0) {
                this.fileListDiv.innerHTML = `
                    <div class="error-message">
                        No supported files found. Supported extensions: ${this.supportedExtensions.join(', ')}
                    </div>
                `;
            }
        } catch (error) {
            console.error("Error loading files:", error);
            this.fileListDiv.innerHTML = `
                <div class="error-message">
                    Unable to load files. Error: ${error.message}
                </div>
            `;
        }
    }

    createFileItem(fileName, filePath) {
        const fileItem = document.createElement('div');
        fileItem.classList.add('file-item');

        fileItem.innerHTML = `
            <span>File: ${fileName}</span>
            <div class="file-actions">
                <button onclick="fileManager.copyFileContent('${filePath}')">Copy Content</button>
                <button onclick="fileManager.downloadFile('${fileName}', '${filePath}')">Download</button>
            </div>
        `;

        this.fileListDiv.appendChild(fileItem);
    }

    async copyFileContent(filePath) {
        try {
            const response = await fetch(filePath);
            if (!response.ok) throw new Error("Failed to fetch file");

            const content = await response.text();
            await navigator.clipboard.writeText(content);

            alert("File content copied to clipboard!");
        } catch (error) {
            console.error("Error copying file content:", error);
            alert("Failed to copy content.");
        }
    }

    downloadFile(fileName, filePath) {
        const a = document.createElement('a');
        a.href = filePath;
        a.download = fileName;
        a.click();
    }
}

class PageManager {
    static initLoginPage() {
        const submitButton = document.querySelector("button");
        if (submitButton) {
            submitButton.addEventListener("click", this.handleLogin.bind(this));
        }
    }

    static handleLogin() {
        const passwordInput = document.getElementById("password");
        const inputPassword = passwordInput.value;

        if (inputPassword === CORRECT_PASSWORD) {
            SessionManager.setAuthenticated();
            window.location.href = "dsapractical.html";
        } else {
            alert("Incorrect password. Try again.");
            passwordInput.value = "";
        }
    }

    static initDashboardPage() {
        if (!SessionManager.isAuthenticated()) {
            window.location.href = "index.html";
            return;
        }
        this.setupSessionMonitoring();
        this.initFileManager();
    }

    static setupSessionMonitoring() {
        let inactivityTimer;

        const resetTimer = () => {
            clearTimeout(inactivityTimer);
            inactivityTimer = setTimeout(() => {
                SessionManager.clearSession();
                window.location.href = "index.html";
            }, INACTIVITY_TIMEOUT);
        };

        const events = ['mousemove', 'keypress', 'click'];
        events.forEach(event => document.addEventListener(event, resetTimer));

        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                SessionManager.clearSession();
                window.location.href = "index.html";
            }
        });

        resetTimer(); // Initial timer start
    }

    static initFileManager() {
        window.fileManager = new FileManager(FILES_DIRECTORY, SUPPORTED_EXTENSIONS);
        fileManager.fetchFileList();
    }
}

// Page initialization
window.addEventListener('DOMContentLoaded', () => {
    const pageName = document.body.getAttribute('data-page');

    switch (pageName) {
        case 'index':
            PageManager.initLoginPage();
            break;
        case 'dsapractical':
            PageManager.initDashboardPage();
            break;
    }
});

const CORRECT_PASSWORD = "2508";
const INACTIVITY_TIMEOUT = 300000; // 5 minutes

// Centralized file configuration
const FILE_CONFIG = {
    DSA: {
        directory: '/dsa/',
        extensions: ['.c', '.cpp', '.BAK'],
        files: [
            'Exp1LinkedList.cpp', 'Exp1LList.cpp', 'Exp2LLFunctions.cpp', 
            'Exp3Poly.cpp', 'Exp4Stack.cpp', 'Exp5InfixtoPostfix.cpp', 
            'Exp7Parenthesis.cpp', 'Exp8LinearQueue.cpp', 'EXP9CI~1.BAK',
            // Add more DSA files as needed
        ]
    },
    PYTHON: {
        directory: '/Expt_ProblemStatements/',
        extensions: ['.py'],
        directories:{
            "Exp2_6": [
                "1LeapYearChecker.ipynb",
                "2Vowel_or_Consonant.ipynb",
                "3ElectricityBillCalculation.ipynb",
                "4BMI_Calculator.ipynb",
                "5Shopping_Discount.ipynb",
                "6ATM_Transaction.ipynb"
            ],
            "Exp3_5": [
                "Anagram Checker.ipynb",
                "Character Frequency Analysis.ipynb",
                "Longest Word Finder.ipynb",
                "Palindrome.ipynb",
                "Word Frequency Counter.ipynb"
            ],
            "Exp4_5": [
                "Dictionary Operations.ipynb",
                "ListOperations.ipynb",
                "Sorting Tuples.ipynb",
                "Tuple Manipulation.ipynb",
                "Tuple-Based Student Records.ipynb"
            ],
            "Exp5_9": [
                "Diagonal_Elements_Sum.ipynb",
                "Find_Maximum_Element.ipynb",
                "Flatten_a_2D_Array.ipynb",
                "Matrix_Addition.ipynb",
                "Matrix_Multiplication.ipynb",
                "Reshape_a_1D_Array.ipynb",
                "Row_and_Column_Averages.ipynb",
                "Sum_of_Array_Elements.ipynb",
                "Transpose_of_a_Matrix.ipynb"
            ],
            "Exp6_6": [
                "Fibonacci_Sequence.ipynb",
                "GCD_By_EuclideanMethod.ipynb",
                "Palindrome_Checker.ipynb",
                "Power_of_a_number.ipynb",
                "String_Reversal.ipynb",
                "Sum_of_Digits.ipynb"
            ],
            "Exp7_5": [
                "Combining_Lists_Element_wise.ipynb",
                "Keeping_Odd_Numbers_In_a_List.ipynb",
                "String_Lengths.ipynb",
                "Sum_of_Even_Numbers.ipynb",
                "Title_Case_Conversion.ipynb"
            ],
            "Exp8_5": [
                "Execution Count.ipynb",
                "Greeting Decorator.ipynb",
                "Simple Logger.ipynb",
                "Simple Timer.ipynb",
                "Uppercase Decorator.ipynb"
            ],
            "Exp9_3": [
                "Bank Account System.ipynb",
                "Employee Management System.ipynb",
                "Library Management System.ipynb"
            ],
            "Exp10_4": [
                "Books and Digital Books.ipynb",
                "Employees and Managers.ipynb",
                "Shapes and Area Calculation.ipynb",
                "Vehicles and Fuel Efficiency.ipynb"
            ],
            "Exp11_4": [
                "Division_Calculator.ipynb",
                "File_Handling_with_Exceptions.ipynb",
                "Handling_Multiple_Exceptions.ipynb",
                "User_Input_Validation.ipynb"
            ],
            "Exp12_4": [
                "Backup_System.ipynb",
                "CSV_Data_Processing.ipynb",
                "File_Integrity_Check.ipynb",
                "Log_File_Analysis.ipynb"
            ],
            "Exp14_4": [
                "Data Analysis with Pandas.ipynb",
                "Data Preprocessing with NumPy and Pandas.ipynb",
                "MachineLearningPackages.ipynb",
                "Statistical Analysis with NumPy.ipynb",
                "Visualization of Data Trends with Matplotlib.ipynb"
            ],
            "Exp15_3": [
                "Cleaning_and_Plotting_Missing_Data.ipynb",
                "Data_Normalization_and_Visualization.ipynb",
                "Handling_Outliers_and_Visualization.ipynb"
            ]
        }
    }
};

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
    static initPythonDirectorySelect() {
        const select = document.getElementById('python-directory-select');
        const directories = Object.keys(FILE_CONFIG.PYTHON.directories);
        
        directories.forEach(dir => {
            const option = document.createElement('option');
            option.value = dir;
            option.textContent = dir.replace(/[-_]/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
            select.appendChild(option);
        });
    }

    static displayFiles(type, directory = null) {
        const displayArea = document.getElementById('file-display-area');
        displayArea.innerHTML = ''; // Clear previous content

        let files = [];
        let baseDirectory = '';

        if (type === 'DSA') {
            files = FILE_CONFIG.DSA.files;
            baseDirectory = FILE_CONFIG.DSA.directory;
        } else if (type === 'PYTHON' && directory) {
            files = FILE_CONFIG.PYTHON.directories[directory];
            baseDirectory = `${FILE_CONFIG.PYTHON.directory}${directory}/`;
        }

        if (files.length === 0) {
            displayArea.innerHTML = `
                <p class="text-center text-red-500">No files found in ${directory || type} directory</p>
            `;
            return;
        }

        const fileListContainer = document.createElement('div');
        fileListContainer.className = 'grid grid-cols-2 gap-4';

        files.forEach(fileName => {
            const fileCard = document.createElement('div');
            fileCard.className = 'bg-white p-4 rounded-lg shadow-md flex justify-between items-center';
            
            fileCard.innerHTML = `
                <span class="text-gray-700">${fileName}</span>
                <div class="space-x-2">
                    <button onclick="FileManager.copyFileContent('${baseDirectory}${fileName}')" 
                            class="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600 transition">
                        Copy
                    </button>
                    <button onclick="FileManager.downloadFile('${fileName}', '${baseDirectory}${fileName}')" 
                            class="bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600 transition">
                        Download
                    </button>
                </div>
            `;

            fileListContainer.appendChild(fileCard);
        });

        displayArea.appendChild(fileListContainer);
    }

    static async copyFileContent(filePath) {
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

    static downloadFile(fileName, filePath) {
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

        resetTimer();
    }

    static initFileManager() {
        FileManager.initPythonDirectorySelect();
    }
}

// Globally accessible functions for HTML onclick events
function showDSAFiles() {
    FileManager.displayFiles('DSA');
}

function showPythonFiles(directory) {
    if (directory) {
        FileManager.displayFiles('PYTHON', directory);
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
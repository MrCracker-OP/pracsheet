const CORRECT_PASSWORD = "2508";
const INACTIVITY_TIMEOUT = 300000; // 5 minutes

// Centralized file configuration
const FILE_CONFIG = {
    DSA: {
        directory: '/ai/',
        extensions: ['.py', '.cpp', '.BAK'],
        files: [
            'EXP 1  BFS DFS.py', 'EXP 2 dls ids .py', 'EXP 3 A_star.py', 
            'EXP 5 Genetic Algo.py', 'EXP 6 minmax.py','genetic2.py','genetic random.py'
            // Add more DSA files as needed
        ]
    },
    PYTHON: {
        directory: '/Expt_ProblemStatements/',
        extensions: ['.py'],
        directories:{
            "Exp2_6": [
                "1LeapYearChecker.py",
                "2Vowel_or_Consonant.py",
                "3ElectricityBillCalculation.py",
                "4BMI_Calculator.py",
                "5Shopping_Discount.py",
                "6ATM_Transaction.py"
            ],
            "Exp3_5": [
                "Anagram Checker.py",
                "Character Frequency Analysis.py",
                "Longest Word Finder.py",
                "Palindrome.py",
                "Word Frequency Counter.py"
            ],
            "Exp4_5": [
                "Dictionary Operations.py",
                "ListOperations.py",
                "Sorting Tuples.py",
                "Tuple Manipulation.py",
                "Tuple-Based Student Records.py"
            ],
            "Exp5_9": [
                "Diagonal_Elements_Sum.py",
                "Find_Maximum_Element.py",
                "Flatten_a_2D_Array.py",
                "Matrix_Addition.py",
                "Matrix_Multiplication.py",
                "Reshape_a_1D_Array.py",
                "Row_and_Column_Averages.py",
                "Sum_of_Array_Elements.py",
                "Transpose_of_a_Matrix.py"
            ],
            "Exp6_6": [
                "Fibonacci_Sequence.py",
                "GCD_By_EuclideanMethod.py",
                "Palindrome_Checker.py",
                "Power_of_a_number.py",
                "String_Reversal.py",
                "Sum_of_Digits.py"
            ],
            "Exp7_5": [
                "Combining_Lists_Element_wise.py",
                "Keeping_Odd_Numbers_In_a_List.py",
                "String_Lengths.py",
                "Sum_of_Even_Numbers.py",
                "Title_Case_Conversion.py"
            ],
            "Exp8_5": [
                "Execution Count.py",
                "Greeting Decorator.py",
                "Simple Logger.py",
                "Simple Timer.py",
                "Uppercase Decorator.py"
            ],
            "Exp9_3": [
                "Bank Account System.py",
                "Employee Management System.py",
                "Library Management System.py"
            ],
            "Exp10_4": [
                "Books and Digital Books.py",
                "Employees and Managers.py",
                "Shapes and Area Calculation.py",
                "Vehicles and Fuel Efficiency.py"
            ],
            "Exp11_4": [
                "Division_Calculator.py",
                "File_Handling_with_Exceptions.py",
                "Handling_Multiple_Exceptions.py",
                "User_Input_Validation.py"
            ],
            "Exp12_4": [
                "Backup_System.py",
                "CSV_Data_Processing.py",
                "File_Integrity_Check.py",
                "Log_File_Analysis.py"
            ],
            "Exp14_4": [
                "Data Analysis with Pandas.py",
                "Data Preprocessing with NumPy and Pandas.py",
                "MachineLearningPackages.py",
                "Statistical Analysis with NumPy.py",
                "Visualization of Data Trends with Matplotlib.py"
            ],
            "Exp15_3": [
                "Cleaning_and_Plotting_Missing_Data.py",
                "Data_Normalization_and_Visualization.py",
                "Handling_Outliers_and_Visualization.py"
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
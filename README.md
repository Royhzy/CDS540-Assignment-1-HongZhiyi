# CDS540 Assignment 1 - Online PK Automation Script for Xiaoyuan Oral Calculation

**Name:** HONG Zhiyi  

## 1. Project Background

This project is inspired by the online mental calculation PK feature of the popular Little Ape mental calculation app, originally intended for elementary school students. Recently, it has gained popularity among college students, transforming into algorithm-based PK, where users employ different algorithms to write scripts for faster mental calculations. By leveraging computer vision technology, specifically dynamic text recognition, I adapted a prior text recognition project into this assignment.

## 2. Project Description

### 2.1 Setup Environment

- **Development Platform:** PyCharm
- **Programming Language:** Python
- **Required Packages:** OpenCV, numpy, pyautogui, pytesseract, keyboard, sys, time

**Simulator:** BlueStacks 5 simulator  
Install the Little Ape Arithmetic app and set up two script shortcut keys: `>` and `<`.  
Enter the Xiaoyuan Oral Calculation APP, click the "Oral Calculation PK" button, and then click "Start PK" to begin. Make sure to run the Python script before starting PK.

![image](https://github.com/user-attachments/assets/02f4bd3a-6802-483d-8479-4a3615d92413)

![image](https://github.com/user-attachments/assets/3c8e942b-30dd-49d0-af39-e3a3b11e08f8)
### 2.2 Load an Image

After entering PK, ten mathematical equations will be presented sequentially. The program captures a region image of each equation using Pyautogui’s screenshot function and stores it in an array with numpy.

### 2.3 Pre-process the Image

The project utilizes grayscale and binary processing for image preprocessing:

- **Grayscale Processing:** Convert color images to grayscale using OpenCV’s `cvtColor` method.

  ![image](https://github.com/user-attachments/assets/ff70cf03-1d2c-47ab-b2d7-68092f55c7af)
  
- **Binary Processing:** Convert images to black and white using OpenCV’s `threshold` method.
  
 ![image](https://github.com/user-attachments/assets/659b79f5-7ac3-462e-a413-cbaf8207e503)

### 2.4 Detect, Extract and Display Text

This project uses `pytesseract`'s `image_to_string` method to identify all numeric texts, which are then split and stored in an array.

### 2.5 Compare Numbers

In the numbers array, `numbers[0]` represents the left number, and `numbers[1]` represents the right number. The system compares these values to determine the output as `>` or `<`. If the system fails to recognize the question, it outputs "Unrecognized number + Unrecognized question" and repeats the recognition process.

### 2.6 Script Input

The system inputs the determined answer back into the app using the `press` method of PyAutoGUI. The correct key (e.g., `.` or `,`) is sent based on the comparison result. The system has a maximum speed setting for inputting answers to expedite the process.

![image](https://github.com/user-attachments/assets/e2f6b209-b721-40bb-b489-53a3bf578668)

## 3. Advantages and Disadvantages of the Project

### 3.1 Advantages

- **Dynamic Text Recognition:** The script automatically answers ten mathematical questions in sequence, switching to the next round upon completion.
- **Innovation:** Combines computer vision techniques with practical applications.

### 3.2 Disadvantages

- Limited computer vision methods due to the project's focus, lacking techniques like blurring and perspective changes. If a more technical project is required, I can submit both projects.

## 4. Efficiency and Effectiveness Evaluation

### 4.1 Efficiency

The average time to complete ten questions is about 9.5 seconds, with potential minor delays due to errors. This time includes APP delay, system execution, and handwriting input time.

### 4.2 Comparison to Other Technical Efficiencies

This project uses computer vision for sequential answering, while mainstream methods can solve all questions within 0.01 seconds. Compared to traditional manual answering, computer vision methods may be slightly faster.

### 4.3 Accuracy of Text Recognition

The script has been executed 20 times with an accuracy rate of over 95%. The manual PK winning rate exceeds 85%.

### 4.4 Subsequent Optimization Plan

Future optimizations will focus on improving the script's execution time and enhancing visual technology methods.


CDS540 Assignment 1 - Online PK automation script for Xiaoyuan oral calculation based on OpenCV text detection
1.Project Background
    The background of this project comes from the online mental calculation PK of the popular Little Ape mental calculation app. This feature was originally intended for elementary school students, but after being recently conquered by college students, online mental calculation PK has become algorithm PK. Everyone uses different algorithms to write scripts, making the speed of mental calculation PK faster and faster. After learning about this project, I found that computer vision technology can be used to write scripts, and it involves dynamic text recognition technology, which is full of innovation. Therefore, I temporarily changed the ordinary text recognition project I had written before to the Little Ape mental calculation script project as this assignment.
2.Project Description
  2.1 Setup Environment:
    In terms of developing automated scripts, based on the PyCharm platform, Python language is used to import packages such as OpenCV, numpy, pyautogui, pytexteract, keyboard, sys, and time.
    In terms of simulators, use the BlueStacks 5 simulator, download the Little Ape Arithmetic installation package and install it on the simulator. Set two script shortcut keys on the simulator, namely '>' and '<' shortcut keys.
    Enter the Xiaoyuan Oral Calculation APP, click the "Oral Calculation PK" button to enter the PK options page, and then click "Start PK" to start PK. Remember to run the Python before the PK starts.
    ![image](https://github.com/user-attachments/assets/02f4bd3a-6802-483d-8479-4a3615d92413)
    ![image](https://github.com/user-attachments/assets/3c8e942b-30dd-49d0-af39-e3a3b11e08f8)
  2.2 Load an Image:
    After entering the PK, there will be ten mathematical equation problems, each of which will be answered sequentially.
    For each question, the Python program uses the screenshot function in the Pyautogui package to capture a region image of the mathematical equation, and then stores the region image in an array using numpy's array function.
  2.3 Pre-process the Image:
    In this project, grayscale processing and binary processing were used for image preprocessing. (For normal text detection, techniques such as blurring, edge detection, and perspective changes should also be used, but since this project only recognizes numbers, these techniques are not necessary.)
    Gray processing, by using OpenCV's cvtColor method, converts color images into grayscale images.An example of image gray processing is shown in the following figure：
    ![image](https://github.com/user-attachments/assets/ff70cf03-1d2c-47ab-b2d7-68092f55c7af)
    Binary processing, by using OpenCV's threshold method, converts images with only black and white binary values for text recognition.An example of image Binary processing is shown in the following figure：
    ![image](https://github.com/user-attachments/assets/659b79f5-7ac3-462e-a413-cbaf8207e503)
  2.4 Detect, Extract and Display Text:
    In terms of detecting,extracting and displaying text, this project uses pytexteract's image_to-sting method to identify all numeric texts, and then uses the split method of strings to separate each digit, which is then stored in an array in sequence.
  2.5 Compare numbers:
    In the numbers array, numbers [0] represents the number on the left, and numbers [1] represents the number on the right.
    Under normal circumstances, the system will compare the values of numbers [0] and numbers [1] to obtain '>' or '<'.
    Of course, sometimes unexpected situations may occur in the system, such as when all ten questions in this round of PK have been answered and the system cannot recognize the questions after entering the settlement interface. Here, I have set a conditional judgment that if the array length is less than 2, the system will output "Unrecognized number+Unrecognized question" and repeat the recognition process by adding 1 to the unrecognized number. When the number of unrecognized times is greater than or equal to 25, the system will click on the relevant area buttons after settlement on the Xiaoyuan oral calculation APP in sequence to proceed to the next round of PK; When the unrecognized count has accumulated n times and the question text is recognized (0<n<20), the system will reset the unrecognized count value to zero.
  2.6 Script input:
    After comparing the values, the system has obtained the answer, but how can we input this answer back into the APP? Here, I have used the press method of PyAutoGUI to write the output when encountering various answer situations, which is to output a key, such as'. ' Or ',' and so on, when passing it into the app's simulator, as mentioned earlier, I have already set up two scripts on the simulator. When the simulator receives' When the button signal is pressed, the handwriting '>' operation is executed; When the simulator receives the ',' key signal, it executes the handwriting '<' operation. In order to make the system answer questions faster, I set the maximum speed for handwriting '>' and '<'. This is also the reason why I use the BlueStacks 5 simulator, which can speed up the answering process.
    The following figure shows the interface for editing scripts in the simulator：
    ![image](https://github.com/user-attachments/assets/e2f6b209-b721-40bb-b489-53a3bf578668)
3.Advantages and disadvantages of the project
  3.1 Advantages:
    This project has many advantages, among which the most obvious one is dynamic text recognition: after entering PK, there will be ten mathematical formula questions, each question will be answered in sequence, and after the ten questions are completed, it will automatically switch to the next round, achieving automated answering. In addition, another advantage of this project is its innovation. Through the computer vision methods learned in this course and my own Python script development methods, combined with current hot topics, this project has been applied in practice.
  3.2 Disadvantages:
    The disadvantage of this project is that there are not enough methods used in computer vision, such as blurring and perspective changes, which cannot be applied in this project. After hesitating between the two projects for a while, I ultimately chose the more innovative and dynamic Xiaoyuan oral calculation PK project. If the teacher needs a more technical project, I can submit both projects
4.Efficiency and Effectiveness Evaluation
  4.1Effiency
    Under the condition of ensuring accuracy, the average time to complete a round of ten questions is about 9.5 seconds. If there is a small probability of errors, it may be 1-2 seconds slower. In 9.5 seconds, it can be divided into two parts: APP delay, system execution, and handwriting input time. System delay time refers to the 0.5s delay after answering each question, while handwriting input time refers to the time it takes to handwrite '>' and '<' at 5x speed during script recording.
    Regarding the setting of system delay time, set the delay through the sleep method in the time package.
  4.2Compared to other technical efficiencies:
    The Xiaoyuan oral calculation PK project is currently divided into two methods: one is the computer vision technology used in this project to answer questions sequentially, and the other is the mainstream method now - grabbing data packets and solving all questions within 0.01 seconds. Obviously, the speed of the former method has fallen far behind that of the latter. Of course, compared to traditional manual answering, computer vision methods may be slightly faster.
  4.3Accuracy of text recognition：
    Up to now, the script has been executed 20 times with an accuracy rate of over 95%. Excluding other packet capture scripts, the winning rate of manual PK is over 85%. (The winning rate of this account did not reach 85% because there were no questions answered during the initial multiple PK, and the script was being developed and tested.)
  4.4Subsequent optimization plan：
    In the future, I can continue to optimize the script for PK using visual technology methods and develop a solution with shorter execution time.

# End of the day

## Prompt

Write a script that emails you and Sky when it's 10 minutes before your shift ends. You can use whatever scripting languages you prefer. This script should be able to run (or be executed) indefinitely so as to notify us every work day (but not the weekend!)

## Submitting

So far, you have been submitting tasks by adding your changes directly to the `master` branch. The `master` branch however is typically reserved for code that can immediately be deployed into production. This time, you will be uploading this assignment using Github Flow, a popular workflow supporting collaboration and regular deployments.

The submission process will look like this:
1. You make changes on a new branch.
2. You make a pull request (PR) from that branch to the `master` branch.
3. We will discuss how you did, give pointers, and ask questions on that PR page
4. If changes are requested, you can make changes to the same branch and they will be added to the PR.
5. Once everything is complete, I will merge the branch to master and you'll be done!

Here is a more detailed explanation on [how to submit](https://github.com/dpac-practicum/Submitting#submitting-tasks) your code.  
Here is more information about [Github Flow](https://guides.github.com/introduction/flow/) if you're interested.

---

## Installation

\<Fill this in with information on how to install your software on whatever OS(s) you are supporting\>

kyoung671 -  No Additional installation required.

## Usage

\<Fill this in with information on how users can run your script.\>  
\<Describe configuration options if there are any, however, do not ask users to modify your source code.\>

kyoung671 - How to Run script using task scheduler
1. open task scheduler under local admin
2. on the left, select "Task Scheduler Library"
3. on the right, click "Create Basic Task..."
4. Give the task a name and provide a description (optional); click Next
5. Choose the appropriate schedule to trigger the script e.g. weekly; click Next
6. Select the days and time you'd like the script to run; click Next
7. Choose the "Start a program" radio button and click Next
8. Under "Program/script:" type:  powershell.exe
9. To the right of "Add arguments (optional): type:  -executionpolicy bypass -file "PATH TO YOUR SCRIPT e.g. c:\script\script.ps1" and then click Next
10. Check the "Open the Properties dialog for this task when I click Finish" checkbox and click Finish
11. In the Security options box click the "Change User or Group..." button
12. Click the "Locations..." button
13. Enter your network credentials; Expand "Entire Directory"; select and highlight your domain and click OK.
14. Type your name or username and click "Check Names", after a brief pause your Name (domain name) should appear underlined.  Click "OK" and you will be returned to the properties of your task.
15. Check the "Run with highest privileges" checkbox. Open the "conditions" tab.
16. Remove the "Start the task only if the computer is on AC power box (optional but recommend if using a laptop). Click OK.
17. When the script is triggered, a dialog box will prompt you for your email credentials.  After doing so your email will be sent.




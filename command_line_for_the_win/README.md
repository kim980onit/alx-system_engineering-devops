bash commands challenge
# SFTP File Transfer Steps

1. **Open Terminal/Command Prompt:**
   - Opened command prompt on my local machine.

2. **Connect to Sandbox Environment:**
   - Use the SFTP command-line tool to establish a connection to the sandbox environment.
     ```bash
     sftp username@hostname
     ```
     Enter the password when prompted.

3. **Navigate to Target Directory:**
   - Once connected, navigated to the directory where I wanted to upload the screenshots in the sandbox environment.
     ```bash
     cd /root/alx-system_engineering-devops/command_line_for_the_win/
   ```

4. **Upload Screenshots:**
   - Use the SFTP put command to upload the screenshots from my local machine to the sandbox environment.
     ```bash
     put 0-first_9_tasks.png
     put 0-first_9_tasks.jpg
     put 1-next_9_tasks.png
     put 1-next_9_tasks.jpg
     put 2-next_9_tasks.jpg
     put 2-next_9_tasks.png
     ```

5. **Confirm Transfer:**
   - Confirm that the screenshots have been successfully transferred by checking the sandbox directory.
     ```bash
     ls
     ```

6. **Close SFTP Session:**
   - Once the transfer is complete, exit the SFTP session.
     ```bash
     exit

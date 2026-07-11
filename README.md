<h1>SmartMark — AI-Powered Attendance System</h1>

SmartMark is a web-based attendance management system built with Streamlit that eliminates manual
roll-calls.Teachers create sessions; students mark themselves present through real-time face 
recognition and voice verification — no paper, no proxies.
<hr>

<h2>Features</h2>

 Dual-role authentication — separate flows for Teachers and Students
 Face Recognition — powered by dlib and face_recognition to verify student identity
 Voice Verification — speaker embedding via resemblyzer + librosa to prevent audio spoofing
 QR Code Auto-Enroll — students scan a join-code QR to instantly enroll in a class
 Supabase Backend — real-time database and auth via supabase-py
 Attendance Dashboard — teachers view live session status and historical records
 Deep-link support — shareable ?join-code= URLs for one-tap class joining.

 <h2>Tech Stack</h2>
 <table>
  <!-- Header Row -->
  <tr>
    <th>Category</th>
    <th>Technology</th>
  </tr>
  
  <tr>
    <td>Frontend/UI</td>
    <td>Streamlit</td>
  </tr>
  
  <tr>
    <td>Face Recognition</td>
    <td>dlib-bin,face_recognition,scikit-learn</td>
  </tr>

   <tr>
    <td>Voice Recognition</td>
    <td>resemblyzer, librosa</td>
  </tr>

   <tr>
    <td>Database & Auth</td>
    <td>Supabase</td>
  </tr>

   <tr>
    <td>QR Code</td>
    <td>segno</td>
  </tr>

   <tr>
    <td>Image Processing</td>
    <td>Pillow,numpy</td>
  </tr>

   <tr>
    <td>Data Handling</td>
    <td>Pandas</td>
  </tr>

   <tr>
    <td>Security</td>
    <td>bcrypt</td>
  </tr>
</table>

<h2>Architecture Overview</h2>
The project is organized into small focused modules:
<ul>
  <li>'screens' handles full-page student, teacher, and home experiences</li>
  <li>'components' contains reusable dialogs and UI blocks</li>
  <li>'pipelines' contains face recognition and voice recognition logic</li>
  <li>'database' manages Supabase configuration and helper methods</li>
  <li>'ui' contains shared styling and layout utilities</li>
</ul>

This structure keeps product flows separated from AI pipelines and database access, which makes the codebase easier to maintain and scale.

<hr>

<h2>Folder Structure</h2>
```
SmartMark/
|-- app.py
|-- requirements.txt
|-- README.md
|-- src/
    |-- components/
    |   |-- create_subject_dialog.py
    |   |-- dialog_add_photo.py
    |   |-- dialog_attendance_results.py
    |   |-- dialog_auto_enroll.py
    |   |-- dialog_enroll.py
    |   |-- dialog_shared_subject.py
    |   |-- dialog_voice_attendance.py
    |   |-- footer.py
    |   |-- header.py
    |   |-- subject_card.py
    |-- database/
    |   |-- config.py
    |   |-- db.py
    |-- pipelines/
    |   |-- face_pipeline.py
    |   |-- voice_pipeline.py
    |-- screens/
    |   |-- home_screen.py
    |   |-- student_screen.py
    |   |-- teacher_screen.py
    |-- ui/
        |-- base_layout.py
```

<hr>
<h2>Getting Started</h2>
<h3>1.Clone the repository</h3>
```text
git clone https://github.com/shravani09-dev/SMARTMARK.git
cd SMARTMARK
```

<h3>2.Create a virtual environment</h3>
```text
python -m venv venv
source venv/bin/activate 
```

<h3>3.Install dependencies</h3>
```text
pip install -r requirements.txt 
```

<h3>4.Configure Supabase secrets</h3>
Creates '.streamlit/secrets.toml' and add:
'''text
SUPABASE_URL = "your_supabase_project_url"
SUPABASE_KEY = "your_supabase_anon_key"
'''

<h3>5.Start the app</h3>
'''text
streamlit run app.py
'''

<hr>
<h2>Expected Database Tables
The current application expects these tables in Supabase:

<ul>
  <li>'teacher'</li>
  <li>'students'</li>
  <li>'subjects'</li>
  <li>'subjects_students' </li>
  <li>'attendance_logs'</li>
</ul>

These tables support:
<ul>
  <li> teacher account records</li>
  <li>student biometric profile records</li>
  <li>subject creation and mapping</li>
  <li>enrollment relationships</li>
  <li>attendance history and session logs</li>
</ul>

<hr>

<h2>How it Works

<h3>Teacher Flow</h3>
<ol>
    <li>Sign up / log in as a Teacher</li>
    <li>Create a class and generate a QR join-code for students</li>
    <li>Start an attendance session</li>
    <li>View real-time attendance as students mark themselves present</li>
</ol>


<h3>Student Flow</h3>
<ol>
    <li>Sign up / log in as a Student</li>
    <li>Scan the QR code (or open the shared link with ?join-code=) to auto-enroll</li>
    <li>Mark attendance via face scan and voice verification</li>
    <li>View your personal attendance history</li>
</ol>


<h3>Future Improvements</h3>
<ul>
     <li>Email/OTP verification for student enrollment</li>
     <li>Exportable attendance reports (CSV / PDF)</li>
     <li>Admin panel for institution-level management</li>
     <li>Mobile-responsive UI enhancements</li>
     <li>Liveness detection to prevent photo spoofing</li>
</ul>
<hr>

<h2>License</h2>
This project is licensed under the [MIT License].

<h1>SmartMark — AI-Powered Attendance System</h1>
<hr>
<h6>SmartMark is a web-based attendance management system built with Streamlit that eliminates manual
  roll-calls.Teachers create sessions; students mark themselves present through real-time face 
  recognition and voice verification — no paper, no proxies.</h6>
<hr>

<h2>Features</h2>
<h6>
 Dual-role authentication — separate flows for Teachers and Students
 Face Recognition — powered by dlib and face_recognition to verify student identity
 Voice Verification — speaker embedding via resemblyzer + librosa to prevent audio spoofing
 QR Code Auto-Enroll — students scan a join-code QR to instantly enroll in a class
 Supabase Backend — real-time database and auth via supabase-py
 Attendance Dashboard — teachers view live session status and historical records
 Deep-link support — shareable ?join-code= URLs for one-tap class joining</h6>

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

<h2>Project Structure</h2>


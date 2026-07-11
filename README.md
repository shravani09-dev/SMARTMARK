#  SmartMark — AI-Powered Attendance System

SmartMark is a web-based attendance management system built with **Streamlit** that eliminates manual roll-calls. Teachers create sessions; students mark themselves present through real-time **face recognition** and **voice verification** — no paper, no proxies.

---

##  Features

-  **Dual-role authentication** — separate flows for Teachers and Students
-  **Face Recognition** — powered by `dlib` and `face_recognition` to verify student identity
-  **Voice Verification** — speaker embedding via `resemblyzer` + `librosa` to prevent audio spoofing
-  **QR Code Auto-Enroll** — students scan a join-code QR to instantly enroll in a class
-  **Supabase Backend** — real-time database and auth via `supabase-py`
-  **Attendance Dashboard** — teachers view live session status and historical records
-  **Deep-link support** — shareable `?join-code=` URLs for one-tap class joining

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend / UI | Streamlit |
| Face Recognition | `dlib-bin`, `face_recognition`, `scikit-learn` |
| Voice Recognition | `resemblyzer`, `librosa` |
| Database & Auth | Supabase |
| QR Code | `segno` |
| Image Processing | `Pillow`, `numpy` |
| Data Handling | `pandas` |
| Security | `bcrypt` |

---

##  Architecture Overview

The project is organized into small focused modules:

- `screens` — handles full-page student, teacher, and home experiences
- `components` — contains reusable dialogs and UI blocks
- `pipelines` — contains face recognition and voice recognition logic
- `database` — manages Supabase configuration and helper methods
- `ui` — contains shared styling and layout utilities

This structure keeps product flows separated from AI pipelines and database access, making the codebase easier to maintain and scale.

---

##  Folder Structure

```
SmartMark/
├── app.py
├── requirements.txt
├── README.md
└── src/
    ├── components/
    │   ├── create_subject_dialog.py
    │   ├── dialog_add_photo.py
    │   ├── dialog_attendance_results.py
    │   ├── dialog_auto_enroll.py
    │   ├── dialog_enroll.py
    │   ├── dialog_shared_subject.py
    │   ├── dialog_voice_attendance.py
    │   ├── footer.py
    │   ├── header.py
    │   └── subject_card.py
    ├── database/
    │   ├── config.py
    │   └── db.py
    ├── pipelines/
    │   ├── face_pipeline.py
    │   └── voice_pipeline.py
    ├── screens/
    │   ├── home_screen.py
    │   ├── student_screen.py
    │   └── teacher_screen.py
    └── ui/
        └── base_layout.py
```

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shravani09-dev/SMARTMARK.git
cd SMARTMARK
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

>  `dlib` requires CMake and a C++ compiler. On Ubuntu: `sudo apt-get install cmake build-essential`. On macOS: `brew install cmake`.

### 4. Configure Supabase secrets

Create `.streamlit/secrets.toml` and add:

```toml
SUPABASE_URL = "your_supabase_project_url"
SUPABASE_KEY = "your_supabase_anon_key"
```

### 5. Start the app

```bash
streamlit run app.py
```

---

##  Expected Database Tables

The application expects the following tables in Supabase:

| Table | Purpose |
|-------|---------|
| `teacher` | Teacher account records |
| `students` | Student biometric profile records |
| `subjects` | Subject creation and mapping |
| `subjects_students` | Enrollment relationships |
| `attendance_logs` | Attendance history and session logs |

---

##  How It Works

### Teacher Flow
1. Sign up / log in as a **Teacher**
2. Create a class and generate a **QR join-code** for students
3. Start an attendance session
4. View real-time attendance as students mark themselves present

### Student Flow
1. Sign up / log in as a **Student**
2. Scan the QR code (or open the shared link with `?join-code=`) to auto-enroll
3. Mark attendance via **face scan** and **voice verification**
4. View your personal attendance history

---

##  Future Improvements

- [ ] Email/OTP verification for student enrollment
- [ ] Exportable attendance reports (CSV / PDF)
- [ ] Admin panel for institution-level management
- [ ] Mobile-responsive UI enhancements
- [ ] Liveness detection to prevent photo spoofing

---

##  License

This project is licensed under the [MIT License](LICENSE).
